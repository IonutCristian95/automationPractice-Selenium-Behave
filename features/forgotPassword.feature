Feature: Forgot Password page test

  Background:
    Given automationPractice: user is on the main page

    Scenario: User tries to renew password using forgot password option
        When automationPractice: user is not logged in
        When automationPractice: user clicks on the Sign In button
        When signInPage: user proceeds to forgot password page
        When ForgotPasswordPage: user inserts his email and clicks the retrieve password button
        Then ForgotPasswordPage: a confirmation alert appears

    @smoke8
    Scenario Outline: User tries to renew password using wrong email format
        When automationPractice: user is not logged in
        When automationPractice: user clicks on the Sign In button
        When signInPage: user proceeds to forgot password page
        When ForgotPasswordPage: user enters "<email>" and clicks the retrieve password button
        Then ForgotPasswordPage: the "<expected_alert>" appears

      Examples:
        |        email       |                expected_alert                 |
        |       asdfgs       |              Invalid email address            |
        |   asdfgs@yahoo.com | no account registered for this email address  |