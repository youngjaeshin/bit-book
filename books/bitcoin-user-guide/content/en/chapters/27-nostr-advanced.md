# 27 Nostr Advanced

## Chapter Digest

Advanced Nostr begins with key management, relays, and event handling rather than with a feed. Nsec and npub identities, NIP-05-style addresses, relay support metadata under NIP-11, and deletion limits under NIP-09 all make the protocol feel more like portable identity infrastructure than a normal social app.

The client walkthroughs make that portability concrete. Primal is easy for first-time users because it can create an account and attach its own Lightning wallet, Damus stores or shows the key on iOS and macOS, and Phoenix is recommended as a browser-friendly client when the user wants NWC-backed zaps from a Lightning node.

Zaps are explained as Lightning payments attached to posts, with NWC and NIP-47 acting as the bridge between client and wallet. That bridge is used to connect Alby Hub wallets, send or receive zaps, and later generate a Lightning address from Zeus.

The guide then moves beyond clients into long-form writing and self-hosting. Habla and Markdown let posts grow into articles, Umbrel can host a private relay, Tailscale can expose it remotely, a domain can make it public, and list or mute controls help fight spam without surrendering control to a central platform.
