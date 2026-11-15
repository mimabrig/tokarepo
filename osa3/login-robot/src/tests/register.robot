*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  matti  meikalainen1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle124
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  k  salasana1
    Output Should Contain  Username not valid

Register With Enough Long But Invalid Username And Valid Password
    Input Credentials  kalle245  salasana1
    Output Should Contain  Username not valid

Register With Valid Username And Too Short Password
    Input Credentials  matti  Sf1
    Output Should Contain  Password not valid

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  matti  meikalainen
    Output Should Contain  Password not valid

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
