---
layout: page
title: Gapmap - R package for gapped dendrogram and heatmap
permalink: gapmap.html
exclude: true
---
One of the common mistakes when interpreting a dendrogram is to assume that two adjacent nodes in the leaf order to be similar. Let me demonstrate with the following example.

![euro_cities_map]({{ site.baseurl }}/assets/euro_cities_map.png)

Let’s use the location of European cities as an input data set with two attributes (longitude and latitude). This data is from “eurodist” in R. Then, we use the Euclidian distance between cities as dissimilarity and perform hierarchical clustering on this distance matrix using the complete linkage algorithm. After sorting the dendrogram (See dendsort post), it results the following dendrogram structure of the European cities.

![default_eurocities]({{ site.baseurl }}/assets/default_eurocities.png)

If you look at the dendrogram and find “Stockholm” and “Lisbon”, they ends up right next each other. Just because they end up right next each other, it does not mean they are actually similar. The distance between “Lisbon” and “Madrid” is actually smaller than that of “Stockholm” and “Lisbon”. In order to compare the distance, (besides your knowledge of geography) you will need to read the height of branch where two nodes meet.

As in one of Gestalt’s principals, the proximity is a fairly strong visual cue for similarity or relatedness. Also, in this case, the actual distance between the cities is encoded vertically in the dendrogram, which feels counter-intuitive. So, we decided to introduce  redundancy in encoding the distances between nodes by introducing gaps. The resulting figure looks like this, and I put two figures on top of each other for comparison.

![eurocities_comparison]({{ site.baseurl }}/assets/eurocities_comparison.png)

This is a rather simple idea, but I find the bottom figure a much more intuitive representation of clusters of European cities. The gap between “Stockholm” and “Lisbon” to encode the distance between these two adjacent nodes. A novice user without the knowledge of how to read a dendrogram may be less like to misinterpret the distance between Stockholm and Lisbon. One down side of the gapped dendrogram may be the fact that it takes more space to draw the same dendrogram structure when every other visual properties are kept the same. Now, you may wonder...  How do the gaps affect the heatmap visualization in cluster heat maps?

The naming of “gapmap” was first introduced by Nils Gehlenborg and Bang Wong in the [Point of view](http://www.nature.com/nmeth/journal/v9/n3/full/nmeth.1902.html) column in Nature Methods. In this article, they “cut” a dendrogram to introduce gaps of the same size to emphasize the relationship between the dendrogram and heatmap. We borrow the name and extend the method to encode the distance between two adjacent nodes. We developed the method in R and published as a package (“gapmap”) on [CRAN](http://cran.r-project.org/web/packages/gapmap/index.html). The vignettes for the package is also available. Here are [two](http://cran.r-project.org/web/packages/gapmap/vignettes/simple_example.html) [examples](http://cran.r-project.org/web/packages/gapmap/vignettes/tcga_example.html).

Our preliminary result of evaluating the gapmap has shown some interesting insights.
Gapped dendrogram worked better than gapped heatmap in general. The power scale of the gap size affect the interpretation of the heatmap. In general, the gapped heatmap which encodes the high level cluster structures was more effective. Perhaps one the reason is when we introduce small gaps or hairline gaps, it affects how your read the color in the cell. Thus, the introduction of small gaps exposes the “weakness” of heatmap: the quantitative value is encoded in color/saturation.

![gapmap_scales]({{ site.baseurl }}/assets/gapmap_scales.png)

If you liked this post, and if you have not yet read the [“dendsort” post]({{ site.baseurl }}/dendsort.html), you may find it interesting…
