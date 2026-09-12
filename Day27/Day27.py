### Exercise 1
import os

print (os.getcwd())

### Exercise 2
files = os.listdir()
print (files)

### Exercise 3
result = os.path.exists("users.json")

print (result)

### Exercise 4
os.mkdir("Test")

### Exercise 5
os.remove("user.json")

### Exercise 6
print (os.getcwd())

files = os.listdir()
print (files)

if not os.path.exists("Backup"):
        os.mkdir("Backup")
