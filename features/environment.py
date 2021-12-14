from features.browser import Browser
from features.tools import get_user_credentials

def before_all(context):
    # user credentials

    username, password = get_user_credentials()[0], get_user_credentials()[1]

    context.browser = Browser()

def after_all(context):
    context.browser.close()