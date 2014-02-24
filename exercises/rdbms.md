
# RDBMS and SQL

In the following exercises, we will be using `sqlite3`. It is a lightweight system for dealing with RDBMS databases that can be stored in normal files on a file system. This is in contrast to systems like MySQL which are more widely used, but require to run a dedicated database server. Consider `sqlite` is like Microsoft Access, where the whole database itself is nothing more than a file in your directory.

A tutorial on `sqlite` can be found [here](http://zetcode.com/db/sqlite/) and instruction videos can be found on Youtube.

We refer to the [description of the datasets](datasets) for more information about what each of them contains.

For this exercise session, we will consider

* data modeling
* data loading
* data querying

**CAUTION**: When using sqlite3, make sure that you know whether you are on the **unix command line** (the place you already know and love: for running commands such as `ls`, `cd some_directory`, `less some_file.txt`, etc), and the **sqlite3 command line** (where you can issue SQL commands such as `SELECT column1, column2 FROM some_table;`). The **unix command line** is similar to this:

    jaerts@ip-10-158-90-118:~$

The **sqlite3 command line** looks like this:

    sqlite> 

To go from the unix command line to the sqlite3 command line, type:

    sqlite3 name_of_my_database.db

To exit the sqlite3 command line and return to the unix command line, type:

    .quit

Do *not* try to run SQL commands on the unix command line; do *not* try to run unix commands on the sqlite3 command line...

Example use for sqlite3 if we want to create a new database called `students`. Here's a sample session (obviously do **not** type in the text of the prompt itself...):

    jaerts@ip-10-158-90-118:~$ sqlite3 students.db
    sqlite> CREATE TABLE individuals (id INTEGER AUTO_INCREMENT, s_number STRING, first_name STRING, last_name STRING);
    sqlite> CREATE TABLE courses (id INTEGER AUTO_INCREMENT, course_number STRING, name STRING);
    sqlite> INSERT INTO individuals (s_number, first_name, last_name) VALUES ('s123456','Tom','Thompson');
    sqlite> INSERT INTO individuals (s_number, first_name, last_name) VALUES ('s987654','John','Jones');
    sqlite> SELECT * FROM individuals;
    sqlite> .quit
    jaerts@ip-10-158-90-118:~$

When on the `sqlite3` prompt, type `.help` for a list of `sqlite3`-specific commands (such as `.quit`).

## Beers

Creating the table to hold the data.

    CREATE TABLE beers(id INTEGER, beer TEXT, type TEXT, alc FLOAT, brewery TEXT);

Select the appropriate field delimiter.

    .separator ","

Import the data. This is easiest from the CSV data.

    .import beers.csv beers

Review whether this was successful and whether the result makes sense.

    SELECT * FROM beers LIMIT 5;

Don't forget the `;` symbol at the end of the line! The first entry in the data is the header, which should be removed.

    DELETE FROM beers WHERE beer="Merk";

Get the top-10 of brewerys based on the number of beers they produce.

    SELECT brewery, COUNT(beer) FROM beers GROUP BY brewery ORDER BY COUNT(beer) DESC LIMIT 10;

Why is AB Inbev not in the top 10? List all beers that are brewed by a brewery that contains the word 'Inbev'. 

    SELECT * FROM beers WHERE brewery LIKE "%Inbev%";

Correct that in the database, giving all entries related to AB Inbev the same name.

    UPDATE beers SET brewery="AB Inbev" WHERE brewery LIKE "%Inbev%";

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
CREATE TABLE drugs1 (
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
CREATE TABLE drugs2 (
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
CREATE TABLE joined 
    AS SELECT cti,mpname,mah,ActSubstName,dosis
    FROM drugs1, drugs2
    WHERE drugs1.cti = drugs2.cti;
```

What is the top-10 of compounds with the most active substances?

```
SELECT cti,COUNT(actsubstname) 
    FROM joined 
    GROUP BY cti 
    ORDER BY COUNT(actsubstname) DESC
    LIMIT 10;
```

What type of compounds/products are in the top-10? Is this normal?

Which companies have compounds on the market with more than 10 active substances? Put this information in a table.

```
CREATE TABLE companies
    AS SELECT mah, COUNT(actsubstname) 
    FROM joined 
    GROUP BY cti 
    HAVING COUNT(actsubstname) > 10 
    ORDER BY COUNT(actsubstname) DESC;
```

From this data, create a table that shows for every of the companies in the table, how many complex compounds they have on the market.

```
SELECT mah, COUNT(mpname) 
    FROM companies 
    GROUP BY mah 
    ORDER BY COUNT(mpname) DESC;
```


## Genotypes

Look at the data. Is this it normalized? Is this a handy form for querying the data?

We will focus first on the limited dataset for the first sample.

Create the table.

```
CREATE TABLE geno(
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
SELECT COUNT(*) FROM geno;
```

```
SELECT COUNT(*) FROM geno WHERE HG00096 NOT LIKE "0|0%";
```

