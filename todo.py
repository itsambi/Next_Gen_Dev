# Define the list to store tasks
tasks = []

# Function to add a task to the list
def add_item(task):
    tasks.append(task)
    print(f"Task '{task}' added to the list!")

# Function to view all tasks in the list
def display_items():
    print("To-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

# Function to delete a task from the list by its number
def remove_item(task_number):
    try:
        del tasks[task_number - 1]
        print(f"Task {task_number} deleted!")
    except IndexError:
        print("Invalid task number!")

# Main program loop
while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")
    option = input("Choose an option: ")

    if option == "1":
        task_description = input("Enter a task: ")
        add_item(task_description)
    elif option == "2":
        display_items()
    elif option == "3":
        task_num = int(input("Enter the task number to delete: "))
        remove_item(task_num)
    elif option == "4":
        break
    else:
        print("Invalid choice!")
