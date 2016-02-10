---
title: Student-only section for I0U19A
layout: page
---
## Access to server
See Toledo

## SQL scripts
* Not normalized

<pre>
CREATE TABLE genotypes (individual STRING,
                                ethnicity STRING,
                                rs12345 STRING,
                                rs12345_amb STRING,
                                chr_12345 STRING,
                                pos_12345 INTEGER,
                                rs98765 STRING,
                                rs98765_amb STRING,
                                chr_98765 STRING,
                                pos_98765 INTEGER,
                                rs28465 STRING,
                                rs28465_amb STRING,
                                chr_28465 STRING,
                                pos_28465 INTEGER);
INSERT INTO genotypes (individual, ethnicity, rs12345, rs12345_amb, chr_12345, pos_12345,
                                                      rs98765, rs98765_amb, chr_98765, pos_98765,
                                                      rs28465, rs28465_amb, chr_28465, pos_28465)
                       VALUES ('individual_A','caucasian','A/A','A','1',12345,
                                                          'A/G','R','1',98765,
                                                          'G/T','K','5',28465);
INSERT INTO genotypes (individual, ethnicity, rs12345, rs12345_amb, chr_12345, pos_12345,
                                                      rs98765, rs98765_amb, chr_98765, pos_98765,
                                                      rs28465, rs28465_amb, chr_28465, pos_28465)
                       VALUES ('individual_A','caucasian','A/C','M','1',12345,
                                                          'G/G','G','1',98765,
                                                          'G/G','G','5',28465);
</pre>

* First normal

<pre>
DROP TABLE genotypes;
CREATE TABLE genotypes (id INTEGER PRIMARY KEY, individual STRING, ethnicity STRING, snp STRING,
                                genotype STRING, genotype_amb STRING, chromosome STRING, position INTEGER);
INSERT INTO genotypes (individual, ethnicity, snp, genotype, genotype_amb, chromosome, position)
                       VALUES ('individual_A','caucasian','rs12345','A/A','A','1',12345);
INSERT INTO genotypes (individual, ethnicity, snp, genotype, genotype_amb, chromosome, position)
                       VALUES ('individual_A','caucasian','rs98765','A/G','R','1',98765);
INSERT INTO genotypes (individual, ethnicity, snp, genotype, genotype_amb, chromosome, position)
                       VALUES ('individual_A','caucasian','rs28465','G/T','K','1',28465);
INSERT INTO genotypes (individual, ethnicity, snp, genotype, genotype_amb, chromosome, position)
                       VALUES ('individual_B','caucasian','rs12345','A/C','M','1',12345);
INSERT INTO genotypes (individual, ethnicity, snp, genotype, genotype_amb, chromosome, position)
                       VALUES ('individual_B','caucasian','rs98765','G/G','G','1',98765);
INSERT INTO genotypes (individual, ethnicity, snp, genotype, genotype_amb, chromosome, position)
                       VALUES ('individual_B','caucasian','rs28465','G/G','G','1',28465);
</pre>

* Second normal

<pre>
DROP TABLE individuals;
DROP TABLE snps;
DROP TABLE genotypes;
CREATE TABLE individuals (id INTEGER PRIMARY KEY, name STRING, ethnicity STRING);
CREATE TABLE snps (id INTEGER PRIMARY KEY, accession STRING, chromosome STRING, position INTEGER);
CREATE TABLE genotypes (id INTEGER PRIMARY KEY, individual_id INTEGER, snp_id INTEGER, genotype STRING, genotype_amb STRING);
INSERT INTO individuals (name, ethnicity) VALUES ('individual_A','caucasian');
INSERT INTO individuals (name, ethnicity) VALUES ('individual_B','caucasian');
INSERT INTO snps (accession, chromosome, position) VALUES ('rs12345','1',12345);
INSERT INTO snps (accession, chromosome, position) VALUES ('rs98765','1',98765);
INSERT INTO snps (accession, chromosome, position) VALUES ('rs28465','5',28465);
INSERT INTO genotypes (individual_id, snp_id, genotype, genotype_amb) VALUES (1,1,'A/A','A');
INSERT INTO genotypes (individual_id, snp_id, genotype, genotype_amb) VALUES (1,2,'A/G','R');
INSERT INTO genotypes (individual_id, snp_id, genotype, genotype_amb) VALUES (1,3,'G/T','K');
INSERT INTO genotypes (individual_id, snp_id, genotype, genotype_amb) VALUES (2,1,'A/C','M');
INSERT INTO genotypes (individual_id, snp_id, genotype, genotype_amb) VALUES (2,2,'G/G','G');
INSERT INTO genotypes (individual_id, snp_id, genotype, genotype_amb) VALUES (2,3,'G/G','G');
</pre>

* Third normal

<pre>
DROP TABLE individuals;
DROP TABLE snps;
DROP TABLE genotypes;
CREATE TABLE individuals (id INTEGER PRIMARY KEY, name STRING, ethnicity STRING);
CREATE TABLE snps (id INTEGER PRIMARY KEY, accession STRING, chromosome STRING, position INTEGER);
CREATE TABLE genotypes (id INTEGER PRIMARY KEY, individual_id INTEGER, snp_id INTEGER, genotype_amb STRING);
INSERT INTO individuals (name, ethnicity) VALUES ('individual_A','caucasian');
INSERT INTO individuals (name, ethnicity) VALUES ('individual_B','caucasian');
INSERT INTO snps (accession, chromosome, position) VALUES ('rs12345','1',12345);
INSERT INTO snps (accession, chromosome, position) VALUES ('rs98765','1',98765);
INSERT INTO snps (accession, chromosome, position) VALUES ('rs28465','5',28465);
INSERT INTO genotypes (individual_id, snp_id, genotype_amb) VALUES (1,1,'A');
INSERT INTO genotypes (individual_id, snp_id, genotype_amb) VALUES (1,2,'R');
INSERT INTO genotypes (individual_id, snp_id, genotype_amb) VALUES (1,3,'K');
INSERT INTO genotypes (individual_id, snp_id, genotype_amb) VALUES (2,1,'M');
INSERT INTO genotypes (individual_id, snp_id, genotype_amb) VALUES (2,2,'G');
INSERT INTO genotypes (individual_id, snp_id, genotype_amb) VALUES (2,3,'G');
</pre>
