#!/usr/bin/python3
"""
1. Export employee TODO list to CSV
Usage: ./1-export_to_CSV.py <employee_id>
"""

import csv
import requests
import sys


def main():
    """Fetch employee tasks from API and export to CSV file."""
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
    todos_resp = requests.get("{}/todos".format(base_url), params={"userId": user_id})
    if todos_resp.status_code != 200:
        sys.exit(1)

    todos = todos_resp.json()

    # CSV file name = USER_ID.csv
    filename = "{}.csv".format(user_id)

    # Write CSV
    with open(filename, mode="w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])


if __name__ == "__main__":
    main()
