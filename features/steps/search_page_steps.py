from behave import *

@when('searchPage: user searches for product "{product}" in the search bar')
def step_impl(context, product):
    context.search_page.search_bar_insert(product)
    context.search_page.click_search_bar_button()

@then('searchPage: relevant results are being displayed')
def step_impl(context):
    context.search_page.returned_results_counter()


@then('searchPage: no results alert is displayed')
def step_impl(context):
    context.search_page.results_alert_displayed()
