name = input("Name: ")
age = input("Age: ")
job = input("Job: ")

file = open("user.txt", "w")
file.write("Name: " + name + "\n")
file.write("Age: " + age + "\n")
file.write("Job: " + job + "\n")
file.close()

file = open("user.txt", "r")
content = file.read()
print (content)
file.close()
