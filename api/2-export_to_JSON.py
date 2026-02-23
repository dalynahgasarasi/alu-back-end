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

    # Get employee username
    user_resp = requests.get(f"{base_url}/users/{user_id}")
    if user_resp.status_code != 200:
        sys.exit(1)

    user = user_resp.json()
    username = user["username"]  # must use direct access

    # Get all tasks for the user
    todos_resp = requests.get(f"{base_url}/todos", params={"userId": user_id})
    if todos_resp.status_code != 200:
        sys.exit(1)

    todos = todos_resp.json()

    # Build list of dicts for JSON
    tasks_list = []
    for task in todos:
        tasks_list.append({
            "task": task["title"],         # direct key access
            "completed": task["completed"],
            "username": username
        })

    # Final JSON structure
    data_to_write = {str(user_id): tasks_list}

    # Write to file with exact formatting (no indent)
    filename = f"{user_id}.json"
    with open(filename, "w") as f:
        json.dump(data_to_write, f)


if __name__ == "__main__":
    main()
