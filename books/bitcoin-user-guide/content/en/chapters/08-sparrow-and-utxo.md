# 08 Sparrow And Utxo

## Chapter Digest

Sparrow is used here as the control room for UTXO-aware Bitcoin spending. The chapter installs Sparrow, connects it to a full node, turns it into a watch-only companion, and then uses coin selection and PSBT flows to show why transaction construction is really about choosing inputs, outputs, and change before a signature is ever made.

UTXO consolidation is the main practical example. By grouping small coins into cleaner denominations, the user learns that fees, privacy, and future spendability are all affected by the shape of the coin set. It also shows how many-input transactions can overrun lightweight air-gapped devices, which is a useful reminder that the wallet interface, the signer’s memory, and the transaction design all have to fit together.

By the end, Sparrow feels less like an app and more like an operations desk. It lets the user inspect the coin set, plan a consolidation path, move the unsigned transaction to a signing device, and return with a signed result that can be broadcast with confidence.
