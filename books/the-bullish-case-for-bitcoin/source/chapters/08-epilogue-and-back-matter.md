# Epilogue & Back Matter

## Source Metadata

- Chapter number: 8
- TOC index: 8
- Part: main
- EPUB src: text/part0017.html#G6PI0-a0ba76e649554092a63ebf0e62dbbf4e
- Extraction mode: spine-range

## Extracted Text

## The Great Debate

What is Bitcoin? This seemingly simple question and the debate that arose to answer it roiled the community of Bitcoin developers and investors for several years, culminating in a schism in the community and a split of the Bitcoin network on August 1, 2017. In the years after Satoshi Nakamoto created Bitcoin, two main ideological factions emerged, each supporting a different vision for its future. The first faction saw Bitcoin primarily as a payment system akin to Visa or PayPal, but without a centralized point of control. They emphasized the transactional use of Bitcoin and believed that money is defined primarily by its role as a medium of exchange. The second faction stressed the importance of Bitcoin being uncensorable and warned of the dangers of ceding control of Bitcoin’s protocol to any particular interest group. This faction envisioned Bitcoin as a digital version of gold, emphasizing its use as a nonsovereign store of value.

Complicating the contention between the two ideological factions was the disappearance of Bitcoin’s creator not long after its creation. On December 12, 2010, 772 days after first appearing online to publish the design of Bitcoin, Satoshi Nakamoto made his final post to an online Bitcoin forum. Nakamoto’s disappearance was of great consequence to the incipient software project that he had founded. Without its creator, the community of developers working on Bitcoin’s software had to continue their work without guidance or a common future vision. One of the clearest statements we have of Nakamoto’s aspirations for the project comes from his seminal publication, the “Bitcoin Whitepaper,” published on October 31, 2008. Yet that short document fails to decisively answer the question of whether Bitcoin should be thought of first as a medium of exchange or as a store of value. Despite writing hundreds of forum posts and emails to the community of developers working on Bitcoin, Satoshi never unambiguously explained its monetary nature. In some of his writing, Nakamoto emphasized Bitcoin’s similarity to gold and its use as a store of value:

[Bitcoin is] more typical of a precious metal. Instead of the supply changing to keep the value the same, the supply is predetermined and the value changes. As the number of users grows, the value per coin increases. It has the potential for a positive feedback loop; as users increase, the value goes up, which could attract more users to take advantage of the increasing value.45

On several other occasions Nakamoto discussed Bitcoin for use in payments, emphasizing the medium-of-exchange role of money.

Embryos of different species appear alike

In its embryonic form, Bitcoin appeared to embody each vision with equal plausibility. On the one hand, Bitcoin’s network began with low transaction fees, allowing bitcoins to be transferred at low cost around the world, seemingly providing a comparative advantage to alternative payments systems such as the Visa credit-card network. On the other hand, the exchange value of bitcoins increased significantly over time, suggesting it was a nascent store-of-value. But just as many species appear alike in their embryonic form, imprinted in their DNA are the instructions that will reveal their great differences in the fullness of time. Bitcoin’s DNA lay in the consensus rules of its protocol and, as we shall see, these rules would make it clear that only one of these visions for Bitcoin would be realizable.

## The Immutability of Protocols

A protocol is a set of rules that participants in a system must abide by when using the system. Examples of software protocols include TCP/IP, which governs how data is encoded and transmitted across the Internet, and SMTP, which governs email-specific Internet traffic. Protocols can also apply to the physical world; for instance, the IEC 60906-2 and NEMA 5-15 standards for power sockets describe the shape of electrical plugs plus the voltage and amperage of the power conducted through the sockets.

The ground slot is a backwards-compatible change to the original socket design

Protocols that are defined for use in software or hardware systems with many participants are usually very difficult to modify once in use, for good reason. Participants usually assume the immutability of a protocol when building businesses or devices that rely on it. Thus, changing a protocol for a widely used system would come at great cost to the ecosystem of participants who depend on it. Consider, for instance, the massive cost to North American households if the shape of power sockets were modified. Every socket in the nation would need to be updated, and every device that relied on the former socket shape would have to be discarded or provided with an adapter to use the new shape. An exception to the costliness of protocol updates are backwards-compatible changes that do not affect systems that use older versions of a protocol. For instance, the ground slot was invented in 1924 and provided a backwards-compatible update to sockets that reduced the risk of electrical shocks. Older devices with two-pronged electrical plugs were still able to use the newly designed sockets.

When Satoshi Nakamoto published the source code for Bitcoin on January 9, 2009, he had essentially produced a protocol for value transfer across the Internet. Nakamoto realized that once his design had come to life in a live, functioning network, it would be very difficult, if not impossible, to make non-backwards-compatible changes to the Bitcoin protocol. Commenting on this on June 17, 2010, Nakamoto observed that “Once version 0.1 was released, the core design was set in stone for the rest of its lifetime.”46

## The Schism

Bitcoin’s protocol is defined by rules that specify which messages sent on the Bitcoin network are valid and these rules are enforced by computers on the network that run the Bitcoin software. Computers that do not abide by the so-called consensus rules are rejected from the network. Most famous among the consensus rules is the rule that determines how many new bitcoins may be minted per block. The block-subsidy rule defines Bitcoin’s overall inflation schedule and limits the eventual total supply to no more than 21 million bitcoins. Another important rule is the maximum size of each block, which limits the total number of transactions that can be processed each time a new block is mined. This rule was originally created in 2010 as a means of hindering denial-of-service attacks to the budding network.47

Bitcoin’s block-size rule was the main point of contention between the two factions debating the future of Bitcoin. One faction, referred to as big-blockers, wanted Bitcoin’s protocol changed so that the block size was larger and could accommodate more transactions. Crucially, the proposed change would not be backwards-compatible and would cause a split in the network unless all network participants adopted it unanimously and at the same time. Big-blockers viewed Bitcoin as a piece of software, such as Microsoft Word, that should be upgraded frequently to satisfy the desires of businesses using it primarily for transactional purposes. The other faction, referred to as small-blockers, resisted such a change and cautioned that it would place control of Bitcoin in the hands of the companies that were pushing for the ostensible upgrade. They also warned that increasing the block size would diminish Bitcoin’s decentralization by necessitating the use of more costly hardware, driving less affluent participants away from the network. Small-blockers viewed Bitcoin not as a piece of software but as a protocol and emphasized the cost to the ecosystem that would come from modifying its rules. Even more importantly, small-blockers recognized that if it became easy to change one consensus rule, then all rules, including Bitcoin’s block subsidy rule, would be easier to modify. Because demand for Bitcoin as a store of value rests largely on the credibility of its fixed-supply monetary policy, changing Bitcoin’s block size would indirectly undermine that credibility.

The fierce debate between Bitcoin’s two factions came to a head on August 1, 2017 when the big-blocker faction modified the software running on their computers to accommodate larger blocks, thus making it incompatible with the rest of Bitcoin’s network. Computers running the new software were rejected from the original Bitcoin network and formed a second network of their own in a process known as a fork. The second network was known as Bitcoin Cash and had its own separate tokens that could be traded on the market. The question of Bitcoin’s future then shifted from a debate internal to the Bitcoin community to the marketplace where bitcoins, using the exchange symbol BTC, and Bitcoin Cash tokens, using the symbol BCH, would trade against each other in an economic test of which vision would attract the greatest investor demand. In the following years, the market overwhelmingly voted in favor of the original network and a vision of Bitcoin as a nonsovereign store of value. The Bitcoin Cash network faded into irrelevance, and its small community was wracked by continued infighting and further schisms.

## Denouement

The market’s support for the Bitcoin network with its original consensus rules made clear that Bitcoin’s value lies more in its existence as a largely immutable protocol than as an upgradeable piece of software. As a protocol with fixed consensus rules, Bitcoin’s block size and the number of transactions that can be supported per block will remain limited. Growing adoption of Bitcoin will result in increasing demand for the limited space per block for transactions, implying that transaction fees must rise over time. Bitcoin’s network will thus become uneconomical for small payments such as the purchase of coffee or bread but will remain suitable for settlement of the type of large value transfers that underpin a global financial system. Smaller payments with bitcoins will happen on layers built on top of the Bitcoin network such as the Lightning network or custodial transfer layers like banks. Hal Finney, the brilliant cryptographer who was first to recognize the potential of Satoshi Nakamoto’s invention, wrote in 2010:

Bitcoin itself cannot scale to have every single financial transaction in the world be broadcast to everyone and included in the block chain. There needs to be a secondary level of payment systems which is lighter weight and more efficient. … I believe this will be the ultimate fate of Bitcoin, to be the “high-powered money” that serves as a reserve currency for banks that issue their own digital cash.48

Finney implicitly recognized that Bitcoin would first need to be established as a store of value, or reserve currency as he called it. Once established, bitcoins could be used for everyday payments using higher-layer systems. He understood that Bitcoin would not serve as a payment system competing directly with Visa or PayPal, but as something far more significant: a nonsovereign store of value that would function as the monetary base for a new global financial system. This was the fate written into Bitcoin’s DNA—its consensus rules—from the very beginning.

## Acknowledgments

When I began writing The Bullish Case for Bitcoin as a long-form article in early 2017, the price of Bitcoin hovered around $1,000 and I hoped the article might help to explain the economic importance of this revolutionary technology to a few friends and perhaps even some Wall Street investors. I did not anticipate that the article would eventually be read by hundreds of thousands of people around the world and be translated into twenty different languages by volunteers. This unexpected readership can be explained in part by a growing demand to understand Bitcoin and its significance, but it can also be attributed to the invaluable help I received in crafting a text that is accessible and interesting to the layperson. In this regard I wish to express my gratitude to those who contributed to the creation of the original article and to the completion of this book, which it significantly expands upon.

First, I would like to thank Michael Saylor for writing the foreword to this book and for his generous efforts in providing free educational content through his charity, Saylor Academy. Second, I would like to thank @BitcoinUltras, a pseudonymous artist that I met on Twitter, who volunteered to create the cover art and the beautiful art that adorns each chapter. Third, I would like to thank my friend Sanjay Mavinkurve who generously created the charts for this book, which epitomize the aphorism that a picture is worth a thousand words. I would like to thank Daniel Coleman, Michael Hartl, Ben Davenport, Mat Balez, and Stephan Kinsella for the diligence they showed in editing my manuscript. Numerous people provided feedback that improved the clarity of my writing, and for this I wish to thank Alex Morcos, John Pfeffer, Pierre Rochard, Koen Swinkels, Ray Boyapati, Michael Angelo, Patri Friedman, Ardian Tola, and Michael Flaxman.

Finally, and most importantly, I wish to thank my wife Lisa for helping me to see this project through and for providing me with the three greatest inspirations in my life, my darling children.

## Disclaimer

The views presented in this book and any errors herein are my own. This book is for information purposes only. It is not intended to be investment advice. Seek a duly licensed professional for investment advice.

## About the Author

Born and raised in Australia, Vijay Boyapati moved to the United States in 2000 to pursue a PhD in Computer Science. Instead of enrolling in a doctoral program, Boyapati ended up at a small startup called Google where he spent several years using his background in machine learning to improve the ranking algorithms used in Google News. Boyapati left his lucrative job in 2007 to work on a grassroots campaign in the 2008 Presidential election, helping to raise millions of dollars and bring hundreds of volunteers to New Hampshire to canvass for Ron Paul. In 2011, Boyapati discovered Bitcoin and went down the proverbial rabbit hole in a quest to understand how a new form of Internet money, backed by no commodity and guaranteed by no government, could have any economic value. Armed with a background in Austrian economics, Boyapati penned “The Bullish Case for Bitcoin” as a long-form article in 2017 to provide the layperson with an economic framework with which they could understand Bitcoin.

Vijay Boyapati has a Bachelor of Science with first class honors from the Australian National University, receiving the University’s highest undergraduate honor, the University Medal. He is a husband and loving father of Addie, Will, and Vivi. He lives with his family in Seattle, Washington.

1 http://bullishcaseforbitcoin.com/references/bitcoin-announcement

2 http://bullishcaseforbitcoin.com/references/finney-skepticism

3 http://bullishcaseforbitcoin.com/references/anarchist-manifesto

4 http://bullishcaseforbitcoin.com/references/szabo-bit-gold

5 http://bullishcaseforbitcoin.com/references/white-paper

6 http://bullishcaseforbitcoin.com/references/shelling-out

7 http://bullishcaseforbitcoin.com/references/nash-equilibrium

8 http://bullishcaseforbitcoin.com/references/lord-keynes-quote

9 http://bullishcaseforbitcoin.com/references/anti-fragility

10 http://bullishcaseforbitcoin.com/references/fake-gold

11 http://bullishcaseforbitcoin.com/references/deep-sea-mining

12 http://bullishcaseforbitcoin.com/references/asteroid-mining

13 http://bullishcaseforbitcoin.com/references/hoxne-hoard

14 http://bullishcaseforbitcoin.com/references/lindy-effect

15 http://bullishcaseforbitcoin.com/references/mtgox-forensics

16 http://bullishcaseforbitcoin.com/references/india-gold-act

17 http://bullishcaseforbitcoin.com/references/jevons-quote

18 http://bullishcaseforbitcoin.com/references/pizza-story

19 http://bullishcaseforbitcoin.com/references/path-dependence

20 http://bullishcaseforbitcoin.com/references/josh-brown-quote

21 http://bullishcaseforbitcoin.com/references/leigh-drogen-quote

22 http://bullishcaseforbitcoin.com/references/speculative-adoption-theory

23 http://bullishcaseforbitcoin.com/references/willy-woo-data

24 http://bullishcaseforbitcoin.com/references/gradwell-quote

25 http://bullishcaseforbitcoin.com/references/benchmarking-study

26 http://bullishcaseforbitcoin.com/references/wsj-quote

27 http://bullishcaseforbitcoin.com/references/hyperbitcoinization

28 http://bullishcaseforbitcoin.com/references/unit-bias

29 http://bullishcaseforbitcoin.com/references/mccook-article

30 http://bullishcaseforbitcoin.com/references/gold-mining-impact

31 http://bullishcaseforbitcoin.com/references/hydro-article

32 http://bullishcaseforbitcoin.com/references/coinshares-paper-1

33 http://bullishcaseforbitcoin.com/references/satoshi-electricity-quote

34 http://bullishcaseforbitcoin.com/references/venezuela-story

35 http://bullishcaseforbitcoin.com/references/quantum-computing

36 http://bullishcaseforbitcoin.com/references/manchin-letter

37 http://bullishcaseforbitcoin.com/references/too-big-to-cheat-paper

38 http://bullishcaseforbitcoin.com/references/coinshares-paper-2

39 http://bullishcaseforbitcoin.com/references/volcker-inflation-fighting

40 http://bullishcaseforbitcoin.com/references/imf-rehypothecation-article

41 http://bullishcaseforbitcoin.com/references/bitmex-story

42 http://bullishcaseforbitcoin.com/references/satoshi-hearn-email

43 http://bullishcaseforbitcoin.com/references/hal-finney-quote

44 http://bullishcaseforbitcoin.com/references/degaulle-speech

45 http://bullishcaseforbitcoin.com/references/satoshi-gold-quote

46 http://bullishcaseforbitcoin.com/references/satoshi-protocol-quote

47 http://bullishcaseforbitcoin.com/references/theymos-dos-quote

48 http://bullishcaseforbitcoin.com/references/finney-second-layer-quote

www.BullishCaseForBitcoin.com
