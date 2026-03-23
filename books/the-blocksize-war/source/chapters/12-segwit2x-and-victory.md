# Chapter 20 + Chapter 21

## Source Metadata

- Chapter number: 12
- TOC index: 12
- Part: main
- EPUB src: text/part0022_split_000.html
- Extraction mode: spine-range

## Extracted Text

20

SegWit2x Most small blockers had been largely quiet when it came to their campaign against phase two of the NYA, hoping for phase one to occur successfully before engaging more aggressively. In August 2017, with SegWit safely locked in, the time came to step up the campaign against phase two. By this point in the conflict, in stark contrast to the start of the war, the small blockers had a clear and strong majority of users behind them. To all intents and purposes, the small blockers had persuaded a large bulk of the community and traders to join their ranks, through both the power of effecting argument and reasoning and the momentum and success they had achieved. Most people just wanted to back the winning side. As the conflict progressed, the main characters on the large block side had changed. In the first round, the small blockers had defeated Gavin Andresen and Mike Hearn, and then Roger Ver and Jihan Wu in round two. Finally, there was a third set of characters to defeat, Jeff Garzik and Mike Belshe. Jeff was the lead developer of the SegWit2x client and Mike, the CEO of BitGo, had somehow taken up the baton for the large block team. Roger Ver and Jihan Wu had mostly stepped back from the war at this point, instead focusing their efforts on promoting Bitcoin Cash. On August 3, 2017 a pull request was merged into Bitcoin Core, and the new code blocked BTC1 peers from making connections to Bitcoin Core.[148]Since the networks were expected to split anyway, it could be argued that this was a good move for both coins, allowing them to have stronger peering with nodes on the same network as them. However, Jeff Garzik was not happy at this and commented: This creates chain splits even though Bitcoin Core and segwit2x nodes are validating 100% the same rules today; it creates chain splits because of a presumed future rule deviation. The outcome is a bunch of non-deterministic islands. This is a very hostile and unsafe change prior to segwit2x fork deployment. Although, technically, this change to Bitcoin Core peering was an advantage for both coins in the event of the split, the political messaging here was clear. Bitcoin Core would not implement SegWit2x and would continue work on the existing Bitcoin chain. Another tactic used by the small blockers in order to try and persuade the community not to run BTC1 was to highlight apparent hypocrisy from Jeff Garzik. In 2012, Garzik appeared to articulate the small block narrative, making exactly the same points small blockers were stating today: 51% hashing power, or even 90%, means nothing if clients collectively refuse to accept and relay your blocks.[149] In February 2013, Garzik even talked about the economic significance of a hardfork and the problems associated with a lack of mandatory replay protection. This was particularly poignant for me, as it’s the first time I was exposed to many of these arguments. And now, ironically, here was the same person developing and promoting the client doing exactly what he had argued against around four years earlier. Of course, changing one’s mind over the course of time can be entirely legitimate, and this does not at all imply Jeff was being malicious or a hypocrite. However, this did cause small blockers to accuse Jeff of “selling out to the suits”. In February 2013, Jeff wrote: It is crucial to understand the concept and, yes, economic impact of a hard fork before even approaching the economic analysis of changing the max block size. A hard fork is a significant event that knocks legitimate users off the network, makes coins unspendable, or potentially makes the same coins spendable in two different locations, depending on whether or not you’re talking to an updated node. It is, to pick a dramatic term, an Extinction Level Event. If done poorly, a hard fork could make it impossible for reasonable merchants to trust the bitcoins they receive, the very foundation of their economic value. Furthermore, a hard fork is akin to a Constitutional Convention: a hard fork implies the ability to rewrite the ground rules of bitcoin, be it block size, 21M limit, SHA256 hash, or other hard-baked behavior. Thus, there is always the risk of unpredictable miners, users and devs changing more than just the block size precisely because it makes the most engineering sense to change other hard-to-change features at the time of hard-fork. It is a nuclear option with widespread economic consequences for all bitcoin users.[150] Another tactic of the small blockers was to work on the official list of SegWit2x supporters based on the NYA document. The plan was to arrange meetings and calls with the companies and to explain the flaws of the NYA; in particular, that it was causing a split which, unlike Bitcoin Cash, lacked mandatory replay protection, which would likely cause loss of funds. There was a long list of companies, and perhaps some of them did not understand the weaknesses of the NYA. If any of them defected, this would greatly undermine the NYA. It would show that the plan had negative momentum and lacked consensus even among the original signatories, let alone consensus from the wider community. The first defection occurred on August 22, 2017. Bitwala, announced that they would not follow the agreement: We have received an increasing number of inquiries regarding Bitwala’s support of the New York Agreement (short “NYA”). … The agreement helped surpass Segregated Witness activation thresholds prematurely so that the necessary soft fork went over without so much as a hitch. At much the same time, a number of miners decided to create a bitcoin fork on the basis of the same genesis block as bitcoin, naming this coin “Bitcoin Cash” (“BCH”) – removing Segregated Witness from that chain and implementing changes which included (among others) support for blocks of up to 8MB. … Bitwala doesn’t employ or sponsor bitcoin developers, so we have little influence over what the Core development team does. We would like to honor the agreement that we subscribed to (as one of the first movers, unbeknownst to the fact that most developers would not enter the agreement). We also, however, are a service company that has and will always follow what our customers use and want to use. … We will not actively fork away from what we view as “bitcoin”, which is the chain that is supported by the current Core dev team.[151] This was a significant moment in the battle against phase two of the NYA: the first defection. However, it was not a perfect defection. Bitwala appeared to want to follow the chain supported by the “current Core dev team”, rather than the existing rules chain, unless there is widespread support to change the rules. This fed into the misconception that this battle was developers vs the miners, and that Bitwala had chosen the developers’ side. Despite this large blocker framing of the conflict, small blockers still celebrated and accepted the win. Despite this defection, Mike Belshe was keen to keep pushing the project ahead and keep things on track. On August 23, 2017, he wrote to the SegWit2x mailing list, stating: As SegWit activates, this is a good time to send out a quick project update. You may have noticed that the SegWit2x team has been pretty quiet lately. That’s a good sign, as it indicates that the code is operating as expected. The goal of SegWit2x is to create a simple and stable codebase that is relatively “boring”. If you don’t hear much from the SegWit2x development in the coming weeks, it is a good sign.[152] On August 31, one of the mining pools which signed the agreement, F2Pool, announced its intention not to support SegWit2x. Although, at that point, the pool still had the “NYA” flag in its blocks, the pool operator Wang Chun said that the pool planned to remove the flag when it restarted its servers.[153]This was another critical defection from the NYA. With a large mining pool, the Bitcoin chain would progress forwards and, as long as investors preferred the original rules Bitcoin chain (which seemed likely at this point), more miners were likely to violate the agreement and mine original Bitcoin to ensure they earned higher profits. On September 1, the CEO and founder of another company which signed the NYA, Wayniloans, tweeted that they never agreed to all of the NYA and that the agreement changed after Wayniloans signed it. This was then confirmed by email a few weeks later, to which Barry Silbert replied, indicating a degree of disappointment: You are of course welcome to withdraw support for SegWit2x, but your statement below is not accurate. I have an email from you on Sunday, May 21 at 8:40 pm ET confirming support of the final, full statement that was published on May 23rd. Also, as a reminder, I was approached about adding Wayniloans to the agreement, not the other way around, so I have no idea what you were told.[154] The number of defections started increasing at this point. On September 26, 2017, Vaultoro defected: We signed way before Bcash fork. Signed because I wanted to help dislodge the stalemate between camps. It worked, we now have segwit. As any good businessman, I stick to my word / signature and would have followed through with 2x but I cannot without replay protection.[155] South American exchange surBTC also retracted their support for the NYA: Nevertheless, we can’t pretend to be bitcoin “scaling experts”. We don’t believe in trying to force a change bitcoin’s core developers don’t feel safe with. The technical background of the team that currently collaborates on the core bitcoin project has an unprecedented level, we believe them to be, at least as a group, unbiased experts who deserve at least a voice on the subject. Even though we would be happy to have moderately larger blocks to accommodate growing demand, we feel that Bitcoin needs (at least a majority) of bitcoin’s core developers’ support in order to do this responsibly. We haven’t seen this support and we don’t like what we currently see on the btc1 code repository in terms of technical considerations and open source collaboration.[156] UK-based exchange Crypto Facilities then left the agreement. The CEO of Kraken, the company that would eventually buy Crypto Facilities, also indicated opposition to SegWit2x due to the lack of replay protection.[157]Another signatory, Bitfury, also indicated it was potentially not willing to go through with phase two of the NYA.[158]It was now almost impossible to keep track of all the defections, and the agreement appeared to be falling apart. There were also defections from the large block side of the camp. Another signatory, Yours, announced it was switching entirely to the Bitcoin Cash chain.[159]Bitmain’s main in-house mining pool, Antpool, had also started mining Bitcoin Cash. Of course, one could argue that supporting or mining Bitcoin Cash is not reneging on the agreement. One could say it’s entirely legitimate for businesses to mine multiple coins in order to generate earnings or support coins on multiple chains. This is, of course, normal and acceptable business. However, if it was the case that signatories could continue to support the two coins after the split and miners were free to mine on both sides of the split, one could also argue that the NYA was largely meaningless and two chains would survive. This, the small blockers argued, was why mandatory replay protection was necessary, and without it, SegWit2x was potentially hostile and should therefore not be supported by responsible businesses. In spite of the fact that prospects of SegWit2x were rapidly diminishing and the demands for replay protection were getting stronger, on October 8, 2017, Mike Belshe continued to push ahead: “Replay protection”, as you call it, splits the chain. It simply doesn’t make sense- you’d suddenly be breaking 10+million SPV clients that otherwise work just fine. It is a goal of segwit2x to help avoid this. Today, we’re on course to deploy segwit2x with a vast majority of miners still signaling for it. On top of that, 99.94% of nodes & SPV clients will automatically follow that longest chain (segwit2x). I know some don’t want Bitcoin to work this way, but this is the way that Bitcoin upgrades are implemented.[160] Some SegWit2x supporters then began to argue that the original rules chain should implement mandatory replay protection, because this was to be the minority hashrate chain. However, this was not really possible, because mandatory replay protection was likely to be an incompatible change and would therefore result in a new coin and a chain-split, resulting in not two, but three coins. Small blockers retorted by arguing that only the incompatible client can implement mandatory replay protection. On October 6, 2017, Bitfinex listed chain-split tokens for the SegWit2x upgrade, just as they had done for Bitcoin Unlimited earlier in the year. The coins traded between 20 percent and four percent of the price of Bitcoin, indicating that the majority of the economy, at least investors and traders, favoured the original rules Bitcoin and not SegWit2x. Bitfinex also clarified its position with respect to the chain-split, stating that initially it would regard the existing rules chain, or what it called the “incumbent implementation” as Bitcoin and the SegWit2x chain as an alternative coin called “B2X”. This Bitfinex policy applied even if B2X had more hashing power. However, Bitfinex did leave the door open to supporting the NYA, stating that “market forces could suggest an alternative labelling scheme”. This was essentially Bitfinex indicating it was ultimately up to investors and traders which coin would be defined as Bitcoin, by determining which coin had the higher market price. As the proposed consensus protocol Segwit2x project appears likely to activate, we have elected to designate the Segwit2x fork as B2X, for now. The incumbent implementation (based on the existing Bitcoin consensus protocol) will continue to trade as BTC even if the B2X chain has more hashing power. We are doing this for practical and operational reasons. Political considerations are irrelevant here. While we cannot change or re-assign ticker symbols, we can change the label or description associated with that ticker symbol. For the time being, BTC will continue to be labeled as “Bitcoin,” and B2X will be labeled as “B2X.” This will remain the case unless and until such time that market forces suggest an alternative, more appropriate, labeling scheme for one or both chains.[161] Around one week later, on October 13, 2017, BitMEX put out an even stronger statement than Bitfinex, again indicating that it would regard B2X as an alternative coin, even if it had a higher hashrate than Bitcoin: The SegWit2x (B2X) proposal is aimed at increasing the blocksize. It is scheduled to take place in November 2017. This change is incompatible with the current Bitcoin ruleset and therefore a new coin may be created. Proponents of this new coin hope it becomes known as Bitcoin, however which coin is known as Bitcoin is not up to the proponents of the new token. Investors and traders may decide which coin has the highest value. In order for this process to work smoothly, strong two way transaction replay protection is necessary. It is our understanding that the SegWit2x proposal does not include two way transaction replay protection, enabled by default. Therefore BitMEX will not be able to support SegWit2x. As such, BitMEX will not support the distribution of B2X, nor will BitMEX be liable for any B2X sent to us. This policy applies even if the SegWit2x chain has the majority hashrate.[162] On October 23, BitMEX’s CEO Arthur Hayes put out a blogpost entitled “Trading ShitCoin2x”.[163]The “ShitCoin2x” meme was celebrated by the smaller blockers, and the situation looked bleak for the last remaining supporters of the NYA. If they launched their coin, it looked like it would be another altcoin trading below 10 percent of the price of Bitcoin. The following day, Jeff Garzik announced he was launching a new alternative coin called “Metronome”. This was another opportunity for the small blockers to rip into the SegWit2x project, claiming the lead developer had lost focus and was now working on other projects. Bloomberg reported the announcement as follows: Jeff Garzik, one of a handful of key developers who helped build the underlying software for bitcoin that is known as blockchain, has seen its shortcomings firsthand. So he decided to create a better digital currency. He’s calling it Metronome and says it will be the first that can jump between different blockchains. The mobility means that if one blockchain dies out as the result of infighting among developers or slackened use, metronome owners can move their holdings elsewhere. That should help the coins retain value, and ensure their longevity, Garzik, co-founder of startup Bloq that created metronome, said in a phone interview.[164] On October 23, 2017, Coinbase announced its policy with respect to SegWit2x. Coinbase was a signatory to the NYA and, by this point, had not reneged on its support for the NYA. The company also had a history of supporting all the other hardfork attempts and therefore its policy with respect to this split was widely anticipated. Just like Bitfinex and BitMEX, Coinbase indicated it had abandoned the NYA and would regard the SegWit2x coin as an alternative coin: Bitcoin Segwit2x - The Bitcoin Segwit2x fork is projected to take place on November 16th and will temporarily result in two bitcoin blockchains. Following the fork, Coinbase will continue referring to the current bitcoin blockchain as Bitcoin (BTC) and the forked blockchain as Bitcoin2x (B2X).[165] Small blockers celebrated the development. Coinbase appeared to have finally joined their camp and this was the final nail in the coffin for SegWit2x. Small blockers sent many emails and messages to Brian Armstrong, the Coinbase CEO, congratulating him on the policy. Coinbase had a fiduciary responsibility to protect client assets and potentially support both sides of the split anyway, therefore some argued it was inappropriate for any custodian to sign any agreement committing to just one side of a potential split. Perhaps the company now realised signing the NYA was inappropriate. However, amazingly, two days later, Coinbase put out another blogpost contradicting the previous one. This time, the company stated it would regard whichever chain had the most accumulated difficulty as Bitcoin: In our prior blogpost we indicated that at the time of the fork, the existing chain will be called Bitcoin and the Segwit2x fork will be called Bitcoin2x. However, some customers asked us to clarify what will happen after the fork. We are going to call the chain with the most accumulated difficulty Bitcoin.[166] Of course, even this statement can be interpreted as reneging on the NYA; the purpose of the original agreement was for the signatories to support the new coin as Bitcoin, not to adopt what appeared to be a neutral stance between the original coin and the new coin. Small blockers reacted in bewilderment to this new Coinbase policy, which was also adopted by several other US-based exchanges such as Gemini[167]. The new Coinbase policy made little sense when one thought through the process in more detail. When it came to the order book and ticker, wouldn’t Coinbase need to pick a coin that would inherit the original? If not, then Coinbase would need to shut down the exchange. This appeared to be a bad business decision, resulting in a loss of revenue just when trading demand would pick up. Also, at which point would Coinbase determine which chain had the most hashrate: after one hour, one day, one week, one month or one year? Coinbase never revealed that. It was, of course, possible that the hashrate lead could oscillate between the competing coins. Miners would also likely be looking at the markets to determine which coin had more value and therefore help inform them about which coin they wanted to mine. If the exchanges shut down, then how would miners make this decision? Both groups, exchanges and miners, would essentially be waiting for each other. Wasn’t Coinbase walking away from its responsibility to help ensure orderly and functioning markets during these uncertain times? And their responsibility to help facilitate the economic process by which investors could express their view, that would then feed down to the miners? It seemed to me that the approach Bitfinex and BitMEX had chosen to take was far more responsible and clearer than the messy and confusing approach of Coinbase. As we reached the end of October, momentum against SegWit2x in the Bitcoin community was almost unstoppable. Local meet-ups around the globe put out statements opposing SegWit2x and confirming they would regard the original rules chain as Bitcoin. The statements were made by local communities in regions which included Korea,[168]Hong Kong,[169]Italy,[170]Germany,[171]Israel,[172]and Brazil and Argentina.[173]The Israeli statement read: We believe that a protocol change in the currency holding the name “Bitcoin”, especially one requiring a hard fork, requires overwhelming consensus. The SegWit2x hard fork does not in any way enjoy such consensus, and while this remains the case we cannot refer to the resulting currency as “Bitcoin”. The Hong Kong community used even stronger language: SegWit2x does not include strong transaction replay protection, nor does it have widespread consensus across the community. Due to the combination of both a lack of consensus across the community and a lack of strong replay protection, we consider SegWit2x a reckless endeavor that will cause disruption and harm to the ecosystem. We therefore strongly oppose SegWit2x. This remains true even if the SegWit2x chain has the majority hashrate or a higher price. The final Scaling conference conducted during the blocksize war, Scaling IV, took place at Stanford University in the US on the weekend of November 4 and 5, 2017. Just like Scaling I in Montreal, I was running out of annual leave at work, therefore I decided to fly over from Hong Kong for a quick weekend visit. The event was a quiet and calm affair and it was clear the war was coming to an end. Virtually no one at the conference was supporting SegWit2x. There was, however, one notable exception to this. Giving a talk at the end of the first day on “Bitcoin in China” was Bobby Lee. Bobby was one of the few enthusiastic supporters of SegWit2x, believing it was a compromise bringing both sides together. By this point, Bobby was one of the last remaining supporters of SegWit2x who still appeared to think it was potentially viable. This is despite the fact that Bobby’s own exchange, BTCC (an NYA signatory), had implemented SegWit2x chain-split tokens and the SegWit2x coin was trading at around 10 percent of the Bitcoin price. Bobby had stubbornly refused to back down from the NYA. At the end of Bobby’s speech in Stanford, it was time for questions. However, just beforehand, Bobby said: I am going to avoid talking about SegWit2x and the NYA, we will just keep it focused on the Chin[ese] market and anything else[174] Bobby seemed to know that SegWit2x was unpopular and that he would be hounded by negatively-framed questions on the proposal. Bobby did not have the courage to face up to it and argue back. So much for the idea of persuading the community to support SegWit2x; at this point, its proponents refused to be scrutinized on the idea. As we reached November, the deadline was approaching. SegWit2x was due to activate at block height 494,784[175]on November 15, 2017. A rumour started circulating in some of the large block channels. Jihan Wu had supposedly said that he would only mine SegWit2x at a loss for two days, at which point if it was not economical to continue mining SegWit2x, he would switch back to Bitcoin and Bitcoin Cash. Bitmain had already spent a lot of money mining Bitcoin Cash at a loss for some periods and was apparently keen to avoid wasting more money. The large blockers never really supported SegWit2x, their hearts went to Bitcoin Cash. SegWit2x did not have support from the users. It had no node network; with almost everyone running Bitcoin Core, the exchanges had either rejected SegWit2x or taken a neutral stance. Now, the one pool of support left for SegWit2x, the miners, looked to be fading away. SegWit2x was dead in the water. The small blockers looked set for a sensational victory. It was no longer a question of if, but when.

21

Victory On Wednesday, November 8, 2017, at 4.58pm UTC, with just one week to go until activation of SegWit2x, an email was sent to the SegWit2x mailing list from Mike Belshe, also signed by the other prominent SegWit2x supporters. The email was essentially an unconditional surrender; phase two of the NYA was officially abandoned. The SegWit2x supporters had little choice: had they gone ahead, it would merely have resulted in a new alternative coin that would have been less popular than Bitcoin Cash. It is at this point, 816 days after the war commenced, that I mark the formal cessation of hostilities. The Segwit2x effort began in May with a simple purpose: to increase the blocksize and improve Bitcoin scalability. At the time, the Bitcoin community was in crisis after nearly 3 years of heavy debate, and consensus for Segwit seemed like a distant mirage with only 30% support among miners. Segwit2x found its first success in August, as it broke the deadlock and quickly led to Segwit’s successful activation. Since that time, the team shifted its efforts to phase two of the project - a 2MB blocksize increase. Our goal has always been a smooth upgrade for Bitcoin. Although we strongly believe in the need for a larger blocksize, there is something we believe is even more important: keeping the community together. Unfortunately, it is clear that we have not built sufficient consensus for a clean blocksize upgrade at this time. Continuing on the current path could divide the community and be a setback to Bitcoin’s growth. This was never the goal of Segwit2x. As fees rise on the blockchain, we believe it will eventually become obvious that on-chain capacity increases are necessary. When that happens, we hope the community will come together and find a solution, possibly with a blocksize increase. Until then, we are suspending our plans for the upcoming 2MB upgrade. We want to thank everyone that contributed constructively to Segwit2x, whether you were in favor or against. Your efforts are what makes Bitcoin great. Bitcoin remains the greatest form of money mankind has ever seen, and we remain dedicated to protecting and fostering its growth worldwide. Mike Belshe, Wences Casares, Jihan Wu, Jeff Garzik, Peter Smith and Erik Voorhees[176] With Bitcoin XT, Bitcoin Classic and Bitcoin Unlimited all falling, and now BTC1 being formally withdrawn by the proponents, the war was over. The large blockers were exhausted; they could see their methodologies did not work and there was no way they were going to launch another contentious hardfork proposal. After more than two years of intense war, this was a sensational victory for the smaller blockers. They finally had their way, not only with respect to the blocksize limit itself, but crucially with respect to how to change the protocol rules. It was now, finally, widely accepted that arranging meetings with large corporates in the space and trying to decide on changes to the protocol rules would not work. The majority of miners also did not have the ability to relax protocol rules. If one wants to change the protocol rules, one has to persuade and campaign for the support of end users and investors, who need to opt-in to the new rules. It was ordinary users who had the final decision-making power, and this was the financial sovereignty that made Bitcoin unique and compelling. After an astounding victory, the small block narrative, that end users had to agree to protocol rule changes, was finally seen as compelling. However, not everyone agreed. Some people, particularly some of the large blockers, interpreted the war as a battle between Bitcoin Core and the miners. In their minds, Bitcoin Core had won and the miners had lost, therefore the Bitcoin Core developers now controlled Bitcoin. This view was still held, despite the fact that Bitcoin Core never implemented the UASF. In some people’s minds, the idea of a system controlled by end users is too difficult to grasp. Instead, they look for somebody or some entity who controls the system. Some people cannot fathom the idea of a system which has global consensus, but lacks a leader. In their minds, in 2015, Gavin was the leader, then it was Jihan and now it was Bitcoin Core. As for whether Bitcoin really is the leaderless system it proclaims to be and whether this will always remain the case, the jury is still out. However, after the drama and shenanigans of the blocksize war, one thing is clear: there is still hope that the claim is true. When news of SegWit2x’s abandonment was released, it caused a tremendous increase in the value of Bitcoin Cash, which was now the last coin standing as far as the large blockers were concerned. On Sunday, November 12, 2017, as the wider cryptocurrency bubble was in full swing, Bitcoin Cash had a monumental rally. Before Mike’s email a few days earlier, Bitcoin Cash traded at around eight percent of the Bitcoin price. However, a couple of days later it reached a peak of around 48 percent of the Bitcoin price, before crashing shortly afterwards. As Bitcoin Cash reached the peak, most small blockers were still delighted about their recent victory and celebrating. However, it is difficult to believe that they didn’t have a few nervous moments contemplating the possibility that they could lose their crown as the largest market capitalisation coin. The rally was said to be driven by retail investors from South Korea, who in this period were particularly frenzied when it came to cryptocurrency markets. However, the rally quickly fizzled out. During the Bitcoin Cash price boom of November 2017, the large blockers were incredibly excited about their massive gains. Some of those I spoke to had purchased more Bitcoin Cash at the height of the bubble, hoping it would overtake Bitcoin. There was a large block Telegram group at the time called “Chain Death”, referring to the potential death of the Bitcoin chain and rise of Bitcoin Cash as the dominant coin. I did not have access to this group, however a member showed me some of the chats on his screen. The group included many prominent large blockers and, during the price rally in November 2017, the activity was intense and the atmosphere in the group was one of sheer jubilation. The idea of “chain death” was that, at some point, the Bitcoin Cash price would increase, due perhaps to its superior utility as a medium of exchange. This would then make Bitcoin Cash more profitable to mine, driving miners away from Bitcoin and towards Bitcoin Cash. At this point, the Bitcoin chain would grind to a halt and not be extended. Bitcoin would then die and Bitcoin Cash would reign supreme. Of course, Bitcoin had a difficulty-adjustment mechanism to defend against this, however that took two weeks to adjust. In the minds of the large blockers, it was possible to kill the Bitcoin chain before this difficulty adjustment occurred. In the minds of small blockers, this hope from the large blockers was sheer idiocy. After all, the small blockers were the patient ones; they would just wait for the difficulty to adjust, no matter how long it took. There was also the matter of the Bitcoin Cash difficulty adjustment, which is much faster than the two weeks in Bitcoin. If the Bitcoin Cash price increased and more miners joined, the Bitcoin Cash difficulty would increase, thereby driving miners back to Bitcoin before the Bitcoin difficulty ever adjusted downwards. The large blockers never seemed to appreciate this aspect of the difficulty adjustment, at least not in this period. On November 15, when the SegWit2x activation point finally came around, it emerged that the client was full of critical bugs. The hardfork was supposed to occur at block height 494,784, however, for some reason, the BTC1 clients became stuck two blocks early at height 494,782.[177]Due to errors in the implementation, the client implemented some aspects the hardfork two blocks earlier than expected. This could have been a disaster for exchanges, which intended to take snapshots of user balances at the hardfork block height. In addition to this, there were other critical bugs in BTC1, making mining on the SegWit2x chain impossible.[178]Jeff first denied there was a problem,[179]before fixing the issue a few days later.[180]Due to these catastrophic bugs, the SegWit2x chain never existed and no blocks on the chain were ever produced. However, even more important than the technical failings of SegWit2x was that it was also defeated using political and economic means. A resounding defeat when looked at through any one of the relevant lenses. On December 20, 2017, there were more Bitcoin Cash trading shenanigans. Coinbase had listed Bitcoin Cash and, in the excitement, the coin traded as high as US$8,500. A record in US dollar terms, but not as high as the November peak in Bitcoin terms. As soon as the coin listed, Coinbase couldn’t handle the demand and the system experienced large delays. This was very much a botched listing, and some of the small blockers, who did not have a favourable view of Coinbase due to its support of Bitcoin XT, Bitcoin Classic and even Bitcoin Unlimited, took a dim view of the situation. They accused Coinbase of insider dealing-related offences, essentially leaking this information to large blockers before Bitcoin Cash was listed. As for Roger Ver, who had been a relentless promoter of larger blocks and a hardfork, he had now become the major promoter of Bitcoin Cash, along with Bitmain. They arranged conferences, events, parties, encouraged merchant adoption, gave away merchandise and free coins, all promoting Bitcoin Cash. They must have spent tens of millions of dollars tirelessly promoting the coin for years. However, in spite of these efforts, the coin never really gained traction compared to Bitcoin. Over the next few years, Bitcoin Cash underperformed Bitcoin with respect to price. Not only that, but Bitcoin Cash even had lower on-chain transaction volume than Bitcoin, when on-chain throughput and a blocksize limit increase was said to be the primary driver behind the coin. Even worse, by March 2018 it emerged that Bitcoin Cash on-chain volume was even lower than SegWit volume on Bitcoin.[181]SegWit had increased on-chain transaction volume faster than Bitcoin Cash. The main narrative behind Bitcoin Cash, larger blocks, had been almost entirely obliterated. However, the key point to the large blockers was not about actual transaction volume, it was about philosophy of surplus capacity; such that, if demand did come, blocks would not fill up. When this war was ancient history, in August 2018, Bitmain attempted to conduct an IPO in Hong Kong. The listing documents indicated that Bitmain invested more than US$888 million into Bitcoin Cash.[182]This was the majority of the free cash flow the company had generated in the 2017 cryptocurrency bull market. At this point, the price performance of Bitcoin Cash had been weak and the company had experienced heavy mark-to-market losses. Jihan had been a passionate advocate of larger blockers and a relentless warrior in a fight that lasted more than two years. However, he had let this cloud his judgement and made poor investment decisions. Bitmain incurred heavy losses in Bitcoin Cash. In part due to the difficulties of conducting a hardfork in Bitcoin, the Bitcoin Cash community opted for a different approach. They conducted a hardfork every six months, in May and November of each year. In November 2018, just over one year since Bitcoin Cash had launched, there were tensions in the Bitcoin Cash community. Craig Wright (The “fake Satoshi”), who had been propped up by many members of the large block community in the past, pops his head into the story once again. Craig had wanted the blocksize limit to be increased to an even more aggressive schedule than many other sections of the Bitcoin Cash community wanted, repeating and regurgitating many of the narrative points the large blockers had used in the blocksize war a few years earlier. Exploiting the scheduled hardfork date of November 15, Bitcoin Cash split into two coins: one following Bitcoin ABC, and one following Bitcoin Satoshi’s Vision, Craig’s chosen coin. The Bitcoin ABC side kept the name Bitcoin Cash, while Bitcoin Satoshi’s Vision became known as BSV. As a result of the split and the resulting uncertainty, the value of Bitcoin Cash compared to Bitcoin continued to decline. Just as the small blockers had expected, some of the large blockers began to slowly see merit in the idea that, in the event of a dispute over the rules, the original rule set is a key schelling point. If one diverts from this philosophy, the risk is that the coin continues to split into smaller and smaller factions. The large blockers were painfully experiencing this first-hand. On November 8, 2018, at the height of the battle between Bitcoin ABC and BSV, Roger Ver, arch large blocker, said the following in a revealing video blog: One thing that I guess I have learnt a little bit here, is that the [Bitcoin] Core people previously were really really really opposed to any sort of contentious hardfork and I think there is some merit to being afraid of that, because we are seeing right now the damage that can be caused by having a contentious hardfork[183] At the time of writing in early 2021, Bitcoin Cash trades at around one percent of the price of Bitcoin and it is widely accepted in the space that the path chosen by the large blockers in the summer of 2017 was not the most effective way forward. However, with respect to the narrow issue of blocksize, the resounding victory for the small blockers does not prove they were correct. On the face of it, Bitcoin has been a tremendous success. Bitcoin has appreciated significantly in value over the years, and the digital gold thesis is proving more relevant. The more patient small block approach looks to have been correct. However, perhaps a moderate blocksize limit increase hardfork, to buy more capacity for a few years, could also have been a good path to take. If this path was chosen, maybe Bitcoin would have been even more successful and retained more merchant adoption. We will never know. While there is uncertainty over who was right on the narrow blocksize issue, there is now little doubt when it comes to the broader issue of the flexibility of the consensus rules and how to change them: the small blockers were on the right side of history. For some of the more extreme small blockers, this was never in doubt: end users always controlled Bitcoin, and the large blockers never had a real chance of winning the war. However, from reading this book, you may reach a different conclusion. The large blockers could have won this war, and they came pretty close. At the start of the conflict, the large blockers had significant support. It was only due to an extraordinary series of events, and several monumental tactical blunders from the large block camp, that crisis was averted and the small blockers succeeded in changing the minds of the community and eventually emerged as resounding victors. In essence, this story is about how the small blockers had constructed a more compelling and attractive narrative than the larger blockers. A new form of money where the users set the rules, simply made for a better story than a high capacity, low fee, global payment system, irrespective of the truth of either claim. Money is ultimately a collective confidence game, the small blockers proved themselves to be quite effective players of the game and for this they were rewarded, with their victory. Over this two-year battle, the small blockers and users had overcome the miners and the large businesses in the space, and, despite their large blocker adversaries investing literally hundreds of millions of dollars into the cause, the small blockers won an incredible and resounding victory. Bitcoin demonstrated that it could be the user-controlled money, that it was always meant to be. However, there is no guarantee this user-controlled money characteristic will persist forever. The blocksize war only bought Bitcoin time, several more years. This war may only be dry run for the challenges to come, when the primary beneficiaries of the centrally-controlled monetary systems finally realise the potential of user-driven money and they may not like it. These future battles may be over censorship resistance, rather than scaling and the blocksize limit. This time, the financial and political establishment are likely to initiate the conflict. They may throw considerable resources at the problem, and the pressure on the system will be immense once again. No doubt history will repeat itself, as the establishment fail to appreciate some of the nuances in the incentives, making blunders on the way, providing users with potential tactical advantages to exploit. The outcome here is far from certain. However, at least for now, the dream of a world where ordinary people have ultimate and direct control over the rules that govern their money, lives on.

[1]https://www.theguardian.com/technology/2015/aug/17/bitcoin-xt-alternative-cryptocurrency-chief-scientist

[2]https://blog.bitmex.com/wp-content/uploads/2017/09/industry-letter.pdf

[3]https://www.huffingtonpost.co.uk/entry/gavin-andresen-bitcoin_n_3093316

[4]https://www.reddit.com/r/Bitcoin/comments/3h9cq4/its_time_for_a_break_about_the_recent_mess/

[5]https://github.com/bitcoin/bitcoin/blob/a30b56ebe76ffff9f9cc8a6667186179413c6349/main.h#L18

[6]https://gist.github.com/gavinandresen/2355445

[7]https://bitcointalk.org/index.php?topic=1347.msg15139#msg15139

[8]https://www.mail-archive.com/cryptography@metzdowd.com/msg09964.html

[9]https://www.mail-archive.com/cryptography@metzdowd.com/msg09963.html

[10]https://bitcointalk.org/index.php?topic=195.msg1611#msg1611

[11]https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2015-August/010238.html

[12]https://bitcoin.org/bitcoin.pdf

[13]http://archive.is/URni1

[14]http://archive.is/URni1

[15]https://bitcointalk.org/index.php?topic=157141.0;all

[16]https://www.youtube.com/watch?v=cZp7UGgBR0I

[17]https://www.youtube.com/watch?v=RIafZXRDH7w

[18]https://bitcoinmagazine.com/articles/the-battle-for-p2sh-the-untold-story-of-the-first-bitcoin-war

[19]http://gavinandresen.ninja/time-to-roll-out-bigger-blocks

[20]https://www.mail-archive.com/bitcoin-development@lists.sourceforge.net/msg07472.html

[21]http://archive.is/kWqW0

[22]https://sourceforge.net/p/bitcoin/mailman/message/34155307/

[23]https://github.com/bitcoin/bips/blob/master/bip-0103.mediawiki

[24]https://bitco.in/forum/threads/gold-collapsing-bitcoin-up.16/page-712#post-25018

[25]https://archive.is/KoknZ#selection-311.0-311.128

[26]https://bitcointalk.org/index.php?topic=7361.msg108052#msg108052

[27]https://www.reddit.com/r/Bitcoin/comments/3hfgpo/an_initiative_to_bring_advanced_privacy_features/cu7mhw8/?context=9

[28]https://www.bitcoin.kn/2015/09/adam-back-gavin-andresen-block-size-increase/

[29]https://diyhpl.us/wiki/transcripts/scalingbitcoin/peter-r/

[30]https://diyhpl.us/wiki/transcripts/scalingbitcoin/issues-impacting-block-size-proposals/

[31]https://tools.ietf.org/html/rfc2418

[32]https://www.wsj.com/articles/BL-HKB-292

[33]https://www.youtube.com/watch?v=FknDfW9em9s

[34]https://www.youtube.com/watch?v=P9oC_goIX8I

[35]https://www.youtube.com/watch?v=UP1YsMlrfF0

[36]https://blog.bitmex.com/the-june-2011-flash-crash-to-0-01/

[37]https://www.youtube.com/watch?v=F41670Wx9Vk

[38]https://diyhpl.us/wiki/transcripts/scalingbitcoin/hong-kong/a-bevy-of-block-size-proposals-bip100-bip102-and-more/

[39]https://twitter.com/gavinandresen/status/800405563909750784

[40]https://www.slideshare.net/jgarzik/bitcoin-status-report-on-chain-scaling-aug-2016

[41]https://bitcoinmagazine.com/articles/segregated-witness-officially-introduced-with-release-of-bitcoin-core-1477611260

[42]https://link.springer.com/chapter/10.1007/978-3-319-21741-3_1

[43]https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2013-April/002417.html

[44]https://www.reddit.com/r/bitcoinxt/comments/3yewit/psa_if_youre_running_an_xt_node_in_stealth_mode/

[45]https://blog.coinbase.com/scaling-bitcoin-the-great-block-size-debate-d2cba9021db0

[46]https://bitcoin.org/bitcoin.pdf

[47]https://github.com/bitcoin-dot-org/Bitcoin.org/commit/7d1cdd94651461ff13ad4ed10b05b2374690fac2

[48]https://blog.plan99.net/the-resolution-of-the-bitcoin-experiment-dabb30201f7#.h81ihjioy

[49]https://twitter.com/JihanWu/status/688300019003162626

[50]https://news.ycombinator.com/item?id=10920902

[51]https://archive.is/6QvMJ

[52]https://bitcointalk.org/index.php?topic=1330553.0

[53]https://github.com/bitcoinclassic/bitcoinclassic/releases/tag/v0.11.2.cl1

[54]https://bitcoinmagazine.com/articles/bitcoin-classic-hard-fork-likely-to-activate-at-hashrate-support-1457020892

[55]https://twitter.com/valeryvavilov/status/688054411650818048

[56]https://blog.coinbase.com/what-happened-at-the-satoshi-roundtable-6c11a10d8cdf

[57]https://www.reddit.com/r/btc/comments/46oa1r/feb_20_hk_coreminer_conference_pics_will_be/

[58]https://medium.com/@bitcoinroundtable/bitcoin-roundtable-consensus-266d475a61ff

[59]https://unispal.un.org/unispal.nsf/0/7D35E1F729DF491C85256EE700686136

[60]https://bitcointalk.org/index.php?topic=1330553.msg14835202#msg14835202

[61]http://gavinandresen.ninja/satoshi

[62]https://twitter.com/peterktodd/status/727078284345917441

[63]https://www.youtube.com/watch?v=pNZyRMG2CjA

[64]https://archive.vn/20160502072026/http://www.drcraigwright.net/jean-paul-sartre-signing-significance/

[65]https://www.reddit.com/r/Bitcoin/comments/4hf4xj/creator_of_bitcoin_reveals_identity/d2pf70v/

[66]https://www.bbc.co.uk/news/technology-36168863

[67]https://www.economist.com/briefing/2016/05/02/craig-steven-wright-claims-to-be-satoshi-nakamoto-is-he

[68]https://www.wired.com/2016/05/craig-wright-privately-proved-hes-bitcoins-creator/

[69]https://www.newsweek.com/2014/03/14/face-behind-bitcoin-247957.html

[70]https://laanwj.github.io/2016/05/06/hostility-scams-and-moving-forward.html

[71]https://www.youtube.com/watch?v=2qLI3VIHuKU

[72]https://archive.is/v8OpD#selection-3389.0-3389.68

[73]http://web.archive.org/web/20151003011022/http://gse-compliance.blogspot.com.au/2008_08_24_archive.html

[74]http://web.archive.org/web/20140602022658/http://gse-compliance.blogspot.com.au/2008_08_24_archive.html

[75]https://www.reddit.com/r/btc/comments/4u0cuq/congratulation_small_blockers_this_is_a_direct/

[76]http://archive.is/76EZY

[77]http://archive.is/7UUrY

[78]https://futurism.com/the-dao-heist-undone-97-of-eth-holders-vote-for-the-hard-fork

[79]https://medium.com/coinmonks/the-dao-is-history-or-is-it-47a6f457338a

[80]http://archive.is/PaGgM

[81]http://archive.is/xfvMY

[82]https://twitter.com/BarrySilbert/status/757628841938472961

[83]https://blog.coinbase.com/coinbase-adds-support-for-ethereum-b8046cf486d0

[84]https://www.coindesk.com/no-scaling-agreements-industry-bitcoin-meetup

[85]https://diyhpl.us/wiki/transcripts/2016-july-bitcoin-developers-miners-meeting/cali2016/

[86]https://github.com/luke-jr/bips/blob/bip-mmhf/bip-mmhf.mediawiki

[87]https://www.etsy.com/uk/listing/593761977/hard-fork-cafe-crypto-blockchain

[88]https://news.bitcoin.com/roger-ver-free-speech-scaling-bitcoin/

[89]https://www.coindesk.com/former-bitmain-chip-designer-seeks-to-revoke-mining-giants-patent

[90]https://github.com/bitcoin/bitcoin/releases?after=v0.11.3

[91]https://www.youtube.com/watch?v=nAqos76JONw

[92]https://bitco.in/forum/threads/gold-collapsing-bitcoin-up.16/page-1163#post-61450

[93]https://twitter.com/lopp/status/825877348096548866

[94]https://bitcoin.stackexchange.com/questions/52154/what-was-the-timeline-of-the-bitcoin-unlimited-hack-as-of-2017-march-and-where-w

[95]https://www.forbes.com/sites/laurashin/2017/03/21/is-this-massive-power-struggle-about-to-blow-up-bitcoin/#326e7aa17325

[96]https://twitter.com/gavinandresen/status/827904756525981697

[97]https://www.reddit.com/r/Bitcoin/comments/6181y2/attacking_a_minority_hashrate_chain_stands/

[98]https://fs.bitcoinmagazine.com/assets/exchange_handling_of_contentious_hard_fork_event.pdf

[99]https://poloniex.com/press-releases/2017.03.17-Hard-Fork/

[100]https://blog.bitmex.com/a-statement-on-the-possible-bitcoin-unlimited-hard-fork/

[101]https://www.bitfinex.com/posts/195

[102]https://coinmarketcap.com/currencies/bitcoin-unlimited/#markets

[103]https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-April/013996.html

[104]https://blog.bitmex.com/wp-content/uploads/2017/09/AsicBoostWhitepaperrev5.pdf

[105]https://blog.bitmain.com/en/regarding-recent-allegations-smear-campaigns/

[106]https://twitter.com/gavinandresen/status/849795178491719681

[107]https://blog.purse.io/ready-for-liftoff-a5533f4de0b6

[108]https://twitter.com/rogerkver/status/849253217321967621

[109]https://coinjournal.net/news/bitmain-co-ceo-micree-zhan-prefers-bitcoin-unlimited-over-segwit-for-now/

[110]https://medium.com/@WhalePanda/the-extended-extension-block-story-5bc3d888bdde

[111]https://bitcoinmagazine.com/articles/there-bitcoin-patent-war-going-initiative-could-end-it

[112]https://asicboost.dance/

[113]https://www.reddit.com/r/btc/comments/63q68x/joseph_poon_to_greg_maxwel_i_was_especially/dfwebqk/

[114]https://telegra.ph/Inside-the-Dragons-Den-Bitcoin-Cores-Troll-Army-04-07

[115]https://youtu.be/aYG0NxoG7yw?t=868

[116]https://ramonquesada.com/english/i-dont-think-craig-is-a-scammer-roger-ver/

[117]https://github.com/litecoin-project/litecoin/blob/v0.13.2.1/doc/release-notes-litecoin.md

[118]https://www.reddit.com/r/litecoin/comments/64ftul/supporting_segwit_on_ltc_by_uasf/

[119]https://bitinfocharts.com/comparison/litecoin-hashrate.html

[120]https://medium.com/@zhangsanbtc/why-i-am-still-not-voting-for-segwit-37b0970f6919

[121]https://medium.com/@Litecoinchina/litecoin-global-roundtable-resolution-001-2017-c67b729bc06d

[122]https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-February/013643.html

[123]https://github.com/bitcoin/bips/blob/master/bip-0148.mediawiki

[124]https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-April/014152.html

[125]https://www.reddit.com/r/Bitcoin/comments/6ef7wb/some_comments_on_the_bip148_uasf_from_the/

[126]https://twitter.com/JihanWu/status/868918286204796928

[127]https://www.newsbtc.com/news/bitcoin/viabtc-enables-bip148-futures-trading-recently-launched-exchange/

[128]https://blog.bitmain.com/en/uahf-contingency-plan-uasf-bip148/

[129]https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-March/013921.html

[130]https://dcgco.medium.com/bitcoin-scaling-agreement-at-consensus-2017-133521fe9a77

[131]https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2017-May/014380.html

[132]https://imgur.com/a/a2oPs

[133]https://github.com/btc1/bitcoin/pull/11

[134]https://lists.linuxfoundation.org/pipermail/bitcoin-segwit2x/2017-June/000006.html

[135]https://lists.linuxfoundation.org/pipermail/bitcoin-segwit2x/2017-June/000010.html

[136]https://twitter.com/cnLedger/status/876018850948567043

[137]https://bitco.in/forum/threads/buip055-passed-increase-the-block-size-limit-at-a-fixed-block-height.2103/

[138]https://github.com/btc1/bitcoin/issues/29

[139]https://lists.linuxfoundation.org/pipermail/bitcoin-segwit2x/2017-June/000060.html

[140]https://lists.linuxfoundation.org/pipermail/bitcoin-segwit2x/2017-July/000082.html

[141]https://twitter.com/JihanWu/status/888035149073457154

[142]https://www.youtube.com/watch?v=By0w43NQdiY

[143]https://viabtc.medium.com/statement-on-bitcoin-user-activated-hard-fork-6e7aebb67e67

[144]https://www.reddit.com/r/btc/comments/6peqwr/if_the_2x_portion_of_segwit2x_fails_to_activate/

[145]https://github.com/Bitcoin-ABC/bitcoin-abc/issues/24

[146]https://reviews.bitcoinabc.org/D371

[147]https://blockchair.com/bitcoin-cash/block/478563

[148]https://github.com/bitcoin/bitcoin/pull/10982

[149]https://bitcointalk.org/index.php?topic=93366.msg1031394#msg1031394

[150]https://bitcointalk.org/index.php?topic=145809.msg1549003#msg1549003

[151]https://web.archive.org/web/20170905013443/https://www.bitwala.com/bitwala-statement-segwit2x/

[152]https://lists.linuxfoundation.org/pipermail/bitcoin-segwit2x/2017-August/000265.html

[153]https://www.coindesk.com/f2pool-reneges-mining-pool-pulls-segwit2x-support-hard-fork?ref=coinwisdom.org

[154]https://lists.linuxfoundation.org/pipermail/bitcoin-segwit2x/2017-September/000304.html

[155]https://twitter.com/JScigala/status/912603668813434880

[156]https://blog.buda.com/our-stance-on-the-segwit2x-hard-fork/

[157]https://twitter.com/TuurDemeester/status/898571708092866560

[158]https://twitter.com/martinjamescox/status/893813681850638336

[159]https://www.reddit.com/r/btc/comments/6w2467/hi_im_ryan_x_charles_cofounder_ceo_of_yours_we/

[160]https://lists.linuxfoundation.org/pipermail/bitcoin-segwit2x/2017-October/000323.html

[161]https://www.bitfinex.com/posts/223

[162]https://blog.bitmex.com/policy-on-bitcoin-hard-forks-update/

[163]https://blog.bitmex.com/trading-shitcoin2x/

[164]https://www.bloomberg.com/news/articles/2017-10-24/bitcoin-pioneer-says-new-coin-to-work-on-multiple-blockchains

[165]https://blog.coinbase.com/timeline-and-support-bitcoin-segwit2x-and-bitcoin-gold-eda72525efd

[166]https://blog.coinbase.com/clarification-on-the-upcoming-segwit2x-fork-d3c0f545c3e0

[167]https://www.gemini.com/blog/upcoming-bitcoin-hard-fork-modified-exchange-operations

[168]https://medium.com/@seoulbitcoin/statement-on-segwit2x-161db1ad1976

[169]https://www.bitcoin.org.hk/segwit2x-statement/

[170]https://medium.com/@BHBnetwork/italian-community-no2x-statement-d14cd06fcc6a

[171]https://www.reddit.com/r/Bitcoin/comments/765k1a/bitcoin_munich_meetup_official_statement_about_b2x/

[172]https://bitcoin.org.il/files/IBA_Statement_Segwit2x.pdf

[173]https://hackernoon.com/why-the-brazilian-and-argentinian-bitcoin-communities-oppose-segwit2x-801edc213af8

[174]https://www.youtube.com/watch?v=LDF8bOEqXt4

[175]https://segwit2x.github.io/segwit2x-announce.html

[176]https://lists.linuxfoundation.org/pipermail/bitcoin-segwit2x/2017-November/000685.html

[177]https://bitcoinmagazine.com/articles/now-segwit2x-hard-fork-has-really-failed-activate

[178]https://twitter.com/jfnewbery/status/931553723532406784

[179]https://twitter.com/jgarzik/status/931543753654902784

[180]https://github.com/btc1/bitcoin/commit/d09f3decfa2806515a0504be927c4384d6241dba

[181]https://thenextweb.com/hardfork/2018/03/23/bitcoin-cash-segwit-transaction-volume/

[182]https://imgur.com/a/HYVg6ZJ

[183]https://www.youtube.com/watch?v=rFU1o-0oU7A&vl=en
