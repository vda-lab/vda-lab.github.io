% Exercises Big Data Course: Datasets
% 12/2/2014

# Datasets, conversions and questions

The datasets can be found under:

    /mnt/bioinformatics_leuven/i0u19a

The different datasets are categorized in their own directory. Please read what follows, because it gives you information on how the data was gathered, processed and what is represented in the data.

You are allowed to copy the data to your personal home directory or to a different/personal PC. Just make sure to use the original version for the final result of the assignments.


## Genotypes

### Source and parsing

Source of the data is 1000 genomes, the first 100K basepairs from chromosome 1:

    /freeware/bioi/tabix/tabix-0.2.5/tabix -h /freeware/bioi/1000genomes/ALL.chr1.phase1_release_v3.20101123.snps_indels_svs.genotypes.vcf.gz 1:0-100000 > chr1-0-100000.vcf

The result of this will be used for the rest of the course. To view the file, it is handy to use `vim` and avoid wrapping the lines (`:set nowrap`).

Extract the data for sample HG000096 (column 10) can easily be done:

    cat chr1-0-100000.vcf| cut -f 1,2,3,4,5,6,7,8,9,10 > chr1-0-100000_HG000096.vcf

The source file is just under 5MB, the resulting file `chr1-0-100000_HG000096.vcf` is only 38K, so this is nice for testing purposes.

An additional `JSON` version of the latter file has been saved under the name `chr1-0-100000_HG000096.json`.


### Questions

1. Does mutation X exist in the dataset? (Think of big data approach!)
2. What mutations does HG000096 have?
3. Report the person with the most mutations.


## Belgian Beers

### Source and parsing

The belgian beers dataset on Wikipedia contains around 1500 beers with data about the kind of beer, the percentage alcohol and the brewery.

Source: [WikiPedia Source](http://nl.wikipedia.org/wiki/Lijst_van_Belgische_bieren)

I created an R script `GetBeers.R` that fetches the data from the Wikipedia page, combines it, cleans up the percentage column and writes the result to two different files:

1. `beers.csv`: This contains the data in a format similar to the original on Wikipedia.
2. `beersMolten`: This is stored in a molten (long) list.

Depending on what needs to be done, one of the two formats can be used. The underlying data is the same.

An derived dataset if provided, where the frequencies of beers per brewery is given: `brouwerij.csv` and `brouwerij.json`.


### Questions

Define the distance between beers as follows:

    distance(x,y) = (alcohol_x - alcohol_y) 
                    + 0 if same brewer, 1 otherwise
                    + 0 if same type, 1 otherwise


1. Report the beers brewed by brewery X
2. What is the distribution of beers per brewery, beers per alcohol percentage?
3. Given a beer, find all beers that have distance 0
4. Why does AB Inbev not occur in the top-10?


## Drug database

### Source and Parsing

Source: [Fgov site, medicines for human use](http://www.fagg-afmps.be/nl/items/gegevensbank_vergunde_geneesmiddelen/)

You need the `mdbtools` package installed in order to extract the data from the `CLI`. On Mac, with `homebrew`, do this:

    brew install mdbtools

This toolbox contains several tools to work with Access Database files. I used the `Hmisc` package in `R` to read and write the data. This package uses `mdbtools` for its functioning.


    library(Hmisc)
    result <- mdb.get("AMM_Pub_H.mdb")
    contents(result)
    contents(result$St_Generic)
    det_H <- mdb.get("AMM_Pub_H.mdb","Tbl_AMM_det_H")
    H <- mdb.get("AMM_Pub_H.mdb","Tbl_AMM_H")

Example searching for a certain component in both lists:

    det_H[det_H$ActSubst.Name == "CYCLOPHOSPHAMIDE",]
    H[grepl("CYCLOPHOSPHAMIDE",H$ActSubsts),]

The key that joins both together is `cti`:

    det_H[det_H$cti == 95,]
    H[H$cti == 95,]

I converted both files to CSV format: `AMM_det_H.csv` and `AMM_H.csv`.

An additional example:

    hcs1 <- H[grepl("PARACETAMOL",H$ActSubsts),]
    hcs2 <- det_H[det_H$ActSubst.Name == "PARACETAMOL",]

The top-10 of companies selling this drug can easily be retrieved:

```
tail(data.frame(sort(table(hcs1$mah))))
                                         sort.table.hcs1.mah..
SANDOZ N.V.                                                  7
TEVA PHARMA BELGIUM NV                                       7
GLAXOSMITHKLINE CONSUMER HEALTHCARE S.A.                     8
JOHNSON & JOHNSON CONSUMER N.V.                             13
BRISTOL-MYERS SQUIBB BELGIUM SA                             15
LABORATOIRES S.M.B. S.A.                                    18
```

### Questions

Define a distance between companies by:

    distance = number of drug compounds that they have in common

1. Query the dataset for a certain drug and report possible companies that sell this drug.
2. Query for drugs that have been added to the list in the last 2 years.
3. Which companies are most/least alike?


# Next steps

See [1. Visualization](1.\ Visualization.html).

