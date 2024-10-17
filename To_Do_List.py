def display_tasks(tasks):
    if not tasks:
        print("Task list is empty.")
    else:
        print("Task list:")
        index = 1
        for task in tasks:
            print(f"{index}. {task}")

def get_valid_input(prompt, valid_choices):
    while True:
        choice = input(prompt)
        if choice in valid_choices:
            return choice
        print(f"Invalid choice. Please enter {', '.join(valid_choices)}.")

def ToDoList():
    tasks = []
    while True:
        print("\nTo-do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        
        choice = get_valid_input("Please make your selection (1/2/3/4): ", ["1", "2", "3", "4"])

        if choice == "1":
            task = input("Enter the task you want to add: ").strip()
            if task: 
                tasks.append(task)
                print(f"\"{task}\" has been added as a task.")
            else:
                print("Task name cannot be empty.")

        elif choice == "2":
            display_tasks(tasks)

        elif choice == "3":
            if not tasks:
                print("Task list is empty.")
            else:
                display_tasks(tasks)
                try:
                    task_number = int(input("Enter the number of the task you want to remove: "))
                    removed_task = tasks.pop(task_number - 1)
                    print(f"\"{removed_task}\" has been removed.")
                except (IndexError, ValueError):
                    print("Invalid task number.")

        elif choice == "4":
            print("Exiting...")
            break

if __name__ == "__main__":
    ToDoList()