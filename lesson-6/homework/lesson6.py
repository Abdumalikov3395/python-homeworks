#Task 1

a=input("Напиши слово!")
i=0
n=0
r=[]
while i<len(a)-3:
  i+=3

  if a[i] in ["a", "e", "i", "o", "u"]: i+=1
  r.append(a[n:i]+"_")
  n=i
r.append(a[n:len(a)])
print("".join(r))

#Task 2

a=int(input("Напиши цифру!"))
i=0
while i<a:
  print(i**2)
  i+=1


#Task 3

#ex1
i=1
while i<=10:
  print(i)
  i+=1

#ex2

i=1
while i<=5:
  n=1
  while n<=i:
    print(n, end="")
    n+=1
  i+=1
  print()

#ex3

a=int(input("Напиши цифру!"))
i=1
b=0
while i<=a:
  b+=i
  i+=1
print("Enter number ", a)
print("Sum is: ", b)

#ex4
i=1
while i<=10:
  print(i)
  i+=1

#ex5
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in (1,2,4):
  print(numbers[i])

#ex6
i=int(input("ВВеди число!"))
a=str(i)
print(len(a))

#ex7

i=5
while i>0:
  n=0
  while n<i:
    print(i-n, end=" ")
    n+=1
  i-=1
  print()

#ex8

list1 = [10, 20, 30, 40, 50]
i=len(list1)-1
while i>=0:
  print(list1[i])
  i-=1


#ex9

i=10
while i>0:
  print("-",i,sep="")
  i-=1

#ex10

i=0
while i<5:
  print(i)
  i+=1
print("Done!")


#ex11

a=int(input("Напиши начало диапазона!"))
print()
b=int(input("Напиши конец диапазона!"))
print()
print(f"Prime numbers between {a} and {b}: ")
c=range(a+1,b)
for el in c:
    i=2
    n=0
    while i<el:
        if el%i==0: 
            n=1
        i+=1
    if n==0: print(el)

#ex12

a=0
b=1
c=1
i=0
print(a, b,c, sep=" ", end=" ")
while i<10:
    a=b+c
    print(a, end=" ")
    c=b
    b=a
    i+=1

#ex13
i=1
b=1
while i<=5:
    b*=i
    i+=1
print("5!=",b)

#Task 4

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
result=[]
for el in list1:
    if el not in list2: result.append(el)
for el in list2:
    if el not in list1: result.append(el)
print(result)
