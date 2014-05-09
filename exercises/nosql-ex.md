% NoSQL - Exercises

- - -

# Exercise 1: Document Databases (MongoDB)

The data for genotypes and beer as used in the course before, is already stored in the mongDB database on the teaching server.


## 1.a. Simple queries

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

Based on what you have learned from the assignment for this session, you should be able to answer the following questions:

* How many beers in the database are of type _hoge gisting_? The type of beer corresponds to the field `Soort` in the database.
* How many beers have a percentage alcohol of more than 8 degrees?

## 1.b. MapReduce in MongoDB

To use mapreduce, you will define two functions: a *map* function and a *reduce* function. Suppose we have a collection of documents that describe purchases made by a customer. These documents therefore look like this:

    {
        _id: ObjectId("50a8240b927d5d8b5891743c"),
        cust_id: "abc123",
        ord_date: new Date("Oct 04, 2012"),
        status: 'A',
        price: 25,
        items: [ { sku: "mmm", qty: 5, price: 2.5 },
                 { sku: "nnn", qty: 5, price: 2.5 } ]
    }

Suppose that we have returning customers who spend different amounts every visit. If we want to calculate how much each customer spent in total (across visits), we can do this using a mapreduce approach. Taken from http://docs.mongodb.org/manual/tutorial/map-reduce-examples/ :

[1] Define the map function to process each input document:

* In the function, the keyword `this` refers to the document that the map-reduce operation is processing.
* The function maps the price to the `cust_id` for each document and emits the `cust_id` and `price` pair.
```
var mapFunction1 = function() {
                        emit(this.cust_id, this.price);
                   };
```
[2] Define the corresponding reduce function with two arguments `keyCustId` and `valuesPrices`:

* `valuesPrices` is an array whose elements are the price values emitted by the map function and grouped by `keyCustId`.
* The function reduces the `valuesPrices` array to the sum of its elements.
```
var reduceFunction1 = function(keyCustId, valuesPrices) {
                          return Array.sum(valuesPrices);
                      };
```
[3] Perform the map-reduce on all documents in the `orders` collection using the `mapFunction1` map function and the `reduceFunction1` reduce function.
```
db.orders.mapReduce(
                 mapFunction1,
                 reduceFunction1,
                 { out: "map_reduce_example" }
               )
```
This command will create a new collection named `map_reduce_example` that will contain the results.

Actual exercise:

* Using a mapreduce approach (create a `mapFunction2` and `reduceFunction2`), get the number of beers per brewery. Store the result in a collection called `<username>Brewery` (*e.g.* `jaertsBrewery`; **not** a collection called `map_reduce_example`).
* Get the top-10 of the breweries.
* Find all entries in the collection `<username>Brewery`, that contain the word 'Inbev' in the brewery field.

You can find info about map reduce in MongoDB here: <http://docs.mongodb.org/manual/core/map-reduce/> and <http://docs.mongodb.org/manual/tutorial/map-reduce-examples/>. The mongoDB shell uses Javascript syntax. 

The way to approach the solution can be found in the exercises concerning MapReduce.


## 1.c Getting ready for the next step

Although the data is now in a schema-free database, it still is very similar to a RDBMS database system. Since we gradually want to move to graph databases, think about how the beer data could be reformulated in terms of a graph schema.

What queries would be needed? What would the data look like? How would you approach this? Write down your ideas in a conceptual way, but don't execute them.


# Exercise 2: Graph databases

The beer data is available in the Neo4J database on the teaching server. The names of the nodes and relations have been translated to English:

* nodes : BeerBrand, BeerType, Brewery
* relations: isa (beertype), hasa (alcoholpercentage), brews (a beerbrand)


## 2.a. Starting up the Neo4J interface

Browse to the Data Browser in the web interface of Neo4J:

    http://50.16.33.38:7474/webadmin

Open the `Data Browser` and in the search field type: 17

* What do you see?
* What is the meaning of it?
* What is the alcoholpercentage of the beer corresponding to node with id 17?

Do the same searches from the `Console` (3rd tab on top).

## 2.b. Simple Queries using Cypher

Cypher is a powerful query language for graph databases that is inspired by ASCII art. Basically, you define the pattern that you're looking for as a picture. For example, looking for a node that is connected through a relationship to a second node could in ASCII art be represented as `()-->()` (imagine 2 circles connected with an arrow). We call the left `()` the *source* of the relationship, and the `()` on the right the *sink*. The parentheses are optional and can be left out. In addition, square brackets can be used in the middle of the arrow for indicating constraints or variables. For example: `a-[rel]->b`.

You can perform these queries in the webinterface to neo4j (see the URL mentioned above), but also on the linux command line. To do this, connect to the server through ssh (as you normally do), and issue the command `/mnt/bioinformatics_leuven/Software/neo4j-community-1.7.2/bin/neo4j-shell`.

Cypher queries consist minimally of a `START` and a `RETURN` clause. Getting all nodes in a graph:
```
START n=node(*) RETURN n
```
An optional `MATCH` can be used that represents (in ASCII art) the pattern that you're looking for. The command below return all possible relationships in a graph database:
```
START n=node(*) MATCH n-[r]->m RETURN n,r,m
```
Similar to SQL, a `WHERE` clause lets you filter the data. For example, suppose that there are nodes with a property `type`. To get all relationships where the sink type = 'BeerBrand', we issue the following search:
```
START n=node(*) MATCH n-[r]->m WHERE m.type = 'BeerBrand' RETURN n,r,m
```

The `START n=node(*)` signifies that you start your pattern search from any node. There are 2 ways to start from a particular node. If you happen to know the ID, just substitute that for the `*`, for example
```
START n=node(17) MATCH n-[r]->m RETURN n,r,m
```
In case you don't know the node ID, but want to do a search on a particular property, you use the `node_auto_index` like this:
```
START n=node:node_auto_index(name="Inbev Belgium") RETURN n
```

For a more extensive introduction to the Cypher language, see the video "Cypher for SQL Professionals" at http://www.neo4j.org/tracks/cypher_track_use. A reference card can be found at http://docs.neo4j.org/refcard/2.0/

As an exercise, do some simple queries using Cypher in the Console window:

* What Node ID does the beer "Orval" have?
* What about "Duvel"?
* What is the Node ID of Brewery node "AB Inbev"?


## 2.c Relationships

Find the following:

* In the first exercise, we have found the brewery that brews the most beers. Get a list of these beers using Cypher.
* All the beers that are brewed by the brewery of the beer "Duvel".
* All Belgian Trappist beers if you know Orval is a Belgian Trappist
* The shortest paths in the graph between two beers, say "Orval" and "Duvel"

