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
    user_resp = requests.get("{}/users/{}".format(base_url, user_id))
    if user_resp.status_code != 200:
        sys.exit(1)

    user = user_resp.json()
    username = user.get("username")
    if not username:
        sys.exit(1)

    # Get employee TODOs
    todos_resp = requests.get(
        "{}/todos".format(base_url), params={"userId": user_id}
    )
    if todos_resp.status_code != 200:
        sys.exit(1)

    todos = todos_resp.json()

    # Prepare data for JSON export
    json_data = []
    for task in todos:
        json_data.append(
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
        )

    data_to_write = {str(user_id): json_data}

    # Write to JSON file
    filename = "{}.json".format(user_id)
    with open(filename, mode="w") as jsonfile:
        json.dump(data_to_write, jsonfile)


if __name__ == "__main__":
    main()
