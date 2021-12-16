from behave import *

@given('automationPractice: user in on the main page')
def step_impl(context):
    context.automationPractice_page.navigate_to_automationPractice_main_page()

@when('automationPractice: user types product "dress" in the search bar')
def step_impl(context):
    context.automationPractice_page.search_bar_insert("dress")


@when('automationPractice: user clicks the search button')
def step_impl(context):
    context.automationPractice_page.click_search_bar_button()

@then('automationPractice: page title changes to Search - My Store')
def step_impl(context):
    context.automationPractice_page.check_search_page_title()

@then('automationPractice: results alert is not displayed')
def step_impl(context):
    if not context.automationPractice_page.results_alert_displayed():
        assert True
    else:
        assert False

