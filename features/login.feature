Feature: Login page test

  Background:
    Given automationPractice: user is on the main page

    Scenario: User successfully logs in
        When automationPractice: user is not logged in
        When automationPractice: user clicks on the Sign In button
        When signInPage: user successfully logs in
        Then automationPractice: user gains access to his account

    @smoke7
    Scenario Outline: User enters wrong credentials when he wants to sign in
        When automationPractice: user is not logged in
        When automationPractice: user clicks on the Sign In button
        When signInPage: user inserts "<email>" and "<password>"
        Then signInPage: the "<expected_alert>" alert appears

      Examples:
        |        email        |    password   |        expected_alert        |
        |        N/A          |      N/A      |    email address required    |
        |       abcdef        |      N/A      |     Invalid email address    |
        |  abdddd@yahoo.com   |      N/A      |     Password is required     |
        |  abdddd@yahoo.com   |   ASDsd234$   |     Authentication failed    |