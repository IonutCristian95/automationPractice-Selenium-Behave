Feature: automationPractice Main Page test

  Background:
    Given automationPractice: user in on the main page

    Scenario Outline: Searching a product and getting results for that product
        When automationPractice: user searches for product "<product>" in the search bar
        Then automationPractice: relevant results are being displayed
        Examples:
            | product |
            |  dress  |
            |  shirt  |

    Scenario: User successfully adds a product in the cart
        When automationPractice: user adds a product in cart
        Then automationPractice: user proceeds to view the cart from the pop up layer

    Scenario: User successfully deletes a product from the cart
        When automationPractice: user adds a product in cart
        When automationPractice: user views the cart
        Then cartPage: user deletes the product from the cart
        And cartPage: shopping cart is empty

    Scenario: User successfully adds a product and completes the order using bankwire payment method
        When automationPractice: user adds a product in cart
        Then automationPractice: user proceeds to checkout
        When signInPage: user successfully logs in
        Then cartPage: user completes the required information
        Then cartPage: user makes the order and pays by bankwire


    Scenario: User successfully adds a product and completes the order using cheque payment method
        When automationPractice: user adds a product in cart
        Then automationPractice: user proceeds to checkout
        When automationPractice: user is already logged in
        Then cartPage: user completes the required information
        Then cartPage: user makes the order and pays by cheque


    Scenario: User is accessing the account management page through the main page
        When automationPractice: user clicks on the Sign In button
        When signInPage: user successfully logs in
        When automationPractice: user clicks on the account management button
        Then accountDetailsPage: user is on the account management page

#    @smoke3
#    Scenario: User checks for two orders, one paid by bankwire, one by cheque
#        When automationPractice: user is already logged in
#        Then automationPractice: user clicks on the account management button
#        When accountDetailsPage: user clicks on "order history and details" button
#        Then accountDetailsPage: user will view current orders - one paid by bankwire and one by cheque

    @smoke4
    Scenario: User successfully logs in

    @smoke5
    Scenario: User tries to renew password using forgot password option

    @smoke6
    Scenario: User wants to subscribe to the newsletter

    @smoke9
    Scenario: User adds a discounted product in cart

#      Negatives

    @smoke10
    Scenario: User tries to complete the order without agreeing to the terms of service

    @smoke7
    Scenario: User enters wrong credentials when he wants to sign in


    @smoke8
    Scenario: User tries to renew password using wrong email format

    Scenario Outline: User searches a product that doesn't exist on the website and gets no results => no results alert is displayed
        When automationPractice: user searches for product "<product>" in the search bar
        Then automationPractice: no results alert is displayed
    Examples:
        | product |
        |  alien  |
        |  cars   |
