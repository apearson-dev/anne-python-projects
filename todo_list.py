tasks = []

while True:
    task = input ("Enter a task (or type 'done'):")

    if task.lower() == "done": 
        break

    tasks.append(task)

print("\nYour Tasks:")

for task in tasks:
    print("_", task)

with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(task + "\n")

for i, task in enumerate(tasks, start=1):
    print(i, task)
            

