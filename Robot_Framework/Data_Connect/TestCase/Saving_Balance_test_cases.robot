*** Settings ***
Library  SeleniumLibrary
Library  OperatingSystem
Resource  ../Keywords/Balance_keywords.robot
Resource  ../Page_Locators/Saving_Balance.robot
Test Setup  initialize_application
Test Teardown  terminate_application

*** Variables ***
${BROWSER}=  Chrome
${URL}=  http://localhost:8084/index
${VALID_USERNAME}=  swati
${VALID_PASSWORD}=  swati
${debit_amount}=  300
${credit_amount}=  500

*** Test Cases ***
Updated balance perform debit operation
    ${db_init}=  Storing Initial Balance
    ${value}=  Storing UI value
    should be equal as numbers  ${db_init}  ${value}
    ${value_update_wihdraw}=  Storing UI value after withdraw amount
    ${db_Updated}=  Storing Final Balance
    should be equal as numbers  ${db_Updated}  ${value_update_wihdraw}

Updated balance perform credit operation
    ${value_update_credit}=  Storing UI value after credit amount
    ${db_Updated}=  Storing Final Balance
    should be equal as numbers  ${db_Updated}  ${value_update_credit}



