expenses = []

while True:
    expense = input ("Enter an expense (or type 'done'):")

    if expense.lower() == "done":
        break

    expenses.append(float(expense))

print("Expenses:", expenses)
print ("Total spent:", sum(expenses))    

if sum(expenses) > 1000:
    print("You spent over R1000")
else:
    print("You spent less than R1000") 
with open("expenses.txt", "w") as file:
    for expense in expenses:
        file.write(str(expense) + "\n")      