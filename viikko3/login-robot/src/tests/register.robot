*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input New Command

*** Test Cases ***
Register With Valid Username And Password
# ...
    Input Credentials  koira  koira123123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  koira123456
    Output Should Contain  Username taken

Register With Too Short Username And Valid Password
    Input Credentials  ka  koira123123
    Output Should Contain  Fix username or password

Register With Valid Username And Too Short Password
    Input Credentials  koira  koira1
    Output Should Contain  Fix username or password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  koira  koirakoira
    Output Should Contain  Fix username or password

*** Keywords ***
Create User And Input New Command
    Create User  kalle  kalle123123
    Input New Command