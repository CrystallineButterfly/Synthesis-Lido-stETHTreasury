# YieldWindow Treasury

- **Repo:** https://github.com/CrystallineButterfly/Synthesis-Lido-stETHTreasury
- **Primary track:** Lido stETH Agent Treasury
- **Overlap targets:** Uniswap Agentic Finance, Bankr Gateway, Celo, PayWithLocus, Octant, MetaMask Delegations
- **Primary contract:** YieldWindowTreasury
- **Primary operator module:** lido_yield_operator
- **Live TxIDs:** PENDING
- **ERC-8004 registrations:** PENDING
- **Demo link:** docs/demo_video_script.md

A guarded treasury that keeps principal untouchable while letting agents spend only staking yield through target whitelists, caps, and time windows.

## Track evidence

- `artifacts/onchain_intents/lido_yield_route.json`
- `artifacts/onchain_intents/celo_payment_settle.json`
- `artifacts/onchain_intents/metamask_delegations_delegate_scope.json`

## Latest verification

```json
{
  "status": "verified",
  "project_name": "YieldWindow Treasury",
  "track": "Lido stETH Agent Treasury",
  "plan_id": "0x4e123112d451952e53fe9ac7b5f974b89109e5e149ec5379a66c7743ff24f257",
  "simulation_hash": "0x943e4e7fe7f4e60f2e0dd03a05ae35d5fd1e692f95d608e98761a29958ad1805",
  "execution_status": "offline_prepared",
  "tx_ids": [],
  "artifact_paths": [
    "artifacts/onchain_intents/lido_yield_route.json",
    "artifacts/onchain_intents/celo_payment_settle.json",
    "artifacts/onchain_intents/metamask_delegations_delegate_scope.json"
  ],
  "partner_statuses": {
    "Lido": "prepared_contract_call",
    "Uniswap": "awaiting_credentials",
    "Bankr Gateway": "awaiting_credentials",
    "Celo": "prepared_contract_call",
    "PayWithLocus": "awaiting_credentials",
    "Octant": "awaiting_credentials",
    "MetaMask Delegations": "prepared_contract_call"
  },
  "created_at": "2026-03-19T03:52:14+00:00"
}
```
