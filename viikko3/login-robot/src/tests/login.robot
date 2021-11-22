*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Login Command

*** Test Cases ***
Login With Correct Credentials
    Input Credentials  kalle  kalle123123
    Output Should Contain  Logged in

Login With Incorrect Password
    Input Credentials  kalle  koira123123
    Output Should Contain  Invalid username or password

Login With Nonexistent Username
    Input Credentials  koira  kalle123123
    Output Should Contain  Invalid username or password

*** Keywords ***
Create User And Input Login Command
    Create User  kalle  kalle123123
    Input Login Command
