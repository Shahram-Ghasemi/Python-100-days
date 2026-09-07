```python
# Day 26 - JSON in Python

# ==========================================
# Exercise 1 - Dictionary to JSON
# ==========================================

import json

user = {
    "name": "Shahram",
    "age": 37,
    "job": "Linux Engineer"
}

data = json.dumps(user)

print(data)


# ==========================================
# Exercise 2 - JSON to Dictionary
# ==========================================

data = '{"name": "Shahram", "age": 37, "job": "Linux Engineer"}'

user = json.loads(data)

print(user)


# ==========================================
# Exercise 3 - Save Dictionary to JSON file
# ==========================================

user = {
    "name": "Shahram",
    "age": 37,
    "job": "Linux Engineer"
}

with open("user.json", "w") as file:
    json.dump(user, file)


# ==========================================
# Exercise 4 - Read JSON file
# ==========================================

with open("user.json", "r") as file:
    user = json.load(file)

print(user)


# ==========================================
# Exercise 5 - Access Dictionary values
# ==========================================

print("Name:", user["name"])
print("Job:", user["job"])


# ==========================================
# Challenge - Multiple Users with JSON
# ==========================================

users = [
    {
        "name": "Shahram",
        "age": 37,
        "job": "Linux Engineer"
    },
    {
        "name": "Ali",
        "age": 30,
        "job": "Network Engineer"
    },
    {
        "name": "Caspar",
        "age": 40,
        "job": "Hacker"
    }
]

# Save users to JSON file
with open("users.json", "w") as file:
    json.dump(users, file)


# Read users from JSON file
with open("users.json", "r") as file:
    users = json.load(file)


# Display users
for user in users:
    print("Name:", user["name"])
    print("Job:", user["job"])
```
