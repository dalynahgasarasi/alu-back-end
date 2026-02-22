#!/usr/bin/python3
"""Script that returns TODO list progress for a given employee ID."""
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com/users/{}"
    user = requests.get(url.format(employee_id)).json()
    url2 = "https://jsonplaceholder.typicode.com/todos?userId={}"
    todos = requests.get(url2.format(employee_id)).json()
    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed") is True]
    total = len(todos)
    done = len(done_tasks)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, done, total))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
