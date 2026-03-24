# 20 Windows Mac Local Integration

## Chapter Digest

This guide shows how a desktop machine can become a local Bitcoin node stack on Windows or macOS without buying a dedicated box. Core or Knots is installed on the same machine, Sparrow is pointed at it, and the wallet talks to the node through the local data folder and the temporary `.cookie` credentials stored there.

For same-device use, Sparrow stays on 127.0.0.1 and port 8332, then connects through File > Settings > Server > Edit Existing Connection. The guide emphasizes that the data folder must be chosen correctly so Sparrow can find the node's Bitcoin data and keep using the temporary RPC username and password exposed through the cookie file.

When the node and wallet live on the same local network, the machine's LAN IP and bitcoin.conf settings matter just as much as the GUI. Windows and macOS each require their own firewall allowances, but the goal is the same: let Sparrow reach the node without handing the connection to a third-party service.

The result is a practical self-hosted backbone that can live on ordinary desktop hardware. The user can verify balances, broadcast transactions, and keep watch-only wallet traffic inside the home network instead of outsourcing those checks to a public server.
