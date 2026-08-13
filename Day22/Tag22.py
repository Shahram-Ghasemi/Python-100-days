for i in range(5):

        name = input("Name: ")
        age = input("Age: ")
        job = input("Job: ")

        file = open("names.txt", "a")
        file.write("Name: " + name + "\n")
        file.write("Age: " + age + "\n")
        file.write("Job: " + job + "\n\n")

        file.close()
