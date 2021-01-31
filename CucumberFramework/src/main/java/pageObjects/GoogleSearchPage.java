package pageObjects;

import managers.FileReaderManager;
import org.openqa.selenium.Keys;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import selenium.Wait;

public class GoogleSearchPage {

    WebDriver driver;

    public GoogleSearchPage(WebDriver driver) {
        this.driver = driver;
        PageFactory.initElements(driver, this);
    }

    @FindBy(xpath = "//*[@id='tsf']/div[2]/div[1]/div[1]/div/div[2]/input")
    private WebElement search_textbox;

    @FindBy(xpath = "//*[@id='tsf']/div[2]/div[1]/div[3]/center/input[1]")
    private WebElement search_button;

    @FindBy(xpath = "//*[@id='rso']/div[1]/div/div[1]/a/h3")
    private WebElement get_contents_of_1st_link;


    public void navigateTo_GoogleSearchPage() {
        driver.get(FileReaderManager.getInstance().getConfigReader().getApplicationUrl());
    }

    public void enter_search_criteria(String search) {
        Wait.untilPageLoadComplete(driver);
        search_textbox.sendKeys(search);
        search_button.click();
    }

    public String return_Search_Results(){
        Wait.untilPageLoadComplete(driver);
        return get_contents_of_1st_link.getText();
    }

}
