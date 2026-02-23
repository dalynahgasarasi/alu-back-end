#!/usr/bin/python3
"""Script that returns TODO list progress for a given employee ID."""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(employee_id)).json()

    todos = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}"
        .format(employee_id)).json()

    employee_name = user.get("name")
    total = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(done_tasks), total))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))
