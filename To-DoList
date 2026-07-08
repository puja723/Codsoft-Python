"""
Project : To-Do List Application
Author  : Swati Ranjita Swain
Language: Python 3

Description:
A professional command-line To-Do List application
to manage daily tasks efficiently.
"""


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("\nTask added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.")
            return

        print("\n========== YOUR TASKS ==========")

        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{index}. [{status}] {task['task']}")

    def mark_completed(self, task_number):
        try:
            self.tasks[task_number - 1]["completed"] = True
            print("\nTask marked as completed.")
        except IndexError:
            print("\nInvalid task number.")

    def delete_task(self, task_number):
        try:
            removed = self.tasks.pop(task_number - 1)
            print(f"\nDeleted: {removed['task']}")
        except IndexError:
            print("\nInvalid task number.")


def menu():
    print("\n" + "=" * 35)
    print("      TO-DO LIST APPLICATION")
    print("=" * 35)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def main():
    todo = TodoList()

    while True:
        menu()

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            todo.view_tasks()

        elif choice == "2":
            task = input("Enter new task: ").strip()

            if task:
                todo.add_task(task)
            else:
                print("Task cannot be empty.")

        elif choice == "3":
            todo.view_tasks()

            if todo.tasks:
                try:
                    number = int(input("Enter task number: "))
                    todo.mark_completed(number)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "4":
            todo.view_tasks()

            if todo.tasks:
                try:
                    number = int(input("Enter task number: "))
                    todo.delete_task(number)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            print("\nThank you for using the To-Do List Application.")
            break

        else:
            print("Invalid choice. Please select between 1 and 5.")


if __name__ == "__main__":
    main()
