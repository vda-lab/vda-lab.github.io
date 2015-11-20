---
layout: post
title:  "IEEE VIS Paris"
date:   2015-01-07 14:31
author: Toni Verbeiren
private: true
categories: main
tags:
- IEEEVIS
- conference
---
This post was long due, and also long been written. As always, the last *mile* is the hardest...

## Introduction

This is/was my first VIS conference. I have been on conferences from purely mathematical and physics related to very applied vendor-specific IT conferences. This conference is somewhere in-between. Lots of models and frameworks that aim to tackle cognition and interaction on a theoretical level, but also lots of very applied visualizations and dashboards aimed at solving practical problems.

In what follows, I will make a distinction between the full-day workshop I attended on Sunday (DECSIVe), the BELIV workshop on Monday and the conference itself.

## DECISIVe

In what follows, I only discuss what resonated with me, the full program, abstracts (and soon papers) are available online.

As a whole, I found this workshop very interesting, with a very nice mix of people from a different background. I gained a lot from participating in it.

### Introduction

DECISIVe started off with some introductory talks by David Peebles and Geoffrey Ellis. Geoffrey focussed on cognitive biases itself, David on [their origins](http://www.slideshare.net/djpeebz/decisive-introtalk).

Some relevant pointers related to the intro:

* ACT-R: <http://act-r.psy.cmu.edu/>
* Slides: <http://www.slideshare.net/djpeebz/decisive-actrtalk>

## Session 1 and 2

The program can be found here: <http://decisive-workshop.dbvis.de/?page_id=152>

[Pierre Dragicevic](https://www.lri.fr/~dragice/) discussed *planning fallacy*, and its consequences. He also talked about possible approaches to mitigating it: awareness, self-logging and group work.

Although Pierre gave a nice talk and the mitigation strategies make sense, I’m convinced they underestimate the potential of our brain to fool us… Additional information can be found in the work by Spyros Makridakis and more recently Nassim Taleb.

Some of the talks were related to the [Valcri project](http://research.dbvis.de/security/projects/valcri/): *Visual Analytics for sense-making in Criminal Intelligence analysis*. Some other are related to the [Recobia project](https://www.recobia.eu/home): *Reduction of Cognitive Biases in intelligence analysis*.

Eventhia Dimira discussed availability bias. The website of the [Aviz project](http://www.aviz.fr/wiki/pmwiki.php) she is part of is worth checking out.

[Paul Weiser](http://www.geoinfo.tuwien.ac.at/staff/?Current_Staff:Weiser%2C_Paul) discussed biases in maps analysis. I found it striking that people misinterpret a political border for a border of e.g. earth quakes. Also interesting is the *confusion* table he uses in his presentation ([extended abstract](ftp://ftp.geoinfo.tuwien.ac.at/weiser/decisive2014_submission_2.pdf)).

[Michael Corell](http://pages.cs.wisc.edu/~mcorrell/) gave a skeptic’s look at two of Tufte’s *laws*: The *data-to-ink ratio* and the *lie factor*. He gave examples of where they break down. Interesting that to see that someone dares to do this! His other contributions later during VIS where also very interesting.

[Donald Kretz](http://www.researchgate.net/profile/Donald_Kretz) discussed the role of biases in intelligence analysis and approaches to overcome them. Some take-away lessons from his talk:

* In some cases, software makes cognitive biases worse.
* Google is the extension of confirmation biases
* Hypothesis generation is harder than hypothesis testing

### Session 3 and 4

After lunch, we moved to a different venue. There was a group-activity, where each group received one cognitive biases and was asked to come up with possible mitigation scenarios.

We all know about the contrast effect, where we see colours differently depending on the background. [Sebastian Mittelstädt](http://www.vis.uni-konstanz.de/en/members/mittelstaedt/) created a filter to make sure that we *perceive* the colours the way they are supposed to be, so correcting for the visual bias. Interesting work.

There was a talk about quantum approaches to cognition by [Juergen Hahn](http://geo.tuwien.ac.at/staff/juergen-hahn/). I find this whole quantum objective quite interesting, being a physicist and all…

[Laura Matzen](http://www.researchgate.net/profile/Laura_Matzen) discussed biases in satellite analysts. It’s interesting to see that people with a lot of expertise are able to filter out noise (shadows) way better than junior ones. The different in speed between experts and juniors is striking. Or, how our brain is a very powerful apparatus!

[Michael Rascke](http://www.vis.uni-stuttgart.de/institut/mitarbeiter/michael-raschke.html) has done extensive work on eye-tracking. One of the challenges he tackles in this work is how to make sense of the results of an eye-tracking experiment? Interesting…

There was also my own talk in the afternoon. I will post my slides later this week…

## BELIV

[BELIV](http://beliv.cs.univie.ac.at/) is about evaluation methods for visualization.

### Keynote

The keynote was given by Pierre Dragicevic. Details about the topic he presented can be found here [on its own website][15].

I agreed with most of what Pierre was arguing, I disagree with some aspects and I have some comments to make…

To start off, saying that ‘*stats have never been an exact science*’ is *absolutely* wrong! Statistics is mathematical domain and is as exact as it can be. It is correct to say that people apply statistics by using cutoffs on p-values that are completely arbitrary and incorrect.

That said, the rest of the talk was interesting and insightful. Check out the [webpage](http://www.aviz.fr/badstats). It’s also definitely worth it to check out [Cumming](http://www.significancemagazine.org/details/review/1477643/Understanding-The-New-Statistics-Effect-Sizes-Confidence-Intervals-and-Meta-Anal.htm)’s work. Some highlights:

* Let science be about discussion and debate, not absolute (but false) conclusions
* P-values do not provide sufficient insight, significance intervals are better.

The comment I want to make, and one that I tend to make for the conference as a whole is the following: what about non-Gaussian errors and distributions?

### The rest of BELIV

If found the rest of BELIV to be a mixed bag, ranging from very interesting to very rough ideas from young researchers in search for feedback on their research proposals.

[John Stasko](http://www.cc.gatech.edu/~john.stasko/) made the interesting point that as far as evaluation of a visualization goes, it’s the insights we gain from it and the questions asked from it that make it valuable.

One thing to explore further is *Rasmussen’s Ladder*.

## VAST & InfoVis

I switched back and forth between both tracks, depending on what I thought was interesting.

Two topics came forward as being trends this year:

1. The focus on models, taxonomies, frameworks, … or in other words the search for a theoretical foundation of the field.
2. The work on basic user-based studies of interaction and cognition. I find this very interesting and relevant, even if the studies *only* validate earlier findings. It’s important to do reproduction experiments in science…

When a topic/talk/paper is not mentioned here, it either means I was not present during the presentation, I followed a different track or I did find the topic relevant for my research/interests.

### Bertifier

[Bertifier](http://aviz.fr/bertifier) is a web application for laying out tabular data in the tradition of [Jacques Bertin](https://en.wikipedia.org/wiki/Jacques_Bertin). Not only is this a great way to create an insightful table, more akin to a visualization. It also has some very interesting user-interaction techniques built-in (e.g. *crossets*) that are new in my opinion. The draft of the paper [can be found here](http://aviz.fr/wiki/uploads/Bertifier/bertifier-authorversion.pdf).

### iVisDesigner

[iVisDesigner](https://donghaoren.org/ivisdesigner/) is a tool very similar to Tableau or Lyra. It is web-based and allows for exporting the resulting set of linked visualizations. The focus is on creating linked views. Interesting concept, but I’m wondering what is the overlap with existing tools? In the paper, the authors write about the following about this:

> Lyra and Vega only operate on tabular datasets, while our work also supports hierarchical datasets with a fixed schema and references between data items. Lyra is more oriented towards designing a single piece of visualization, while our system focuses on canvases that allow users to draw and link different designs. Furthermore, our system supports designing interactions such as brushing and linking.

It’s certainly interesting to check out. The tool is web-based, but is not compatible with `D3.js` from what I’ve read in the paper.

### PanoramicData

[PanoramicData](http://cs.brown.edu/research/ptc/PanoramicData.html) is so cool! It is a tool to work with SQL data on a large canvas by means of a touch interface. Watch the video to get an idea. I would love to see this combined with iVisDesigner discussed above. Unfortanetly, there does not appear to be any source code or prototype available.

### The effect of latency on exploratory visual analysis

Jeff Heer gave the talk because Zhicheng Liu did not get a visum in time. This is interesting research, back to the basics of doing user studies.

This study is important in our work, so I payed careful attention. I still have to read the paper, though.

The thing I took home is that users score lower latency interactions as being better, even though they did not explicitly noticed a difference in latency.

### Visualizing Statistical Mix Effects and Simpson’s Paradox

On how a simple question leads to a [sophisticated approach](http://research.google.com/pubs/pub42901.html) to visualizing it. This is a contribution by Google and came out of practical questions and issues within the company.

### Genotet

[Genotet](http://cds.nyu.edu/projects/genotet-interactive-web-based-visual-exploration-framework-support-validation-gene-regulatory-networks/) combines [different tools](http://vimeo.com/102601345):

* Cytoscape
* IGV
* VistaClara
* R

Switching between apps is not efficient, integrating them is one step towards enabling researchers to be more productive.

Other, similar tools:

* Genome Sequences
* Cerebral
* Compressed Adjecency MAtrix
* GENeVis

This application includes yet another genome browser, incl panning and zooming.

I will check out the source at a later stage: <https://github.com/ViDA-NYU/genotet>.

### An Algebraic Process for Visualization Design

The talk about this work reminds me a lot of what I’ve read from category theory in mathematics. I should check the paper in more detail…

### Error Bars Considered Harmful: Exploring Alternate Encodings for Mean and Error

I encountered Michael Correll already during the DECISIVe workshop. This work deals with error bars and the interpretion of them. Very interesting material, and worth a further look for everyone dealing with errors in measurements.

### LifeFlow

[Krist Wongsuphasawat](http://kristw.yellowpigz.com/) discussed [LifeFlow](http://kristw.yellowpigz.com/projects/lifeflow), working on aggregated Twitter data in the browser. Cool stuff.

### Perceptual Kernel

How [closely related](https://github.com/uwdata/perceptual-kernels) are certain glyphs for use in visualizations? This can be deduced from large-scale experiments and checked with what is known from Gestalt Laws and other social experiments. Interesting stuff, back to basics but nevertheless very relevant.

### Visualization of Correlations

What visualization is best for showing correlations between datasets? It sounds like an easy question, the answer is a little harder. [Lane Harrison](http://www.eecs.tufts.edu/~lane/) spent some time researching that, with [some very nice results](http://www.eecs.tufts.edu/~lane/files/harrison2014ranking.pdf).

### Scagnostics

It’s interesting to see [how people are using](http://www.cs.uic.edu/~tdang/publications.html) *derived* parameters of a scatterplot, aka scagnostics, to interpret data. Although I tend to like this kind of approach because of its intrinsic ease of interpretation, it is always dangerous to start middling with data because in the end you will always find a transformation that suites your need. Didn’t we call this *overfitting*? Whether you fit with with too many degrees of freedom, or use too many transformations, the result is similar.

Earlier work of the same author(s) along the same lines seems to me more interesting: <http://www.cs.uic.edu/~tdang/file/ScagExplorer.pdf>

### Infuse & Progressive Insights

The [INFUSE paper](http://perer.org/papers/adamPerer-INFUSE-VAST2014.pdf) contains some interesting approaches to dealing with multi-dimesional data. I’m not convinced that this is the best way to approach the problem, but it certainly doesn’t hurt that many people try things out…

From [the same team](http://perer.org/), [Progressive Insights](http://perer.org/papers/adamPerer-Progressive-VAST2014.pdf) offers a way to do visual tree-structure analysis. Also here, some interesting concepts…

### Visualization of Cohort Study Data

The [project page](http://wwwisg.cs.uni-magdeburg.de/visualisierung/wiki/doku.php?id=research:cohort_vis:start) gives an overview of what the *tool* is all about. From what I’ve seen in the presentation, this is very interesting and also applicable outside epidemiology.

I personally think this was the slickest presentation of all, all slides were carefully crafted and the transitions made sense. Very cool!

### Caleydo and its children

The [Caleydo project](http://caleydo.org/) offers a kind of framework for the analysis of biological data. There were a few project presented at VIS this year that are based on Caleydo: [enTourage](http://caleydo.org/projects/pathways/), [Contour](http://caleydo.org/projects/contour/).

### Log & Performance Analysis

Something I can relate to, because it used to be part of my past life, is log file analysis and performance analysis. I saw some interesting applications for both of them. Interesting stuff...

## Conclusions

So, as mentioned already, two themes are apparent for me: the back-to-basics research with fundamental questions on cognition of chart types and the focus on models in order to give visualization a theoretically sound foundation.

One BIG question remains in my opinion: what if data/errors are not Gaussian distributed but rather fat-tailed? This leads to model error, similar to the financial crisis, but also Fukushima and other disasters.
