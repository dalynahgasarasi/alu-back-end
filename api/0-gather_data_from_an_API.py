#!/usr/bin/python3
"""
Gather data from an API for a given employee ID.
"""

import requests
import sys


if __name__ == "__main__":
    user_id = int(sys.argv[1])

    user_response = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(user_id))
    todos_response = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id))

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")

    done_tasks = [t.get("title") for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(done_tasks), len(todos)))

    for title in done_tasks:
        print("\t {}".format(title))
