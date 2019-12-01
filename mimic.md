---
layout: page
title: Applying STAD to ICD9 diagnosis codes and developing a new distance metric on the way
permalink: mimic.html
custom_css: with_tables
use_math: true
---
_This is work performed by Daniel Alcaide, unless otherwise mentioned. It is currently being written up._

Patient profiling and selection receive growing attention due to the large economic and societal value. The involvement of analytical methods that are able to handle the increasing amount of healthcare data can make this process more agile and facilitate, for example, patient recruitment in clinical trials. However, these processes are currently extremely labor-intensive. Here we present the application of [STAD]({{ site.baseurl }}/stad.html) on intensive care unit patients.

A proof-of-principle interface can be found at [https://dalcaide.shinyapps.io/diagnosis_explorer/](https://dalcaide.shinyapps.io/diagnosis_explorer/). The code underlying this interface is available on github at [https://github.com/vda-lab/ICD_diagnosis_explorer](https://github.com/vda-lab/ICD_diagnosis_explorer).

## What's the distance between diagnoses?
The [MIMIC-III critical care database](https://mimic.physionet.org/) (described in [this paper](http://www.nature.com/articles/sdata201635)) contains deidentified health data for almost 60,000 intensive care unit patients. A lot of information is available for each patient, including a list of diagnoses (encoded using [ICD-9](https://www.cdc.gov/nchs/icd/icd9.htm)). For see if we can find substructures in this patient population, we need to calculate distances between them, and we'll focus on the diagnoses to do this.

Unfortunately, there is an issue: no simple distance metric exists for lists of diagnoses for patients. This is because they are categorical data (i.e. each diagnosis is a category) that are put in a specific order (i.e. the first diagnosis in the list is the most important, and importance drops as you go down the list).

<table>
<tr>
<td colspan="3">Patient X</td>
<td colspan="3">Patient Y</td>
</tr>
<tr>
<td>Order</td><td>ICD</td><td>Description</td><td>Order</td><td>ICD</td><td>Description</td>
</tr>
<tr>
<td>1</td><td>99662</td><td>Infection and inflammatory reaction due to other vascular device, implant, and graft</td><td>1</td><td>4329</td><td>Unspecified intracranial hemorrhage</td>
</tr>
<tr>
<td>2</td><td>99591</td><td>Sepsis</td><td>2</td><td>4019</td><td>Unspecified essential hypertension</td>
</tr>
<tr>
<td>3</td><td>5990</td><td>Urinary tract infection, site not specified (5990)</td><td>3</td><td>99702</td><td>Iatrogenic cerebrovascular infarction or hemorrhage</td>
</tr>
<tr>
<td>4</td><td>4019</td><td>Unspecified essential hypertension</td><td>4</td><td>99591</td><td>Sepsis</td>
</tr>
<tr>
<td></td><td></td><td></td><td>5</td><td>5990</td><td>Urinary tract infection, site not specified</td>
</tr>
<tr>
<td></td><td></td><td></td><td>6</td><td>43491</td><td>Cerebral artery occlusion, unspecified with cerebral infarction</td>
</tr>
</table>

Codes 2, 3 and 4 of patient 1 correspond to codes 4, 5 and 2 of patient 2 (in that order). To make sure that not only presence/absence of a code is considered, but also its position, we can use the following distance metric:

$$
M_{c_{X},c_{Y}} = ln(1 + \frac{1}{max(position_{c_{X}}, position_{c_{Y}})})
$$

where $c_{X}$ and $c_{Y}$ are the same code in patient X or Y, respectively.

To get to the distance between _patients_ rather than between a single code in 2 patients, we sum these values:

$$
D(X,Y) = 1 - S(X,Y) = 1 - \sum_{i=1}^{n}M(X \cap Y)
$$

## What does such network look like?
Using this metric, the STAD network for patients in the MIMIC-III database that suffer from a "pathological fracture of vertebrae" looks like this:

<img src="{{ site.baseurl }}/assets/pathological_fracture_annotated.png" width="600px" />

As usual, colours are assigned automatically using community detection.

A complete user interface to explore these networks can be found at [https://dalcaide.shinyapps.io/diagnosis_explorer/](https://dalcaide.shinyapps.io/diagnosis_explorer/).
