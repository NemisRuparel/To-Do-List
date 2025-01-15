import json

tasks = {}

def add_task(task_name):
    tasks[task_name] = False
    print(f"Task '{task_name}' added.")

def complete_task(task_name):
    if task_name in tasks:
        tasks[task_name] = True
        print(f"Task '{task_name}' marked as complete.")
    else:
        print(f"Task '{task_name}' not found!")

def incomplete_task(task_name):
    if task_name in tasks:
        tasks[task_name] = False
        print(f"Task '{task_name}' marked as incomplete.")
    else:
        print(f"Task '{task_name}' not found!")

def delete_task(task_name):
    if task_name in tasks:
        del tasks[task_name]
        print(f"Task '{task_name}' deleted.")
    else:
        print(f"Task '{task_name}' not found!")

def edit_task(task_name):
    if task_name in tasks:
        new_task_name = input("Enter the new task name: ")
        tasks[new_task_name] = tasks.pop(task_name)
        print(f"Task '{task_name}' renamed to '{new_task_name}'.")
    else:
        print(f"Task '{task_name}' not found!")

def clear_all_tasks():
    global tasks
    tasks = {}
    print("All tasks cleared!")

def save_tasks():
    filename = input("Enter filename to save tasks (e.g., tasks.json): ")
    with open(filename, 'w') as file:
        json.dump(tasks, file)
    print(f"Tasks saved to {filename}")

def load_tasks():
    filename = input("Enter filename to load tasks (e.g., tasks.json): ")
    try:
        with open(filename, 'r') as file:
            global tasks
            tasks = json.load(file)
        print(f"Tasks loaded from {filename}")
    except FileNotFoundError:
        print(f"File '{filename}' not found!")

def show_tasks():
    if not tasks:
        print("No tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for task, status in tasks.items():
            status_text = "Complete" if status else "Incomplete"
            print(f"- {task} [{status_text}]")
    print()

def menu():
    while True:
        print("1. Add task")
        print("2. Mark task as complete")
        print("3. Mark task as incomplete")
        print("4. Edit task")
        print("5. Delete task")
        print("6. Show all tasks")
        print("7. Clear all tasks")
        print("8. Save tasks to file")
        print("9. Load tasks from file")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == '2':
            task_name = input("Enter task name to mark as complete: ")
            complete_task(task_name)
        elif choice == '3':
            task_name = input("Enter task name to mark as incomplete: ")
            incomplete_task(task_name)
        elif choice == '4':
            task_name = input("Enter task name to edit: ")
            edit_task(task_name)
        elif choice == '5':
            task_name = input("Enter task name to delete: ")
            delete_task(task_name)
        elif choice == '6':
            show_tasks()
        elif choice == '7':
            clear_all_tasks()
        elif choice == '8':
            save_tasks()
        elif choice == '9':
            load_tasks()
        elif choice == '10':
            print("Exiting To-Do List Application.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

menu()