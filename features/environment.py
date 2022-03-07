from features.browser import Browser
from features.tools import get_user_credentials
from features.pages.automationPractice_page import AutomationPracticePage
from features.pages.cart_page import CartPage
from features.pages.sign_in_page import SignInPage
from features.pages.forgot_password_page import ForgotPasswordPage
from features.pages.account_details_page import AccountDetails
from features.pages.search_page import SearchPage
from features.pages.order_history_page import OrderHistoryPage

def before_all(context):
    context.email = get_user_credentials()[0]
    context.password = get_user_credentials()[1]

    context.browser = Browser()
    context.cart_page = CartPage()
    context.search_page = SearchPage()
    context.sign_in_page = SignInPage()
    context.order_history_page = OrderHistoryPage()
    context.forgot_password_page = ForgotPasswordPage()
    context.automationPractice_page = AutomationPracticePage()
    context.account_details_page = AccountDetails()
    context.automationPractice_page.navigate_to_automationPractice_main_page()


def after_all(context):
    context.browser.close()

