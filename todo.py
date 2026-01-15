# Simple To-Do List Program

todo_list = []

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter a new task: ")
        todo_list.append(task)
        print("Task added successfully!")

    elif choice == '2':
        if not todo_list:
            print("No tasks in the list.")
        else:
            print("\nYour Tasks:")
            for i in range(len(todo_list)):
                print(f"{i + 1}. {todo_list[i]}")

    elif choice == '3':
        if not todo_list:
            print("No tasks to remove.")
        else:
            task_no = int(input("Enter task number to remove: "))
            if 1 <= task_no <= len(todo_list):
                removed_task = todo_list.pop(task_no - 1)
                print(f"Task '{removed_task}' removed.")
            else:
                print("Invalid task number.")

    elif choice == '4':
        print("Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
