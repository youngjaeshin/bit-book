# 20 Windows Mac Local Integration

## Chapter Digest

Windows and Mac users get a local-node workflow that keeps the node and Sparrow on the same machine or the same local network. The chapter covers installing Core or Knots, opening the firewall for RPC access when needed, and configuring Sparrow so it can talk to the local node cleanly and reliably.

The same pattern appears on both platforms, but each operating system asks for slightly different steps. Windows uses Control Panel and inbound firewall rules, while Mac users check the firewall state, allow the node app if necessary, and then point Sparrow at the local IP address and the exact RPC credentials stored in bitcoin.conf. Success is confirmed when the connection test turns green.

The point is that a local node is not only for dedicated hardware. Even a desktop or laptop that already exists can become a self-hosted backbone for monitoring and spending as long as the local integration is configured carefully.
