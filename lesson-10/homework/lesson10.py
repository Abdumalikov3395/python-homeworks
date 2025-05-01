
from datetime import date

#ex1-------
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = False

    def mark_complete(self):
        self.status = True

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all(self):
        for task in self.tasks:
            status = "✅" if task.status else "❌"
            print(f"{task.title} | {task.description} | Due: {task.due_date} | {status}")

    def list_incomplete(self):
        for task in self.tasks:
            if not task.status:
                print(f"{task.title} | {task.description} | Due: {task.due_date} | ❌")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print("Task not found.")

#ex2-------
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        for post in self.posts:
            print(f"Title: {post.title}\nAuthor: {post.author}\nContent: {post.content}\n{'-'*30}")

    def display_by_author(self, author_name):
        for post in self.posts:
            if post.author == author_name:
                print(f"Title: {post.title}\nContent: {post.content}\n{'-'*30}")

    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                print(f"Post '{title}' updated.")
                return
        print("Post not found.")

    def latest_posts(self, count=3):
        for post in self.posts[-count:]:
            print(f"Title: {post.title}\nAuthor: {post.author}\n{'-'*30}")


#ex3-------

class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.acc_number] = account

    def check_balance(self, acc_number):
        acc = self.accounts.get(acc_number)
        return acc.balance if acc else "Account not found."

    def deposit_money(self, acc_number, amount):
        if acc_number in self.accounts:
            self.accounts[acc_number].deposit(amount)
        else:
            print("Account not found.")

    def withdraw_money(self, acc_number, amount):
        if acc_number in self.accounts:
            self.accounts[acc_number].withdraw(amount)
        else:
            print("Account not found.")

    def transfer(self, from_acc, to_acc, amount):
        if from_acc in self.accounts and to_acc in self.accounts:
            if self.accounts[from_acc].balance >= amount:
                self.accounts[from_acc].withdraw(amount)
                self.accounts[to_acc].deposit(amount)
                print("Transfer successful.")
            else:
                print("Insufficient funds.")
        else:
            print("One or both accounts not found.")

    def display_account(self, acc_number):
        acc = self.accounts.get(acc_number)
        if acc:
            print(f"Account Number: {acc.acc_number}\nHolder: {acc.holder_name}\nBalance: {acc.balance}")
        else:
            print("Account not found.")

