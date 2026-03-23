# 02 Basics

## Chapter Digest

Self-custody begins with the accounting model behind Bitcoin. BTC and sats, balance and UTXO thinking, air-gapped and watch-only wallets, PSBTs, xpubs, derivation paths, address reuse, and gap limits all belong to the same operational picture rather than separate trivia. Even the warnings about dice entropy, passphrases, the 5-dollar wrench attack, and KYC/travel-rule friction sit in the same frame because custody is always a mix of security, recovery, and privacy.

Transaction size and fee pressure matter just as much as key storage. The chapter links UTXO structure to mempool behavior so the reader can understand why consolidation changes future costs, why multiple inputs make fees rise, and why address discipline affects both privacy and operational simplicity. Knowing how transactions are signed, how addresses are derived, and how invoices or Lightning addresses fit into the picture makes the later wallet chapters much easier to follow.

The result is a working map rather than a glossary. Once the user understands what needs to stay secret, what can be monitored, and which trade-offs come with each wallet type, the rest of the book becomes a sequence of decisions instead of a pile of device names.
