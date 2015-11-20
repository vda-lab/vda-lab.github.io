---
layout: post
title:  "Get to know the data"
author: Jan Aerts
date: 2015-10-31 13:55
categories: main
tags:
- visualization
- howto
- methodology
---
This is part 2 of a 3-part series which might help some of our students in their first steps in data visualization. Make sure to also check out the other 2 parts: [get to know the user]({{ site.baseurl }}/2015/10/get-to-know-the-user/index.html) and explore visual designs.

No data visualization without data. And before visualizing your data, you should understand the shape of the data itself. So get to grips with [R](https://www.r-project.org/) or python [pandas](http://pandas.pydata.org/)...

Some things you want to find out:

* **How many dimensions** are there? What are the **types** for each dimension: categorical, numeric, geo-spatial, ...?
* For each of these dimensions, or at least the most important ones: how are the data **distributed**?
* Are there any **correlations** between the dimensions?
* What does a **principal component analysis**, **independent component analysis**, or **singular value decomposition** reveal?
* What does a **hierarchical clustering** show?
* Are there any **local clusters**? Have a look at [topological data analysis](https://www.youtube.com/watch?v=3Z73Wd2T1xE) (perhaps using the [R TDA module](https://cran.r-project.org/web/packages/TDA/vignettes/article.pdf)), which can reveal such local clusters in a global context.

Create loads of simple plots and really take your time for this.
