*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Library  ../Libraries/DB_init.py
Library  ../Libraries/DB_Updated.py

*** Keywords ***
initialize_application
    open browser  ${URL}  ${BROWSER}
    maximize browser window
    set selenium speed  0.2s

terminate_application
    run keyword if test failed  capture page screenshot
    close browser

Storing Initial Balance
    ${db_init}=  init_balance
    Log To Console  ${db_init}
    [return]  ${db_init}

Storing UI value
    input text  ${USERNAME_ELEMENT}  ${VALID_USERNAME}
    input text  ${PASSWORD_ELEMENT}  ${VALID_PASSWORD}
    click button  ${SIGN_IN_BUTTON}
    ${value}=  get text  ${initial_balance_UI}
    Log To Console  ${value}
    [return]  ${value}

Storing UI value after withdraw amount
    click element  ${Go_To_Withdrawal}
    click element  ${Account_Field}
    click element  ${Account_Type}
    input text  ${Amount}  ${debit_amount}
    click button  ${Deposit_Button}
    ${value_update_wihdraw}=  get text  ${Update_balance_UI}
    Log To Console  ${value_update_wihdraw}
    [return]  ${value_update_wihdraw}

Storing UI value after credit amount
    input text  ${USERNAME_ELEMENT}  ${VALID_USERNAME}
    input text  ${PASSWORD_ELEMENT}  ${VALID_PASSWORD}
    click button  ${SIGN_IN_BUTTON}
    click element  ${Go_To_Deposit}
    click element  ${Account_Field}
    click element  ${Account_Type}
    input text  ${Amount}  ${credit_amount}
    click button  ${Deposit_Button}
    ${value_update_credit}=  get text  ${Update_balance_UI}
    Log To Console  ${value_update_credit}
    [return]  ${value_update_credit}

Storing Final Balance
    ${db_final}  final_balance
    Log To Console  ${db_final}
    [return]  ${db_final}
