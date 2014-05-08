% NoSQL - Exercises

- - -

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

Solution:

!!! in en out

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

Solution:

    db.beers.mapReduce(function() {emit(this.Brouwerij, 1);}, function(key,values) {return Array.sum(values);},{out: "tverbeirenBrewery"})
    
    db.tverbeirenBrewery.find().sort({"value":-1}).limit(10)

    db.tverbeirenBrewery.find({"_id": /Inbev/})


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


