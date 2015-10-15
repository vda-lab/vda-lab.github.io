---
layout: post
title:  "Hierarchical clustering"
date:   2014-02-06 15:29
author: Raf Winand
categories: clustering b-slim
published: false
tags:
- clustering
- b-slim
---
## Hierarchical Clustering
Agglomerative hierarchical clustering starts with the points as individual clusters and with each step merges the closest pair of clusters.

The key in these algorithms is defining the proximity between clusters. This proximity can be defined in many different ways. You have for instance MIN or single link where the proximity is defined by the closest two points of different clusters, MAX or complete link takes the farthest two points in the different clusters and Group Average takes the average pairwise proximities of all pairs of point in the different clusters. In addition you can also take the distance between prototypes (centroids) of the clusters or you can use Ward's method which also assumes that the cluster is represented by a centroid but measures the increase in SSE when merging two clusters.

* Single link is good at handling non-elliptical shapes but is sensitive to noise and outliers
* Complete link is less susceptible to noise and outliers but can break large clusters and favours globular shapes.
* Centroid methods can lead to inversions, i.e. two clusters that are merged can be more similar than the clusters that were merged in a previous step.

There are some key issues in hierarchical clustering:

* There is no global objective function. At each step it is decided locally which clusters should be merged
* Different cluster sizes can be handled and you can take a weighted or unweighted approach. The weighted approach will treat all clusters equally and the unweighted methods take the number of points in each cluster into account (e.g. UPGMA)
* Merging decisions are final and are made locally. Because of this you will nog have a global optimisation criterion

Hierarchical clustering is typically used for the creation of clusters that require a form of hierarchy. A disadvantage is that it has high computational and storage requirements. Because all merges are final it might have problems with high-dimensional data. You can overcome part of these disadvantages by first partially clustering the data with e.g. K-means.

## DBSCAN
With DBSCAN regions of high density are located that are separated by regions of lower density. There are several ways to define density but here I will only focus on center-based density. In this case density is measured for a particular point by counting the number of points that are found within a certain radius from that point. The problem then is how to set the radius because a too large radius will include all points while a too small radius will only include one point.

In the center-based approach points are classified into three categories:

* Core points that are in the interior of a cluster. A point is called a core point when there is minimum number of points (user-defined) in the neighbourhood of the point.
* Border points are not core point but fall in the neighbourhood of a core point.
* Noise points are neither a border point nor a core point.

The algorithm works by putting two core points that are close enough in the same cluster. Any border point that is close enough to a core point is also put in the same cluster as the core point. Noise points are discarded in this case. The difficulty is in selecting the parameters of distance and minimum number of points. The basic approach is looking at the distances from a particular point to its k-th neighbour. For points that are not in the cluster that value will be high compared to the points inside a cluster. So if you calculate this distance for all points and sort them in increasing order, you will see a sharp change in distances at a suitable distance parameter. If you then take the value of *k *as the minimum number of points you will label points as core points when their k-distance is less then the previously selected value.

The advantage of DBSCAN is that it is relatively resistant to noise and can handle clusters of different shapes and sizes. On the other hand when the density of clusters varies widely, DBSCAN can get into problems by misclassifying the points. It also has troubles with high-dimensional data because density can not be easily determined in this case. It can also be computationally expensive when computing the nearest neighbours requires computing all pairwise proximities as is the case with high-dimensional data.
