#import datetime
#d=datetime.datetime.now()
#print(d)
#print(d.year)
#print(d.month)
#print(d.day)
# print(d.hour)
# print(d.ctime()) #current time
# print(d)

import calendar
import datetime

d=datetime.datetime.now()
print(calendar.month(d.year,d.month))