import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import ast
import json
with open('articles.json') as json_file:
    data = json.load(json_file)

#Code to Create Articles.csv
import csv
# open a file for writing
mongo_article_file = open('mongo_article.csv', 'wb')
#article_csvwriter = csv.writer(article_file,delimiter="\t")
mongo_article_csvwriter = csv.writer(mongo_article_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
mongo_article_csvwriter.writerow(["_id", "Title","Magazine_Name","Volume","Year","Pages","Authors"])
for i in range(1,len(data)):
	if ('author' not in data[i]) or (data[i]["author"] is None) or ('pages' not in data[i]) :
		pass
	else:	
		try:
			mongo_article_csvwriter.writerow([i,data[i]['title'],data[i]['journal'],data[i]['volume'],data[i]['year'],data[i]['pages'],(data[i]['author'])])
		except UnicodeDecodeError:
			pass
mongo_article_file.close()
author_article_file = open('author_article.csv', 'wb')
#Code to Create Magazine,Volume and Article for MYSQL
import csv
magazine_check_list = []
volume_check_list = []
# open a file for writing
magazineId = 4
articleId = 1
magazine_file = open('magazine.csv',"wb")
volume_file   = open('volume.csv',"wb")
article_file   = open('article.csv',"wb")
author_article_file = open('author_article.csv', 'wb')
author_article_csvwriter = csv.writer(author_article_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
magazine_csvwriter = csv.writer(magazine_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
volume_csvwriter = csv.writer(volume_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
article_csvwriter = csv.writer(article_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
author_article_csvwriter.writerow(["articleId","authorId"])
magazine_csvwriter.writerow(["magazineId","magazineName"])
volume_csvwriter.writerow(["volNo","magazineId","year"])
article_csvwriter.writerow(["articleId","volNo","title","pageNo"])
for i in range(1,len(data)):
	if data[i]["journal"] not in magazine_check_list:
		magazine_csvwriter.writerow([magazineId,(data[i]["journal"]).replace("'",'')])
		magazine_check_list.append(data[i]["journal"])
		volume_csvwriter.writerow([data[i]['volume'],magazineId,data[i]['year']])
		magazineId +=1
	else: 
		volume_csvwriter.writerow([data[i]['volume'],magazineId,data[i]['year']])	
	if('pages' not in data[i]) :
		pass
	else :
		article_csvwriter.writerow([articleId,data[i]['volume'],str(data[i]['title']).replace("'",''),data[i]['pages']])
	articleId  +=1
magazine_file.close()
volume_file.close()
article_file.close()
art_id = 1
auth_id = 1
for i in range(1,len(data)):
    #print(data[i]['author'])
	if ('author' not in data[i]) or (data[i]["author"] is None) or ('pages' not in data[i]) :
		pass
	else:
		check = type(data[i]['author'])
		if check is list:
			for x in (data[i]['author']):
				author_article_csvwriter.writerow([art_id,auth_id])
				auth_id +=1
			art_id +=1
		else :
			author_article_csvwriter.writerow([art_id,auth_id])
			art_id +=1
			auth_id +=1
author_article_file.close()
#Fname, Lname split function
def parsename(name):
    email = "NULL"
    if len(name.split())>2:
        a = (name.split())
        fname = str(a[0]).replace("'","")
        lname = str(" ".join(a[1:])).replace("'","")
    elif len(name.split())==2:
        fname , lname = name.split()
        fname = fname.replace("'","")
        lname = lname.replace("'","")
    else:
        fname = str(name).replace("'","")
        lname = 'NULL'
    return fname ,lname , email
#Code to create author.csv
import csv
# open a file for writing
author_file = open('author.csv', 'wb')
author_csvwriter = csv.writer(author_file,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
author_csvwriter.writerow(["fname","lname","email"])
for i in range(1,len(data)):
    #print(data[i]['author'])
	if ('author' not in data[i]) or (data[i]["author"] is None) or ('pages' not in data[i]) :
		pass
	else:
		check = type(data[i]['author'])
		if check is list:
			for x in (data[i]['author']):
				fname, lname , email = parsename(x)
				author_csvwriter.writerow([(fname).replace("'",''),(lname).replace("'",''),email])
		else :
				fname, lname , email = parsename(data[i]['author'])
				author_csvwriter.writerow([fname,lname,email])
author_file.close()