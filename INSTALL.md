# Installation notes for server used for I0U19A

On https://biocloudcentral.herokuapp.com/launch: provide access key and secret access key for IAM user jaerts
username/password: ubuntu / i0u19a

cluster name: bioinformatics_leuven
IP: 50.16.33.38

How to access 1000Genome data from cloudbiolinux: http://www.youtube.com/watch?v=A8JLh44L1Cw&feature=youtu.be 

## Create account for aerts

ssh ubuntu@54.196.240.172

sudo adduser --home /home/jaerts jaerts (pwd = lex)
sudo usermod -a -G admin jaerts

ssh jaerts@50.16.33.38

## Create EBS volume

On EBS: new volume (in region US-East!!): 500Gb
Right-click => attach => use "instance" number of running EC2 instance (attached as /etc/xvdf)

## Format EBS and mount

After logging in, EBS will be available as /dev/xvdf or similar.

sudo fdisk /dev/xvdf
m
l
n -> p -> 1
w

sudo mkfs.ext4 /dev/xvdf
sudo mkdir /mnt/bioinformatics_leuven
sudo mount /dev/xvdf /mnt/bioinformatics_leuven
sudo mkdir /mnt/bioinformatics_leuven/homes
sudo chmod 777 /mnt/bioinformatics_leuven/homes


## Create user accounts

sudo adduser --home /mnt/bioinformatics_leuven/homes/tverbeiren tverbeiren (pwd = pwd!18324)
sudo adduser --home /mnt/bioinformatics_leuven/homes/rwinand rwinand (pwd = pwd!78447)
sudo adduser --home /mnt/bioinformatics_leuven/homes/rsakai rsakai (pwd = pwd!79569)
sudo usermod -a -G admin tverbeiren
sudo usermod -a -G admin rwinand
sudo usermod -a -G admin rsakai

Created file CourseAdministration/accounts.txt
demeulemeester:!demeulemeester158649::course:Jonas Demeulemeester:/mnt/bioinformatics_leuven/homes/demeulemeester:/bin/bash
vanhul:!vanhul181899::course:Simeon Van Hul:/mnt/bioinformatics_leuven/homes/vanhul:/bin/bash
mertens:!mertens205473::course:Jan Mertens:/mnt/bioinformatics_leuven/homes/mertens:/bin/bash
wittouck:!wittouck217094::course:Stijn Wittouck:/mnt/bioinformatics_leuven/homes/wittouck:/bin/bash
vanoekelen:!vanoekelen218733::course:Oliver Van Oekelen:/mnt/bioinformatics_leuven/homes/vanoekelen:/bin/bash
tchuenchekouam:!tchuenchekouam221889::course:Emmanuel Staffor Tchuenche Kouam:/mnt/bioinformatics_leuven/homes/tchuenchekouam:/bin/bash
calaerts:!calaerts259827::course:Jens Calaerts:/mnt/bioinformatics_leuven/homes/calaerts:/bin/bash
merlevede:!merlevede260163::course:Adriaan Merlevede:/mnt/bioinformatics_leuven/homes/merlevede:/bin/bash
terronmelguizo:!terronmelguizo291319::course:Javier Terron Melguizo:/mnt/bioinformatics_leuven/homes/terronmelguizo:/bin/bash
omrani:!omrani292706::course:Maryam Omrani:/mnt/bioinformatics_leuven/homes/omrani:/bin/bash
manriqueruiz:!manriqueruiz359637::course:Aracelli Manrique Ruiz:/mnt/bioinformatics_leuven/homes/manriqueruiz:/bin/bash
mdamukong:!ndamukong417710::course:Eugene Ambe Ndamukong:/mnt/bioinformatics_leuven/homes/ndamukong:/bin/bash
filiz:!filiz436281::course:Enes Filiz:/mnt/bioinformatics_leuven/homes/filiz:/bin/bash
kasapovic:!kasapovic437705::course:Srdjan Kasapovic:/mnt/bioinformatics_leuven/homes/kasapovic:/bin/bash
allendecid:!allendecid438013::course:Christian Alejandro Allende Cid:/mnt/bioinformatics_leuven/homes/allendecid:/bin/bash
zhang:!zhang438885::course:Xinyuan Zhang:/mnt/bioinformatics_leuven/homes/zhang:/bin/bash
shin:!shin439412::course:Seungyeon Shin:/mnt/bioinformatics_leuven/homes/shin:/bin/bash
kontopoulos:!kontopoulos442018::course:Charalampos Kontopoulos:/mnt/bioinformatics_leuven/homes/kontopoulos:/bin/bash
rodriguesyamamoto:!rodriguesyamamoto442380::course:Lidia Aparecida Rodrigues Yamamoto:/mnt/bioinformatics_leuven/homes/rodriguesyamamoto:/bin/bash
bungwa:!bungwa443233::course:Kehbuma Petclean Bungwa:/mnt/bioinformatics_leuven/homes/bungwa:/bin/bash
verweij:!verweij443605::course:Richard Jan Theodoor Verweij:/mnt/bioinformatics_leuven/homes/verweij:/bin/bash
efuetakoa:!efuetakoa443718::course:Charles Efuetakoa:/mnt/bioinformatics_leuven/homes/efuetakoa:/bin/bash
sohn:!sohn448259::course:Erik Sohn:/mnt/bioinformatics_leuven/homes/sohn:/bin/bash
mathad:!mathad448441::course:Mithila Mathad:/mnt/bioinformatics_leuven/homes/mathad:/bin/bash
verbeke:!verbeke465154::course:Lynn Verbeke:/mnt/bioinformatics_leuven/homes/verbeke:/bin/bash
dewaegeneer:!dewaegeneer469481::course:Maxime De Waegeneer:/mnt/bioinformatics_leuven/homes/dewaegeneer:/bin/bash
bogaerts:!bogaerts471035::course:Bert Bogaerts:/mnt/bioinformatics_leuven/homes/bogaerts:/bin/bash

sudo newusers ~/admin/accounts.txt

## Open necessary ports

For Spark:
In AWS management console: Network&Security => Security groups
     => Inbound
     => Create a new rule: "Custom TCP rule"
     => Port range: "8090"
     => Source: "0.0.0.0/0"

## Mount 1000Genomes

sudo mkdir /mnt/1000genomes
sudo s3fs 1000genomes -o allow_other,public_bucket=1,readwrite_timeout="120" /mnt/1000genomes ===> DOES NOT WORK


## Install software

log in as jaerts

sudo apt-get install bedtools

## Visualization

To make port 8000 accessible: on AWS console:
     Security Group
     => CloudMan
     => Inbound
     => new custom TCP rule:
               port range: 8000
               source: 0.0.0.0/0

in ~/visualization
screen
  => python -m SimpleHTTPServer
  => Ctrl-a Ctrl-d

Data now accessible through http://50.16.33.38:8000

### Data for TourDeFrance

http://www.interactivegraphics.org/Datasets_files/TDF2005.txt

### Install MongoDB

sudo apt-get install mongodb
sudo mkdir /data
sudo mkdir /data/db
sudo mongod --rest --fork --logpath /home/jaerts/mongodb.log

### Install Neo4J

cd /mnt/bioinformatics_leuven/Software/neo4j
sudo wget http://dist.neo4j.org/neo4j-community-1.7.2-unix.tar.gz
sudo tar -xvzf neo4j-community-1.7.2-unix.tar.gz
cd neo4j-community-1.7.2
sudo ./bin/neo4j start => starts server on 7474

To make port 7474 accessible: on AWS console:
     Security Group
     => CloudMan
     => Inbound
     => new custom TCP rule:
               port range: 7474
               source: 0.0.0.0/0

**!!!Does not work... But does work on Mac => run example on local machine**

### Installing Voldemort key-value store (see http://www.project-voldemort.com/voldemort/quickstart.html) 

sudo wget https://github.com/downloads/voldemort/voldemort/voldemort-0.96.tar.gz
sudo tar -xvzf voldemort-0.96.tar.gz
cd voldemort-0.96
in screen: sudo ./bin/voldemort-server.sh config/single_node_cluster > /tmp/voldemort.log
bin/voldemort-shell.sh test tcp://localhost:6666
> put "hello" "world"
> get "hello"
> delete "hello"
> get "hello"
> exit

To batch load data: created file "i0u19a/data/voldemort_import.txt". Inserted by "cat voldemort_import.txt | pbcopy" and then pasting in voldemort shell.
