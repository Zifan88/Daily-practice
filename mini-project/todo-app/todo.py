tasks = []


def add_task(title):
    tasks.append(title)
    print(f"Added: {title}")


def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")


add_task("Learn Git")
add_task("Practice Python")
show_tasks()