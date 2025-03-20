# Task 1

a=dict(wolf=5,bear=2,lion=4,ellaphant=3,rabbit=1)
b=dict(sorted(a.items(), key=lambda x: x[1] , reverse=True ) )
c=dict(sorted(a.items(), key=lambda x: x[1] , reverse=False ) )
print("desc = ",b)
print("asc = ", c)

# Task 2

a=dict(wolf=5,bear=2,lion=4,ellaphant=3,rabbit=1)
b=a|dict(eggs=10)
print(b)


# Task 3

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
b=dic1|dic2|dic3
print(b)


# Task 4


print("write n")
n=int(input())
i=1
b=dict()
while i<=n:
    b=b|{i:i*i}
    i+=1
print(b)


# Task 5

n=15
i=1
b=dict()
while i<=n:
    b=b|{i:i*i}
    i+=1
print(b)

# Sets
# Task 1

s={1,2,5,10} 
print(type(s))


# Task 2

s={1,2,5,10} 
for i in s:
    print(i)



# Task 3

s={1,2,5,10} 
s.add(22)
print(s)



# Task 4

s={1,2,5,10} 
s.remove(2)
print(s)



# Task 5

s={1,2,5,10} 
s.discarde(2)
print(s)
