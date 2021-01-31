package stepDefinitions;

import cucumber.api.java.en.Then;
import org.junit.Assert;

public class CucmberThenSteps {

    @Then("^I should have \"([^\"]*)\" cucumbers in the basket$")
    public void i_should_have_cucumbers_in_the_basket(String six) throws Throwable {
        System.out.println(six);
        Assert.assertTrue(Integer.parseInt(six) == 6);
    }
}
