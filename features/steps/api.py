from behave import given
import requests
import os.path

@given(u'a database of employees exists')
def step_impl(context):
    check_file = os.path.isfile('/Users/klevleev/Documents/uiprpo_lab8/employees.txt')
    assert check_file

@given('the API is running')
def step_impl(context):
    # Make a GET request to the /health endpoint to check that the API is running
    response = requests.get("http://127.0.0.1:5000")
    assert response.status_code == 200

@then('the response status code should be "{code}"')
def step_impl(context, code):
    assert context.response.status_code == int(code)