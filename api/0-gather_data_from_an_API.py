import requests
import sys

def get_employee_info(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"

    # Fetch employee details
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data["name"]

    # Fetch employee's TODO list
    response = requests.get(todos_url)
    todos_data = response.json()

    # Calculate the number of completed tasks
    completed_tasks = [task for task in todos_data if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos_data)

    # Print employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for i, task in enumerate(completed_tasks, 1):
        print(f"\t{i}. {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_info(employee_id)
