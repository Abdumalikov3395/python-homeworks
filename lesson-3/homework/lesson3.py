# Task 1

a=["apple", "watermallon", "banana", "pear", "pine-apple" ]
print(a[2])

# Task 2

a=[1, 2, 3 ]
b=[4, 5, 6 ]
c=a+b
print(c)

# Task 3

a=[1, 2, 3, 4, 5 ]
b=[]
b.append(a[0])
b.append(a[2])
b.append(a[4])
print(b)

# Task 4

a=["Pirats","Interstellar","Suits", "Ben 10","King Kong"]
b=tuple(a)
print(b)

# Task 5

a=["Paris","Tashkent","Samarkand", "Moscow","Astana"]
if "Paris" in a: print("Paris is in list")
print(a)


# Task 6

a=[1, 2, 3, 4, 5 ]
b=list(a)
print(b)

# Task 7

a=[1, 2, 3, 4, 5 ]
b=a[0]
a[0]=a[-1]
a[-1]=b
print(a)

# Task 8

a=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(a[2:6])

# Task 9

a=["blue","green","blue","yellow","white",]
print(a.count("blue") )

# Task 10

a=("wolf","bear","lion","ellaphant","rabbit")
print(a.index("lion") )

# Task 11

a=(1, 2, 3 )
b=(4, 5, 6)
c=a+b
print(c)

# Task 12

a=[1, 2, 3,4,5 ]
b=(4, 5, 6)
print("lenght of list a is ",len(a) )
print("lenght of tuple b is ",len(b) )

# Task 13

b=(4, 5, 6, 7, 8)
a=list(b)
print(a)

# Task 14

b=(4, 5, 6, 7, 8)
print("max in tuple is ",max(b))
print("min in tuple is ",min(b))

# Task 15

a=("wolf","bear","lion","ellaphant","rabbit")
print(a[-1::-1])
