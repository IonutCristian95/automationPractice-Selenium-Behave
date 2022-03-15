from behave import *


@when('ForgotPasswordPage: user inserts his email and clicks the retrieve password button')
def step_impl(context):
    context.forgot_password_page.insert_email('g.ionutcristian95@gmail.com')
    context.forgot_password_page.click_retrieve_password_button()


@then('ForgotPasswordPage: a confirmation alert appears')
def step_impl(context):
    context.forgot_password_page.is_alert_active_confirmation_email()


@when('ForgotPasswordPage: user enters "{email}" and clicks the retrieve password button')
def step_impl(context, email):
    context.forgot_password_page.insert_email(email)
    context.forgot_password_page.click_retrieve_password_button()


@then('ForgotPasswordPage: the "{expected_alert}" appears')
def step_impl(context, expected_alert):
    context.forgot_password_page.alerts_forgot_password(expected_alert)
