from behave import *


@when('productPage: user adds the product to the wishlist')
def step_impl(context):
    context.product_page.add_to_wishlist()


@then('productPage: added to wishlist alert is displayed')
def step_impl(context):
    context.product_page.added_to_wishlist_alert()
