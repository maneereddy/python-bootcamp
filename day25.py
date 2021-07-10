#1)
import datetime
def convert(date_time):
    format = '%b %d %Y %I:%M%p'
    string1 = datetime.datetime.strptime(date_time, format)
    return string1
date_time = 'Jul 9 2021 08:08PM'
print(convert(date_time))
#2)
from datetime import date, timedelta , datetime
dt = date.today() - timedelta(5)
print("current date :",date.today())
print("5 days beforencurrent date : ",dt)
#3)
dt1 = date.today()
print(datetime.combine(dt1, datetime.min.time()))
#4)
import datetime
base = datetime.datetime.today()
for x in range(0,7):
    print(base + datetime.timedelta(days=x))
