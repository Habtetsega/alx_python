python
import requests

def employee_details():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    return response.json()

def employee_details():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1/todos")
    return response.json()

if __name__ == "__main__":
    employee_name = employee['name']
    total_tasks = len(todos)
    done_tasks = sum(todo['completed'] for todo in todos)

    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")
