import csv
f = open('insert_queries.sql', 'w')
g = open('magazine.csv')
csv_g = csv.reader(g)
next(csv_g)
for row in csv_g:
  f.write(str("insert IGNORE into MAGAZINE(name) values (")+str("'")+row[1]+str("');")+str('\n'))
  
m = open('volume.csv')
csv_f = csv.reader(m)
next(csv_f)
for row in csv_f:
  f.write(str("insert IGNORE into VOLUME(volumeid,magazineid,publicationyear) values (")+str("'")+row[0]+str("','")+row[1]+str("','")+row[2]+str("');")+str('\n'))
   
h = open('author.csv')
csv_f = csv.reader(h)
next(csv_f)
for row in csv_f:
  f.write(str("insert IGNORE into AUTHOR(lname,fname,email) values (")+str("'")+row[1]+str("','")+row[0]+str("','")+row[2]+str("');")+str('\n'))

l = open('article.csv')
csv_f = csv.reader(l)
next(csv_f) 
for row in csv_f:
	f.write(str("insert IGNORE into ARTICLES(volumeid,title,pageno) values (")+str("'")+row[1]+str("','")+row[2]+str("','")+row[3]+str("');")+str('\n'))
		
q = open('author_article.csv')
csv_f = csv.reader(q)
next(csv_f) 
for row in csv_f:
	f.write(str("insert IGNORE into ARTICLE_WRITTEN(article_id,author_id) values (")+str("'")+row[0]+str("','")+row[1]+str("');")+str('\n'))
f.close()

# Magazine
# Volume
# Author
# Article 
