#!/bin/bash
#
###COMMAND TO CREATE THE EXISTING TABLE ####
db="$1"
user="$2"
##read -s pass
pass="$3"
mysql -u "$2" --password="$3" "$1" -e "source existing_tables.sql;"
echo 
echo  "--> CREATED THE EXISTING TABLES IN MYSQL DATABASE"
echo
mysql -u "$2" --password="$3" "$1" -e "select * from AUTHOR;" > AUTHORS.tsv
###COMMAND TO CREATE THE NEW TABLES ###

mysql -u "$2" --password="$3" "$1"  -e "source new_tables.sql;"
echo 
echo "--> CREATED THE NEW TABLES IN MYSQL DATABASE"

###COMMAND TO DROP THE COLLECTIONS IF EXISTS
echo "--> DROPPING EXISTING MONGO COLLECTIONS"
echo  "db.articles.drop()" | mongo "$1" -u"$2" -p"$3" 
echo  "db.authors.drop()"  | mongo "$1" -u"$2" -p"$3"

###COMMAND TO EXECUTE THE PYTHON SCRIPT TO GET THE CLEAN DATA
echo
echo "--> RUNNING PYTHON SCRIPT TO GENERATE THE DATA FROM JSON"

chmod +x data_to_mongo.py
python data_to_mongo.py


#### COMMAND TO CREATE THE COLLECTIONS 
echo "--> GENERATING MONGO COLLECTIONS"
mongo "$1" -u"$2" -p"$3" --eval 'db.createCollection("articles")'

mongo "$1" -u"$2" -p"$3" --eval 'db.createCollection("authors")'

####COMMAND TO INSERT THE DATA INTO COLLECTION FROM JSON FILE
echo "--> INSERTING THE DATA INTO MONGO COLLECTIONS "
mongoimport -d "$1" -u"$2" -p"$3" -c "articles"  --type csv --file mongo_article.csv --headerline

mongoimport -d "$1" -u"$2" -p"$3" -c "authors" --type tsv --headerline --file AUTHORS.tsv

