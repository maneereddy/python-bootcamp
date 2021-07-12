from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
url = requests.get("https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports")
soup = BeautifulSoup(url.text,"lxml")
a = csv.writer(open("scholar.csv","w"))
a.writerow(["title"])
a.writerow([soup.title.text])
