tasks = []

# Load existing tasks
try:
    with open("tasks.txt", "r") as file: 
        for line in file:
            tasks.append(line.strip())
except FileNotFoundError:
    pass
while True:
    print("\nTO-DO LIST")
    print("1. View tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Save and Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter a task: ")
        if task.strip():
            tasks.append(task.strip())
            print("Task added!")
        else:
            print("Empty task not added.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                idx = int(input("Enter task number to delete: "))
                if 1 <= idx <= len(tasks):
                    removed = tasks.pop(idx-1)
                    print(f"Removed: {removed}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(task + "\n")
        print("Tasks saved. Exiting.")
        break

    else:
        print("Invalid option. Choose 1-4.")
          