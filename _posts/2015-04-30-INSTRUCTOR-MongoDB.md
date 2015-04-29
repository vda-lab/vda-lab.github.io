---
title: Instructor notes for MongoDB
layout: page
instructor: "true"
---

# Exercise 1: Document Databases (MongoDB)

Some data has been prepared in the MongoDB instance. This is done already for you by using the following commands:

    mongoimport --db exercises --collection beers --type json --file /mnt/bioinformatics_leuven/i0u19a/data/beer/beers.json --jsonArray

    mongoimport --db exercises --collection genotypes --type tsv --file /mnt/bioinformatics_leuven/i0u19a/data/genotypes/chr1-0-100000.vcf --stopOnError --fieldFile header.txt

The percentage alcohol in the beer database has been converted to floats using the following instruction:

    db.beers.find({"Percentagealcohol" : {$exists : true}}).forEach( function(obj) { obj.Percentagealcohol = Number( obj.Percentagealcohol ); db.beers.save(obj); } );

The result is that the genotypes data and beer data is already stored in the mongDB database on the teaching server.


## 1.a. Simple queries

Connect to the mongoDB instance using the `mongo` shell. This is done by typing the following command in the shell on the teaching server:

    tverbeiren@ip-10-158-90-118:~$ mongo
    MongoDB shell version: 2.0.4
    connecting to: test
    >

You now get the MongoDB prompt in which we will work now. At the end, you can escape the MongoDB shell by typing exit. Connect to the database for this exercise:

    > use exercises

Based on what you have learned from the assignment for this session, you should be able to answer the following questions:

* How many beers in the database are of type _hoge gisting_? The type of beer corresponds to the field `Soort` in the database.
* How many beers have a percentage alcohol of more than 8 degrees?
* How many beers have an **unknown** alcohol percentage?

#### Solution

``` javascript
db.beers.find({"Soort":"hoge gisting"}).count()
-> 170

db.beers.find({"Percentagealcohol": {$gt: 8}}).count()
-> 399

db.beers.find({"Percentagealcohol": NaN}).count()
-> 12```


## 1.b. MapReduce in MongoDB

###1. A basic MapReduce exercise

* Using a MapReduce approach (create a `mapFunction2` and `reduceFunction2`), get the number of beers per brewery. Store the result in a collection called `<username>Brewery` (*e.g.* `tverbeirenBrewery`; **not** a collection called `map_reduce_example`).
* Get the top-10 of the breweries.  How can we define a sort `High->Low`?
* Find all entries in the collection `<username>Brewery`, that contain the word 'Inbev' in the brewery field. Do you get 3 or 9 results? Why?

####Solution

``` javascript
db.beers.mapReduce(
    function() {
        emit(this.Brouwerij, 1);
    },
    function(key,values) {
        return Array.sum(values);
    },
    {out: "tverbeirenBrewery"});

db.tverbeirenBrewery.find().sort({"value":-1}).limit(10);

db.tverbeirenBrewery.find({"_id": /Inbev/}).count()
-> 3

// Case-insensitive version of regex has suffix "i"
db.tverbeirenBrewery.find({"_id": /Inbev/i}).count()
-> 9```


###2. Filter and aggregate with MapReduce

Belgium is known for brewing excellent strong beers. Let's define a strong beer as having an **alcohol percentage of more than 8 degrees**.

* Using a MapReduce approach, we are now interested in calculating the number of **STRONG** beers per brewery. Notice that this exercise is an elaboration of the previous MapReduce exercise. In addition, you will need a strategy for expressing the fact we only want to count beers with `Percentagealcohol` > 8. Store the result in a new collection called `<username>Strong` (e.g. `mjacksonStrong`).

  **Hint:** Different approaches for defining the filter are possible! Can you do it without changing the map or reduce functions of the previous exercise?

* Which brewery is the champion of strong beers?

#### Solution
``` javascript
// The filter step should be defined in the `query` clause of the MapReduce operation.
// It is also possible to implement the filter as a condition before emitting in the map
// function. We prefer the first approach.

var fmap2 = function() {
    emit(this.Brouwerij, 1);
}

var fred2 = function(key, values) {
    return Array.sum(values);
}

db.beers.mapReduce(
    fmap2,
    fred2,
    {query: {"Percentagealcohol": {$gt : 8}}, // <- THE QUERY CLAUSE
     out : "mjacksonStrong"});

db.mjacksonStrong.find().sort({"value":-1}).limit(1);
-> { "_id" : "Brouwerij Alvinne", "value" : 16 }
```

###3. MapReduce statistics for Glory!

Data scientists are interested in calculating statistics. Let's investigate how we can accomplish that with MapReduce.

* Using a MapReduce approach, calculate the **maximum alcohol percentage** per type (`Soort`) of beer. This exercise is similar to the previous ones, but instead of calculating a count by brewery, we will now calculate the maximum `Percentagealcohol` per `Soort`. Store the result in a new collection called `<username>StatsMax` (e.g. `cdarwinStatsMax`).

  **Hint:** First think about how to calculate the maximum number from an array of numbers in JavaScript.

#### Solution
``` JavaScript
// To calculate the maximum from an array of numbers:
var a = [2.3, 7.1, 4.0]
Math.max.apply(null, a)
> 7.1

var fmap3 = function() {
    emit(this.Soort, this.Percentagealcohol);
};

var fred3 = function(key, values) {
    return Math.max.apply(null, values);
};

db.beers.mapReduce(
	fmap3,
	fred3,
	{out: "mjacksonStatsMax"});

db.mjacksonStatsMax.find().sort({"value": -1}).limit(1);
-> { "_id" : "Russian Imperial Stout, Eisbockmethode", "value" : 26 }```

###4. MapReduce statistics for Great Justice!

* Using a MapReduce approach, calculate the **average alcohol percentage** per type (`Soort`) of beer. Remember that in order to calculate an average, you will first need a sum and a count. Store the result in a new collection called `<username>StatsAvg` (e.g. `jwatsonStatsAvg`).

  **Hint:** This exercise will require you to define a finalizing step in the MapReduce operation. Revisit the MongoDB [examples](http://docs.mongodb.org/manual/tutorial/map-reduce-examples/) if this doesn't ring a bell.

* Remember from the query exercises that we have some beers with unknown `Percentagealcohol` in our database. This can be problematic when calculating statistics. Can you define a filter that makes sure we only use beers with known `Percentagealcohol` in our calculation?

* Give an overview of the average `Percentagealcohol` of all Christmas beers (beers where `Soort` contains "kerst").

#### Solution

```javascript
// For calculating the average from the sum and the count, we will need a "finalize"
// function.

var fmap4 = function() {
    emit(this.Soort, {count: 1,
                      sum: this.Percentagealcohol});
};

var fred4 = function(key, values) {
    var result = {count: 0, sum: 0};

    for (var v in values) {
        result.count += values[v].count;
        result.sum += values[v].sum;
    }

    return result;
};

var fin4 = function(key, reduced) {
    return reduced.sum / reduced.count;
};

db.beers.mapReduce(
	fmap4,
	fred4,
	{finalize: fin4, // <- FINALIZE CLAUSE
     query: {"Percentagealcohol": {$ne : NaN}},
     out: "mjacksonStatsAvg"});

db.mjacksonStatsAvg.find({"_id": /kerst/i});
-> { "_id" : "Erkend Belgisch Abdijbier, kerstbier", "value" : 8.5 }
   { "_id" : "abdijbier, kerstbier", "value" : 8.875 }
   { "_id" : "amber, kerstbier", "value" : 6.5 }
   ...
```

## 1.c Getting ready for the next step

Although the data is now in a schema-free database, it still is very similar to a RDBMS database system. Since we gradually want to move to graph databases, think about how the beer data could be reformulated in terms of a graph schema.

What queries would be needed? What would the data look like? How would you approach this? Write down your ideas in a conceptual way, but don't execute them.

Solution:

Store relevant data in nodes and relations collection. MongoDB keys (`_id`) are used to connect the nodes.

    db.beers.find(
      {"Merk" : {$exists : true}}
    ).forEach(
      function(obj) {
        // Nodes
        var MerkDoc = {name: obj.Merk, type: "Merk"};
        var AlcoholDoc = {name: obj.Percentagealcohol, type: "Alcohol"};
        var BrouwerijDoc = {name: obj.Brouwerij, type: "Brouwerij"};
        var SoortDoc = {name: obj.Soort, type: "Soort"};
        db.tverbeirenNodes.save(MerkDoc);
        db.tverbeirenNodes.save(AlcoholDoc);
        db.tverbeirenNodes.save(BrouwerijDoc);
        db.tverbeirenNodes.save(SoortDoc);

        // Relations
        var AlcoholRelation = {name: "hasAlcohol", from: MerkDoc._id, to: AlcoholDoc._id };
        var BrewedByRelation = {name: "BrewedBy", from: MerkDoc._id, to: BrouwerijDoc._id };
        var isaRelation = {name: "isa", from: MerkDoc._id, to: SoortDoc._id };
        db.tverbeirenRelations.save(AlcoholRelation);
        db.tverbeirenRelations.save(isaRelation);
        db.tverbeirenRelations.save(BrewedByRelation);
      });



# Exercise 2: Graph databases

Start the server:

    /mnt/bioinformatics_leuven/Software/neo4j-community-1.7.2$ sudo ./bin/neo4j start

Some settings/modifications are in order:

`neo4j.properties`:

    # The node property keys to be auto-indexed, if enabled
    node_keys_indexable=name,age

    #enable auto-indexing for relationships, default is false
    relationship_auto_indexing=true

    # The relationship property keys to be auto-indexed, if enabled
    relationship_keys_indexable=name,age

`neo4j-server.properties`:

    # let the webserver only listen on the specified IP. Default
    # is localhost (only accept local connections). Uncomment to allow
    # any connection. Please see the security section in the neo4j
    # manual before modifying this.
    org.neo4j.server.webserver.address=0.0.0.0

Now, restart the server. We will be using the REST API in this exercise. First, take a look at the installation:

    curl http://localhost:7474

Thanks to [a blog article](http://neo4j.com/blog/fun-with-beer-and-graphs/) by a Neo4J sales person, getting the data into the database is relatively easy. Since he delivers the neo4j database as a zip file, it's possible to replace the existing one with this one.

Indexes should be automatically created when updating the conf file as described above. In order to check this, type:

    index --indexes

To check whether the node index works, use this:

    start a = node:node_auto_index(name="Orval") return a

The names of the nodes and relations have been translated to English:

* nodes : BeerBrand, BeerType, Brewery
* relations: isa (beertype), hasa (alcoholpercentage), brews (a beerbrand)


## 2.a. Starting up the Neo4J interface

Browse to the Data Browser in the web interface of Neo4J:

    http://50.16.33.38:7474/webadmin

Open the `Data Browser` and in the search field type: 17

* What do you see?
* What is the meaning of it?
* What is the alcoholpercentage of the beer corresponding to node with id 17?

Do the same searches from the `Console` (3d tab on top).

## 2.b. Simple Queries

Do some simple queries using Cypher in the Console window:

* What Node ID does "Orval" (BeerBrand) have?
* What about "Duvel"?
* What is the Node ID of Brewery node "AB Inbev"?

Solution:

```
start a = node:node_auto_index(name="Orval") return a
start a = node:node_auto_index(name="AB Inbev") return a
```


## 2.c Relationships

Find the following:

* In the first exercise, we have found the brewery that brews the most beers. Get a list of these beers using Cypher.
* All the bears that are brewed by the brewery of the beer "Duvel".
* All Belgian Trappist beers if you know Orval is a Belgian Trappist
* The shortest paths in the graph between two beers, say "Orval" and "Duvel"

Solution:

```
start huyghe=node:node_auto_index(name="Brouwerij Huyghe")
match huyghe<-[:Brews]->beer
return beer.name
```

```
start duvel=node:node_auto_index(name="Duvel")
match
duvel<-[:Brews]->brouwerij,
duvel-[:isa]->biertype,
anderbier<-[:Brews]->brouwerij,
anderbier-[:isa]->biertype2
return
anderbier.name AS name,
collect(biertype2.name) AS biertype
```

```
start orval=node:node_auto_index(name="Orval")
match
orval<-[:Brews]->brouwerij,
orval-[:isa]->biertype,
anderbier-[:isa]->biertype
return
anderbier.name AS name,
collect(biertype.name) AS biertype
order by anderbier.name;
```

```
START
  duvel=node:node_auto_index(name="Duvel"),
  orval=node:node_auto_index(name="Orval")
MATCH p = AllshortestPaths( duvel-[*]-orval )
return p;
```


