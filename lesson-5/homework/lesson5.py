# Task 1

a=int(input("Write year!"))
if (a%4==0 and a%100!=0) or a%400==0: 
    print(True)
else: 
    print(False)

# Task 2

a=int(input("Write n!"))
if a%2==1: 
    print("Weird")
else: 
    if a>=2  and a<=5: 
        print("No Weird")
    elif a>=5  and a<=20:
        print("Weird")
    else: 
        print("No Weird")
