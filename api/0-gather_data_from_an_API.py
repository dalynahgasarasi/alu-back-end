#!/usr/bin/python3
"""
Gather data from an API for a given employee ID.
"""

import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")

    total_tasks = 0
    done_tasks = 0
    completed_titles = []

    for task in todos:
        if task.get("userId") == int(user_id):
            total_tasks += 1
            if task.get("completed") is True:
                done_tasks += 1
                completed_titles.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done_tasks, total_tasks))

    for title in completed_titles:
        print("\t {}".format(title))
