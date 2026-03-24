# 10 Passphrase And Multisig

## Chapter Digest

Passphrases are treated as an advanced salt in PBKDF2, which means they create a completely different wallet rather than a small extra lock. Because of that, the chapter warns against using them casually: the seed must already be backed up, signing and recovery need to be familiar, and the user should understand why a passphrase can separate one wallet from another so completely.

The device walkthroughs make that difference concrete. Keystone forgets the passphrase when it powers off, SeedSigner asks for a BIP-39 passphrase immediately after loading a seed, and BlueWallet on an air-gapped phone uses the password checkbox to enable the same idea. In every case the resulting MFP changes, so the watch-only xpub has to be exported again after the new wallet is created.

If signing fails, the first suspect is the passphrase. The guide tells the user to compare MFP values across watch-only wallets and the signing device, then try the plausible passphrase variants until the correct wallet appears. If the MFP matches but signing still fails, the problem is usually the watch-only setup, so the xpub needs to be re-exported or the descriptor state checked again.

Multisig expands the same discipline across multiple keys. BlueWallet requires an English wallet name because BSMS encoding can break on Korean text, Nunchuk imports keys from Keystone and other signers, and Sparrow builds multisig through New Wallet and descriptor-style backups. The signing practice sends 10,000 sats to the wallet, rebuilds a spend to self, signs on each device, and finally broadcasts only after the threshold is met; restoring the watch-only wallet from BSMS or descriptor files proves that recovery is part of the design.
