# I0U19A - Management of large-scale omics data

Prof Jan Aerts - Faculty of Engineering ESAT/STADIUS

jan.aerts@esat.kuleuven.be - http://visualanalyticsleuven.be

Teaching assistants:

* Toni Verbeiren (toni.verbeiren@esat.kuleuven.be)
* Ryo Sakai (ryo.sakai@esat.kuleuven.be)
* Raf Winand (raf.winand@esat.kuleuven.be)



## Course overview

![Concept map of the course](images/conceptmap_I0U19A.png "Conceptmap of the course")


## Schedule

| Week | Date | Room | Type | Topic |
|------|------|------|------|-------|
| 1 | 13/2/2014 | LAND 91.30 | lecture | What is big data? |
| 2 | 20/2/2014 | LAND 91.30 | lecture | Visual Analytics |
| 3 | 27/2/2014 | LAND 91.30 | exercise | Visual Analytics |
| 4 | 6/3/2014 | no lecture	 | (SQL exercise)  |  |
| 5 | 13/3/2014 | LAND 91.30 | lecture | Lambda Architecture |
| 6 | 20/3/2014 | LAND 91.30 | lecture | Data processing |
| 7 | 27/3/2014 | LAND 91.30 | exercise | Data processing |
| 8 | 3/4/2014 | no lecture |  |  |
| 9 | 24/4/2014 | LAND 00.210 | lecture | Document and graph databases |
| 10 | 8/5/2014 | LAND 00.210 | exercise | Document databases |
| 11 | 15/5/2015 | LAND 00.210 | exercise | Graph databases |
| 12 | 22/5/2014 | LAND 00.210 | exam | |


## Exercises

Three datasets:

* genotypes
* beers in Belgium
* approved drugs

<br>
Modeled and stored using different database technologies => which technology (or combination of technologies) fits a particular dataset (and its intended use) best?

Preparation of exercise session: assignment including e.g. modelling of data => answers will be used in exercise session


## Evaluation

Combination of:

* permanent evaluation (including preparation of exercise sessions): 10%
* take-home data visualization assignment: 10%
* open-book written exam: 80%

<br>
At least 8/20 for each.


## Interesting books

* Marz N & Warren J (2013). Big Data. Manning Publications.
* McCreary D & Kelly A (2013). Making Sense of NoSQL. Manning Publications.
* Wood D, Zaidman M & Ruth L (2013). Linked Data. Manning Publications.


## Your background

* scripting?
* SQL?


## Today - What is big data?

![Concept map of the course](images/conceptmap_I0U19A_introduction.png "Conceptmap of the course")



## What is big data?

How would *you* describe "big data"? Can you give examples?


## Some examples

* **Netflix** - analysis of traffic patterns across device types to improve reliability of video streaming; recommendation engine based on viewing habits
* **Politics: project "Narwhal"** - Obama campaign operations: don't knock on door of people who have already volunteered, don't send email asking for money to people who already contributed
* **WeatherSignal** - repurposes sensors in Android smartphones to map atmospheric readings (barometer, hygrometer, ambient thermometer, light meter)
* **Retail (Target)** - predict future purchasing habits (e.g. pregnancy) => targeted ads


## Why are these examples different?

* Data collection is easy
* Data is often unstructured
* Data can be used for many things

<br>
Example datasets available at http://www.datasciencecentral.com/profiles/blogs/big-data-sets-available-for-free