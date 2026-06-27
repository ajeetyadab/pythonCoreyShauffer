from nine_modules import search_index as si,test
import sys
import random
import datetime
import calendar
import os


subjects = ["arts","social science","polity"]

index = si(subjects,"polity")
print(index,test)

for path in sys.path:
    print(path)


print(random.random())
print(random.randint(1,10))

subs = random.choice(subjects)
print(subs)
print(datetime.datetime.now())

print(calendar.isleap(2020))

print(os.getcwd())
print(random.__file__)