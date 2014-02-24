
# RDMS and SQL

In the following exercises, we will be using `sqlite3`. It is a lightweight system for dealing with RDBMS databases that can be stored in normal files on a file system.

A tutorial on `sqlite` can be found [here](http://zetcode.com/db/sqlite/) and instruction videos can be found on Youtube.

We refer to the [description of the datasets](datasets) for more information about what each of them contains.


## Beers

Creating the table to hold the data.

    CREATE TABLE beers(key INTEGER, beer TEXT, type TEXT, alc FLOAT, brewery TEXT);

Select the appropriate field delimiter.

    .separator ","

Import the data. This is easiest from the CSV data.

    .import beers.csv beers

Review whether this was succesful and whether the result makes sense.

    select * from beers limit 5;

Don't forget the `;` symbol at the end of the line! The first entry in the data is the header, which should be removed.

    DELETE FROM beers WHERE beer="Merk";

Get the top-10 of brewerys based on the number of beers they produce.

    select brewery, count(beer) from beers Group By brewery order by count(beer) DESC limit 10;

Why is AB Inbev not in the top 10? List all beers that are brewed by a brewery that contains the word 'Inbev'. 

    select * from beers where brewery like "%Inbev%";

Correct that in the database, giving all entries related to AB Inbev the same name.

    update beers set brewery="AB Inbev" where brewery like "%Inbev%";

Suddenly, probably as expected, AB Inbev ranks highest. 

How many times does it occur? What is the top-10 now?


## drugdb

We mentioned that one of the two datafiles contains a subset of the parameters of the large one. Check this explicitely. Make sure you save the routine for importing the data into `sqlite`.

Remember that there are two source files:

* `AMM_det_H` contains the active substances in the doses they have been granted permission to use in drug compounds.
* `AMM_H` contains the drug compounds that can be sold on the market.

Is this data normalized? What is the key that joins both datasets together? Does it make sense to organize the data in this way?

First import the full database.

```
create table drugs1 (
    nr INTEGER,
    cti INTEGER,
    mpname TEXT,
    mah TEST,
    Registratienummer TEXT,
    registdate TEXT,
    generic INTEGER,
    packsize TEXT,
    supplyproblem TEXT,
    PharmFormNl TEXT,
    PharmFormFr TEXT,
    PharmFormDe TEXT,
    PharmFormEn TEXT,
    PackNl TEXT,
    PackFr TEXT,
    PackDe TEXT,
    PackEn TEXT,
    CommNl TEXT,
    CommFr TEXT,
    CommDe TEXT,
    CommEn TEXT,
    DelivNl TEXT,
    DelivFr TEXT,
    DelivDe TEXT,
    DelivEn TEXT,
    ActSubsts TEXT,
    GenNl TEXT,
    GenFr TEXT,
    GenDe TEXT,
    GenEn TEXT,
    GenPK TEXT
    );
.separator ","
.import AMM_H.csv drugs1
```

Do the same for the subset database.

```
create table drugs2 (
    nr INTEGER,
    cti INTEGER,
    ActSubstName TEXT,
    unit TEXT,
    dosis TEXT,
    DateNew DATE
);
.separator ","
.import AMM_det_H.csv drugs2
```

What are the dimensions of both tables?
```
    select count(*) from drugs1;
    select count(*) from drugs2;
```

Which one is bigger? Join the data and look at some entries.

Note: to make life easier, you can change the _output mode_ of sqlite: `.mode column` for instance.

```
create table joined 
    as select cti,mpname,mah,ActSubstName,dosis from drugs1 
    join drugs2 
    using (cti);
```

What is the top-10 of compounds with the most active substances?

```
select cti,count(actsubstname) 
    from joined 
    group by cti 
    order by count(actsubstname) 
    desc limit 10;
```

What type of compounds/products are in the top-10? Is this normal?

Which companies have compounds on the market with more than 10 active substances? Put this information in a table.

```
create table companies
    as select mah,count(actsubstname) 
    from joined 
    group by cti 
    having count(actsubstname) > 10 
    order by count(actsubstname) desc;
```

From this data, create a table that shows for every of the companies in the table, how many complex compounds they have on the market.

```
select mah,count(mpname) 
    from companies 
    group by mah 
    order by count(mpname) desc;
```


## Genotypes

Look at the data. Is this it normalized? Is this a handy form for querying the data?

We will focus first on the limited dataset for the first sample.

Create the table.

```
create table geno(
   chrom CHARACTER,
   pos INTEGER,
   id TEXT,
   ref CHARACTER,
   alt CHARACTER,
   qual TEXT,
   filter TEXT,
   info TEXT,
   format TEXT,
   HG00096 TEXT);
```

Import the data. In order to make life easy, start from the HG000096 sample and manually remove the comments and header row. Then import the data.

```
.mode tabs
.import test.vcf geno
```

How many mutations are known for this genomic region on chromosome 1?

How many of these are there in this region for sample HG00096? If you don't know the way this information is encoded in the vcf file, refer to the web for more information. What is a good way to get all the mutations for this sample? Think about it.

```
select count(*) from geno;
```

```
select count(*) from geno where HG00096 not like "0|0%";
```

