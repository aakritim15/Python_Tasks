class ToDoList:
    def __init__(self):
        self.tasks = []
#ADD A TASK
    def at(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added successfully.")
#VIEW A TASK
    def vt(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
# COMPLETE A TASK
    def ct(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            completed_task = self.tasks.pop(task_index - 1)
            print(f"Task '{completed_task}' marked as completed.")
        else:
            print("Invalid task index.")

if __name__ == "__main__":
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List!!")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the task: ")
            todo_list.at(task)
        elif choice == '2':
            todo_list.vt()
        elif choice == '3':
            todo_list.vt()
            task_index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.ct(task_index)
        elif choice == '4':
            print("Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
