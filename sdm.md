---
layout: page
title: Software and data management
permalink: sdm.html
custom_css: with_tables
---
[ECTS file](https://uhintra03.uhasselt.be/studiegidswww/opleidingsonderdeel.aspx?a=2016&i=3561&n=4&t=04)

## Course information 2019-2020

This page concerns the "concepts of data management and structured query language" part of the Software and Data Management (SDM) course of MSc Statistics at UHasselt (see ECTS file above). For R and SAS, see blackboard.

This part is organised in 2 lectures and 1 practical session. **Study material** is available as 3 blog posts on [http://vda-lab.be/teaching]({{site.baseurl}}/teaching), of which PDFs are also available on [blackboard](https://bb.uhasselt.be).

  1. [Session 1: Introduction and database design]({{ site.baseurl }}/2019/08/extended-introduction-to-relational-databases)
  1. [Session 2: Beyond SQL]({{site.baseurl}}/2019/09/beyond-sql)
  1. [Session 3: Practical session](): Querying the [chinook database](https://www.sqlitetutorial.net/sqlite-sample-database/)

### Practical information

**Software** used throughout the lectures and in the practical session is `sqlite`. We'll use the command line interface, as well as the graphical user interface "DB Browser for SQLite" which you can find at [http://sqlitebrowser.org](http://sqlitebrowser.org).

The 3 **homework assignments** should be performed _individually_ and _after each lecture_.

The **exam** is pen-and-paper, and closed book.

### Schedule

| Date | Time | Topic | Location |
| :-- | :-- | :-- | :-- |
| Tue 24/09 | 9:30 - 12:30 | Introduction and database design | |
| Mon 14/10 | 23:59 | Due date: Homework 1 | BlackBoard |
| Fri 18/10 | 09:00 – 12:30 | Session 2: SQL | |
| Thu 07/11 | 23:59 | Due date: Homework 2 | BlackBoard |
| Fri 08/11 | 09:00 – 17:00* | Practical Session | C108B / C113 |
| Thu 28/11 | 23:59 | Due date: Homework 3 | BlackBoard |

<small>* _For the practical session, the group will be split in half. Morning session 09:00 –
12:30 and afternoon session 13:30 – 17:00._</small>

### Goal of (this part of) the course
Students should be able to construct and retrieve information from a normalised database using Structured Query Language (SQL) in sqlite, as well as understand the possibilities of NoSQL databases (i.c. ArangoDB).

- normalised database = a collection of data tables with desirable relational properties respecting particular data requirements. This enables unambiguous data retrieval, efficient data storage, data protection, etc
- SQL = standardised system used to combine data tables in a normalised relational database. This enables retrieval of data, answers to ad-hoc questions, etc
- sqlite = Data Base Management System (DBMS) that allows you to store the collection of data (= database), supports a query
language, produces reports, and creates data entry screens. Other examples are Microsoft Access, Oracle DB, Filemaker, etc.

The data management part covers:
- what data do we need to record and how are we going to collect them?
- how to store this data in an efficient way (i.c. in a relational database or a NoSQL database)
- how to ask this data questions
