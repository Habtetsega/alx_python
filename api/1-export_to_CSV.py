import csv
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: python3 export_to_CSV.py <user_id>")
        exit(1)

    user_id = argv[1]

    # Retrieve user data
    response_user = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
    user_data = response_user.json()
    username = user_data.get("username")

    # Retrieve tasks data
    response_tasks = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={user_id}")
    tasks_data = response_tasks.json()

    # Create CSV file
    filename = f"{user_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks_data:
            task_completed = str(task.get("completed"))
            task_title = task.get("title")
            writer.writerow([user_id, username, task_completed, task_title])

    print(f"Data exported to {filename} successfully.")
