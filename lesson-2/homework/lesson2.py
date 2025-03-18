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
if date(today.year,month,day)<=today:
  print(f"{name}'s age = {today.year-year}")
else :
  print(f"{name}'s age = {today.year-year-1}")

  
  # Task 2
txt = 'LMaasleitbtui'
print(txt[0::2])
print(txt[1::2])


  # Task 3
txt = 'MsaatmiazD'
print(txt[0::2])
print(txt[-1::-2])


  # Task 4
txt = "I'am John. I am from London"
print(txt[21:])


 # Task 5
txt=input()
print(txt[-1::-1])


# Task 6

print("Write your word")
a=input()
i=0
n=0
while i<len(a):
    if a[i] in "aeiouAEIOU" :n+=1
    i+=1
print(" Vowels quantity is ",n)

# Task 7
print("How many values is in your list?")
a=int(input())
b=[]
i=1
while i<=a:
    b.append(int(input()))
    i+=1
print("Max value is ",max(b))


# Task 8

print("Write your word")
a=input()
if a==a[-1::-1] : print("Yes, This word is palindrome")
else: print("No, This word is not palindrome")

# Task 9
print("Write your email!")
a=input()
b=a.index("mail.")
print("Domen is ",a[b+5:])
