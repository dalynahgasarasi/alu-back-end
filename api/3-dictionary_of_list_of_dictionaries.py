#!/usr/bin/python3
"""Script that exports all employee TODO data to JSON format."""
import json
import requests

if __name__ == "__main__":
    users = requests.get(
        "https://jsonplaceholder.typicode.com/users"
    ).json()
    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    ).json()
    all_data = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        all_data[user_id] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user.get("id")
        ]
    with open("todo_all_employees.json", "w") as f:
        json.dump(all_data, f)
