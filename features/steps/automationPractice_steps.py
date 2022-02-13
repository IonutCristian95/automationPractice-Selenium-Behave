from time import sleep

from behave import *


@given('automationPractice: user in on the main page')
def step_impl(context):
    context.automationPractice_page.navigate_to_automationPractice_main_page()


@when('automationPractice: user searches for product "{product}" in the search bar')
def step_impl(context, product):
    context.automationPractice_page.search_bar_insert(product)
    context.automationPractice_page.click_search_bar_button()


@then('automationPractice: relevant results are being displayed')
def step_impl(context):
    context.automationPractice_page.returned_results_counter()


@then('automationPractice: no results alert is displayed')
def step_impl(context):
    context.automationPractice_page.results_alert_displayed()


@when('automationPractice: user adds a product in cart')
def step_impl(context):
    context.automationPractice_page.add_to_cart(1)


@then('automationPractice: user proceeds to view the cart from the pop up layer')
def step_impl(context):
    context.automationPractice_page.proceed_to_checkout()
    sleep(2)


@when('automationPractice: user views the cart')
def step_impl(context):
    context.automationPractice_page.click_continue_shopping_btn_layer_cart()
    sleep(2)
    context.automationPractice_page.click_view_cart_button()


@then('automationPractice: user increases the quantity of the product')
def step_impl(context):
    context.cart_page.increase_quantity_of_a_specific_product(1)
    sleep(2)
    context.cart_page.decrease_quantity_of_a_specific_product(1)
    sleep(2)
    context.cart_page.increase_quantity_of_a_specific_product(1)
    sleep(2)


@then('automationPractice: user proceeds to checkout')
def step_impl(context):
    # Proceeds from the main page to the cart page
    context.automationPractice_page.proceed_to_checkout()
    # Proceeds to complete the required information
    context.cart_page.proceed_to_checkout_button()

@when('automationPractice: user is already logged in')
def step_impl(context):
    context.automationPractice_page.is_user_already_logged_in()
