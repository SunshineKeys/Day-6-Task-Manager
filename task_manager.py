import json
import os

TASKS_FILE = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)


def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Task title cannot be empty.")
        return

    task = {
        "title": title,
        "status": "todo"
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")


def list_tasks(tasks, filter_status=None):
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        if filter_status and task["status"] != filter_status:
            continue
        print(f"{i}. [{task['status']}] {task['title']}")


def update_task_status(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to update: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    print("1) todo")
    print("2) in-progress")
    print("3) done")

    choice = input("Choose new status: ").strip()
    status_map = {
        "1": "todo",
        "2": "in-progress",
        "3": "done"
    }

    if choice not in status_map:
        print("Invalid choice.")
        return

    tasks[index]["status"] = status_map[choice]
    save_tasks(tasks)
    print("Task updated.")


def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if index < 0 or index >= len(tasks):
            print("Invalid task number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    removed = tasks.pop(index)
    save_tasks(tasks)
    print(f"Deleted task: {removed['title']}")


def main():
    tasks = load_tasks()

    while True:
        print("\n=== Task Manager ===")
        print("1) Add task")
        print("2) List all tasks")
        print("3) List tasks by status")
        print("4) Update task status")
        print("5) Delete task")
        print("6) Quit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            print("1) todo")
            print("2) in-progress")
            print("3) done")
            status_choice = input("Filter by: ").strip()
            status_map = {
                "1": "todo",
                "2": "in-progress",
                "3": "done"
            }
            list_tasks(tasks, status_map.get(status_choice))
        elif choice == "4":
            update_task_status(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
