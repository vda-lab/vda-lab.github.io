---
title: Datasets for the course
layout: page
exclude: true
---

# Datasets

The different datasets are categorized in their own directory. Please read what follows, because it gives you information on how the data was gathered, processed and what is represented in the data.

You are allowed to copy the data to your personal home directory or to a different/personal PC. Just make sure to use the original version for the final result of the assignments.

All the file are located under the following directory:

    /mnt/bioinformatics_leuven/i0u19a/data/

## Genotype ##

We selected the first 100K basepairs from chromosome 1 from the [1000 genome project](http://www.1000genomes.org/). The is data for all 1000 samples is in `chr1-0-100000.vcf`. For convenience, this file has already been converted to JSON format in `chr1-0-100000.json`.

A subset of the data (only sample `HG000096`) can be found in the smaller files.

### Questions we want to answer ###

* Does mutation X exist in the dataset? (Think of big data approach!)
* What mutations does HG000096 have?
* Report the person with the most mutations.


## Beers ##

The [belgian beers dataset on Wikipedia](http://nl.wikipedia.org/wiki/Lijst_van_Belgische_bieren) contains around 1500 beers with data about the kind of beer, the percentage alcohol and the brewery.

The data has been downloaded from the web and converted to two formats: `beers.csv` and `beers.json`.

### Questions we want to answer ###

* Report the beers brewed by brewery X
* What is the distribution of beers per brewery, beers per alcohol percentage?
* Why does AB Inbev not appear to occur in the top-10 op breweries?


## Drugs ##

The database of drugs that can be sold in Belgium from the [Federal Government](http://www.fagg-afmps.be/nl/items/gegevensbank_vergunde_geneesmiddelen/).

The datasets consists of 2 files: `AMM_det_H.csv` and `AMM_H.csv`:

* `AMM_det_H` contains the active substances in the doses they have been granted permission to use in drug compounds.
* `AMM_H` contains the drug compounds that can be sold on the market.

What is the key that joins both datasets together?

For convenience, the compounds dataset has been converted to JSON as well: `AMM_H.json`. Easy conversion to JSON can be done for example via [http://www.convertcsv.com](http://www.convertcsv.com/csv-to-json.htm).


### Questions we want to answer ###

* Query the dataset for a certain drug and report possible companies that sell this drug.
* Query for drugs that have been added to the list in the last 2 years.
* Which companies are most/least alike?


## Tour de France ##

The results from the 2005 Tour de France are stored in the TDF2005 folder in json format. The datafiles are:

* `riders.json` - Names of all riders with (among others) team, nationality, etc.
* `times.json` - For each rider: his time for each trip.
* `rankings.json` - For each rider: his ranking for each trip.

### Questions we want to answer ###

We actually don't know. This dataset will be used for a visualization exercise to find out if we can find interesting hypotheses that could be tested.
