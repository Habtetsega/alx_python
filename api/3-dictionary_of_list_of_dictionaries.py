import json
import requests


if __name__ == "__main__":
    # Retrieve user data
    response_users = requests.get("https://jsonplaceholder.typicode.com/users")
    users_data = response_users.json()

    # Retrieve tasks data
    response_tasks = requests.get("https://jsonplaceholder.typicode.com/todos")
    tasks_data = response_tasks.json()

    # Create tasks dictionary
    tasks = {}
    for user in users_data:
        user_id = user.get("id")
        username = user.get("username")
        user_tasks = []
        
        for task in tasks_data:
            if task.get("userId") == user_id:
                task_title = task.get("title")
                task_completed = task.get("completed")
                task_dict = {"username": username, "task": task_title, "completed": task_completed}
                user_tasks.append(task_dict)
        
        tasks[user_id] = user_tasks

    # Create JSON file
    filename = "todo_all_employees.json"
    with open(filename, "w") as jsonfile:
        json.dump(tasks, jsonfile)

