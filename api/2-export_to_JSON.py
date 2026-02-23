#!/usr/bin/python3
"""
2. Export employee TODO list to JSON
Usage: ./2-export_to_JSON.py <employee_id>
"""

import json
import requests
import sys


def main():
    """Fetch employee tasks from API and export to JSON file."""
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee info
    user_resp = requests.get(f"{base_url}/users/{user_id}")
    if user_resp.status_code != 200:
        sys.exit(1)

    user = user_resp.json()
    username = user.get("username")
    if not username:
        sys.exit(1)

    # Get employee TODOs
    todos_resp = requests.get(f"{base_url}/todos", params={"userId": user_id})
    if todos_resp.status_code != 200:
        sys.exit(1)

    todos = todos_resp.json()

    # Prepare JSON data: list of dicts
    tasks_list = []
    for task in todos:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        }
        tasks_list.append(task_dict)

    # Outer dict: key = str(user_id), value = list of dicts
    data_to_write = {str(user_id): tasks_list}

    # Write JSON file with no extra formatting
    filename = f"{user_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump(data_to_write, jsonfile)


if __name__ == "__main__":
    main()
