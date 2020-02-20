#!/bin/bash

#
db="$1"
user="$2"
pass="$3"
##read -s pass


 ###COMMAND TO INSERT INTO MAGAZINE, ARTICLE, AUTHOR AND MAGAZINEVOLUME TABLE 

##echo "SET FOREIGN_KEY_CHECKS=0;" | mysql "$db" -u "$user" -p"$pass"
##echo "set sql_mode='STRICT_ALL_TABLES';"| mysql "$db" -u "$user" -p"$pass"
echo "-> CREATING INSERT QUERIES........"
echo 
chmod +x csv_to_sql.py
python csv_to_sql.py

echo "-> INSERTING DATA INTO MySQL......."
echo
mysql -u "$user" --password="$pass" "$db" -e "source insert_queries.sql;"
echo "-> MYSQL DATA INSERTION COMPLETED"
echo "-> REMOVING TEMP FILES......."
echo
rm AUTHORS.tsv
rm volume.csv
rm author.csv
rm article.csv
rm author_article.csv
rm insert_queries.sql
rm mongo_artcles.tsv
rm magazine.csv
echo "-> EXECUTION COMPLETED."
