from features.browser import Browser
from features.tools import get_user_credentials
from features.pages.automationPractice_page import AutomationPracticePage


def before_all(context):
    username = get_user_credentials()[0]
    password = get_user_credentials()[1]

    context.browser = Browser()
    context.automationPractice_page = AutomationPracticePage()
    context.automationPractice_page.navigate_to_automationPractice_main_page()


def after_all(context):
    context.browser.close()
