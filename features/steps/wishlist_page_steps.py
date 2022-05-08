from behave import *
from time import sleep


@then('wishlistPage: wishlist page currently displayed')
def step_impl(context):
    context.wishlist_page.is_wishlist_page_currently_displayed()


@then('wishlistPage: default wishlist "My Wishlist" should be created')
def step_impl(context):
    context.wishlist_page.default_wishlist_created()


@then('wishlistPage: user creates a new wishlist named "{wishlist_name}"')
def step_impl(context, wishlist_name):
    context.wishlist_page.create_new_wishlist(wishlist_name)


@when('wishlistPage: user clicks to view the empty wishlist named "{wishlist_name}"')
def step_impl(context, wishlist_name):
    context.wishlist_page.view_wishlist(wishlist_name)


@then('wishlistPage: No products alert is displayed')
def step_impl(context):
    context.wishlist_page.no_products_alert_displayed()


@when('wishlistPage: user clicks to delete the "{wishlist_name}" wishlist')
def step_impl(context, wishlist_name):
    context.wishlist_page.delete_wishlist(wishlist_name)
    context.wishlist_page.confirm_wishlist_delete()


@then('wishlistPage: "{wishlist_name}" is deleted')
def step_impl(context, wishlist_name):
    if not context.wishlist_page.search_for_wishlist(wishlist_name):
        assert True  # If the wishlist was not found in the list, assert True
    else:
        assert False
