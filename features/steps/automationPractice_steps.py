from time import sleep

from behave import *


@given('automationPractice: user is on the main page')
def step_impl(context):
    context.automationPractice_page.navigate_to_automationPractice_main_page()


@when('automationPractice: user adds a product in cart')
def step_impl(context):
    context.automationPractice_page.add_to_cart(1)


@when('automationPractice: user proceeds to view the cart from the pop up layer')
@then('automationPractice: user proceeds to view the cart from the pop up layer')
def step_impl(context):
    context.automationPractice_page.proceed_to_checkout()
    sleep(2)


@when('automationPractice: user views the cart')
def step_impl(context):
    context.automationPractice_page.click_continue_shopping_btn_layer_cart()
    sleep(2)
    context.automationPractice_page.click_view_cart_button()


@when('automationPractice: user proceeds to checkout')
def step_impl(context):
    # Proceeds from the main page to the cart page
    context.automationPractice_page.proceed_to_checkout()
    # Proceeds to complete the required information
    context.cart_page.proceed_to_checkout_button()


@when('automationPractice: user is already logged in')
def step_impl(context):
    context.automationPractice_page.is_user_already_logged_in()


@when('automationPractice: user is not logged in')
def step_impl(context):
    context.automationPractice_page.user_logged_out()


@when('automationPractice: user logs in')
def step_impl(context):
    try:
        context.automationPractice_page.click_sign_in_button()
        sleep(2)
        context.sign_in_page.sign_in(context.email, context.password)
        sleep(2)
        context.automationPractice_page.navigate_to_automationPractice_main_page()
    except Exception as e:
        print(e)
    finally:
        assert True


@when('automationPractice: user clicks on the Sign In button')
def step_impl(context):
    context.automationPractice_page.click_sign_in_button()


@when('automationPractice: user clicks on the account management button')
def step_impl(context):
    context.automationPractice_page.click_account_management_button()


@when('automationPractice: user inserts the email address "{email}"')
def step_impl(context, email):
    context.automationPractice_page.insert_email_newsletter(email)


@when('automationPractice: user clicks the newsletter subscription button')
def step_impl(context):
    context.automationPractice_page.click_subscribe_newsletter_button()


@then('automationPractice: newsletter subscription confirmation message appears')
def step_impl(context):
    context.automationPractice_page.newsletter_confirmation_message()


@then('automationPractice: already subscribed alert message appears')
def step_impl(context):
    context.automationPractice_page.newsletter_already_subscribed_alert()


@then('automationPractice: invalid email address error message appears')
def step_impl(context):
    context.automationPractice_page.newsletter_invalid_email_error()


@then('automationPractice: user gains access to his account')
def step_impl(context):
    context.automationPractice_page.logged_in_options_present()


@when('automationPractice: user clicks on a product')
def step_impl(context):
    context.automationPractice_page.view_product(1)


@when('automationPractice: user adds a discounted product in cart')
def step_impl(context):
    context.automationPractice_page.add_to_cart(7)
