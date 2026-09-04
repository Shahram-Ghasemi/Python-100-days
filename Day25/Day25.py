```python
# Day 25 - with open()
# File Handling in Python


# ==========================================
# Exercise 1 - Read a file
# ==========================================

with open("names.txt", "r") as file:
    content = file.read()
    print(content)


# ==========================================
# Exercise 2 - Write user information
# ==========================================

name = input("Name: ")
age = input("Age: ")
job = input("Job: ")

with open("user.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Job: " + job + "\n")


# ==========================================
# Exercise 3 - Append a name
# ==========================================

name = input("Name: ")

with open("names.txt", "a") as file:
    file.write("Name: " + name + "\n")


# ==========================================
# Challenge - Save and read users
# ==========================================

name = input("Name: ")
age = input("Age: ")
job = input("Job: ")

# Add new user without deleting previous users
with open("users.txt", "a") as file:
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Job: " + job + "\n")

# Read and display all users
with open("users.txt", "r") as file:
    content = file.read()
    print(content)
```
