# Technology A

## Source Metadata

- Chapter number: 6
- TOC index: 17
- Part: main
- EPUB src: OEBPS/part0037.xhtml
- Extraction mode: spine-range

## Extracted Text

Part III Technology

Technology

“Now, I’ll manage better this time” she said to herself, and began by taking the little golden key, and unlocking the door that led into the garden

– Lewis Carroll, Alice in Wonderland

Golden keys, clocks which only work by chance, races to solve strange riddles, and builders that don’t have faces or names. What sounds like fairy tales from Wonderland is daily business in the world of Bitcoin.

As we explored in Chapter II, large parts of the current financial system are systematically broken. Like Alice, we can only hope to manage better this time. But, thanks to a pseudonymous inventor, we have incredibly sophisticated technology to support us this time around: Bitcoin.

Solving problems in a radically decentralized and adversarial environment requires unique solutions. What would otherwise be trivial problems to solve are everything but in this strange world of nodes. Bitcoin relies on strong cryptography for most solutions, at least if looked at through the lens of technology. Just how strong this cryptography is will be explored in one of the following lessons.

Cryptography is what Bitcoin uses to remove trust in authorities. Instead of relying on centralized institutions, the system relies on the final authority of our universe: physics. Some grains of trust still remain, however. We will examine these grains in the second lesson of this chapter.

Part III – Technology:

- Strength in numbers

- Reflections on “Don’t Trust, Verify”

- Telling time takes work

- Move slowly and don’t break things

- Privacy is not dead

- Cypherpunks write code

- Metaphors for Bitcoin’s future

The last couple of lessons explore the ethos of technological development in Bitcoin, which is arguably as important as the technology itself. Bitcoin is not the next shiny app on your phone. It is the foundation of a new economic reality, which is why Bitcoin should be treated as nuclear-grade financial software.

Where are we in this financial, societal, and technological revolution? Networks and technologies of the past may serve as metaphors for Bitcoins future, which are explored in the last lesson of this chapter.

Once more, strap in and enjoy the ride. Like all exponential technologies, we are about to go parabolic.

15 Strength in Numbers

“Let me see: four times five is twelve, and four times six is thirteen, and four times seven is fourteen—oh dear! I shall never get to twenty at this rate!”

– Lewis Carroll, Alice in Wonderland

Numbers are an essential part of our everyday life. Large numbers, however, aren’t something most of us are too familiar with. The largest numbers we might encounter in everyday life are in the range of millions, billions, or trillions. We might read about millions of people in poverty, billions of dollars spent on bank bailouts, and trillions of national debt. Even though it’s hard to make sense of these headlines, we are somewhat comfortable with the size of those numbers.

Although we might seem comfortable with billions and trillions, our intuition already starts to fail with numbers of this magnitude. Do you have an intuition how long you would have to wait for a million/billion/trillion seconds to pass? If you are anything like me, you are lost without actually crunching the numbers.

Let’s take a closer look at this example: the difference between each is an increase by three orders of magnitude: 106, 109, 1012. Thinking about seconds is not very useful, so let’s translate this into something we can wrap our head around:

- 106: One million seconds was 11∕2 weeks ago.

- 109: One billion seconds was almost 32 years ago.

- 1012: One trillion seconds ago Manhattan was covered under a thick layer of ice.57

Figure 15.1:About 1 trillion seconds ago. Source: xkcd 1225

As soon as we enter the beyond-astronomical realm of modern cryptography, our intuition fails catastrophically. Bitcoin is built around large numbers and the virtual impossibility of guessing them. These numbers are way, way larger than anything we might encounter in day-to-day life. Many orders of magnitude larger. Understanding how large these numbers truly are is essential to understanding Bitcoin as a whole.

Let’s take SHA-25658, one of the hash functions59 used in Bitcoin, as a concrete example. It is only natural to think about 256 bits as “two hundred fifty-six,” which isn’t a large number at all. However, the number in SHA-256 is talking about orders of magnitude — something our brains are not well-equipped to deal with.

While bit length is a convenient metric, the true meaning of 256-bit security is lost in translation. Similar to the millions (106) and billions (109) above, the number in SHA-256 is about orders of magnitude (2256).

So, how strong is SHA-256, exactly?

“SHA-256 is very strong. It’s not like the incremental step from MD5 to SHA1. It can last several decades unless there’s some massive breakthrough attack.”

– Satoshi Nakamoto60

Let’s spell things out. 2256 equals the following number:

115 quattuorvigintillion 792 trevigintillion 89 duovigintillion 237 unvigintillion 316 vigintillion 195 novemdecillion 423 octodecillion 570 septendecillion 985 sexdecillion 8 quindecillion 687 quattuordecillion 907 tredecillion 853 duodecillion 269 undecillion 984 decillion 665 nonillion 640 octillion 564 septillion 39 sextillion 457 quintillion 584 quadrillion 7 trillion 913 billion 129 million 639 thousand 936.

That’s a lot of nonillions! Wrapping your head around this number is pretty much impossible. There is nothing in the physical universe to compare it to. It is far larger than the number of atoms in the observable universe. The human brain simply isn’t made to make sense of it.

One of the best visualizations of the true strength of SHA-256 is a video by Grant Sanderson. Aptly named “How secure is 256 bit security?”61 it beautifully shows how large a 256-bit space is. Do yourself a favor and take the five minutes to watch it. As all other 3Blue1Brownvideos it is not only fascinating but also exceptionally well made. Warning: You might fall down a math rabbit hole.

Figure 15.2:Illustration of SHA-256 security. Original graphic by Grant Sanderson aka 3Blue1Brown.

Bruce Schneier [66] used the physical limits of computation to put this number into perspective: even if we could build an optimal computer, which would use any provided energy to flip bits perfectly [87], build a Dyson sphere62 around our sun, and let it run for 100 billion billion years, we would still only have a 25% chance to find a needle in a 256-bit haystack.

“These numbers have nothing to do with the technology of the devices; they are the maximums that thermodynamics will allow. And they strongly imply that brute-force attacks against 256-bit keys will be infeasible until computers are built from something other than matter and occupy something other than space.”

– Bruce Schneier63

It is hard to overstate the profoundness of this. Strong cryptography inverts the power-balance of the physical world we are so used to. Unbreakable things do not exist in the real world. Apply enough force, and you will be able to open any door, box, or treasure chest.

Bitcoin’s treasure chest is very different. It is secured by strong cryptography, which does not give way to brute force. And as long as the underlying mathematical assumptions hold, brute force is all we have. Granted, there is also the option of a global $5 wrench attack (Figure 15.3) But torture won’t work for all bitcoin addresses, and the cryptographic walls of bitcoin will defeat brute force attacks. Even if you come at it with the force of a thousand suns. Literally.

Figure 15.3:$5 wrench attack. Source: xkcd 538

This fact and its implications were poignantly summarized in the call to cryptographic arms: “No amount of coercive force will ever solve a math problem.”

“It isn’t obvious that the world had to work this way. But somehow the universe smiles on encryption.”

– Julian Assange64

Nobody yet knows for sure if the universe’s smile is genuine or not. It is possible that our assumption of mathematical asymmetries is wrong and we find that P actually equals NP [95], or we find surprisingly quick solutions to specific problems [79] which we currently assume to be hard. If that should be the case, cryptography as we know it will cease to exist, and the implications would most likely change the world beyond recognition.

“Vires in Numeris” = “Strength in Numbers”65

Vires in numerisis not only a catchy motto used by bitcoiners. The realization that there is an unfathomable strength to be found in numbers is a profound one. Understanding this, and the inversion of existing power balances which it enables changed my view of the world and the future which lies ahead of us.

One direct result of this is the fact that you don’t have to ask anyone for permission to participate in Bitcoin. There is no page to sign up, no company in charge, no government agency to send application forms to. Simply generate a large number and you are pretty much good to go. The central authority of account creation is mathematics. And God only knows who is in charge of that.

Figure 15.4:Elliptic curve examples. Graphic cc-by-sa Emmanuel Boutet.

Bitcoin is built upon our best understanding of reality. While there are still many open problems in physics, computer science, and mathematics, we are pretty sure about some things. That there is an asymmetry between finding solutions and validating the correctness of these solutions is one such thing. That computation needs energy is another one. In other words: finding a needle in a haystack is harder than checking if the pointy thing in your hand is indeed a needle or not. And finding the needle takes work.

The vastness of Bitcoin’s address space is truly mind-boggling. The number of private keys even more so. It is fascinating how much of our modern world boils down to the improbability of finding a needle in an unfathomably large haystack. I am now more aware of this fact than ever.

Bitcoin taught me that there is strength in numbers.

16 Reflections on “Don’t Trust, Verify”

“Now for the evidence,” said the King, “and then the sentence.”

– Lewis Carroll, Alice in Wonderland

Bitcoin aims to replace, or at least provide an alternative to, conventional currency. Conventional currency is bound to a centralized authority, no matter if we are talking about legal tender like the US dollar or modern monopoly money like Fortnite’s V-Bucks. In both examples, you are bound to trust the central authority to issue, manage and circulate your money. Bitcoin unties this bound, and the main issue Bitcoin solves is the issue of trust.

“The root problem with conventional currency is all the trust that’s required to make it work. [...] What is needed is an electronic payment system based on cryptographic proof instead of trust”

– Satoshi Nakamoto66

Bitcoin solves the problem of trust by being completely decentralized, with no central server or trusted parties. Not even trusted thirdparties, but trusted parties, period. When there is no central authority, there simply isno-one to trust. Complete decentralization is the innovation. It is the root of Bitcoin’s resilience, the reason why it is still alive. Decentralization is also why we have mining, nodes, hardware wallets, and yes, the blockchain. The only thing you have to “trust” is that our understanding of mathematics and physics isn’t totally off and that the majority of miners act honestly (which they are incentivized to do).

While the regular world operates under the assumption of “trust, but verify,”Bitcoin operates under the assumption of “don’t trust, verify.”Satoshi made the importance of removing trust very clear in both the introduction as well as the conclusion of the Bitcoin whitepaper.

“Conclusion: We have proposed a system for electronic transactions without relying on trust.”

– Satoshi Nakamoto67

Note that without relying on trustis used in a very specific context here. We are talking about trusted third parties, i.e. other entities which you trust to produce, hold, and process your money. It is assumed, for example, that you can trust your computer.

As Ken Thompson showed in his Turing Award lecture, trust is an extremely tricky thing in the computational world. When running a program, you have to trust all kinds of software (and hardware) which, in theory, could alter the program you are trying to run in a malicious way. As Thompson summarized in his Reflections on Trusting Trust: “The moral is obvious. You can’t trust code that you did not totally create yourself.” [71]

Figure 16.1:Excerpts from Ken Thompson’s paper ‘Reflections on Trusting Trust’

Thompson demonstrated that even if you have access to the source code, your compiler — or any other program-handling program or hardware — could be compromised and detecting this backdoor would be very difficult. Thus, in practice, a truly trustless system does not exist. You would have to create all your software andall your hardware (assemblers, compilers, linkers, etc.) from scratch, without the aid of any external software or software-aided machinery.

“If you wish to make an apple pie from scratch, you must first invent the universe.”

– Carl Sagan68

The Ken Thompson Hack is a particularly ingenious and hard-to-detect backdoor, so let’s take a quick look at a hard-to-detect backdoor which works without modifying any software. Researchers found a way to compromise security-critical hardware by altering the polarity of silicon impurities. [9] Just by changing the physical properties of the stuff that computer chips are made of they were able to compromise a cryptographically secure random number generator. Since this change can’t be seen, the backdoor can’t be detected by optical inspection, which is one of the most important tamper-detection mechanism for chips like these.

Figure 16.2:Stealthy Dopant-Level Hardware Trojans by Becker, Regazzoni, Paar, Burleson

Sounds scary? Well, even if you would be able to build everything from scratch, you would still have to trust the underlying mathematics. You would have to trust that secp256k1is an elliptic curve without backdoors. Yes, malicious backdoors can be inserted in the mathematical foundations of cryptographic functions and arguably this has already happened at least once. [80] There are good reasons to be paranoid, and the fact that everything from your hardware, to your software, to the elliptic curves used can have backdoors [82] are some of them.

“Don’t trust. Verify.”

– Bitcoiners everywhere

The above examples should illustrate that trustlesscomputing is utopic. Bitcoin is probably the one system which comes closest to this utopia, but still, it is trust-minimized— aiming to remove trust wherever possible. Arguably, the chain-of-trust is neverending, since you will also have to trust that computation requires energy, that P does not equal NP, and that you are actually in base reality and not imprisoned in a simulation by malicious actors.

Developers are working on tools and procedures to minimize any remaining trust even further. For example, Bitcoin developers created Gitian69, which is a software distribution method to create deterministic builds. The idea is that if multiple developers are able to reproduce identical binaries, the chance of malicious tampering is reduced. Fancy backdoors aren’t the only attack vector. Simple blackmail or extortion are real threats as well. As in the main protocol, decentralization is used to minimize trust.

Various efforts are being made to improve upon the chicken-and-egg problem of bootstrapping which Ken Thompson’s hack so brilliantly pointed out [20]. One such effort is Guix70 (pronounced geeks), which uses functionally declared package management leading to bit-for-bit reproducible builds by design. The result is that you don’t have to trust any software-providing servers anymore since you can verify that the served binary was not tampered with by rebuilding it from scratch. Recently, a pull-request was merged to integrate Guix into the Bitcoin build process.71

Figure 16.3:Which came first, the chicken or the egg?

Luckily, Bitcoin doesn’t rely on a single algorithm or piece of hardware. One effect of Bitcoin’s radical decentralization is a distributed security model. Although the backdoors described above are not to be taken lightly, it is unlikely that every software wallet, every hardware wallet, every cryptographic library, every node implementation, and every compiler of every language is compromised. Possible, but highly unlikely.

Note that you can generate a private key without relying on any computational hardware or software. You can flip a coin [4] a couple of times, although depending on your coin and tossing style this source of randomness might not be sufficiently random. There is a reason why storage protocols like Glacier72 advise to use casino-grade dice as one of two sources of entropy.

Bitcoin forced me to reflect on what trusting nobody actually entails. It raised my awareness of the bootstrapping problem, and the implicit chain-of-trust in developing and running software. It also raised my awareness of the many ways in which software and hardware can be compromised.

Bitcoin taught me not to trust, but to verify.
