# Technology 3: Thermodynamics ~ Gall’s Law

## Source Metadata

- Chapter number: 7
- TOC index: 7
- Part: main
- EPUB src: xhtml/xhtml-0-38.xhtml#aid_101
- Extraction mode: fragment-aware-spine-range

## Extracted Text

Thermodynamics: 1st Law

Energy cannot be created nor destroyed in isolated systems. It can only be transformed.

—

To explain the link between thermodynamics and bitcoin, let’s start with understanding commodities. As a category of economic goods, commodities possess the property of fungibility, such that the market does not differentiate between who produced them.

All commodities (i.e., metals, agricultural, energy) require some form of energy conversion in their extraction or farming. Whether it be cattle consuming feed or an excavator combusting diesel, there is no substitute for this process. Bitcoin represents the world’s first rivalrous digital commodity, anchoring issuance to energy expended (for computation) in the physical world.

“There is no shortcut to these computations, which is why the physics inherent in computation—the very physical process of flipping bits—is undeniably embedded in the information that is produced.”—Gigi

However, unlike other commodities, bitcoin’s rate of issuance is predetermined and unaffected by fluctuations in the amount of energy employed in its production. This attribute is core to bitcoin’s attractiveness as money. Issuance is meritocratic, while supply is known, verifiable, and enforceable.

Miners expend computational power (converting electricity into hashes and dissipating heat) in the search for a random number known as a nonce. When combined with transaction data, the resulting hash can permit miners to collect a reward if it meets current parameters.

This process increases the settlement assurances of already confirmed transactions by increasing the cost of altering history.

Incurring real-world resource costs incentivizes miners to submit valid work to the network, especially when validation is trivial. Attempting to include an invalid transaction in a proposed block would quickly be detected and rejected by nodes, but the computational work performed would have already been sacrificed.

"Consensus mechanisms that don't involve work... instead involve governance."—Lyn Alden

Bitcoin’s proof of work consensus mechanism enables strangers to reach agreement without a third party, at regular intervals, as to which addresses contain bitcoin.

“Bitcoin is robust historical immutability by thermodynamic law. We only need one proof-of-work immutable ledger.”—Andreas Antonopoulos

Thermodynamics: 2nd Law

The entropy of the universe always increases with time.

—

Thermodynamic entropy can be considered a measure of a system’s disorder or randomness. Lower entropy, less randomness; higher entropy, more randomness.

The information about how the state of a system changes has to get observed, processed, and ultimately recorded somewhere.

Ordered systems in our world, such as a living human or the bitcoin blockchain, require constant input of energy

such that useful work can be conducted to build and maintain that order. The by-product of this process is heat which can no longer do any useful work. Taken together, the ordered system and the energy consumed to maintain that order, plus the waste heat produced, ultimately increase the entropy of the universe as a whole consistent with the 2nd law.

But this is a one-way process. You can’t combine heat with a human and get back the food they’ve already consumed. Similarly, with bitcoin's blockchain, the 2nd law ensures that the bitcoin clock can only run one way, and its past is increasingly locked in place by an ever-growing thermodynamic energy wall.

Arrow of Time

Establishing the one-way direction of time by distinguishing past from present.

—

A chain is a series of links. bitcoin forms a tamper-evident sequence of its history by consistently linking the most recent block to the second most recent. The information contained in each block acts like cement drying in layers, becoming harder to impact with time.

Block production occurs at consistent intervals, regardless of computational power directed at the network, thanks to an ingenious mechanism that adjusts the difficulty level of finding a nonce to meet a target rate.

"The only thing that is truly ticking in the Bitcoin network is the global clock: a block clock, where every block is one unit of time."—Gigi

The bitcoin protocol creates a consistent stream of information forged by energy conversion and locked by the 2nd law of thermodynamics. It provides us with the ability to distinguish the past from the present and independently establish the direction of time.

Information Theory

How digital information is communicated, stored, and quantified.

—

Information theory is the study of how digital information is communicated, stored, and quantified. At

its core, this concept is concerned with the ability of the receiver to accurately reconstruct a message when faced with anoisychannel (caused by external interference).

In the case of a monetary network, redundancy of information storage is critical. Bitcoin’s network of independent nodes enables retrieval, recreation, and validation of the entire chain with just one other peer.

This attribute enables the network to function without a central authority and increases the odds of network survivability.

"The fundamental problem of communication is that of reproducing at one point, either exactly or approximately, a message selected at another point."—Claude Shannon

Moore’s Law

The observation that the number of transistors on a computer chip doubles approximately every two years.

"Moore’s law is really about economics.”—Gordon Moore

—

Technology deflation is a beautiful thing. It enables us to reap the compounding benefits of innovation. Whether that means reducing the inputs required in a process or achieving increased performance from the same inputs.

The effect of microprocessors on every aspect of modern life is astonishing. They’ve radically altered how we behave and communicate and are gradually shifting how society has been structured since the Industrial Age.

Moore’s Law helps explain the exponential growth we’ve witnessed in computational power due to increasing density and falling costs over the last 50 years.

"The universal deployment of these increasingly powerful microprocessors.. has affected every sector of manufacturing, transportation, services, and communication.. accompanied by steadily declining costs and improving reliability."—Vaclav Smil

The bitcoin network benefits from this phenomenon as network nodes continue to proliferate around the world. If any monetary network is to be capable of resisting jurisdiction-specific attacks, it must achieve a certain threshold of decentralization among nodes that makes it infeasible to shut down.

Therefore, the ability to operate a node and independently verify transactions must be within reach for a sufficiently large number of people. The availability and the costs of necessary hardware are key factors in this.

"[microprocessors] have incubated a whole range of technologies that enhance the capacity of small groups and even individuals to function independently of central authority."—James Dale Davidson & William Rees-Mogg

Unlike miners, validating nodes don’t require top-of-the-line hardware or varying degrees of computational power. Additionally, the linear growth of the blockchain (in terms of memory) means that future storage needs are predictable and negligible.

Antifragility

Things that actively gain from volatility and unpredictability by using rapid feedback loops to evolve.

"Given the unattainability of perfect robustness, we need a mechanism by which the system regenerates itself continuously by using, rather than suffering from, random events, unpredictable shocks, stressors, and volatility.”—Nassim Taleb

—

The bitcoin network is not just difficult to kill, it actively becomes more resilient with each attempt (like muscle tissue repairing stronger after a strenuous workout). This is due to its peer-to-peer network architecture.

No single point of failure exists, as every full node possesses a valid history of the blockchain and all nodes exist on equal footing in the eyes of the protocol.

There are no special bitcoin nodes; all nodes are the same.”–Andreas Antonopoulos

Over time, the bitcoin network has grown in size (# of nodes) and become increasingly decentralized as a result. It is now capable of withstanding and hardening from nation-state-level attacks.

“When something is a decentralized, organic creature that is rapidly evolving and adapting, it becomes excessively antifragile because every time you kill it or an element of it, the elements you don’t kill get that much stronger.”—Michael Saylor

Gall’s Law

Incremental improvements made to a functional system is superior to building a complex system from scratch.

—

Taken from John Gall’s bookSystemantics: How Systems Really Work and How They Fail(1977), this heuristic explains the success behind the systems we take for granted today, which evolved from simple yet reliable foundations. The same attitude was (and continues to be) taken towards developing the bitcoin protocol. A steadfast foundation grows long-term confidence for investments of time, capital, and technology infrastructure adoption.

“Creeping featurism is the tendency to add to the number of features that a device can do, often extending the number beyond all reason.. But each new set of features adds immeasurably to the size and complexity of the system.”—Donald Norman

Complex systems are less able to respond with flexibility to entropy as one must take into account how any minor change will impact many individual components. In contrast, simple, functional systems may enable innovation (through iteration) as an extension, without risk to the underlying foundation.

“Bitcoin is too important to follow the Silicon Valley mantra of move fast and break things. Instead, it’s move slowly and don’t break anything. If a global financial system is to be built on a decentralized monetary system, the foundation must be protected at all cost.”—Parker Lewis
