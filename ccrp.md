---
layout: page
title: Data-driven 3D Sculpture - Cosmopolitan Chicken Research Project
permalink: ccrp.html
---
*Contribution by Ryo Sakai*

![Poulet de Bresse]({{ site.baseurl }}/assets/Bresse.png) ![Mechelse Koekoek]({{ site.baseurl }}/assets/MechKoe.png) ![Mechelse Ancona]({{ site.baseurl }}/assets/MechAnc.png)

In collaboration with a Belgian artist, Koen Vanmechelen, I wrote a code to generate 3D models based on the SNP array data in Processing.

Koen Vanmechelen started the Cosmopolitan Chicken Project to reflect on the issues of (biological, cultural, behavioural, …) diversity in the human population in 90s. Vanmechelen crosses pure-bred chicken lines in order to create the true “cosmopolitan chicken”. At present, 16 different breeds have been combined in a single hybrid.

![pedigree]({{ site.baseurl }}/assets/pedigree.png)

To generate the data sculpture, the program counted the numbers of homozygous and heterozygous genotypes and binned based on chromosomal positions, and translated as peaks in the 3 dimensional spaces. Chromosomes are laid out in circles, connecting at one tip of the chromosome and wrapped in spherical shapes. The longest chromosomes (chromosomes 1 and 2) cross at the top of the sphere.

![backbone]({{ site.baseurl }}/assets/backbone.png)

The number of homozygous and heterozygous polymorphisms along the chromosomes are indicated by peaks pointing inwards and outwards, respectively. As a result, inbred chickens have relatively more peaks pointing inwards while crossbred chickens have more peaks pointing outwards.

![chr1]({{ site.baseurl }}/assets/chr1.png)

To generate .STL file, I used the [toxiclibs](http://toxiclibs.org/) library and especially the [VolumentricBrush](http://toxiclibs.org/docs/volumeutils/toxi/volume/RoundBrush.html) to translate the data into the volume. These files were 3D printed and became a part of Vanmechelen’s exhibition, which is currently shown in [Venice, Italy](http://www.ccrp.be/evolution-of-a-hybrid/).

Although 3D printing is still quite expensive, I found it very rewarding to have something physical at the end of coding. It was also great to be able to touch and feel spikes and its delicateness. I hope it will be cheaper and more accessible in the near future, so that we can generate more creative data sculptures and print them!

![photo1]({{ site.baseurl }}/assets/ccrp_photo1.jpg)
![photo2]({{ site.baseurl }}/assets/ccrp_photo2.jpg)

![Cosmopolitan Chicken Project]({{ site.baseurl }}/assets/cosmopolitan_picture.png)
