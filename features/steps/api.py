from behave import given
import requests
from pathlib import Path

@given('the API is running')
def step_impl(context):
    # Make a GET request to the /health endpoint to check that the API is running
    response = requests.get("http://localhost:8000")
    assert response.status_code == 200

@then('the response status code should be "{code}"')
def step_impl(context, code):
    assert context.response.status_code == int(code) 