import json
import os

FILE_PATH = os.path.join(os.path.dirname(__file__), "tasks.json")
tasks = []


def load_tasks():
    global tasks
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            tasks = json.load(f)


def save_tasks():
    with open(FILE_PATH, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(title):
    tasks.append({"title": title, "done": False})
    save_tasks()
    print(f"Added: {title}")


def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "x" if task["done"] else " "
        print(f"{i}. [{status}] {task['title']}")


def delete_task(number):
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return
    removed = tasks.pop(number - 1)
    save_tasks()
    print(f"Deleted: {removed['title']}")


def mark_done(number):
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return
    tasks[number - 1]["done"] = True
    save_tasks()
    print(f"Marked as done: {tasks[number - 1]['title']}")


def edit_task(number, new_title):
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return
    new_title = new_title.strip()
    if not new_title:
        print("Title cannot be empty.")
        return
    old_title = tasks[number - 1]["title"]
    tasks[number - 1]["title"] = new_title
    save_tasks()
    print(f"Edited: '{old_title}' -> '{new_title}'")


if __name__ == "__main__":
    load_tasks()
    print("Tasks loaded from file:")
    show_tasks()