% NoSQL - Solutions

- - -

# Exercise 1: Document Databases (MongoDB)

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

Possible solution:

    mongo
    show dbs
    use exercises
    db.beers.find({"Soort":"hoge gisting"}).count()
    db.beers.find({"Percentagealcohol": {$gt: 8}}).count()


## 1.b. MapReduce in MongoDB

Implement a map reduce approach to get the number of beers per brewery. 

* Store the result in a collection called `<username>Brewery`.
* Get the top-10 of the breweries.
* Find all entries in the collection `<username>Brewery`, that contain the word 'Inbev' in the brewery field.

You can find info about map reduce in MongoDB here: <http://docs.mongodb.org/manual/core/map-reduce/>. The mongoDB shell uses Javascript syntax. 

The way to approach the solution can be found in the exercises concerning MapReduce.

Possible solution:

    db.beers.mapReduce(
        function() {
            emit(this.Brouwerij, 1);}, 
        function(key,values) {
            return Array.sum(values);},
        {out: "tverbeirenBrewery"})

    db.tverbeirenBrewery.find().sort({"value":-1}).limit(10)
    db.tverbeirenBrewery.find({"_id": /Inbev/})


## 1.c Getting ready for the next step

Although the data is now in a schema-free database, it still is very similar to a RDBMS database system. Since we gradually want to move to graph databases, think about how the beer data could be reformulated in terms of a graph schema.

What queries would be needed? What would the data look like? How would you approach this? Write down your ideas in a conceptual way, but don't execute them.

Possible solution:

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

Possible solution:

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

Possible solutions:

```
START huyghe=node:node_auto_index(name="Brouwerij Huyghe") 
MATCH huyghe<-[:Brews]->beer 
RETURN beer.name
```

```
START duvel=node:node_auto_index(name="Duvel")
MATCH
    duvel<-[:Brews]->brouwerij,
    anderbier<-[:Brews]->brouwerij,
RETURN anderbier.name
```

```
START orval=node:node_auto_index(name="Orval")
MATCH
    orval-[:isa]->biertype,
    anderbier-[:isa]->biertype
RETURN
    anderbier.name
```

```
START
  duvel=node:node_auto_index(name="Duvel"),
  orval=node:node_auto_index(name="Orval")
MATCH p = AllshortestPaths( duvel-[*]-orval )
RETURN p;
```
