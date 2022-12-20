import datetime

my_time = datetime.time(17, 35)
print(type(my_time))
print(f'hour is {my_time.minute} and minute is {my_time.hour}')
print(my_time)
my_date = datetime.date(2025, 10, 17)
print(type(my_date))
print(my_date)
print(my_date.ctime())
print(my_date.today())

# Date and time together
from datetime import datetime

my_date = datetime(2025, 5, 15, 22, 10, 15, 2500)
print(my_date)

from datetime import date

birth = date(1995, 3, 5)
death = date(2095, 6, 19)

life = death - birth
print(life)
print(life.days)

wokeup = datetime(2025, 5, 15, 22, 5, 7, 30)
sleep = datetime(2025, 5, 15, 22, 5, 23, 45)
wakefulness = sleep - wokeup
print(wakefulness)


