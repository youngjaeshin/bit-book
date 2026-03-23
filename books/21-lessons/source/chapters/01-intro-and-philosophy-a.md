# Intro + Philosophy A

## Source Metadata

- Chapter number: 1
- TOC index: 1
- Part: main
- EPUB src: OEBPS/part0001.xhtml
- Extraction mode: spine-range

## Extracted Text

21 Lessons

What I’ve Learned from Falling Down the Bitcoin Rabbit Hole

Gigi

21 Lessons What I’ve Learned From Falling Down the Bitcoin Rabbit HoleFirst edition. Version 0.3.11-e, git commit 7a7b71d.Copyright ©2018–2020 Gigi / @dergigi / dergigi.comThis book and its online version are distributed under the terms of the Creative Commons Attribution-ShareAlike 4.0 license. A reference copy of this license may be found at the official creative commons page.1

Dedicated to my wife, my child, and all the children of this world. May bitcoin serve you well, and provide a vision for a future worth fighting for.

21 Lessons

“Oh, you foolish Alice!” she said again, “how can you learn lessons in here? Why, there’s hardly room for you, and no room at all for any lesson-books!”

– Lewis Carroll, Alice in Wonderland

Foreword

Some call it a religious experience. Others call it Bitcoin.

I first met Gigi in one of my spiritual homes – Riga, Latvia – the home of The Baltic HoneybadgerConference, where the most fervent of the Bitcoin faithful make a yearly pilgrimage. After a deep lunchtime conversation, the bond Gigi and I forged was as set in stone as a Bitcoin transaction that was processed when we first shook hands a few hours prior.

My other spiritual home, Christ Church, Oxford, where I had the privilege to study for my MBA, was where I had my “Rabbit Hole” moment. Like Gigi, I transcended the economic, technical and social realms, and was spiritually enveloped by Bitcoin. After “buying high” in the November 2013 bubble, there were several extremely hard-learned lessons to be had in the relentlessly crushing and seemingly never-ending 3-year bear market. These 21 Lessons would indeed have served me very well in that time. Many of these lessons are simply natural truths that, to the uninitiated, are obscured by an opaque, fragile film. By the end of this book however, the façade will fragment fiercely.

On a crystal-clear night in Oxford in late-August 2016, just a few weeks after the knife twisted in my heart again when the Bitfinex Exchange was hacked, I sat in quiet contemplation at Christ Church’s Master’s Garden. Times were tough, and I was at my mental and emotional breaking-point after what seemed to be a lifetime of torture; not because of financial loss, but of the crushing spiritual loss I felt being isolated in my world view. If only there were resources like this one at the time to see that I was not alone. The Master’s Garden is a very special place to me and many who came before me over the centuries. It was there where one Charles Dodgson, a Math Tutor at Christ Church, observed one of his young pupils, Alice Liddell, the daughter of the Dean of Christ Church. Dodgson, better known by his pen-name, Lewis Carroll, used Alice and The Garden as his inspiration, and in the magic of that hallowed turf, I stared deeply into the crypto-chasm, and it stared blazingly back, annihilating my arrogance, and slapping my self-pride square in the face. I was finally at peace.

21 Lessons takes you on a true Bitcoin journey; not just a journey of philosophy, technology and economics, but of the soul.

As you dive deeper into the philosophy tersely laid out in 7 of the 21 Lessons, one can go as far as to understand the origin of all beings with enough time and contemplation. His 7 lessons on economics captures, in simple terms, how we are at the financial mercy of a small group of Mad Hatters, and how they have successfully managed to put blinders on our minds, hearts and souls. The 7 lessons on technology lay out the beauty and technologically-Darwinian perfection of Bitcoin. Being a non-technical Bitcoiner, the lessons provide a salient review of the underlying technological nature of Bitcoin, and indeed, the nature of technology itself.

In this transient experience we call life, we live, love and learn. But what is life but a timestamped order of events?

Conquering the Bitcoin mountain is not easy. False summits are rife, rocks are rough, and cracks and crevices are ubiquitously lying in wait to swallow you up. After reading this book, you will see that Gigi is the ultimate Bitcoin Sherpa, and I will appreciate him forever.

Hass McCook November 29, 2019

“Would you tell me, please, which way I ought to go from here?”“That depends a good deal on where you want to get to.”“I don’t much care where –”“Then it doesn’t matter which way you go.”

– Lewis Carroll, Alice in Wonderland

Contents

I Philosophy

1 Immutability and Change

2 The Scarcity of Scarcity

3 Replication and Locality

4 The Problem of Identity

5 An Immaculate Conception

6 The Power of Free Speech

7 The Limits of Knowledge

II Economics

8 Financial Ignorance

9 Inflation

10 Value

11 Money

12 The History and Downfall of Money

13 Fractional Reserve Insanity

14 Sound Money

III Technology

15 Strength in Numbers

16 Reflections on “Don’t Trust, Verify”

17 Telling Time Takes Work

18 Move Slowly and Don’t Break Things

19 Privacy is Not Dead

20 Cypherpunks Write Code

21 Metaphors for Bitcoin’s Future

III Final Thoughts

About This Book (... and About the Author)

This is a bit of an unusual book. But hey, Bitcoin is a bit of an unusual technology, so an unusual book about Bitcoin might be fitting. I’m not sure if I’m an unusual guy (I like to think of myself as a regularguy) but the story of how this book came to be, and how I came to be an author, is worth telling.

First of all, I’m not an author. I’m an engineer. I didn’t study writing. I studied code and coding. Second of all, I never intended to write a book, let alone a book about Bitcoin. Hell, I’m not even a native speaker.2 I’m just a guy who caught the Bitcoin bug. Hard.

Who am Ito write a book about Bitcoin? That’s a good question. The short answer is easy: I’m Gigi, and I’m a bitcoiner.

The long answer is a bit more nuanced.

My background is in computer science and software development. In a previous life, I was part of a research group that tried to make computers think and reason, among other things. In yet another previous life I wrote software for automated passport processing and related stuff which is even scarier. I know a thing or two about computers and our networked world, so I guess I have a bit of a head-start to understand the technical side of Bitcoin. However, as I try to outline in this book, the tech side of things is only a tiny sliver of the beast which is Bitcoin. And every single one of these slivers is important. This book came to be because of one simple question: “What have you learned from Bitcoin?”I tried to answer this question in a single tweet. Then the tweet turned into a tweetstorm. The tweetstorm turned into an article. The article turned into three articles. Three articles turned into 21 Lessons. And 21 Lessons turned into this book. So I guess I’m just really bad at condensing my thoughts into a single tweet.

“Why write this book?”, you might ask. Again, there is a short and a long answer. The short answer is that I simply had to. I was (and still am) possessedby Bitcoin. I find it to be endlessly fascinating. I can’t seem to stop thinking about it and the implications it will have on our global society. The long answer is that I believe that Bitcoin is the single most important invention of our time, and more people need to understand the nature of this invention. Bitcoin is still one of the most misunderstood phenomena of our modern world, and it took me years to fully realize the gravitas of this alien technology. Realizing what Bitcoin is and how it will transform our society is a profound experience. I hope to plant the seeds which might lead to this realization in your head. While this section is titled “About This Book (... and About the Author)”, in the grand scheme of things, this book, who I am, and what I did doesn’t really matter. I am just a node in the network, both literally andfiguratively. Plus, you shouldn’t trust what I’m saying anyway. As we bitcoiners like to say: do your own research, and most importantly: don’t trust, verify.

I did my best to do my homework and provide plenty of sources for you, dear reader, to dive into. In addition to the footnotes and citations in this book, I try to keep an updated list of resources at 21lessons.com/rabbithole and on bitcoin-resources.com, which also lists plenty of other curated resources, books, and podcasts that will help you to understand what Bitcoin is.

In short, this is simply a book about Bitcoin, written by a bitcoiner. Bitcoin doesn’t need this book, and you probably don’t need this book to understand Bitcoin. I believe that Bitcoin will be understood by you as soon as youare ready, and I also believe that the first fractions of a bitcoin will find you as soon as you are ready to receive them. In essence, everyone will get itcoin at exactly the right time. In the meanwhile, Bitcoin simply is, and that is enough.3

Preface

Falling down the Bitcoin rabbit hole is a strange experience. Like many others, I feel like I have learned more in the last couple of years studying Bitcoin than I have during two decades of formal education.

The following lessons are a distillation of what I’ve learned. First published as an article series titled “What I’ve Learned From Bitcoin,”what follows can be seen as a third edition of the original series.

Like Bitcoin, these lessons aren’t a static thing. I plan to work on them periodically, releasing updated versions and additional material in the future.

Unlike Bitcoin, future versions of this project do not have to be backward compatible. Some lessons might be extended, others might be reworked or replaced.

Bitcoin is an inexhaustible teacher, which is why I do not claim that these lessons are all-encompassing or complete. They are a reflection of my personal journey down the rabbit hole. There are many more lessons to be learned, and every person will learn something different from entering the world of Bitcoin.

I hope that you will find these lessons useful and that the process of learning them by reading won’t be as arduous and painful as learning them firsthand.

Introduction

“But I don’t want to go among mad people,” Alice remarked. “Oh, you can’t help that,” said the Cat: “we’re all mad here. I’m mad. You’re mad.” “How do you know I’m mad?” said Alice. “You must be,” said the Cat, “or you wouldn’t have come here.”

– Lewis Carroll, Alice in Wonderland

In October 2018, Arjun Balaji asked the innocuous question, What have you learned from Bitcoin?After trying to answer this question in a short tweet, and failing miserably, I realized that the things I’ve learned are far too numerous to answer quickly, if at all.

The things I’ve learned are, obviously, about Bitcoin - or at least related to it. However, while some of the inner workings of Bitcoin are explained, the following lessons are not an explanation of how Bitcoin works or what it is, they might, however, help to explore some of the things Bitcoin touches: philosophical questions, economic realities, and technological innovations.

The 21 Lessonsare structured in bundles of seven, resulting in three chapters. Each chapter looks at Bitcoin through a different lens, extracting what lessons can be learned by inspecting this strange network from a different angle.

Chapter 1 explores the philosophical teachings of Bitcoin. The interplay of immutability and change, the concept of true scarcity, Bitcoin’s immaculate conception, the problem of identity, the contradiction of replication and locality, the power of free speech, and the limits of knowledge.

Chapter 2 explores the economic teachings of Bitcoin. Lessons about financial ignorance, inflation, value, money and the history of money, fractional reserve banking, and how Bitcoin is re-introducing sound money in a sly, roundabout way.

Chapter 3 explores some of the lessons learned by examining the technology of Bitcoin. Why there is strength in numbers, reflections on trust, why telling time takes work, how moving slowly and not breaking things is a feature and not a bug, what Bitcoin’s creation can tell us about privacy, why cypherpunks write code (and not laws), and what metaphors might be useful to explore Bitcoin’s future.

Each lesson contains several quotes and links throughout the text. If an idea is worth exploring in more detail, you can follow the links to related works in the footnotes or in the bibliography.

Even though some prior knowledge about Bitcoin is beneficial, I hope that these lessons can be digested by any curious reader. While some relate to each other, each lesson should be able to stand on its own and can be read independently. I did my best to shy away from technical jargon, even though some domain-specific vocabulary is unavoidable.

I hope that my writing serves as inspiration for others to dig beneath the surface and examine some of the deeper questions Bitcoin raises. My own inspiration came from a multitude of authors and content creators to all of whom I am eternally grateful.

Last but not least: my goal in writing this is not to convince you of anything. My goal is to make you think, and show you that there is way more to Bitcoin than meets the eye. I can’t even tell you what Bitcoin is or what Bitcoin will teach you. You will have to find that out for yourself.

“After this, there is no turning back. You take the blue pill — the story ends, you wake up in your bed and believe whatever you want to believe. You take the red pill4 — you stay in Wonderland, and I show you how deep the rabbit hole goes.”

– Morpheus

Figure 0.1:*

Remember: All I’m offering is the truth. Nothing more.

Part I Philosophy

Philosophy

The mouse looked at her rather inquisitively, and seemed to her to wink with one of its little eyes, but it said nothing.

– Lewis Carroll, Alice in Wonderland

Looking at Bitcoin superficially, one might conclude that it is slow, wasteful, unnecessarily redundant, and overly paranoid. Looking at Bitcoin inquisitively, one might find out that things are not as they seem at first glance.

Bitcoin has a way of taking your assumptions and turning them on their heads. After a while, just when you were about to get comfortable again, Bitcoin will smash through the wall like a bull in a china shop and shatter your assumptions once more.

Figure 0.2:Blind monks examining the Bitcoin bull

Bitcoin is a child of many disciplines. Like blind monks examining an elephant, everyone who approaches this novel technology does so from a different angle. And everyone will come to different conclusions about the nature of the beast.

The following lessons are about some of my assumptions which Bitcoin shattered, and the conclusions I arrived at. Philosophical questions of immutability, scarcity, locality, and identity are explored in the first four lessons. Every part consists of seven lessons.

Part I – Philosophy:

- Immutability and change

- The scarcity of scarcity

- Replication and locality

- The problem of identity

- An immaculate conception

- The power of free speech

- The limits of knowledge

Lesson 5 explores how Bitcoin’s origin story is not only fascinating but absolutely essential for a leaderless system. The last two lessons of this chapter explore the power of free speech and the limits of our individual knowledge, reflected by the surprising depth of the Bitcoin rabbit hole.

I hope that you will find the world of Bitcoin as educational, fascinating and entertaining as I did and still do. I invite you to follow the white rabbit and explore the depths of this rabbit hole. Now hold on to your pocket watch, pop down, and enjoy the fall.

1 Immutability and Change

“I wonder if I’ve been changed in the night. Let me think. Was I the same when I got up this morning? I almost think I can remember feeling a little different. But if I’m not the same, the next question is ‘Who in the world am I?’ Ah, that’s the great puzzle!”

– Alice

Bitcoin is inherently hard to describe. It is a new thing, and any attempt to draw a comparison to previous concepts – be it by calling it digital gold or the internet of money – is bound to fall short of the whole. Whatever your favorite analogy might be, two aspects of Bitcoin are absolutely essential: decentralization and immutability.

One way to think about Bitcoin is as an automated social contract5. The software is just one piece of the puzzle, and hoping to change Bitcoin by changing the software is an exercise in futility. One would have to convince the rest of the network to adopt the changes, which is more a psychological effort than a software engineering one.

The following might sound absurd at first, like so many other things in this space, but I believe that it is profoundly true nonetheless: You won’t change Bitcoin, but Bitcoin will change you.

“Bitcoin will change us more than we will change it.”

– Marty Bent6

It took me a long time to realize the profundity of this. Since Bitcoin is just software and all of it is open-source, you can simply change things at will, right? Wrong. Verywrong. Unsurprisingly, Bitcoin’s creator knew this all too well.

“The nature of Bitcoin is such that once version 0.1 was released, the core design was set in stone for the rest of its lifetime.”

– Satoshi Nakamoto7

Many people have attempted to change Bitcoin’s nature. So far all of them have failed. While there is an endless sea of forks and altcoins, the Bitcoin network still does its thing, just as it did when the first node went online. The altcoins won’t matter in the long run. The forks will eventually starve to death. Bitcoin is what matters. As long as our fundamental understanding of mathematics and/or physics doesn’t change, the Bitcoin honeybadger will continue to not care.

“Bitcoin is the first example of a new form of life. It lives and breathes on the internet. It lives because it can pay people to keep it alive. […] It can’t be changed. It can’t be argued with. It can’t be tampered with. It can’t be corrupted. It can’t be stopped. […] If nuclear war destroyed half of our planet, it would continue to live, uncorrupted.”

– Ralph Merkle8

The heartbeat of the Bitcoin network will outlast all of ours.

Realizing the above changed me way more than the past blocks of the Bitcoin blockchain ever will. It changed my time preference, my understanding of economics, my political views, and so much more. Hell, it is even changing people’s diets9. If all of this sounds crazy to you, you’re in good company. All of this is crazy, and yet it is happening.

Bitcoin taught me that it won’t change. I will.

2 The Scarcity of Scarcity

“That’s quite enough - I hope I sha’n’t grow any more…”

– Alice

In general, the advance of technology seems to make things more abundant. More and more people are able to enjoy what previously have been luxurious goods. Soon, we will all live like kings. Most of us already do. As Peter Diamandis wrote in Abundance [23]: “Technology is a resource-liberating mechanism. It can make the once scarce the now abundant.”

Bitcoin, an advanced technology in itself, breaks this trend and creates a new commodity which is truly scarce. Some even argue that it is one of the scarcest things in the universe. The supply can’t be inflated, no matter how much effort one chooses to expend towards creating more.

“Only two things are genuinely scarce: time and bitcoin.”

– Saifedean Ammous10

Paradoxically, it does so by a mechanism of copying. Transactions are broadcast, blocks are propagated, the distributed ledger is — well, you guessed it — distributed. All of these are just fancy words for copying. Heck, Bitcoin even copies itself onto as many computers as it can, by incentivizing individual people to run full nodes and mine new blocks.

All of this duplication wonderfully works together in a concerted effort to produce scarcity.

In a time of abundance, Bitcoin taught me what realscarcity is.
