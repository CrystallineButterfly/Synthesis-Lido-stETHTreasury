"""Project-specific context module."""

from __future__ import annotations

PROJECT_CONTEXT = {
  "project_name": "YieldWindow Treasury",
  "track": "Lido stETH Agent Treasury",
  "pitch": "A guarded treasury that keeps principal untouchable while letting agents spend only staking yield through target whitelists, caps, and time windows.",
  "overlap_targets": [
    "Uniswap Agentic Finance",
    "Bankr Gateway",
    "Celo",
    "PayWithLocus",
    "Octant",
    "MetaMask Delegations"
  ],
  "goals": [
    "discover a bounded opportunity",
    "plan a dry-run-first action",
    "verify receipts and proofs"
  ]
}


def seed_targets() -> list[str]:
    """Return the first batch of overlap targets for planning."""
    return list(PROJECT_CONTEXT['overlap_targets'])
