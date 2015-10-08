---
layout: post
title:  "k-means clustering"
date:   2014-02-06 13:05
author: Raf Winand
categories: clustering b-slim
published: false
---
For the clustering of the data in the b-slim project I'm going through the book that Dusan gave me: Introduction to Data Mining by Pang-Ning Tan, Michael Steinbach & Vipin Kumar. In this post I will give an overview of three simple clustering techniques that are in itself rather simple but show the different (dis)advantages for each technique.

# K-means
K-means is a partitional and prototype-based clustering technique that ames to partition the observations in *k* clusters which are represented by their centroids. In addition to K-means you can also use the K-medoid technique which uses an actual data point (medoid) as the prototype instead of the mean of a group of points (centroid).

In each iteration you first assign each point to the closest centroid  and then recalculate the centroid of each cluster. You keep performing iterations until the centroids don't change or change minimally. To calculate the distance you can use different proximity functions based on type of centroid.

![proximity functions]({{ site.baseurl }}/assets/proximity_functions.png)

The quality of a cluster can be defined as the cluster that has the smallest sum of the squared error (SSE). You calculate the sum of squared distances to the centroid from each point of the cluster. The cluster that has the smallest SSE value is then the cluster with the highest quality.

To start K-means clustering you first have to select the different initial centroids. Selecting the centroids randomly may lead to a clustering that does not find the minimum SSE. Indeed some of the clusters that are found may actually be a larger cluster that is split in two while other cluster may consist of two or more other 'natural' clusters.

Two approaches can be useful instead of the random assignment of centroids. First, you can take a sample of the points and create a hierarchical clustering and use the centroids of those clusters as the initial centroids. Second, you can select a random centroid and place each additional centroid as far away as possible from the other(s). Keep doing this until you have *k* centroids.

Other issues with K-means clustering:

* Handling empty clusters When no data points are in a cluster when assigning the centroids you will get an empty cluster and thus a larger SSE. In this case you can assign a centroid that is the farthest away from any other centroid or choose the replacement centroid from the cluster with the highest SSE
* Outliers When outliers are present, these can influence the SSE of the clusters so you should remove these before clustering but keep in mind that some of the outliers may contain information that is relevant for the data you are analysing
* You can reduce the SSE or the number of clusters by postprocessing:
  * Split cluster with the largest SSE or standard deviation per attribute
  * Create new centroid at the point that is farthest from any cluster center
  * Disperse a cluster by removing a centroid and assigning the points from that cluster to another centroid. You should pick the clusters that lead to the smallest increase in SSE
  * Merge two clusters that result in the smallest increase in SSE

You can also use bisecting K-means. This algorithm starts with two clusters and then you split the cluster with the highest SSE and/or size in two. Keep doing this until you get *k* clusters. The final set of clusters here will not represent a cluster that is a minimum with respect to the total SSE but instead a local SSE minimum.

The advantages of K-means are:

* Simple
* Can be used for different data types
* Efficient (bisecting K-means is even more efficient)

The disadvantages are:

* Not suitable for ALL data types
* It cannot handle non-globular clusters
* It cannot handle clusters of different sizes and/or densities
* Sometimes you only find 'pure' cluster when you have a large number of clusters specified
* It has problems with outliers
* You need to be able to define a center (centroid) which is not always possible
