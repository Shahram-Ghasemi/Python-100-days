# Day 28 - pathlib

from pathlib import Path


# Exercise 1
path = Path("test.txt")

print(path)


# Exercise 2
current_path = Path.cwd()

print(current_path)


# Exercise 3
current_path = Path.cwd()

for item in current_path.iterdir():
    print(item)


# Exercise 4
path = Path("users.json")

print(path.exists())


# Exercise 5
path = Path("users.json")

print(path.is_file())
print(path.is_dir())


# Exercise 6
path = Path("PythonTest")

path.mkdir()


# Exercise 7
path = Path("Backup")

path.mkdir(exist_ok=True)


# Exercise 8
path = Path("user.json")

path.unlink()


# Exercise 9
path = Path("logs/server.log")

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)


# Final Challenge
current_path = Path.cwd()

for item in current_path.iterdir():

    if item.is_file():
        print("FILE:", item.name)

    elif item.is_dir():
        print("DIR:", item.name)
