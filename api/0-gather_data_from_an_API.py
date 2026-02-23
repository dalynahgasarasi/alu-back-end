#!/usr/bin/python3
"""
0. Gather data from an API
Usage: ./0-gather_data_from_an_API.py <employee_id>
"""
import sys
import requests


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee info
    user_resp = requests.get("{}/users/{}".format(base_url, employee_id))
    if user_resp.status_code != 200:
        sys.exit(1)

    user = user_resp.json()
    employee_name = user.get("name")
    if not employee_name:
        sys.exit(1)

    # Get employee TODOs
    todos_resp = requests.get("{}/todos".format(base_url), params={"userId": employee_id})
    if todos_resp.status_code != 200:
        sys.exit(1)

    todos = todos_resp.json()
    total_tasks = len(todos)
    done_tasks = [t for t in todos if t.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(done_tasks), total_tasks))
    for task in done_tasks:
        title = task.get("title", "")
        print("\t {}".format(title))


if __name__ == "__main__":
    main()
