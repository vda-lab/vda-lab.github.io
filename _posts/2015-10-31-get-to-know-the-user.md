---
layout: post
title:  "Get to know the user"
author: Jan Aerts
date: 2015-10-31 13:55
tags:
- visualization
- howto
- methodology
---
In my lectures on data visualization where that topic is only part of another course, I describe the practical part as consisting of 3 stages:

1. Get to know the user
1. Get to know the data
1. Explore visual designs

These are a simplified version of the often-cited [process described by Ben Fry](http://benfry.com/phd/dissertation-110323c.pdf) or others, which include data acquisition, parsing, etc.

![Ben Fry's visualization process]({{ site.baseurl }}/assets/BenFry_process.png)

*Figure 1 - Ben Fry's visualization process*

As the more involved version, the simplified process also constantly switches between these 3 phases.

![Simplified workflow]({{ site.baseurl }}/assets/simplified_workflow.png)

*Figure 2 - Simplified workflow*

In this and the next two blog posts (see [Get to know the data]({{ site.baseurl }}/2015/10/get-to-know-the-data/index.html) and "Explore visual designs" (latter to be written)), I'll briefly go over each of these. These posts are not a thorough review of the existing literature, but rather the practical advice that I give my MSc students for their little data visualization projects.

## Get to know the user
It's very important to understand the motivating goals of the user. As design space is effectively infinite, the user's requirements can **narrow down** that part of the space that you actually need to investigate.

![Smaller design space to explore]({{ site.baseurl }}/assets/design-space-that-exists-with-arrows.png)

*Figure 3 - Trying to limit the design space that you need to explore*

In our case, the user is very often an expert in some scientific field who has gathered data. This might be a geneticist, a biologist, ... We see 2 phases in getting to know the user: [1] talking to the expert user; [2] analyzing the talk.

### Talking to the expert user
So how do you find out what the user (e.g. the PhD student with the data) wants from the data? Naively, you could say "just ask the user what he/she wants". Unfortunately, **what the user says they *want* is often not what they *need***. You will get an answer like "I want a scatterplot with this as the x-axis, that as the y-axis, and the colour defined by that variable". In that case: let them make it themselves. If you really want to help your user to gain insight in their data with data visualization, you have to find out what the **underlying goals** are that they want to address using the data.

The problem is that the user will naturally phrase their needs within the context of current **constraints**. Unfortunately, this can result in very limited discussions where you're basically stuck in the status quo. We try to force them to think further by **letting them imagine what might have been possible if some technologies were available that are (still) science fiction** (such as mini-robots that roam your body), or even going the *fantasy* way.

![Il était une fois]({{ site.baseurl }}/assets/il_etait_une_fois_la_vie.jpg)

Do you remember the cartoon series "Il était une fois la vie"? That cartoon teaches children about biology - how oxygen is carried through the blood, how pathogens are eliminated, how cells take up nutrients - by anthropomorphizing the whole process. The red blood cells, for example, are little creatures that carry oxygen molecules while walking through your veins and arteries. Now imagine that you could communicate with these creatures and ask them if they are OK, or if they encountered something on while traveling through your veins...

This might seem strange, but putting the user in this state of mind can help to let them think more freely and digg deeper into what they really want to achieve. In contrast to when you stick to the (types of) data that currently exists, you won't be held back because one particular type of data is not available yet. It can help the expert and yourself to think further than what is possible today or tomorrow. One key aspect here is to reveal which **assumptions** that the expert has on the data.

Whereas this approach is very open and helps break open the discussion, other methods exist to get a deeper view of the user's needs. One example is (open and closed) [**card sorting**]({{ site.baseurl }}/2015/06/eurovis-2015-short-paper-on-card-sorting/index.html) as described in our EuroVis 2015 short paper.

### Analyzing the talk post-hoc
So you've talked to the expert, and took ten pages of notes. What do you do now? In the next step, you probably will want to encode this information in a more organized way. One option here is to match the needs from the expert to an **taxonomy** like the one defined in Tamara Munzner's book "Visualization Design and Analysis".

![Tamara Munzner task abstraction]({{ site.baseurl }}/assets/task-abstraction.png)

*Figure 4 - Taken from the book "Visualization Analysis and Design" by Tamara Munzner available from [CRC press](https://www.crcpress.com/Visualization-Analysis-and-Design/Munzner/9781466508910)*

Does the user want to *identify* certain datapoints? *Compare* different (sets of) datapoints? *Annotate* *correlations*? Etc. Go through the discussion you had with the domain expert, and try to extract a list of these goals. This list will become the basis to work on your visual designs.
