
#Task 1

from datetime import date

today = date.today()
print("Write your name!")
name=input()
print("Write date of birthday")
print("Year=" , end=" ")
year=int(input())
print("Month=" , end=" ")
month=int(input() )
print("Day=", end=" ")
day=int(input())
if date(today.year,month,day)>=today:
  print(f"{name}'s age = {today.year-year}")
else :
  print(f"{name}'s age = {today.year-year}")
