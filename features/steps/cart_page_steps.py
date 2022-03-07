from behave import *

from time import sleep


@when('cartPage: user completes the required information')
def step_impl(context):
    context.cart_page.procees_address()
    context.cart_page.accept_terms_of_service()
    context.cart_page.procees_carrier()


@then('cartPage: shopping cart is empty')
def step_impl(context):
    context.cart_page.is_alert_active_empty_cart()


@when('cartPage: user deletes the product from the cart')
def step_impl(context):
    context.cart_page.delete_a_specific_product(1)
    sleep(3)


@when('cartPage: user makes the order and pays by bankwire')
def step_impl(context):
    context.cart_page.select_payment_method("bankwire")


@when('cartPage: user makes the order and pays by cheque')
def step_impl(context):
    context.cart_page.select_payment_method("cheque")


@then('cartPage: user clicks the confirm order button')
def step_impl(context):
    context.cart_page.click_confirm_order_btn()
