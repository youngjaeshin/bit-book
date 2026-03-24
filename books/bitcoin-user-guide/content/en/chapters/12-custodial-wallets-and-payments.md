# 12 Custodial Wallets And Payments

## Chapter Digest

This guide treats a custodial Lightning wallet as convenience with a clear trust cost. The user installs the wallet, completes the provider's required steps, and uses the service knowing that the operator still sits in the middle and can freeze or redirect access if it chooses.

Once the account is active, a custom Lightning address can be issued and used as the public receiving identity. From there the flow is straightforward: on-chain deposits move bitcoin into the custodial balance, and on-chain withdrawals move it back out when the user wants to leave the Lightning environment.

The guide then uses that same structure for cash-out planning. If the goal is to withdraw value to KRW, bitcoin can be sent from the custodial Lightning wallet to an exchange and then converted through the usual exchange flow. The point is to make the path explicit instead of pretending that convenience comes without any custody trade-off.

In that sense the chapter is not an argument against custodial wallets. It is a practical reminder that the user should know exactly where custody begins, where Lightning addresses live, and which steps leave the self-controlled path and enter a provider-controlled one.
