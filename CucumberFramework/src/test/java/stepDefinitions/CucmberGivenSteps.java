package stepDefinitions;

import cucumber.api.java.en.Given;

public class CucmberGivenSteps {

    @Given("^I have \"([^\"]*)\" cucumbers in the basket$")
    public void i_have_cucumbers_in_the_basket(String two) throws Throwable {
        System.out.println(two);
    }
}
