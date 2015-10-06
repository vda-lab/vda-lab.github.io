---
layout: post
title:  "Cluster evaluation"
date:   2014-02-20 07:16
author: Raf Winand
categories: clustering
published: false
---
Although it may seem that cluster evaluation is not necessary because of the exploratory nature of clustering, performing cluster evaluation is indeed important because it allows you to determine if there is a non-random structure in the data or if the clusters represent some random data points.

There are several important issues for cluster validation:

* Determining the clustering tendency of a dataset. This is verifying whether a non-random structure actually exists in the data.
* Determining the correct number of clusters
* Evaluating how well the results fit the data without reference to external information
* Comparing the results to external information
* Comparing two sets of clusters and determine which one is better

The first three items do not use any external information and are therefore unsupervised technique. The fourth item is a supervised technique and the last item can be both supervised and unsupervised.

Whatever the measure is that you want to use, you have to make sure that (1) it needs to be applicable (e.g. 2D or 3D data), (2) the measurement has to be interpretable and (3) it needs to be simple enough so that the user can apply and understand it.

The cluster evaluation measures are typically classified into three different types:

* Unsupervised: measures the goodness of a clustering structure without respect to external information (e.g. SSE). Further division into cluster cohesion and cluster separation. These measures are called internal indices because no external information is used.
* Supervised: measures whether the discovered structure matches an external structure. These measurement are called external indices because information that is not present in the data is used.
* Relative: compares different clusterings by either unsupervised or supervised methods.

The sum of the SSE and the between group sum of squares (SSB) is a constant. That means that when you try to minimise the cohesion (e.g. SSE), you do the same as trying to maximise the separation (e.g. SSB). You can also use these measures to evaluate individual clusters and objects. This way you may choose to split a cluster with a low cohesion value or you may choose to merge two clusters that are not well separated.

When using unsupervised clustering evaluation using a proximity matrix you can use a visual approach to judge the quality of the clusters. When plotting the similarity scores you will get a roughly block-diagonal similarity matrix. Keep in mind though that although you might see these blocks, sometimes even random data will produce matrices that look like blocks.

The previous methods were all for partitional clustering. When using hierarchical clustering you can use the cophenetic distance as an evaluation measure.
