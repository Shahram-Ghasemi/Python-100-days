from pathlib import Path


# Exercise 1 - Build a path

folder = Path("Logs")

file = folder / "Server.log"

print(file)


# Exercise 2 - Create file

folder = Path("Logs")
folder.mkdir(exist_ok=True)

file = folder / "Server.log"

file.touch()


# Exercise 3 - Write text

folder = Path("Logs")
folder.mkdir(exist_ok=True)

file = folder / "Server.log"

file.write_text("Server Started Successfully")


# Exercise 4 - Read text

folder = Path("Logs")

file = folder / "Server.log"

content = file.read_text()

print(content)


# Exercise 5 - Append text

folder = Path("Logs")

file = folder / "Server.log"

with file.open("a") as f:
    f.write("\nServer Stopped")


# Exercise 6 - Log Manager

folder = Path("Logs")
folder.mkdir(exist_ok=True)

file = folder / "Server.log"

if not file.exists():
    file.touch()

with file.open("a") as f:
    f.write("Server Started\n")

content = file.read_text()

print(content)
