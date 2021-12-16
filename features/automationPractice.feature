Feature: automationPractice Main Page test

  Background:
    Given automationPractice: user in on the main page

    @smoke
    Scenario: Searching a product
        When automationPractice: user types product "dress" in the search bar
        When automationPractice: user clicks the search button
        Then automationPractice: page title changes to Search - My Store
        Then automationPractice: results alert is not displayed