from behave import given, when, then
import requests

@when('the user requests all employees')
def step_impl(context):
    # Send a GET request to the /employees endpoint to retrieve all employees
    context.response = requests.get("http://127.0.0.1:5000/employees")

@then('the response body should be a list of employees')
def step_impl(context):
    assert isinstance(context.response.json(), list)

@then('the response body should contain the employee with name "{name}" and email "{email}"')
def step_impl(context, name, email):
    employees = context.response.json()
    for employee in employees:
        if employee["name"] == name and employee["email"] == email:
            break
    else:
        assert False, f"No employee found with name {name} and email {email}"
