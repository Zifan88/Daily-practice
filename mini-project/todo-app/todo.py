tasks = []


def add_task(title):
    tasks.append({"title": title, "done": False})
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
    print(f"Deleted: {removed['title']}")


def mark_done(number):
    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return
    tasks[number - 1]["done"] = True
    print(f"Marked as done: {tasks[number - 1]['title']}")


add_task("Learn Git")
add_task("Practice Python")
add_task("Write test cases")
show_tasks()

mark_done(1)
show_tasks()

delete_task(2)
show_tasks()

mark_done(10)