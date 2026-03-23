# 09 Fees Rbf Cpfp

## Chapter Digest

Fee selection is treated as a market decision, not a fixed number. The chapter explains how on-chain fees are measured in sat/vB, why larger transactions cost more because they consume more virtual bytes, and how mempool conditions determine which transactions get mined first.

That logic leads naturally to the practical rescue tools. RBF lets the user replace a transaction with a higher-fee version, while CPFP lets a later child transaction pull an earlier parent into a block by paying enough fee on the combined package. The chapter also returns to coin consolidation and the hardware limits that appear when too many inputs are packed into one signing session, so the user sees fee management and transaction design as one problem.

The result is a calmer relationship with the mempool. Instead of hoping that a low-fee transaction will somehow succeed, the reader learns how to inspect conditions, choose an appropriate fee rate, and recover when the network is congested or a payment has been underestimated.
