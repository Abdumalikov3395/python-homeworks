from datetime import *
#ex1
# class circle:
#     def init(self, radius):
#         self.radius=radius
#     def area(self):
#         return 3.14*self.radius*self.radius
#     def perimetr(self):
#         return 3.14*2*self.radius


# a=circle(5)
# print(a.area())
# print(a.perimetr())

#ex2
# from datetime import *
# class persons:
#     def init(self, name, country, day,month,year):
#         self.name=name
#         self.county=country
#         self.DateofBirthday=date(year,month,day)
    
#     def age(self):
#         years = date.today().year - self.DateofBirthday.year
#         if (date.today().month, date.today().day) < (self.DateofBirthday.month, self.DateofBirthday.day):
#             years -= 1
#         return years
# b=persons("Bahodir","UZB",16,6,2002)
# print(b.age())

#ex3
# class calculator:
#     def init(self, x,y):
#         self.x=x
#         self.y=y
#     def sum(self):
#         print(self.x+self.y)
#     def minus(self):
#         print(self.x-self.y)   
#     def multiply(self):
#         print(self.x*self.y)
#     def divide(self):
#         print(self.x/self.y)
# ex1=calculator(10,5)
# ex1.sum()
# ex1.minus()
# ex1.multiply()
# ex1.divide()

#ex-4

# import math

# # Base class
# class Shape:
#     def area(self):
#         raise NotImplementedError("Subclass must implement area method")

#     def perimeter(self):
#         raise NotImplementedError("Subclass must implement perimeter method")

# # Subclass for Circle
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return math.pi * self.radius ** 2
    
#     def perimeter(self):
#         return 2 * math.pi * self.radius

# # Subclass for Triangle
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
    
#     def perimeter(self):
#         return self.a + self.b + self.c
    
#     def area(self):
#         s = self.perimeter() / 2
#         return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))  # Heron's formula

# # Subclass for Square
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
    
#     def area(self):
#         return self.side ** 2
    
#     def perimeter(self):
#         return 4 * self.side

# # Example usage
# if __name__ == "__main__":
#     circle = Circle(5)
#     print("Circle - Area:", circle.area())
#     print("Circle - Perimeter:", circle.perimeter())

#     triangle = Triangle(3, 4, 5)
#     print("\nTriangle - Area:", triangle.area())
#     print("Triangle - Perimeter:", triangle.perimeter())

#     square = Square(4)
#     print("\nSquare - Area:", square.area())
#     print("Square - Perimeter:", square.perimeter())


#ex-5

# class Node:
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, key):
#         if self.root is None:
#             self.root = Node(key)
#         else:
#             self._insert(self.root, key)

#     def _insert(self, current, key):
#         if key < current.val:
#             if current.left is None:
#                 current.left = Node(key)
#             else:
#                 self._insert(current.left, key)
#         else:
#             if current.right is None:
#                 current.right = Node(key)
#             else:
#                 self._insert(current.right, key)

#     def search(self, key):
#         return self._search(self.root, key)

#     def _search(self, current, key):
#         if current is None or current.val == key:
#             return current is not None
#         if key < current.val:
#             return self._search(current.left, key)
#         return self._search(current.right, key)

# # Example usage
# bst = BinarySearchTree()
# bst.insert(10)
# bst.insert(5)
# bst.insert(20)
# print(bst.search(10))  # True
# print(bst.search(15))  # False


# #ex-6

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         return None

#     def is_empty(self):
#         return len(self.stack) == 0

# # Example usage
# stack = Stack()
# stack.push(1)
# stack.push(2)
# print(stack.pop())  # 2
# print(stack.pop())  # 1


# #ex-7

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

#     def insert(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def delete(self, key):
#         current = self.head

#         if current and current.data == key:
#             self.head = current.next
#             return

#         prev = None
#         while current and current.data != key:
#             prev = current
#             current = current.next

#         if current:
#             prev.next = current.next

# # Example usage
# ll = LinkedList()
# ll.insert(1)
# ll.insert(2)
# ll.insert(3)
# ll.display()  # 3 -> 2 -> 1 -> None
# ll.delete(2)
# ll.display()  # 3 -> 1 -> None




# #ex-8

# class ShoppingCart:
#     def __init__(self):
#         self.items = {}

#     def add_item(self, item, price):
#         self.items[item] = price

#     def remove_item(self, item):
#         if item in self.items:
#             del self.items[item]

#     def total_price(self):
#         return sum(self.items.values())

# # Example usage
# cart = ShoppingCart()
# cart.add_item("Apple", 1.5)
# cart.add_item("Banana", 2.0)
# print("Total:", cart.total_price())  # Total: 3.5
# cart.remove_item("Apple")
# print("Total:", cart.total_price())  # Total: 2.0



# #ex-9

# class Stack:
#     def __init__(self):
#         self.stack = []

#     def push(self, item):
#         self.stack.append(item)

#     def pop(self):
#         if not self.is_empty():
#             return self.stack.pop()
#         return None

#     def display(self):
#         print("Stack:", self.stack)

#     def is_empty(self):
#         return len(self.stack) == 0

# # Example usage
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.display()  # Stack: [10, 20]
# stack.pop()
# stack.display()  # Stack: [10]




# #ex-10

# class Queue:
#     def __init__(self):
#         self.queue = []

#     def enqueue(self, item):
#         self.queue.append(item)

#     def dequeue(self):
#         if not self.is_empty():
#             return self.queue.pop(0)
#         return None

#     def is_empty(self):
#         return len(self.queue) == 0

# # Example usage
# queue = Queue()
# queue.enqueue(1)
# queue.enqueue(2)
# print(queue.dequeue())  # 1
# print(queue.dequeue())  # 2


# #ex-11

# class BankAccount:
#     def __init__(self, account_holder, balance=0):
#         self.account_holder = account_holder
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"${amount} deposited. New balance: ${self.balance}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"${amount} withdrawn. New balance: ${self.balance}")
#         else:
#             print("Insufficient balance!")

#     def display_balance(self):
#         print(f"Account holder: {self.account_holder}, Balance: ${self.balance}")

# # Example usage
# account = BankAccount("John Doe", 1000)
# account.deposit(500)
# account.withdraw(200)
# account.display_balance()
