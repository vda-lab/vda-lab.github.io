---
title: GraphDB
layout: page
opacity: "false"
highlight: "true"
excerpt: The exercises concerning graph databases, especially Neo4J.
---

# 1. Introduction

Learn about the Cypher language for querying Neo4J [here](http://www.neo4j.org/learn/cypher): <http://www.neo4j.org/learn/cypher>. Go through the different steps.

_Don't_ do the last step (installation of Neo4J), but you're obviously free to do so on your own pc later at home if you want to.


# 2. Neo4J web interface and the Cypher shell

Browse to the user interface via [web interface of Neo4J](http://54.93.45.232:7474/browser):

    http://54.93.45.232:7474/browser

Click on Brews on the left and take a look at the resulting graph.

* What do you see?
* What is the meaning of it?
* Dubble-click on some of the nodes in order to expand their relations to other nodes.

Do the same searches from the `Console` (3rd tab on top). Use your _cypher skills_ acquired earlier.


# 3. Neo4J in practice

The beer data is available in the Neo4J database on the teaching server. The names of the nodes and relations have been translated to English:

* nodes : `BeerBrand`, `BeerType`, `Brewery`
* relations: `isa` (beertype), `hasa` (alcoholpercentage), `brews` (a beerbrand)

You can perform queries in the webinterface to neo4j (see the URL mentioned above). Just type the query in the field above and press the arrow or `CTRL-ENTER`.

Cypher queries consist minimally of a `START` and a `RETURN` clause. Getting all nodes in a graph (limited to the 10 first):

```
MATCH (n) RETURN n LIMIT 10
```

The command below return all possible relationships in a graph database:

```
MATCH n-[r]->m RETURN n,r,m LIMIT 10
```

Similar to SQL, a `WHERE` clause lets you filter the data. For example, suppose that there are nodes with a property `type`. To get all relationships where the sink type = 'BeerBrand', we issue the following search:

```
START n=node(*)
MATCH n-[r]->m WHERE m.type = 'BeerBrand' 
RETURN n,r,m LIMIT 10
```

The `START n=node(*)` signifies that you start your pattern search from any node and can be omited in this case. If you _do_ want to start from a specific node, there are 3 ways to do that: If you happen to know the ID, just substitute that for the `*`, for example

```
START n=node(17) MATCH n-[r]->m RETURN n,r,m
```

In case you don't know the node ID, but want to do a search on a particular property, you use the `node_auto_index` like this:

```
START n=node:node_auto_index(name="Inbev Belgium") RETURN n
```

An alternative is by not using `START` at all, but using `WHERE` on a `MATCH`:

```
MATCH n WHERE n.name = 'Inbev Belgium' 
RETURN n
```

For a more extensive introduction to the Cypher language, see the video "Cypher for SQL Professionals" at <http://www.neo4j.org/tracks/cypher_track_use>. A reference card can be found at <http://docs.neo4j.org/refcard/2.0/>

## 3.a Simple queries

As an exercise, do some simple queries using Cypher in the Console window:

* What Node ID does the beer "Orval" have?
* What about "Duvel"?
* What is the Node ID of Brewery node "AB Inbev"?


## 3.b Relationships

In the exercise session about MongoDB, we have found the brewery that brews the most beers: `Brouwerij Huyghe`.

Find the following:

* Get a list of the beers by `Brouwery Huyghe`.
* Find all the beers that are brewed by the brewery of the beer "Duvel".
* All Belgian Trappist beers if you know Orval is a Belgian Trappist
* The shortest paths in the graph between two beers, say "Orval" and "Duvel"


## 3.c Adding nodes and relations

Add a node with your name (node type `Person`) and a link `loves` to a beer of your choice.

Query for the beers with the most `loves`. Create a top-10.


- - -

_When you have time left, please take a look at the following exercise:_




# 4. Roundup

Remember the different [datasets](datasets/datasets.html) we introduced earlier? We used these datasets to run RDBMS queries.

We now turn the question around: **For the 3 datasets each, write down a question that fits nicely with each of 3 database technologies: RDBMS, Document based and Graph DBs.**

What you should get is a table like this where every cell contains a question that can be answered about the respective dataset by using a the given database technology.

{:.table .table-bordered .table-condensed}
|                |   **drugs**  |   **beer**  |  **genotype**  |
| -------------- |  ----------- |  ---------- | -------------- |
| **RDBMS**      |              |             |                |
| **Document**   |              |             |                |
| **Graph**      |              |             |                |

