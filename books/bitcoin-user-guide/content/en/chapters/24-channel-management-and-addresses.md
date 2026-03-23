# 24 Channel Management And Addresses

## Chapter Digest

Channel management is where Lightning becomes operational rather than merely installed. The chapter explains routing fees, shows what happens when a single node absorbs too much liquidity, and then walks through channel-specific fee tweaks, minimum and maximum HTLC settings, and the more important judgment call of choosing better peers instead of endlessly tuning fees.

Closing channels and backing up the SCB file show that maintenance is not optional. The user has to know how to shut channels down cleanly and how to recover the watch-only and channel state if the node has to be rebuilt. That same operational discipline extends to Lightning addresses, where Alby and Amboss are used to publish node identity, set profiles, and make the node discoverable.

The chapter makes public identity and channel health feel like the same problem from different angles. A well-run Lightning node is one that can be found, trusted, and repaired when necessary.
