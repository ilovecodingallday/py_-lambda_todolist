tasks = []

# Add a task to the to-do list
add_task = lambda task: tasks.append(task)

# Remove a task from the to-do list
remove_task = lambda task: tasks.remove(task) if task in tasks else print("Task not found!")

# Print the to-do list
print_list = lambda: print("To-Do List:", tasks)

# Loop to receive user input
while True:
    print("\nSelect an option:\n1. Add task\n2. Remove task\n3. Print list\n4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == "3":
        print_list()
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
