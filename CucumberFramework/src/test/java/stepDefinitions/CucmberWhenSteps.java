package stepDefinitions;

import cucumber.api.java.en.When;

public class CucmberWhenSteps {

    @When("^I add \"([^\"]*)\" cucumbers in the basket$")
    public void i_add_cucumbers_in_the_basket(String four) throws Throwable {
        System.out.println(four);
    }
}
