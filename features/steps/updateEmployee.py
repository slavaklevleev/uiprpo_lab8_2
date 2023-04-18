from behave import given, when, then
import requests

@given('there is an employee with the name "{name}"')
def step_impl(context, name):
    # Send a GET request to the /employees endpoint to check that the employee exists
    response = requests.get("http://localhost:5000/employees")
    employees = response.json()
    for employee in employees:
        if employee["name"] == name:
            context.employee_id = employee["id"]
            break
    else:
        assert False, f"No employee found with name {name}"

@when('the user updates the employee\'s email to "{email}"')
def step_impl(context, email):
    # Send a PUT request to the /employees/:id endpoint to update the employee's email
    response = requests.put(f"http://localhost:5000/employees/{context.employee_id}", json={"email": email})
    context.response = response

@then('the response body should contain previous name "{name}"')
def step_impl(context, name):
    assert context.response.json()["name"] == name

@then('the response body should contain updated email "{email}"')
def step_impl(context, email):
    assert context.response.json()["email"] == email
