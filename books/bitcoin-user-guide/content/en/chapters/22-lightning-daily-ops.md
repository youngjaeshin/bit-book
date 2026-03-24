# 22 Lightning Daily Ops

## Chapter Digest

Daily Lightning use starts by redefining what a channel is. A channel is a jointly funded on-chain output that then behaves like an off-chain ledger for most routine activity. Opening and closing remain on-chain events; the many updates in between happen without touching the chain each time. That is why Lightning feels fast while still depending on Bitcoin as the final settlement layer.

The guide then turns liquidity vocabulary into operating knowledge. Outbound liquidity is the ability to send, inbound liquidity is the ability to receive, and both depend on where balance sits inside the channel. MPP, HTLCs, cooperative closes, force closes, and CSV are introduced as the concepts that explain why some payments route smoothly, why others fail, and why some exits are cheap while others are slow and punitive.

Node profiles are treated as practical design choices rather than abstract categories. A drain node can pull liquidity to one side and create an ongoing rebalancing burden. A hub-style node may be more helpful for inbound capacity and route diversity, but then fee strategy and peer selection become more consequential. The guide pushes the operator to think in terms of purpose: is the node mainly for paying, receiving, routing, or some mixture of all three?

That is why the chapter lands on maintenance rather than installation. Daily operation means funding the on-chain wallet, searching for and adding peers, opening more than one channel, watching the channel set for inbound capacity, and adjusting balances and counterparties over time. Lightning is presented as a living payment system that stays useful only if someone keeps its liquidity and topology aligned with real payment habits.
