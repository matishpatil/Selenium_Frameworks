Feature: Automated End2End Tests
Description: The purpose of this feature is to test End 2 End integration.
 
#Scenario Outline: Customer place an order by purchasing an item from search
#	Given user is on Home Page
#	When he search for "dress"
#	And choose to buy the first item
#	And moves to checkout from mini cart
#	And enter "<customer>" personal details on checkout page
#	And select same delivery address
#	And select payment method as "check" payment
#	And place the order
#	Then verify the order details
#Examples:
#	|customer|
#	|Lakshay|

	@IntegrationTest
	Scenario Outline: Verify the search on google
		Given I am on google search page
		When I enter "<search>" criteria
		Then I should be able to get "<search>" results
		Examples:
		|search|
		|Google|
		|India|


	@Sample
	Scenario: Verify successful login
		Given I login to the application with "Test" and "pass" as password
		When  I click on "Login" button
		Then I should be able to see "Welcome" message


	Scenario Outline: Verify the elements on the page
		Given I am on practice page
		When I select a "<radio>" button
		Then It should be able to select the "<radio>" button
		When I select a value from "<dropdown>"
		Then It should show the selected "<dropdown>" value
		When I select "<one value>" from multi select
		And I select "<another value>" from multi select
		Then I should have "<one value>" and "<another value>" in the multi select
		Examples:
		|radio|dropdown|one value|another value|
		|Benz |Benz    |Apple    |Orange       |