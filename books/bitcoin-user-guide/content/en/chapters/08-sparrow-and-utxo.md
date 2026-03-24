# 08 Sparrow And Utxo

## Chapter Digest

Sparrow is presented as the desktop control room for UTXO-aware Bitcoin spending. The guide begins on a PC or laptop with a webcam, installs Sparrow from the official download page, and starts from a public server configuration before the book later moves toward self-hosted nodes.

The wallet is created as a watch-only wallet with no password, which keeps the signing key elsewhere while still letting Sparrow inspect the coin set, labels, and transaction construction. The point is not to treat the wallet as a balance-only display; it is to use it as a desk for planning how inputs, outputs, and change should be arranged before a signature is made.

UTXO consolidation is explained through the Alice example. Large coins leak privacy, tiny coins inflate fees, and a practical middle range matters more than a neat balance number. The guide recommends roughly 0.01 to 0.02 BTC, or about 100k to 200k sats, for coins meant to cover near-term spending, while keeping KYC and non-KYC coins separated when possible.

From there the workflow becomes concrete: select the UTXOs, send only the chosen inputs, build the unsigned transaction, and move it to a signing device before broadcasting the result. Sparrow feels less like a generic wallet and more like an operations desk for shaping future spendability, not just showing a present balance.
