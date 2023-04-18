from behave import given, when, then
import requests

@when('the user adds a new employee with name "{name}" and email "{email}"')
def step_impl(context, name, email):
    # Send a POST request to the /employees endpoint with the new employee data
    context.employee = {"name": name, "email": email}
    headers = {"Content-Type": "application/json"}
    context.response = requests.post("http://localhost:5000/employees", json=context.employee, headers=headers)

@then('the response body should contain the name "{name}"')
def step_impl(context, name):
    assert context.employee["name"] in context.response.json()["name"]

@then('the response body should contain the email "{email}"')
def step_impl(context, email):
    assert context.employee["email"] in context.response.json()["email"]
