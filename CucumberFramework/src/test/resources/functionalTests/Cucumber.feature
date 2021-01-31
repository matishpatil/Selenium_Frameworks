Feature: Verify cucumbers in the basket

  Scenario: Verify the cucumber count in the basket
    Given I have "2" cucumbers in the basket
    When I add "4" cucumbers in the basket
    Then I should have "6" cucumbers in the basket