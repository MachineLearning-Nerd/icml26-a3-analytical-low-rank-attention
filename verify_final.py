#!/usr/bin/env python3
"""Verify the A3 audit dossier and live GitHub state."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
REPOSITORY = "icml26-a3-analytical-low-rank-attention"
CANONICAL = (
    "MachineLearning-Nerd",
    "37579156+MachineLearning-Nerd@users.noreply.github.com",
)
REQUIRED_PATHS = [
    "README.md",
    "STATUS.md",
    "AUTONOMOUS_STATE.json",
    "branch-audit.md",
    "BRANCH_AUDIT.md",
    "CLAIM_EVIDENCE.md",
    "SOURCE_AUDIT.md",
    "ENVIRONMENT.md",
    "REPORT.md",
    "AUTHOR_THANK_YOU.md",
    "CITATION.cff",
    "claims.json",
    "EVIDENCE_MANIFEST.json",
    "verify_final.py",
    "contract/live_claims.json",
    "contract/metadata.json",
    "evidence/source/SHA256SUMS",
    "evidence/claim1_attempt1/source_protocol_audit.md",
    "evidence/official_code_audit.md",
    "evidence/claim5_attempt1/SHA256SUMS",
    "evidence/claim5_attempt1/a3_qk_ov_excerpt.tex",
    "evidence/claim5_attempt1/a3_mlp_excerpt.tex",
    "src/claim5_a3_conformance.py",
    "outputs/claim5_a3_conformance/config.json",
    "outputs/claim5_a3_conformance/results.csv",
    "outputs/claim5_a3_conformance/summary.json",
    "outputs/claim5_a3_conformance/SHA256SUMS",
]
EXPECTED_STATUSES = [
    "inconclusive_source_protocol",
    "unverified",
    "unverified",
    "unverified",
    "toy_finite_conformance",
    "unverified",
]


def fail(message: str) -> None:
    print(f"FINAL_AUDIT=FAILED {message}", file=sys.stderr)
    raise SystemExit(1)


def require(condition: bool, message: str) -> None:
    if not condition:
        fail(message)


def run(*args: str) -> str:
    result = subprocess.run(
        args,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        fail(f"command failed: {' '.join(args)}\n{result.stderr.strip()}")
    return result.stdout


def current_bytes(path: str) -> bytes:
    local = ROOT / path
    if local.exists():
        return local.read_bytes()
    result = subprocess.run(
        ["git", "show", f"HEAD:{path}"],
        cwd=ROOT,
        check=False,
        capture_output=True,
    )
    if result.returncode:
        fail(f"required path is unavailable: {path}")
    return result.stdout


def current_json(path: str) -> object:
    try:
        return json.loads(current_bytes(path))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path}: {exc}")
    return None


def verify_manifest() -> None:
    manifest = current_json("EVIDENCE_MANIFEST.json")
    require(isinstance(manifest, dict), "manifest is not an object")
    require(manifest.get("schema_version") == 1, "unsupported manifest schema")
    require(manifest.get("hash_algorithm") == "sha256", "manifest hash algorithm changed")
    entries = manifest.get("entries")
    require(isinstance(entries, list) and entries, "evidence manifest is empty")
    seen = set()
    for entry in entries:
        require(isinstance(entry, dict), "manifest entry is not an object")
        path = entry.get("path")
        expected = entry.get("sha256")
        require(isinstance(path, str), "manifest path is missing")
        require(isinstance(expected, str) and len(expected) == 64, f"bad manifest hash for {path}")
        require(path not in seen, f"duplicate manifest path: {path}")
        seen.add(path)
        actual = hashlib.sha256(current_bytes(path)).hexdigest()
        require(actual == expected, f"manifest hash mismatch: {path}")


def main() -> None:
    origin = run("git", "config", "--get", "remote.origin.url").strip()
    require(
        origin in {
            f"https://github.com/MachineLearning-Nerd/{REPOSITORY}.git",
            f"git@github.com:MachineLearning-Nerd/{REPOSITORY}.git",
        },
        f"unexpected origin: {origin}",
    )
    require(
        "ref: refs/heads/main\tHEAD"
        in run("git", "ls-remote", "--symref", "origin", "HEAD"),
        "origin/HEAD is not main",
    )

    remote_lines = run("git", "ls-remote", "--heads", "origin").splitlines()
    remote_heads = {}
    for line in remote_lines:
        commit, ref = line.split("\t", 1)
        require(ref.startswith("refs/heads/"), f"unexpected remote ref: {ref}")
        remote_heads[ref.removeprefix("refs/heads/")] = commit
    require(set(remote_heads) == {"main"}, "remote branch set is not exactly main")
    require(
        remote_heads["main"] == run("git", "rev-parse", "origin/main").strip(),
        "origin/main differs from the live main tip",
    )

    local_heads = set(
        run("git", "for-each-ref", "--format=%(refname:strip=2)", "refs/heads")
        .splitlines()
    )
    require(local_heads <= {"main"}, "unexpected local branch")
    refs = run("git", "for-each-ref", "--format=%(refname)", "refs").splitlines()
    require(not any("refs/original/" in ref for ref in refs), "refs/original remains")

    identities = set()
    for line in run("git", "log", "--all", "--format=%an\t%ae\t%cn\t%ce").splitlines():
        if line.strip():
            identities.add(tuple(line.split("\t")))
    require(
        identities == {(CANONICAL[0], CANONICAL[1], CANONICAL[0], CANONICAL[1])},
        f"non-canonical reachable identity: {sorted(identities)}",
    )
    require(
        "co-authored-by:" not in run("git", "log", "--all", "--format=%B").lower(),
        "co-author trailer found",
    )
    commit_count = int(run("git", "rev-list", "--count", "--all").strip())
    require(commit_count >= 7, f"unexpectedly short history: {commit_count}")

    for path in REQUIRED_PATHS:
        require((ROOT / path).exists(), f"required path missing: {path}")

    claims = current_json("claims.json")
    require(isinstance(claims, dict), "claims.json is not an object")
    require(
        claims.get("repository") == f"MachineLearning-Nerd/{REPOSITORY}",
        "claims repository mismatch",
    )
    require(claims.get("publication_allowed") is False, "publication block changed")
    rows = claims.get("claims")
    require(isinstance(rows, list) and len(rows) == 6, "claims.json must contain six claims")
    statuses = [row.get("status") for row in rows]
    require(statuses == EXPECTED_STATUSES, f"unexpected claim statuses: {statuses}")

    live_claims = current_json("contract/live_claims.json")
    require(
        isinstance(live_claims, list)
        and len(live_claims) == 6
        and all(row.get("status") == "unverified" for row in live_claims),
        "live claim contract changed",
    )
    metadata = current_json("contract/metadata.json")
    require(metadata.get("openreview") == "https://openreview.net/forum?id=aeeo8ZAftQ", "OpenReview metadata changed")
    require(metadata.get("arxiv") == "2505.12942", "arXiv metadata changed")

    state = current_json("AUTONOMOUS_STATE.json")
    require(state.get("phase") == "published_and_verified", "state is not final")
    require(state.get("publication_allowed") is False, "state publication block changed")
    require(state.get("last_known_git_commit"), "state has no recorded commit")

    summary = current_json("outputs/claim5_a3_conformance/summary.json")
    require(summary.get("verdict") == "toy", "Claim 5 was promoted beyond toy")
    require(summary.get("seeds") == [11, 23, 47, 89, 131], "Claim 5 seeds changed")
    require(abs(summary["mean_qk_activation_aware_error"] - 0.10332385678007772) < 1e-12, "QK result changed")
    require(abs(summary["mean_ov_activation_aware_error"] - 0.13610705728604083) < 1e-12, "OV result changed")
    require(abs(summary["mean_mlp_keep_error"] - 0.2948223031179342) < 1e-12, "MLP result changed")
    require(summary["mean_qk_raw_svd_error"] > summary["mean_qk_activation_aware_error"], "QK control did not degrade")
    require(summary["mean_ov_raw_svd_error"] > summary["mean_ov_activation_aware_error"], "OV control did not degrade")
    require(summary["mean_mlp_low_energy_error"] > summary["mean_mlp_keep_error"], "MLP control did not degrade")

    source_sums = current_bytes("evidence/source/SHA256SUMS").decode()
    require(
        "98b5c258ec9f331d44d748afa1681058849f4b25a52fc4a8d8238abe82e325c0" in source_sums
        and "6fcb09f188b7c8723c9fc8e8afbf8447837ace219377b9c4147c0fe5bdf46e2b" in source_sums,
        "source hashes are not pinned",
    )
    official = current_bytes("evidence/official_code_audit.md").decode()
    require(
        "f688fc5d270ea9185fe29ea656bf168f0fab787a" in official
        and "rank-search" in official
        and "vc" in official,
        "official implementation audit changed",
    )
    claim1 = current_bytes("evidence/claim1_attempt1/source_protocol_audit.md").decode()
    require("Inconclusive" in claim1 and "70B" in claim1, "Claim 1 protocol audit changed")

    verify_manifest()
    statuses_text = ",".join(f"{row['id']}:{row['status']}" for row in rows)
    print(
        f"FINAL_AUDIT=VERIFIED branches={len(remote_heads)} commits={commit_count} "
        f"claims={statuses_text} c5=toy publication_allowed=false"
    )


if __name__ == "__main__":
    main()
