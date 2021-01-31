*** Settings ***
Documentation  This is some basic info about the whole suite
Library  SeleniumLibrary
Library  C:/Demo/Robot/Data_Connect/Data_Connect/Tests/test.py

*** Variables ***
${WEB}=  http://www.amazon.com
${BROWSER}=  chrome
${TYPE OF FILE}=  jpg
${filename}=  fileres
*** Keywords ***

*** Test Cases ***
Open amazon home page
    open browser  ${WEB}  ${BROWSER}
    maximize browser window
    ${pathvar}=  getNewlyCreatedFolderName
    Set Global Variable  ${path}  ${pathvar}/screenshot
    Set Screenshot Directory  ${path}
    #Wait Until Page Contains Element
    Capture Page Screenshot  ${filename}.${TYPE OF FILE}
    close browser
    #Open Browser  http://www.amazon.com  ie
    #Close Browser





