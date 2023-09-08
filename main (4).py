#write a program determine year centered uses leap year or not using if elif else statement.
# Leap year

"""
year % 4 == 0 &
year % 100 ! = 0 /
year % 400 == 0

"""
def isLeapyear(year):
  if (year % 4 == 0 and year % 100 != 0)or year % 400 == 0:
    return True
  else :
    return False

year = 2013

if isLeapyear(year):
  print('{} is a leap year.'.format)
else:
  print('{} is not a leap year.'. format(year))