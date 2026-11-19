import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "mini-project", "todo-app"))
import todo


@pytest.fixture(autouse=True)
def clean_state(tmp_path, monkeypatch):
    """Use a temporary file and an empty task list for every test."""
    monkeypatch.setattr(todo, "FILE_PATH", str(tmp_path / "tasks.json"))
    monkeypatch.setattr(todo, "tasks", [])


def test_add_task():
    todo.add_task("Learn Git")
    assert len(todo.tasks) == 1
    assert todo.tasks[0] == {"title": "Learn Git", "done": False}


def test_mark_done():
    todo.add_task("Learn Git")
    todo.mark_done(1)
    assert todo.tasks[0]["done"] is True


def test_delete_task():
    todo.add_task("Task A")
    todo.add_task("Task B")
    todo.delete_task(1)
    assert len(todo.tasks) == 1
    assert todo.tasks[0]["title"] == "Task B"


def test_delete_invalid_number(capsys):
    todo.add_task("Task A")
    todo.delete_task(5)
    assert len(todo.tasks) == 1
    assert "Invalid task number." in capsys.readouterr().out


def test_mark_done_invalid_number(capsys):
    todo.mark_done(1)
    assert "Invalid task number." in capsys.readouterr().out


def test_save_and_load_persistence():
    todo.add_task("Saved task")
    todo.tasks = []
    todo.load_tasks()
    assert todo.tasks == [{"title": "Saved task", "done": False}]




def test_edit_task():
    todo.add_task("Old title")
    todo.edit_task(1, "New title")
    assert todo.tasks[0]["title"] == "New title"


def test_edit_task_empty_title(capsys):
    todo.add_task("Keep me")
    todo.edit_task(1, "   ")
    assert todo.tasks[0]["title"] == "Keep me"
    assert "Title cannot be empty." in capsys.readouterr().out