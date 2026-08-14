# Exercise 1

file = open("names.txt", "r")

lines = file.readlines()

for line in lines:
    print(line.strip())

file.close()


# Exercise 2

file = open("names.txt", "r")

lines = file.readlines()

for line in lines:
    if "IT" in line:
        print(line.strip())

file.close()


# Exercise 3

file = open("names.txt", "r")

lines = file.readlines()

count = 0

for line in lines:
    count = count + 1

print("Number of lines:", count)

file.close()
