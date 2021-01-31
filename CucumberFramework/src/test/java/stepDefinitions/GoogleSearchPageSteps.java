package stepDefinitions;

import cucumber.TestContext;
import cucumber.api.java.en.Given;
import cucumber.api.java.en.Then;
import cucumber.api.java.en.When;
import org.junit.Assert;
import pageObjects.GoogleSearchPage;


public class GoogleSearchPageSteps {

    TestContext testContext;
    GoogleSearchPage googleSearchPage;

    public GoogleSearchPageSteps(TestContext context) {
        testContext = context;
        googleSearchPage = testContext.getPageObjectManager().getGoogleSearchPage();
    }

    @Given("^I am on google search page$")
    public void i_am_on_google_search_page() throws Throwable {
        googleSearchPage.navigateTo_GoogleSearchPage();
    }

    @When("^I enter \"([^\"]*)\" criteria$")
    public void i_enter_criteria(String stringToSearch) throws Throwable {
        googleSearchPage.enter_search_criteria(stringToSearch);
    }

    @Then("^I should be able to get \"([^\"]*)\" results$")
    public void i_should_be_able_to_get_results(String search) throws Throwable {
        String searchResultsString = googleSearchPage.return_Search_Results();
        Assert.assertTrue(searchResultsString.toLowerCase().contains(search.toLowerCase()));
    }
}
