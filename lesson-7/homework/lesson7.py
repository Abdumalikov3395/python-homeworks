#Task 1

def is_prime(a:int):
    i=2
    n=0
    while i<a:
        if a%i==0: 
            n=1
        i+=1
    if (n==0 and a>1) or a==2: print(True)   
    else : print(False)
a=int(input("Write number!"))
is_prime(a)

#Task 2

def digit_sum(a:str):
    b=0
    for i in a:
        b+=int(i)
    return b
        
a=input("Write number!")
print(digit_sum(a))

#Task 3

def two_degree(a:int):
    b=2
    while b<=a:
        print(b, end=" ")
        b*=2
        
a=int(input("Write number!"))
two_degree(a)
