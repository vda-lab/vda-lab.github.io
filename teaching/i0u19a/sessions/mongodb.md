---
title: MongoDB
layout: page
exclude: true
---

# 1. Document Databases (MongoDB)

Read and follow the following tutorial pages (from the official [MongoDB tutorials](http://docs.mongodb.org/getting-started/shell/)):

- <http://docs.mongodb.org/getting-started/shell/client/>
- <http://docs.mongodb.org/getting-started/shell/insert/>
- <http://docs.mongodb.org/getting-started/shell/query/>
- <http://docs.mongodb.org/getting-started/shell/update/>
- <http://docs.mongodb.org/getting-started/shell/remove/>
- <http://docs.mongodb.org/getting-started/shell/aggregation/>
- <http://docs.mongodb.org/getting-started/shell/indexes/>

You can go through the whole tutorial of course, but the above is relevant for the exercises that follow. More information on how updates work in MongoDB [can be found here](http://docs.mongodb.org/manual/core/crud-introduction/).

**Please note:**
The data about beers as used in the course before, is already stored in the mongDB database on the teaching server.

**Pro tip:** A good programmer chooses her tools wisely! As we will be writing MongoDB queries in JavaScript, consider installing a good text/code editor like [Brackets](http://brackets.io/) on your machine. Text editors with JavaScript support can help you find syntax errors more easily than typing directly into the MongoDB shell.


# 2. Simple Queries using the Mongo Shell

## Introduction

Connect to the mongoDB instance using the `mongo` shell. This is done by typing the following command in the shell on the teaching server:

    tverbeiren@ip-10-158-90-118:~$ mongo
    MongoDB shell version: 2.0.4
    connecting to: test
    >

You now get the MongoDB prompt in which we will work. At the end, you can escape the MongoDB shell by typing exit. Type

    > show dbs

to know what databases are available. Connect to the database for this exercise:

    > use exercises

The command

    > show collections

returns the list of collections ("tables") that are stored in the collection

To exit the MongoDB shell and return to your linux prompt, use

    > quit()


## Exercises

Based on what you have learned from the assignment for this session, you should be able to answer the following questions:

* How many beers in the database are of type _hoge gisting_? The type of beer corresponds to the field `Soort` in the database.
* How many beers have a percentage alcohol of more than 8 degrees?
* How many beers have an **unknown** alcohol percentage?


# 3. MapReduce in MongoDB

## Example

Taken from <http://docs.mongodb.org/manual/tutorial/map-reduce-examples/>.

To use mapreduce, you will define two functions: a `map` function and a
`reduce` function. Suppose we have a collection of documents that describe purchases made by a customer. These documents therefore look like this:

    {
        _id: ObjectId("50a8240b927d5d8b5891743c"),
        cust_id: "abc123",
        ord_date: new Date("Oct 04, 2012"),
        status: 'A',
        price: 25,
        items: [ { sku: "mmm", qty: 5, price: 2.5 },
                 { sku: "nnn", qty: 5, price: 2.5 } ]
    }

Suppose that we have returning customers who spend different amounts every visit. If we want to calculate how much each customer spent in total (across visits), we can do this using a mapreduce approach.

**1. Define the map function to process each input document**

* In the function, the keyword `this` refers to the document that the map-reduce operation is processing.
* The function maps the price to the `cust_id` for each document and emits the
`cust_id` and `price` pair.

In code for the Mongo shell, this means:

``` javascript
var mapFunction1 = function() {
                    emit(this.cust_id, this.price);
               };
```


**2. Define the corresponding reduce function with two arguments `keyCustId` and `valuesPrices`:**

- `valuesPrices` is an array whose elements are the price values emitted by the map function and grouped by `keyCustId`.
- The function reduces the `valuesPrices` array to the sum of its elements.

In code for the Mongo shell, this means:

``` javascript
var reduceFunction1 = function(keyCustId, valuesPrices) {
                              return Array.sum(valuesPrices);
                          };
```

**3. Perform the map-reduce on all documents in the `orders` collection using the `mapFunction1` map function and the `reduceFunction1` reduce function:**

``` javascript
db.orders.mapReduce(
                 mapFunction1,
                 reduceFunction1,
                 { out: "map_reduce_example" }
               )
```

This command will create a new collection named `map_reduce_example` that will contain the results.


## Exercises

You can find info about MapReduce in MongoDB here: <http://docs.mongodb.org/manual/core/map-reduce/> and <http://docs.mongodb.org/manual/tutorial/map-reduce-examples/>. The mongoDB shell uses Javascript syntax.

#### 1. Basic MapReduce exercise

* Using a MapReduce approach (create a `mapFunction2` and `reduceFunction2`), get the number of beers per brewery. Store the result in a collection called `<username>Brewery` (*e.g.* `tverbeirenBrewery`; **not** a collection called `map_reduce_example`).

* Get the top-10 of the breweries. How can we define a sort `High->Low`?

* Find all entries in the collection `<username>Brewery`, that contain the word 'Inbev' in the brewery field. Do you get 3 or 9 results? Why?

#### 2. Filter and aggregate with MapReduce

Belgium is notorious for brewing excellent strong beers. Let's define a strong beer as having an **alcohol percentage of more than 8 degrees**.

* Using a MapReduce approach, we are now interested in calculating the number of **STRONG** beers per brewery. Notice that this exercise is an elaboration of the previous MapReduce exercise. In addition, you will need a strategy for expressing the fact we only want to count beers with `Percentagealcohol` > 8. Store the result in a new collection called `<username>Strong` (e.g. `mjacksonStrong`).

  **Hint:** Different approaches for defining the filter are possible! Can you do it without changing the map or reduce functions of the previous exercise?

* Which brewery is the champion of strong beers?


#### 3. MapReduce statistics for Glory!

Data scientists are interested in calculating statistics. Let's investigate how we can accomplish that with MapReduce.

* Using a MapReduce approach, calculate the **maximum alcohol percentage** per type (`Soort`) of beer. This exercise is similar to the previous ones, but instead of calculating a count by brewery, we will now calculate the maximum `Percentagealcohol` per `Soort`. Store the result in a new collection called `<username>StatsMax` (e.g. `cdarwinStatsMax`).

  **Hint:** First think about how to calculate the maximum number from an array of numbers in JavaScript.

* Which type of beer is the winner?

#### 4. MapReduce statistics for Great Justice!

* Using a MapReduce approach, calculate the **average alcohol percentage** per type (`Soort`) of beer. Remember that in order to calculate an average, you will first need a sum and a count. Store the result in a new collection called `<username>StatsAvg` (e.g. `jwatsonStatsAvg`).

  **Hint:** This exercise will require you to define a finalizing step in the MapReduce operation. Revisit the MongoDB [examples](http://docs.mongodb.org/manual/tutorial/map-reduce-examples/) if this doesn't ring a bell.

* Remember from the query exercises that we have some beers with unknown `Percentagealcohol` in our database. This can be problematic when calculating statistics. Can you define a filter that makes sure we only use beers with known `Percentagealcohol` in our calculation?

* Give an overview of the average `Percentagealcohol` of all Christmas beers (beers where `Soort` contains "kerst").


# 4 Getting ready for the next step

Although the data is now in a schema-free database, it still is very similar to a RDBMS database system. Since we gradually want to move to graph databases, think about how the beer data could be reformulated in terms of a graph schema.

- What queries would be needed?
- What would the data look like?
- How would you approach this?
- Write down your ideas in a conceptual way, but don't execute them.
