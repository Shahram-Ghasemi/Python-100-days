# =========================
# Exercise 1
# =========================

text = "Shahram IT Engineer"

words = text.split()

for word in words:
    print(word)


# =========================
# Exercise 2
# =========================

user = "Shahram,37,IT Engineer"

data = user.split(",")

print("Name:", data[0])
print("Age:", data[1])
print("Job:", data[2])


# =========================
# Exercise 3
# =========================

file = open("users.txt", "r")

lines = file.readlines()

for line in lines:
    line = line.strip()
    data = line.split(",")

    print("Name:", data[0])
    print("Age:", data[1])
    print("Job:", data[2])

file.close()


# =========================
# Challenge
# =========================

file = open("employees.txt", "r")

lines = file.readlines()

for line in lines:
    line = line.strip()
    data = line.split(",")

    salary = int(data[3])

    if salary >= 3000:
        print("Name:", data[0])
        print("Age:", data[1])
        print("Job:", data[2])
        print("Salary:", salary)
        print()

file.close()
