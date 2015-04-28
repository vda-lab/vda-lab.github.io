---
title: GraphDB
layout: page
opacity: "true"
excerpt: The exercises concerning NoSQL databases&#58; MongoDB and Neo4J.
---

# Exercise 1: Graph Databases (Neo4J)

Learn about the Cypher language for querying Neo4J [here](http://www.neo4j.org/learn/cypher): <http://www.neo4j.org/learn/cypher>. Go through the different steps.

You don't _have_ to do the last step (installation of Neo4J), but you're obviously free to do so if you want to.


# Exercise 2: Application

Remember the different [datasets](datasets/datasets.html) we introduced earlier? We used these datasets to run RDBMS queries.

We now turn the question around: **For the 3 datasets each, write down a question that fits nicely with each of 3 database technologies: RDBMS, Document based and Graph DBs.**

What you should get is a table like this where every cell contains a question that can be answered about the respective dataset by using a the given database technology.

{:.table .table-bordered .table-condensed}
|                |   **drugs**  |   **beer**  |  **genotype**  |
| -------------- |  ----------- |  ---------- | -------------- |
| **RDBMS**      |              |             |                |
| **Document**   |              |             |                |
| **Graph**      |              |             |                |

The questions for every combination, as well as a short description of how you would want to tackle the problem can be put on Toledo.



# Exercise 3: Graph databases in practice

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

