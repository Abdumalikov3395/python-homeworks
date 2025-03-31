#Exception Handling Exercises

#ex1
try:
    num = float(input("Enter a number: "))
    denom = float(input("Enter another number: "))
    result = num / denom
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numbers.")

#ex2

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("Error: Invalid input. Please enter numbers.")

#ex3

try:
    a = open("lesson-8/example.txt")
except FileNotFoundError:
    print("Error: File Not Found. Please check the folder.")

#ex4

try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter second number: "))
except TypeError:
    print("Error: Invalid input. Please enter numbers.")

#ex5

try:
    a = open("lesson-8/example.txt")
except PermissionError:
    print("Error: You do not have permission to access this file.")

#ex6

try:
    my_list = [10, 20, 30, 40, 50]  
    index = int(input("Enter an index: "))
    print("Element at index", index, ":", my_list[index])
except IndexError:
    print("Error: Index is out of range.")

#ex7

try:
    num = float(input("Enter a number: "))
    print("You entered:", num)
except KeyboardInterrupt:
    print("Operation canceled by user.")

#ex8

try:
    num = float(input("Enter the numerator: "))
    denom = float(input("Enter the denominator: "))
    result = num / denom
    print("Result:", result)
except ArithmeticError:
    print("Error: An arithmetic error occurred (possibly division by zero).")

#ex9

try:
    with open("lesson-8/example.txt", mode="r") as file:
        content = file.read()
        print("File content:\n", content)
except UnicodeDecodeError:
    print("Error: Unable to decode the file. Try opening it with a different encoding.")


#ex10

try:
    my_list = [1, 2, 3, 4, 5]
    operation = input("Enter an operation (e.g., append, sort, reverse, upper): ")
    
    if hasattr(my_list, operation):  # Check if the attribute exists
        method = getattr(my_list, operation)
        if callable(method):
            method()  # Execute the method if it's callable
            print("Updated list:", my_list)
    else:
        raise AttributeError(f"'list' object has no attribute '{operation}'")

except AttributeError as e:
    print(f"Error: {e}")



#Python File Input Output: Exercises, Practice, Solution

#ex1

a=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r")
print(a.read())
a.close()

#ex2

a=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r")
n=int(input())
i=0
while i<n:
    print(a.readline(), end="")
    i+=1
a.close()

#ex3

a=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="a")
a.write("I love Data\n")
a.close()

a=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r")
print(a.read())
a.close()

#ex4

a=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r")
n=int(input("How many lasts lines?\n"))
l=a.readlines()
for i in l[-n:]:
    print(i, end="")
a.close()


#ex5

l=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r").readlines()
l.close()

#ex6

l=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r").read()

#ex7

l=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r").readlines()
l.close()

#ex8

words=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r").read().split()
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]
print("Longest words:", longest_words)
words.close()

#ex9

a=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r").readlines()
print(len(a))
a.close()

#ex10

a=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r").read().split()
print(len(a))
a.close()

#ex11

import os
print(os.path.getsize("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt"), "bytes")

#ex12

data = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

with open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="a") as file:
    for i in data:
        file.write(i+"\n")

#ex13

l=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r").read()
m=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example2.txt", mode="w")
m.write(l)
l.close()
m.close()

#ex14

l=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r").readlines()
m=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example2.txt", mode="r").readlines()
x=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example3.txt", mode="w")
for i in range( 0,max(len(l),len(m)) ):
               if i<len(l) and i<len(m) : x.write(l[i][:-1]+m[i])
               elif i<len(l) and i>=len(m) : x.write(l[i])
               elif i<len(m) and i>=len(l) : x.write(m[i])
l.close()

#ex15

import random
l=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r").readlines()
m=random.randint(1, len(l)-1)
print(l[m])
l.close()

#ex16

l=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r")
print("Is the file closed?", l.closed)
l.close()

#ex17


with open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r") as file:
    lines = file.readlines()

cleaned_lines = [line.strip() for line in lines]
print("\n".join(cleaned_lines))

#ex18

a=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r").read().split()
print(len(a))
a.close()

#ex19


characters=[]
with open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example.txt", mode="r") as file:
    content = file.read()
    characters.extend(list(content))
print(characters)

#ex20


for i in [chr(i) for i in range(65, 91)]:
    file_path="C:/Users/Bakhodir.Abdumalikov/Desktop/"+i+".txt"
    with open(file_path, mode="w") as file:
        l="this is file "+i
        file.write(l)

#ex21

a=open("C:/Users/Bakhodir.Abdumalikov/Desktop/Example4.txt", mode="w")
n=int(input("Enter the number of letters per line: "))
for i in [chr(i) for i in range(65, 91)]:
    m=n*(i+" ")+"\n"
    a.write(m)
a.close()
