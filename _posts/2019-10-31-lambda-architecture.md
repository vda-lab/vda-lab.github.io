---
layout: post
title:  "The Lambda Architecture - how to handle huge and complex data"
date:   2019-10-31
author: Jan Aerts
categories: main
custom_css: with_tables
use_math: true
tags:
- nosql
---
This post is part of the course material for the Software and Data Management course at UHasselt. The contents of this post is licensed as CC-BY: feel free to copy/remix/tweak/... it, but please credit your source.

![CC-BY]({{ site.baseurl }}/assets/ccby.png)

- [Part 1]({{ site.baseurl }}/2019/08/extended-introduction-to-relational-databases): Relational database design and SQL
- [Part 2]({{site.baseurl}}/2019/09/beyond-sql): Beyond SQL
- Part 3 (this post): Lambda Architecture

**For a particular year's practicalities, see [http://vda-lab.be/teaching]({{ site.baseurl }}/teaching)**

## Table of contents

* Do not remove this line (it will not be displayed)
{:toc}

In this post, we'll revisit some of the more conceptual differences between using SQL and NoSQL databases, and touch upon the lambda architecture, which is a model that can help you think about
