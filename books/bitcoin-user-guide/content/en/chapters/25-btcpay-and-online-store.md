# 25 Btcpay And Online Store

## Chapter Digest

BTCPay Server is used here as the payment backend for an online store built on WordPress and WooCommerce. The guide installs the BTCPay and WooCommerce plugins, chooses a theme, adds products, and keeps the checkout flow inside a stack the merchant can actually control.

The infrastructure work is part of the store, not a separate concern. Umbrel is used to download and configure BTCPay Server, Cloudflare is used to create an account and a tunnel, the domain is wired in, SSL is applied, and the merchant then links WooCommerce back to the BTCPay instance.

That connection turns a WordPress shop into a Bitcoin-accepting storefront with a payment processor the merchant operates directly. The guide also leaves room for extra settings so the reader sees the setup as an integrated system instead of a single plugin toggle.

Legal and tax questions stay visible at the end because online Bitcoin commerce is still commerce. The technical path is one layer, while accounting, policy, and compliance decisions sit on top of it and need to be thought through separately.
