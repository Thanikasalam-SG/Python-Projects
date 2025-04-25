tasks = []


def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added successfully.")


def view_task():
    if len(tasks) == 0:
        print("There are no tasks.")
    else:
        print("List of tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")


def delete_task():
    if len(tasks) == 0:
        print("There are no tasks to delete.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")  # Fixed printing issue

        try:
            choice = int(input("Enter the task number to delete: "))
            if 0 < choice <= len(tasks):
                del tasks[choice - 1]
                print("Task deleted successfully.")
            else:
                print("Invalid task number. Please enter a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        print("\n===== To-Do-List Application =====")
        print("1. Add task")
        print("2. View tasks")  # Grammar fix: 'tasks' (plural)
        print("3. Delete task")
        print("4. Quit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                add_task()
            elif choice == 2:
                view_task()
            elif choice == 3:
                delete_task()
            elif choice == 4:
                print("Thank you for using the To-Do-List Application.")  # Fixed grammar
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()
