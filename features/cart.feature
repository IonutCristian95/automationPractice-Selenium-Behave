Feature: Cart page automation

  Background:
    Given automationPractice: user is on the main page

    Scenario: User successfully adds a product in the cart
        When automationPractice: user adds a product in cart
        Then automationPractice: user proceeds to view the cart from the pop up layer

    Scenario: User successfully deletes a product from the cart
        When automationPractice: user adds a product in cart
        When automationPractice: user views the cart
        When cartPage: user deletes the products from the cart
        Then cartPage: shopping cart is empty


    Scenario: User successfully adds a product and completes the order using bankwire payment method
        When automationPractice: user adds a product in cart
        When automationPractice: user proceeds to checkout
        When signInPage: user successfully logs in
        When cartPage: user completes the required information
        When cartPage: user makes the order and pays by bankwire
        Then cartPage: user clicks the confirm order button


    Scenario: User successfully adds a product and completes the order using cheque payment method
        When automationPractice: user adds a product in cart
        When automationPractice: user proceeds to checkout
        When automationPractice: user is already logged in
        When cartPage: user completes the required information
        When cartPage: user makes the order and pays by cheque
        Then cartPage: user clicks the confirm order button


    Scenario: User checks for two orders, one paid by bankwire, one by cheque
        When automationPractice: user is already logged in
        When automationPractice: user clicks on the account management button
        When accountDetailsPage: user clicks on "order history and details" button
        Then orderHistoryPage: user will view current orders - one paid by bankwire and one by cheque


    Scenario: User tries to complete the order without agreeing to the terms of service
        When automationPractice: user adds a product in cart
        When automationPractice: user proceeds to checkout
        When automationPractice: user is already logged in
        When cartPage: user completes the required information