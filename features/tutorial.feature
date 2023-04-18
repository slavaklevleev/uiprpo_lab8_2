Feature: Employee Management
    As an employer
    I want to manage my employees
    So that I can keep track of their information and make updates as needed

    Background:
        Given a database of employees exists
        And the API is running

    Scenario: Add a new employee
        When the user adds a new employee with name "John Smith" and email "john.smith@example.com"
        Then the response status code should be "201"
        And the response body should contain the name "John Smith"
        And the response body should contain the email "john.smith@example.com"

    Scenario: Get all employees
        When the user requests all employees
        Then the response status code should be "200"
        And the response body should be a list of employees
        And the response body should contain the employee with name "John Smith" and email "john.smith@example.com"

    Scenario: Update an employee
        Given there is an employee with the name "John Smith"
        When the user updates the employee's email to "jsmith@example.com"
        Then the response status code should be "200"
        And the response body should contain previous name "John Smith"
        And the response body should contain updated email "jsmith@example.com"

    Scenario: Delete an employee
        Given there is an employee with the name "John Due" and email "john.due@example.com"
        When the user deletes the employee
        Then the response status code should be "204"
        And the employee with the name "John Due" should no longer exist in the database
