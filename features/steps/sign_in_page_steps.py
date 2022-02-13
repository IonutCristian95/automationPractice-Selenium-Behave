from behave import *


@when('signInPage: user successfully logs in')
def step_impl(context):
    context.sign_in_page.sign_in(context.email, context.password)
