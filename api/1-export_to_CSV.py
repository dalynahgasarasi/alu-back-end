#!/usr/bin/python3
"""Script that exports TODO list data to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}"
    user = requests.get(url.format(employee_id)).json()
    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todos = requests.get(url2.format(employee_id)).json()
    username = user.get("username")
    with open("{}.csv".format(employee_id), "w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                str(task.get("completed")),
                task.get("title")
            ])
