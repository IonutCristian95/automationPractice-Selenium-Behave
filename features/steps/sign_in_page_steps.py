from behave import *


@when('signInPage: user successfully logs in')
def step_impl(context):
    context.sign_in_page.sign_in(context.email, context.password)


@when('signInPage: user proceeds to forgot password page')
def step_impl(context):
    context.sign_in_page.click_forgot_password_option()


@when('signInPage: user inserts "{email}" and "{password}"')
def step_impl(context, email, password):
    context.sign_in_page.sign_in(email, password)


@then('signInPage: the "{expected_alert}" alert appears')
def step_impl(context, expected_alert):
    context.sign_in_page.alerts_sign_in_page(expected_alert)
