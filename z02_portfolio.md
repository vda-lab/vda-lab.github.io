---
layout: page
title: Portfolio
permalink: portfolio.html
---
A selection of projects run in the lab…

## :: Card sorting ::

One of the most important steps in a data visualization project is to find out what the underlying goals are of the person who wants to investigate a dataset. Ryo developed a card sorting technique to help this process. See [**here**]({{ site.baseurl }}/card_sorting.html) for a full description.

## :: Aracari ::

The award-winning contribution to the data visualization challenge at the BioVis 2011 conference. The data consists of 2-locus eQTL data in which the contestants were asked to identify genes responsible for a hypothetical disease. See [this screencast](https://vimeo.com/45585178).

![Aracari screenshot]({{ site.baseurl }}/assets/aracari_screenshot.png)

Reference: Bartlett, Christopher W, Soo Yeon Cheong, Liping Hou, Jesse Paquette, Pek Yee Lum, Günter Jäger, Florian Battke, et al. 2012. “An eQTL Biological Data Visualization Challenge and Approaches from the Visualization Community.” BMC Bioinformatics 13 Suppl 8: S8.

## :: Triovis ::

One of the most important steps in SNP discovery is to remove false positive, for example by filtering on read depth for each SNP. Unfortunately, the cut-offs that one uses (typically: remove SNPs with coverage lower than 3 or higher than 1,200) are based on the 1,000 Genome Project data analysis and might not be ideal for the data at hand. When sequencing trios (father, mother and offspring), it is however possible to include the trio-information at the filtering stage. For example, many SNPs in the filtered data where both parents are reference/reference and the offspring is alternative/alternative, indicates that the there are issues with the cut-off values used. The Triovis tool provides live feedback of what the effects of these different cut-offs are on “possible” and “impossible” inheritance patterns.

![Triovis screenshot]({{ site.baseurl }}/assets/triovis_screenshot.png)

Reference: Sakai, Ryo, Alejandro Sifrim, Andrew Vande Moere, and Jan Aerts. 2013. “TrioVis: A Visualisation Approach for Filtering Genomic Variants of Parent-Child Trios.” Bioinformatics (Oxford, England) (May 8): 2–3.

## :: Sequence Diversity Diagram ::

The sequence logo has been the quintessential representation of DNA, RNA or protein sequence conservation and is typically used to represent recurring sequence motifs. Although very useful, it has several issues, including losing the connection between consecutive bases or aminoacids, and difficulties in comparing different motifs. The sequence diversity diagram is a redesign of the sequence logo that allows to identify additional patterns.

![SeDD screenshot]({{ site.baseurl }}/assets/sedd_9.png)

See [**here**]({{ site.baseurl }}/sedd.html) for a more elaborate description including the visual design process.

References:

* Sakai, Ryo, and Jan Aerts. 2014. “Sequence Diversity Diagram for Comparative Analysis of Multiple Sequence Alignments.” BMC Proceedings 8: S9
* Pougach, Ksenia, et al. 2014. “Duplication of a Promiscuous Transcription Factor Drives the Emergence of a New Regulatory Network.” Nature Communications 5 (January): 4868

## :: Gene interaction network ::

Supporting the work by Katja Nowick (Leipzig, Germany), looking at how gene interaction networks change during evolution.

![network comparison screenshot]({{ site.baseurl }}/assets/network_comparison_screenshot.png)

## :: ExaScience ::

As visualization plays an important role in data-driven research and the data-driven economy for finding new hypotheses and identifying novel leads, there is the issue of scalability in interactive data visualization. Visualizing a big dataset in an interactive way is not a trivial task. In addition, we aim to do this on the CPU rather than the GPU because the typical data analyst does not necessarily know/want to work on the GPU.

## :: Cosmopolitan Chicken Project ::

Data-driven art in collaboration with Koen Vanmechelen. Check out this TEDxFlanders presentation by the artist covering our work.

![Cosmopolitan Chicken Project]({{ site.baseurl }}/assets/cosmopolitan_picture.png)
