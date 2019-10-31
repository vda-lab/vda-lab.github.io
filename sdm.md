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

  1. [Part 1: Relational database design and SQL]({{ site.baseurl }}/2019/08/extended-introduction-to-relational-databases)
  1. [Part 2: Beyond SQL]({{site.baseurl}}/2019/09/beyond-sql)
  1. [Part 3: Lambda architecture]({{ site.baseurl }}/2019/10/lambda-architecture)

### Practical information

**Software** used throughout the lectures and in the practical session is `sqlite`. We'll use the command line interface, as well as the graphical user interface "DB Browser for SQLite" which you can find at [http://sqlitebrowser.org](http://sqlitebrowser.org).

The 3 **homework assignments** should be performed _individually_ and _after each lecture_.

The **exam** is pen-and-paper, and closed book.

### Schedule
The schedule below is for information purposes only; the _official_ schedule is available on BlackBoard!

#### 1. On-campus version

| Date | Time | Topic | Location |
| :-- | :-- | :-- | :-- |
| Tue 24/09 | 9:30-12:30 | Session 1: Relational database design and SQL | |
| Mon 14/10 | 23:59 | Due date: Homework 1 | BlackBoard |
| Fri 18/10 | 09:00–12:30 | Session 2: Beyond SQL | |
| Mon 04/11 | 23:59 | Due date: Homework 2 | BlackBoard |
| Fri 08/11 | 09:00–17:00* | Session 3: Lambda architecture & answers for homeworks | C108B / C113 |
| Mon 25/11 | 23:59 | Due date: Homework 3 | BlackBoard |

<small>* _For the practical session, the group will be split in half. Morning session 09:00 –
12:30 and afternoon session 13:30 – 17:00._</small>

Optional but recommended

| Date | Time | Topic | Location |
| :-- | :-- | :-- | :-- |
| Tue 12/11 | 9:00-12:30 or 13:30-17:00 | Practical session 1 | C108, C113 |
| Mon 02/12 | 9:00-12:30 or 13:30-17:00 | Practical session 2 | C108, C113 |
| Tue 17/11 | 9:00-12:30 or 13:30-17:00 | Practical session 3 | C108, C113 |

#### 2. Distance-learning version
Suggested timings

| Week | Topic |
| :-- | :-- |
| Week 3: 30/09-04/10 | Relational database design and SQL |
| Week 5: 14/10-18/10 | Beyond SQL |
| Week 9: 11/11-15/11 | Structured self study |

Key dates

| Date | Time | Activity |
| :-- | :-- | :-- | :-- |
| Wed 16/10 | 17:00-19:00 | Contact moment 1 |
| Mon 21/10 | 23:59 | Deadline Homework 1 |
| Mon 28/10 | 17:00-19:00 | Contact moment 2 |
| Wed 04/11 | 23:59 | Deadline Homework 2 |
| Wed 06/11 | 17:00-19:00 | Contact moment 3 |
| Tue 12/11 | 23:59 | Deadline Homework 3 |

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
