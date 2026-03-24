# 04 Seedsigner Wallet

## Chapter Digest

SeedSigner is framed as a build-it-yourself air-gapped wallet built on Raspberry Pi Zero hardware and open software. The guide starts with the parts list first: the correct Pi board, the 1.3-inch 240 x 240 LCD, the camera module, an 8GB microSD card, a case, tweezers or a thin screwdriver, a card reader, a micro USB cable, and a power source are all part of the trust model before the wallet even exists.

Before flashing anything, the software image is verified on Windows and Mac by downloading the image, the SHA256 text file, and its signature, then checking the hash and signature with Gpg4win or GPG. That verification step matters because the device is supposed to be offline from the start; the chapter keeps repeating that the user should know exactly what was written to the card before the card ever reaches the board.

Once the boot microSD is prepared, the device is assembled, the wireless module is removed on Zero W boards, and the result is a tiny offline computer whose only job is to keep the seed and signing path isolated from the network. The build stage is not an aside: it is the first part of the security story.

Wallet creation, SeedQR generation, manual mnemonic entry or QR scanning, xpub export to BlueWallet, Nunchuk, and Coconut Wallet, and signing practice all turn that hardware into an operational cold-wallet workflow. The recovery drills and the final game-console trick reinforce the same lesson: SeedSigner is not just a niche device, but a switchable offline host that teaches the user how air-gapping actually works.
