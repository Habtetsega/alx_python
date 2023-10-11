""""this is to docment I import json requests and argv from sys"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python3 export_to_JSON.py <user_id>")
        exit(1)

    user_id = argv[1]

    # Retrieve user data
    response_user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    user_data = response_user.json()
    username = user_data.get("username")

    # Retrieve tasks data
    response_tasks = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
    tasks_data = response_tasks.json()

    # Create tasks list
    tasks = []
    for task in tasks_data:
        task_completed = task.get("completed")
        task_title = task.get("title")
        task_dict = {"task": task_title, "completed": task_completed, "username": username}
        tasks.append(task_dict)

    # Create JSON file
    filename = f"{user_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump({user_id: tasks}, jsonfile)

