The different datasets are categorized in their own directory. Please read what follows, because it gives you information on how the data was gathered, processed and what is represented in the data.

You are allowed to copy the data to your personal home directory or to a different/personal PC. Just make sure to use the original version for the final result of the assignments.

### Genotype ###

*description of the dataset*

#### Questions we want to answer ####

* Does mutation X exist in the dataset? (Think of big data approach!)
* What mutations does HG000096 have?
* Report the person with the most mutations.

### Beers ###

The belgian beers dataset on Wikipedia contains around 1500 beers with data about the kind of beer, the percentage alcohol and the brewery.

#### Questions we want to answer ####

If we define the distance between beers as follows:
```
distance(x,y) = (alcohol_x - alcohol_y) 
                + 0 if same brewer, 1 otherwise
                + 0 if same type, 1 otherwise
```

* Report the beers brewed by brewery X
* What is the distribution of beers per brewery, beers per alcohol percentage?
* Given a beer, find all beers that have distance 0
* Why does AB Inbev not occur in the top-10?

### Drugs ###

*need to provide description*

#### Questions we want to answer ####

If we define a distance between companies as
```
distance = number of drug compounds that they have in common
```

* Query the dataset for a certain drug and report possible companies that sell this drug.
* Query for drugs that have been added to the list in the last 2 years.
* Which companies are most/least alike?

### Tour de France ###

The results from the 2005 Tour de France are stored in the TDF2005 folder in json format. The datafiles are:

* riders.json - Names of all riders with (among others) team, nationality, etc.
* times.json - For each rider: his time for each trip.
* rankings.json - For each rider: his ranking for each trip.

#### Questions we want to answer ####

We actually don't know. This dataset will be used for a visualization exercise to find out if we can find interesting hypotheses that could be tested.
