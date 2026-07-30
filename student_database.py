name = input("Enter your name: ")

with open("students.txt", "a") as file:
    file.write(name + "\n")

print("Name saved!") 