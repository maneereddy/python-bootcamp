import bs4
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

#Go to webpage and scrape data

html = urlopen('https://en.wikipedia.org/wiki/List_of_largest_recorded_music_markets')
bsobj = soup(html.read())
tbody = bsobj('table',{'class':'wikitableplainrowheaders sortable'})[0].findAll('tr')
xl = []
for row in tbody:
    cols = row.findChildren(recursive = False)
cols = tuple(element.text.strip().replace('%','') for element in cols)
xl.append(cols)
xl = xl[1:-1]


import pymysql


import configparser
config = configparser.RawConfigParser()
config.read(filenames = 'my.properties')
print(config.sections())

h = config.get('mysql','host')
u = config.get('mysql','user')
p = config.get('mysql','password')
db = config.get('mysql','db')



scrap_db = pymysql.connect(h,u,p,db)

cursor = scrap_db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS WIKI2 ")

# Create table as per requirement
sql = """CREATE TABLE WIKI2 (
 RANKINGINT,
 MARKETCHAR(50),
 RETAIL_VALUECHAR(20),
 PHYSICALINT,
 DIGITALINT,
 PERFORMANCE_RIGHTSINT,
 SYNCHRONIZATIONINT
 )"""

cursor.execute(sql)
#Save data to the table

scrap_db = pymysql.connect(h,u,p,db)
mySql_insert_query = """INSERT INTO WIKI2 (RANKING, MARKET, RETAIL_VALUE, PHYSICAL,DIGITAL,PERFORMANCE_RIGHTS,SYNCHRONIZATION) 
VALUES (%s, %s, %s, %s ,%s, %s, %s) """

records_to_insert = xl

cursor = scrap_db.cursor()
cursor.executemany(mySql_insert_query, records_to_insert)
scrap_db.commit()
print(cursor.rowcount, "Record inserted successfully into WIKI2 table")

# disconnect from server
scrap_db.close()