# 10 Passphrase And Multisig

## Chapter Digest

Passphrases add another secret layer, but they also add another way to lock yourself out. It walks through setting a passphrase on Keystone, SeedSigner, and an air-gapped phone wallet while stressing that the phrase must be backed up and remembered with the same discipline as the seed itself. When signing fails, the cause may be a wrong passphrase rather than a broken wallet, so the workflow has to be deliberate.

Multisig extends that logic by splitting signing authority across devices and keys. It builds multisig wallets in BlueWallet, Nunchuk, and Sparrow, then practices signing from each interface so the user can see how the same wallet behaves when one key is missing, one device is deleted, or the watch-only copy must be reconstructed from QR data or descriptor-style backups. Recovery is shown as a normal part of the design, not an emergency workaround.

Its real message is that higher security comes with higher operational load. Passphrases and multisig are powerful only when the user is ready for the extra backup, the extra recovery path, and the extra care that keeps the setup usable after something goes wrong.
