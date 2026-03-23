# 18 Remote Access And Watch Only

## Chapter Digest

Remote access is what turns a node from a box in a room into something useful on the move. It uses Tailscale to let the user reach Umbrel from elsewhere, then installs Electrs so watch-only wallets can read balances and transactions from the user’s own infrastructure instead of from a third-party explorer.

BlueWallet, Nunchuk, Coconut Wallet, and Sparrow are then connected to that node, either on the local network or through Tor. The result is a monitoring setup where private keys stay elsewhere while the node provides the balance and transaction view, making the watch-only model feel like a natural extension of self-custody rather than a compromise.

It also shows that remote access is not only about convenience. It reduces the temptation to fall back on outside services whenever the user is away from the node, which keeps the habit of verification tied to the user’s own hardware.
