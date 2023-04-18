import requests
from behave import *

@given('there is an employee with the name "{name}" and email "{email}"')
def step_impl(context, name, email):
    # Add the employee to the database
    employee_data = {"name": name, "email": email}
    response = requests.post(f"http://localhost:8000/employees", json=employee_data)
    context.employeeToDelete = response.json()
    assert response.status_code == 201

@when('the user deletes the employee')
def step_impl(context):
    # Get the id of the employee to delete
    employee_id = context.employeeToDelete['id']

    print(employee_id)

    # Delete the employee
    response = requests.delete(f"http://localhost:8000/employees/{employee_id}")
    context.response = response

@then('the employee with the name "{name}" should no longer exist in the database')
def step_impl(context, name):
    # Check that the employee no longer exists
    response = requests.get(f"http://localhost:8000/employees")
    employees = response.json()
    for employee in employees:
        print(employee["name"], name)
        assert employee["name"] != name
