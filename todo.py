class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("\nTask added successfully.\n")

    def view_tasks(self):
        if not self.tasks:
            print("\nNo tasks available.\n")
            return

        print("\nYour Tasks:\n")

        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task["completed"] else "✗"
            print(f"{index}. [{status}] {task['task']}")

        print()

    def complete_task(self, index):
        try:
            self.tasks[index - 1]["completed"] = True
            print("\nTask marked as completed.\n")
        except IndexError:
            print("\nInvalid task number.\n")

    def delete_task(self, index):
        try:
            deleted = self.tasks.pop(index - 1)
            print(f"\nDeleted: {deleted['task']}\n")
        except IndexError:
            print("\nInvalid task number.\n")


def main():
    todo = TodoList()

    while True:
        print("========== TO-DO LIST ==========")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            todo.view_tasks()

        elif choice == "2":
            task = input("Enter task: ").strip()

            if task:
                todo.add_task(task)
            else:
                print("\nTask cannot be empty.\n")

        elif choice == "3":
            todo.view_tasks()

            if todo.tasks:
                try:
                    index = int(input("Enter task number: "))
                    todo.complete_task(index)
                except ValueError:
                    print("\nPlease enter a valid number.\n")

        elif choice == "4":
            todo.view_tasks()

            if todo.tasks:
                try:
                    index = int(input("Enter task number: "))
                    todo.delete_task(index)
                except ValueError:
                    print("\nPlease enter a valid number.\n")

        elif choice == "5":
            print("\nThank you for using the To-Do List Application.")
            break

        else:
            print("\nInvalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
