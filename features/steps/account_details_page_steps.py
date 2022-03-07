from behave import *

@then('accountDetailsPage: user is on the account management page')
def step_impl(context):
    context.account_details_page.confirm_account_details_page_displayed()


@when('accountDetailsPage: user clicks on "order history and details" button')
def step_impl(context):
    context.account_details_page.view_order_history()


