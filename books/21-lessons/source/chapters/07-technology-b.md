# Technology B

## Source Metadata

- Chapter number: 7
- TOC index: 19
- Part: main
- EPUB src: OEBPS/part0042.xhtml
- Extraction mode: spine-range

## Extracted Text

17 Telling Time Takes Work

“Dear, dear! I shall be too late!”

– Lewis Carroll, Alice in Wonderland

It is often said that bitcoins are mined because thousands of computers work on solving very complexmathematical problems. Certain problems are to be solved, and if you compute the right answer, you “produce” a bitcoin. While this simplified view of bitcoin mining might be easier to convey, it does miss the point somewhat. Bitcoins aren’t produced or created, and the whole ordeal is not really about solving particular math problems. Also, the math isn’t particularly complex. What is complex is telling the timein a decentralized system.

As outlined in the whitepaper, the proof-of-work system (aka mining) is a way to implement a distributed timestamp server.

Figure 17.1:Excerpts from the whitepaper. Did someone say timechain?

When I first learned how Bitcoin works I also thought that proof-of-work is inefficient and wasteful. After a while, I started to shift my perspective on Bitcoin’s energy consumption [29]. It seems that proof-of-work is still widely misunderstood today, in the year 10 AB (after Bitcoin).

Since the problems to be solved in proof-of-work are made up, many people seem to believe that it is uselesswork. If the focus is purely on the computation, this is an understandable conclusion. But Bitcoin isn’t about computation. It is about independently agreeing on the order of things.

Proof-of-work is a system in which everyone can validate what happened and in what order it happened. This independent validation is what leads to consensus, an individual agreement by multiple parties about who owns what.

In a radically decentralized environment, we don’t have the luxury of absolute time. Any clock would introduce a trusted third party, a central point in the system which had to be relied upon and could be attacked. “Timing is the root problem,” as Grisha Trubetskoy points out [73]. And Satoshi brilliantly solved this problem by implementing a decentralized clock via a proof-of-work blockchain. Everyone agrees beforehand that the chain with the most cumulative work is the source of truth. It is per definition what actually happened. This agreement is what is now known as Nakamoto consensus.

“The network timestamps transactions by hashing them into an ongoing chain which serves as proof of the sequence of events witnessed”

– Satoshi Nakamoto73

Without a consistent way to tell the time, there is no consistent way to tell before from after. Reliable ordering is impossible. As mentioned above, Nakamoto consensus is Bitcoin’s way to consistently tell the time. The system’s incentive structure produces a probabilistic, decentralized clock, by utilizing both greed and self-interest of competing participants. The fact that this clock is imprecise is irrelevant because the order of events is eventually unambiguous and can be verified by anyone.

Thanks to proof-of-work, both the work andthe validation of the work are radically decentralized. Everyone can join and leave at will, and everyone can validate everything at all times. Not only that, but everyone can validate the state of the system individually, without having to rely on anyone else for validation.

Understanding proof-of-work takes time. It is often counter-intuitive, and while the rules are simple, they lead to quite complex phenomena. For me, shifting my perspective on mining helped. Useful, not useless. Validation, not computation. Time, not blocks.

Bitcoin taught me that telling the time is tricky, especiallyif you are decentralized.

18 Move Slowly and Don’t Break Things

So the boat wound slowly along, beneath the bright summer-day, with its merry crew and its music of voices and laughter…

– Lewis Carroll, Alice in Wonderland

It might be a dead mantra, but “move fast and break things” is still how much of the tech world operates. The idea that it doesn’t matter if you get things right the first time is a basic pillar of the fail early, fail oftenmentality. Success is measured in growth, so as long as you are growing everything is fine. If something doesn’t work at first you simply pivot and iterate. In other words: throw enough shit against the wall and see what sticks.

Bitcoin is very different. It is different by design. It is different out of necessity. As Satoshi pointed out, e-currency has been tried many times before, and all previous attempts have failed because there was a head which could be cut off. The novelty of Bitcoin is that it is a beast without heads.

“A lot of people automatically dismiss e-currency as a lost cause because of all the companies that failed since the 1990’s. I hope it’s obvious it was only the centrally controlled nature of those systems that doomed them.”

– Satoshi Nakamoto74

One consequence of this radical decentralization is an inherent resistance to change. “Move fast and break things” does not and will never work on the Bitcoin base layer. Even if it would be desirable, it wouldn’t be possible without convincing everyoneto change their ways. That’s distributed consensus. That’s the nature of Bitcoin.

“The nature of Bitcoin is such that once version 0.1 was released, the core design was set in stone for the rest of its lifetime.”

– Satoshi Nakamoto75

This is one of the many paradoxical properties of Bitcoin. We all came to believe that anything which is software can be changed easily. But the nature of the beast makes changing it bloody hard.

As Hasu beautifully shows in Unpacking Bitcoin’s Social Contract [32], changing the rules of Bitcoin is only possible by proposinga change, and consequently convincingall users of Bitcoin to adopt this change. This makes Bitcoin very resilient to change, even though it is software.

This resilience is one of the most important properties of Bitcoin. Critical software systems have to be antifragile, which is what the interplay of Bitcoin’s social layer and its technical layer guarantees. Monetary systems are adversarial by nature, and as we have known for thousands of years solid foundations are essential in an adversarial environment.

“The rain came down, the floods came, and the winds blew, and beat on that house; and it didn’t fall, for it was founded on the rock.”

– Matthew 7:24–27

Arguably, in this parable of the wise and the foolish builders Bitcoin isn’t the house. It is the rock. Unchangeable, unmoving, providing the foundation for a new financial system.

Just like geologists, who know that rock formations are always moving and evolving, one can see that Bitcoin is always moving and evolving as well. You just have to know where to look and how to look at it.

The introduction of pay to script hash76 and segregated witness77 are proof that Bitcoin’s rules can be changed if enough users are convinced that adopting said change is to the benefit of the network. The latter enabled the development of the lightning network78, which is one of the houses being built on Bitcoin’s solid foundation. Future upgrades like Schnorr signatures [60] will enhance efficiency and privacy, as well as scripts (read: smart contracts) which will be indistinguishable from regular transactions thanks to Taproot [31]. Wise builders do indeed build on solid foundations.

Satoshi wasn’t only a wise builder technologically. He also understood that it would be necessary to make wise decisions ideologically.

“Being open source means anyone can independently review the code. If it was closed source, nobody could verify the security. I think it’s essential for a program of this nature to be open source.”

– Satoshi Nakamoto79

Openness is paramount to security and inherent in open source and the free software movement. As Satoshi pointed out, secure protocols and the code which implements them have to be open — there is no security through obscurity. Another benefit is again related to decentralization: code which can be run, studied, modified, copied, and distributed freely ensures that it is spread far and wide.

The radically decentralized nature of Bitcoin is what makes it move slowly and deliberately. A network of nodes, each run by a sovereign individual, is inherently resistant to change — malicious or not. With no way to force updates upon users the only way to introduce changes is by slowly convincing each and every one of those individuals to adopt a change. This non-central process of introducing and deploying changes is what makes the network incredibly resilient to malicious changes. It is also what makes fixing broken things more difficult than in a centralized environment, which is why everyone tries not to break things in the first place.

Bitcoin taught me that moving slowly is one of its features,not a bug.

19 Privacy is Not Dead

The players all played at once without waiting for turns, and quarrelled all the while at the tops of their voices, and in a very few minutes the Queen was in a furious passion, and went stamping about and shouting “off with his head!” of “off with her head!” about once in a minute.

– Lewis Carroll, Alice in Wonderland

If pundits are to believed, privacy has been dead since the 80ies80. The pseudonymous invention of Bitcoin and other events in recent history show that this is not the case. Privacy is alive, even though it is by no means easy to escape the surveillance state.

Satoshi went through great lengths to cover up his tracks and conceal his identity. Ten years later, it is still unknown if Satoshi Nakamoto was a single person, a group of people, male, female, or a time-traveling AI which bootstrapped itself to take over the world. Conspiracy theories aside, Satoshi chose to identify himself to be a Japanese male, which is why I don’t assume but respect his chosen gender and refer to him as he.

Figure 19.1:I am not Dorian Nakamoto.

Whatever his real identity might be, Satoshi was successful in hiding it. He set an encouraging example for everyone who wishes to remain anonymous: it is possible to have privacy online.

“Encryption works. Properly implemented strong crypto systems are one of the few things that you can rely on.”

– Edward Snowden81

Satoshi wasn’t the first pseudonymous or anonymous inventor, and he won’t be the last. Some have directly imitated this pseudonymous publication style, like Tom Elvis Yedusor of MimbleWimble [72] fame, while others have published advanced mathematical proofs while remaining completely anonymous [3].

It is a strange new world we are living in. A world where identity is optional, contributions are accepted based on merit, and people can collaborate and transact freely. It will take some adjustment to get comfortable with these new paradigms, but I strongly believe that all of this has the potential to change the world for the better.

We should all remember that privacy is a fundamental human right82. And as long as people exercise and defend these rights the battle for privacy is far from over.

Bitcoin taught me that privacy is not dead.

20 Cypherpunks Write Code

“I see you’re trying to invent something.”

– Lewis Carroll, Alice in Wonderland

Like many great ideas, Bitcoin didn’t come out of nowhere. It was made possible by utilizing and combining many innovations and discoveries in mathematics, physics, computer science, and other fields. While undoubtedly a genius, Satoshi wouldn’t have been able to invent Bitcoin without the giants on whose shoulders he was standing on.

“He who only wishes and hopes does not interfere actively with the course of events and with the shaping of his own destiny.”

– Ludwig von Mises83

One of these giants is Eric Hughes, one of the founders of the cypherpunk movement and author of A Cypherpunk’s Manifesto. It’s hard to imagine that Satoshi wasn’t influenced by this manifesto. It speaks of many things which Bitcoin enables and utilizes, such as direct and private transactions, electronic money and cash, anonymous systems, and defending privacy with cryptography and digital signatures.

“Privacy is necessary for an open society in the electronic age. [...] Since we desire privacy, we must ensure that each party to a transaction have knowledge only of that which is directly necessary for that transaction. [...] Therefore, privacy in an open society requires anonymous transaction systems. Until now, cash has been the primary such system. An anonymous transaction system is not a secret transaction system. [...] We the Cypherpunks are dedicated to building anonymous systems. We are defending our privacy with cryptography, with anonymous mail forwarding systems, with digital signatures, and with electronic money. Cypherpunks write code.”

– Eric Hughes84

Cypherpunks do not find comfort in hopes and wishes. They actively interfere with the course of events and shape their own destiny. Cypherpunks write code.

Thus, in true cypherpunk fashion, Satoshi sat down and started to write code. Code which took an abstract idea and proved to the world that it actually worked. Code which planted the seed of a new economic reality. Thanks to this code, everyone can verify that this novel system actually works, and every 10 minutes or so Bitcoin proofs to the world that it is still living.

Figure 20.1:Code excerpts from Bitcoin version 0.1

To make sure that his innovation transcends fantasy and becomes reality, Satoshi wrote code to implement his idea before he wrote the whitepaper. He also made sure not to delay85 any release forever. After all, “there’s always going to be one more thing to do.”

“I had to write all the code before I could convince myself that I could solve every problem, then I wrote the paper.”

– Satoshi Nakamoto86

In today’s world of endless promises and doubtful execution, an exercise in dedicated building was desperately needed. Be deliberate, convince yourself that you can actually solve the problems, and implement the solutions. We should all aim to be a bit more cypherpunk.

Bitcoin taught me that cypherpunks write code.

21 Metaphors for Bitcoin’s Future

“I know something interesting is sure to happen…”

– Lewis Carroll, Alice in Wonderland

In the last couple of decades, it became apparent that technological innovation does not follow a linear trend. Whether you believe in the technological singularity or not, it is undeniable that progress is exponential in many fields. Not only that, but the rate at which technologies are being adopted is accelerating, and before you know it the bush in the local schoolyard is gone and your kids are using Snapchat instead. Exponential curves have the tendency to slap you in the face way before you see them coming.

Bitcoin is an exponential technology built upon exponential technologies. Our World in Data87 beautifully shows the rising speed of technological adoption, starting in 1903 with the introduction of landlines (see Figure 21.1). Landlines, electricity, computers, the internet, smartphones; all follow exponential trends in price-performance and adoption. Bitcoin does too [22].

Figure 21.1:Bitcoin is literally off the charts.

Bitcoin has not one but multiple network effects88, all of which resulting in exponential growth patterns in their respective area: price, users, security, developers, market share, and adoption as global money.

Having survived its infancy, Bitcoin is continuing to grow every day in more aspects than one. Granted, the technology has not reached maturity yet. It might be in its adolescence. But if the technology is exponential, the path from obscurity to ubiquity is short.

Figure 21.2:Mobile phone, ca 1965 vs 2019.

In his 2003 TED talk, Jeff Bezos chose to use electricity as a metaphor for the web’s future.89 All three phenomena — electricity, the internet, Bitcoin — are enablingtechnologies, networks which enable other things. They are infrastructure to be built upon, foundational in nature.

Electricity has been around for a while now. We take it for granted. The internet is quite a bit younger, but most people already take it for granted as well. Bitcoin is ten years old and has entered public consciousness during the last hype cycle. Only the earliest of adopters take it for granted. As more time passes, more and more people will recognize Bitcoin as something which simply is.90

In 1994, the internet was still confusing and unintuitive. Watching this old recording of the Today Show91 makes it obvious that what feels natural and intuitive now actually wasn’t back then. Bitcoin is still confusing and alien to most, but just like the internet is second nature for digital natives, spending and stacking sats92 will be second nature to the bitcoin natives of the future.

“The future is already here — it’s just not very evenly distributed.”

– William Gibson93

In 1995, about 15% of American adults used the internet. Historical data from the Pew Research Center [27] shows how the internet has woven itself into all our lives. According to a consumer survey by Kaspersky Lab [40], 13% of respondents have used Bitcoin and its clones to pay for goods in 2018. While payments aren’t the only use-case of bitcoin, it is some indication of where we are in Internet time: in the early- to mid-90s.

In 1997, Jeff Bezos stated in a letter to shareholders [11] that “this is Day 1 for the Internet,” recognizing the great untapped potential for the internet and, by extension, his company. Whatever day this is for Bitcoin, the vast amounts of untapped potential are clear to all but the most casual observer.

Figure 21.3:The internet, 1982 vs 2005. Source: cc-by Merit Network, Inc. and Barrett Lyon, Opte Project

Bitcoin’s first node went online in 2009 after Satoshi mined the genesis block94 and released the software into the wild. His node wasn’t alone for long. Hal Finney was one of the first people to pick up on the idea and join the network. Ten years later, as of this writing, more than 75.00095 nodes are running bitcoin.

Figure 21.4:Hal Finney authored the first tweet mentioning bitcoin in January 2009.

The protocol’s base layer isn’t the only thing growing exponentially. The lightning network, a second layer technology, is growing at an even faster rate.

In January 2018, the lightning network had 40 nodes and 60 channels [103]. In April 2019, the network grew to more than 4000 nodes and around 40.000 channels. Keep in mind that this is still experimental technology where loss of funds can and does occur. Yet the trend is clear: thousands of people are reckless and eager to use it.

Figure 21.5:Lightning Network, January 2018 vs December 2018. Source: Jameson Lopp

To me, having lived through the meteoric rise of the web, the parallels between the internet and Bitcoin are obvious. Both are networks, both are exponential technologies, and both enable new possibilities, new industries, new ways of life. Just like electricity was the best metaphor to understand where the internet is heading, the internet might be the best metaphor to understand where bitcoin is heading. Or, in the words of Andreas Antonopoulos, Bitcoin is The Internet of Money. These metaphors are a great reminder that while history doesn’t repeat itself, it often rhymes.

Exponential technologies are hard to grasp and often underestimated. Even though I have a great interest in such technologies, I am constantly surprised by the pace of progress and innovation. Watching the Bitcoin ecosystem grow is like watching the rise of the internet in fast-forward. It is exhilarating.

My quest of trying to make sense of Bitcoin has led me down the pathways of history in more ways than one. Understanding ancient societal structures, past monies, and how communication networks evolved were all part of the journey. From the handaxe to the smartphone, technology has undoubtedly changed our world many times over. Networked technologies are especially transformational: writing, roads, electricity, the internet. All of them changed the world. Bitcoin has changed mine and will continue to change the minds and hearts of those who dare to use it.

Bitcoin taught me that understanding the past is essentialto understanding its future. A future which is justbeginning…
