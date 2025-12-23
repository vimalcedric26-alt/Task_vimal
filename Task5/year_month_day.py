from datetime import datetime

dt = datetime.now()
extract  = lambda x: (x.year,x.month,x.day)
print("year:","month:","date:",extract(dt))