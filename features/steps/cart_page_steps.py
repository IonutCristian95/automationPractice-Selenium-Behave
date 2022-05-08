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


@when('cartPage: user deletes the products from the cart')
def step_impl(context):
    context.cart_page.delete_products_in_cart()


@when('cartPage: user makes the order and pays by bankwire')
def step_impl(context):
    context.cart_page.select_payment_method("bankwire")


@when('cartPage: user makes the order and pays by cheque')
def step_impl(context):
    context.cart_page.select_payment_method("cheque")


@then('cartPage: user clicks the confirm order button')
def step_impl(context):
    context.cart_page.click_confirm_order_btn()


@then('cartPage: user increases the quantity of the product')
def step_impl(context):
    context.cart_page.increase_quantity_of_a_specific_product(1)
    sleep(2)
    context.cart_page.decrease_quantity_of_a_specific_product(1)
    sleep(2)
    context.cart_page.increase_quantity_of_a_specific_product(1)
    sleep(2)


@then('cartPage: the discounted product appears in the shopping cart')
def step_impl(context):
    context.cart_page.check_for_price_reduction()
