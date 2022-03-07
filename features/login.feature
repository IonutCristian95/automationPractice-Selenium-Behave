Feature: Login page test

  Background:
    Given automationPractice: user is on the main page

    @smoke4
    Scenario: User successfully logs in
        When automationPractice: user is not logged in
        When automationPractice: user clicks on the Sign In button
        When signInPage: user successfully logs in
        Then automationPractice: user gains access to his account
        When automationPractice: user is not logged in

    @smoke5
    Scenario: User tries to renew password using forgot password option

    @smoke8
    Scenario: User tries to renew password using wrong email format

    @smoke7
    Scenario: User enters wrong credentials when he wants to sign in