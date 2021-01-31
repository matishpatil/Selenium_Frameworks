package stepDefinitions;

import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;

public class E2ESteps {
    @Given("^I login to the application with \"([^\"]*)\" and \"([^\"]*)\" as password$")
    public void iLoginToTheApplicationWithAndAsPassword(String userName, String password) throws Throwable {
        System.out.println("Username is "+ userName);
        System.out.println("Password is "+ password);
    }

    @When("^I click on \"([^\"]*)\" button$")
    public void iClickOnButton(String arg0) throws Throwable {
        System.out.println("I am in when");
    }

    @Then("^I should be able to see \"([^\"]*)\" message$")
    public void iShouldBeAbleToSeeMessage(String arg0) throws Throwable {
        System.out.println("I am in Then");
    }
}
