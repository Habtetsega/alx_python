python
import requests
import sys

def get_employee_details(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_employee_todos(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def display_todo_progress(employee_id):
    employee = get_employee_details(employee_id)
    todos = get_employee_todos(employee_id)

    if employee is None or todos is None:
        print("Failed to retrieve employee data.")
        return

    employee_name = employee['name']
    total_tasks = len(todos)
    done_tasks = sum(todo['completed'] for todo in todos)

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_todo_progress(employee_id)
