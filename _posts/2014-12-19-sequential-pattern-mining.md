---
layout: post
title:  "Sequential pattern mining"
date:   2014-12-19 12:21
author: Raf Winand
categories: main
tags:
- data-mining
---
The goal of sequential pattern mining is to find relevant patterns that are contained in a set of sequences. It is useful for e.g. identifying shopping patterns (for instance: first buy a computer, then a printer, then a camera a few months later), DNA sequences, ...

A sequence is a list of events and can be described as  < e<sub>1</sub>, e<sub>2</sub>, e<sub>3</sub>, ... , e<sub>n</sub> >. For instance <(b**k**)f**ds**(**a**b**g**)c**d**> is a sequence where (bk) is an item in that sequence. Mining algorithms will try to find all frequent subsequences in the data. In this case a possible subsequence would be <kds(ag)d>. When mining the data you can specify a minimal support threshold that will disregard any subsequences that occur less times than specified. For a list of 1,000 sequences you could for instance specify that a subsequence should occur at least 200 times for it to be considered a valid pattern.

The mining algorithm should be able to find all the possible sequential patterns that are hidden in the data above a certain threshold. Several algorithms exist:

* GSP
* SPADE
* FreeSpan
* PrefixSpan
* MAPres

These algorithms assume discrete data. Finding patterns and predicting future values from non-linear and continuous variables is not directly possible with this approach. One way to overcome this problem is by converting the variables to discrete values. This way the algorithm can identify a pattern that would otherwise not be found. In some cases this does not look advisable as an autoregressive model should be ideally suited for this kind of problem and the number of variables can be very high making it hard to define a conversion for each individual variable.
