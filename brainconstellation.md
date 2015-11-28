---
layout: page
title: Brain Constellation
permalink: brainconstellation.html
---
The BioVis 2014 data contest focused on the domain of resting state functional connectivity networks (rs-fMRI network). These networks are derived from functional magnetic resonance imaging scans of human subjects, which measured the blood oxygenation level dependent (BOLD) activity over a period of time in different regions of the brain. The data were pre-processed to weighted adjacency matrices with each row and column corresponding to a region of interest (ROI) and the value corresponding to the strength of coupling between two anatomical regions. For more details, please visit the [archived website](http://www.biovis.net/year/2014/info/data_contest).

![Brain constellation]({{ site.baseurl }}/assets/brainconstellation.png)

The contest provided two analysis tasks:

1. to characterize most consistent/variable properties of the network across the population of subjects provided
1. to classify unknown networks to the corresponding subject network.

To address these tasks visually, we developed an interactive visual analytics tool, named Brain Constellation. In this project, there were 2 key ideas that are considered as milestones in the design process.

The first is the use of a 2D template to project 169 regions of interest. In the field of visualization research, the use of the 3D coordinate system requires a sensible justification because viewing of 3D rendered image on the 2D computer monitor suffers the occlusion issues. In the relevant scientific literature, either the brain volumetric rendered or the brain is sliced using the coronal, sagittal, and/or transverse planes. Both methods suffer from the issue of occlusions and requires more than one view to show multiple connectivities. Neither of the solutions was suitable for comparison of multiple samples at once.

This has led us to test projecting the 3 dimensional coordinate of regions of interest to 2D plane. In order to minimise the overlap, in other words to find the plane that capture the variance in the data the most, we used the Principal Component Analysis (PCA) to achieve such 2D projection. As shown in the figure below, the center of mass for each ROI was projected onto the 2D plane. We use this layout, like a constellation map, for small multiples to compare between different networks.

![bc_image_2]({{ site.baseurl }}/assets/bc_image_2.png)

The second turning point was the use of correlation of correlation matrix as a measure of similarity between subjects. This is specifically for the classification task. In order to compare two networks, we calculated ROI-wise correlation to measure the correlation coefficient of correlation patterns for one anatomical region between two samples. A schematic diagram of this approach is shown below. This calculation results a vector of ROI-wise correlation when two subject networks are compared. We used this vector to filter and highlight those brain regions that showed highly correlated connectivity patterns. We hypothesised that when we looked at 169 brain regions, the matching network pair should have the largest number of correlated brain regions.

![bc_image_3]({{ site.baseurl }}/assets/bc_image_3.png)

The video below is the screen capture of Brain Constellation, demonstrating how we addressed the tasks.

<iframe src="https://player.vimeo.com/video/143813795" width="500" height="281" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>

As a result, we were able to address both analysis tasks and achieve the perfect classification result via visual analysis. Our entry won the Overall Favorite Data Contest Award at BioVis2014 (ISMB 2014). The comments from reviewers were positive and scored highly because of the simplicity. Although our 2D template had anatomical relevance, most of the reviewers suggested to link back to 3D rendering of the brain.

This comment about linking back to 3D rendering of the brain is an intriguing one, because we generated the 2D projection to abstract away from the 3D rendering and the reviewers liked the simplicity of the tool. The comment suggests that the use of 2D layout was useful for identifying the most variable or consistent properties, but it was not as intuitive as 3D rendering to interpret the anatomical structure.

The design of data visualization often, if not always, involves the evaluation of the pros and cos of a particular method. One method is better for showing a certain property or pattern in the data at a cost of possibly obscuring other attributes about the data. I think this tool, even though it is still premature and should be considered as a prototype, demonstrate the trade-off you see in visualisation design.

This tool addressed the analysis tasks well, however these tasks were “toy” tasks which were designed to help the contest organizers to evaluate each entry, consequently these questions are somewhat removed from the real research questions.

The following images are some “sketches” we made to try out different concepts:

![bc_dots]({{ site.baseurl }}/assets/bc_dots.png)

Comparison of dot size and the background color:

![bc_with_fde_bundling]({{ site.baseurl }}/assets/bc_with_fde_bundling.png)

Testing the edge bundling. It resulted more “organic” appearance of the network, however the calculation was computational too heavy and it was not feasible to support interactive interaction with dynamic bundling.

This was a collaborative work with Nico Verbeeck, Jaak Simm and Jan Aerts.
