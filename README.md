# YieldWindow Treasury

- **Repo:** [Synthesis-Lido-stETHTreasury](https://github.com/CrystallineButterfly/Synthesis-Lido-stETHTreasury)
- **Primary track:** Lido stETH Agent Treasury
- **Category:** treasury
- **Primary contract:** `YieldWindowTreasury`
- **Primary module:** `lido_yield_operator`
- **Submission status:** implementation ready, waiting for credentials and TxIDs.

## What this repo does

A guarded treasury that keeps principal untouchable while letting agents spend only staking yield through target whitelists, caps, and time windows.

## Why this build matters

A guarded treasury contract models untouchable principal, yield-only allowances, target whitelists, caps, and time windows. The Python operator loop computes spendable yield, runs dry-run checks, and emits draft actions for Uniswap swaps, Locus payments, or Octant grants while keeping principal off-limits.

## Submission fit

- **Primary track:** Lido stETH Agent Treasury
- **Overlap targets:** Uniswap Agentic Finance, Bankr Gateway, Celo, PayWithLocus, Octant, MetaMask Delegations
- **Partners covered:** Lido, Uniswap, Bankr Gateway, Celo, PayWithLocus, Octant, MetaMask Delegations

## Idea shortlist

1. Yield-Powered Autonomous Trader
2. Payroll Float for Multi-Agent Swarms
3. Public-Goods Yield Payroll

## System graph

```mermaid
flowchart TD
    Signals[Discover signals]
    Planner[Agent runtime]
    DryRun[Dry-run artifact]
    Contract[YieldWindowTreasury policy contract]
    Verify[Verify and render submission]
    Signals --> Planner --> DryRun --> Contract --> Verify
    Contract --> lido[Lido]
    Contract --> uniswap[Uniswap]
    Contract --> bankr_gateway[Bankr Gateway]
    Contract --> celo[Celo]
    Contract --> paywithlocus[PayWithLocus]
    Contract --> octant[Octant]
```

## Repository contents

| Path | What it contains |
| --- | --- |
| `src/` | Shared policy contracts plus the repo-specific wrapper contract. |
| `script/Deploy.s.sol` | Foundry deployment entrypoint for the policy contract. |
| `agents/` | Python runtime, project spec, env handling, and partner adapters. |
| `scripts/` | Terminal entrypoints for run, demo planning, and submission rendering. |
| `docs/` | Architecture, credentials, security notes, and demo steps. |
| `submissions/` | Generated `synthesis.md` snippet for this repo. |
| `test/` | Foundry tests for the Solidity control layer. |
| `tests/` | Python tests for runtime and project context. |
| `agent.json` | Submission-facing agent manifest. |
| `agent_log.json` | Local execution log and status trail. |

## Autonomy loop

1. Discover signals relevant to the repo track and its overlap targets.
2. Build a bounded plan with per-action and compute caps.
3. Persist a dry-run artifact before any live execution.
4. Enforce onchain policy through the guarded contract wrapper.
5. Verify outputs, update receipts, and render submission material.

## Security controls

- Admin-managed allowlists for targets and selectors.
- Per-action caps, daily caps, cooldown windows, and a principal floor.
- Reporter-only receipt anchoring and proof attachment.
- Env-only secrets; no committed private keys or partner tokens.
- Pause switch plus dry-run-first execution flow.

## Action catalog

| Action | Partner | Purpose | Max USD | Sensitivity |
| --- | --- | --- | --- | --- |
| `lido_yield_route` | Lido | Use Lido for a bounded action in this repo. | $200 | medium |
| `uniswap_quote_route` | Uniswap | Use Uniswap for a bounded action in this repo. | $220 | medium |
| `bankr_gateway_compute_route` | Bankr Gateway | Use Bankr Gateway for a bounded action in this repo. | $10 | high |
| `celo_payment_settle` | Celo | Use Celo for a bounded action in this repo. | $150 | low |
| `paywithlocus_subaccount_pay` | PayWithLocus | Use PayWithLocus for a bounded action in this repo. | $120 | medium |
| `octant_signal_publish` | Octant | Use Octant for a bounded action in this repo. | $25 | medium |
| `metamask_delegations_delegate_scope` | MetaMask Delegations | Use MetaMask Delegations for a bounded action in this repo. | $2 | high |

## Local terminal flow (Anvil + Sepolia)

```bash
export SEPOLIA_RPC_URL=https://sepolia.infura.io/v3/YOUR_KEY
anvil --fork-url "$SEPOLIA_RPC_URL" --chain-id 11155111
cp .env.example .env
# keep private keys only in .env; TODO.md stays local-only too
forge script script/Deploy.s.sol --rpc-url "$RPC_URL" --broadcast
python3 scripts/run_agent.py
python3 scripts/render_submission.py
```

## Commands

```bash
python3 -m unittest discover -s tests
forge test
python3 scripts/run_agent.py
python3 scripts/plan_live_demo.py
python3 scripts/render_submission.py
```

## Credentials

| Partner | Variables | Docs |
| --- | --- | --- |
| Lido | RPC_URL | https://docs.lido.fi/ |
| Uniswap | UNISWAP_API_KEY, UNISWAP_QUOTE_URL | https://developers.uniswap.org/ |
| Bankr Gateway | BANKR_API_KEY, BANKR_CHAT_COMPLETIONS_URL, BANKR_MODEL | https://bankr.bot/ |
| Celo | CELO_RPC_URL | https://docs.celo.org/ |
| PayWithLocus | LOCUS_API_KEY, LOCUS_PAYMENT_URL | https://docs.locus.finance/ |
| Octant | OCTANT_SIGNAL_URL | https://octant.app/ |
| MetaMask Delegations | RPC_URL | https://docs.metamask.io/delegation-toolkit/ |

## Live demo plan

1. Copy .env.example to .env and fill the required keys.
2. Deploy the contract with forge script script/Deploy.s.sol --broadcast for YieldWindowTreasury.
3. Run python3 scripts/run_agent.py to produce a dry run for lido_yield_operator.
4. Set LIVE_MODE=true and rerun python3 scripts/run_agent.py with real credentials.
5. Run python3 scripts/render_submission.py and attach TxIDs plus repo links.
