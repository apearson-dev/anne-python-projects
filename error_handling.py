print("PROGRAM STARTED")

try:
    age = int(input("Enter your age: "))
    print("Next year you will be", age + 1)

except ValueError:
    print("Please enter a number.")
                