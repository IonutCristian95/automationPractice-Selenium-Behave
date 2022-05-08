Feature: automationPractice Main Page test

  Background:
    Given automationPractice: user is on the main page

    Scenario Outline: Searching a product and getting results for that product
        When searchPage: user searches for product "<product>" in the search bar
        Then searchPage: relevant results are being displayed
        Examples:
            | product |
            |  dress  |
            |  shirt  |


    Scenario: User is accessing the account management page through the main page
        When automationPractice: user clicks on the Sign In button
        When signInPage: user successfully logs in
        When automationPractice: user clicks on the account management button
        Then accountDetailsPage: user is on the account management page

    Scenario Outline: The user is subscribing to the newsletter
        When automationPractice: user inserts the email address "<email>"
        When automationPractice: user clicks the newsletter subscription button
        Then automationPractice: newsletter subscription confirmation message appears
    Examples:
      |                     email                       |
      |    test.email.automation.practice.111111110@gmail.com   |

    Scenario Outline: User is already subscribed to the newsletter
        When automationPractice: user inserts the email address "<email>"
        When automationPractice: user clicks the newsletter subscription button
        Then automationPractice: already subscribed alert message appears
    Examples:
      |                     email                  |
      | test.email.automation.practice.111111110@gmail.com |

    Scenario Outline: User tries to subscribe to the newsletter with wrong email format
        When automationPractice: user inserts the email address "<email>"
        When automationPractice: user clicks the newsletter subscription button
        Then automationPractice: invalid email address error message appears
    Examples:
        |    email   |
        |    test    |
        | @yahoo.com |

    Scenario: User adds a discounted product in cart
        When automationPractice: user adds a discounted product in cart
        When automationPractice: user proceeds to view the cart from the pop up layer
        Then cartPage: the discounted product appears in the shopping cart

    Scenario Outline: User searches a product that doesn't exist on the website and gets no results => no results alert is displayed
        When searchPage: user searches for product "<product>" in the search bar
        Then searchPage: no results alert is displayed
    Examples:
        |   product   |
        |   hardware  |
        |   electric  |
