from features.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UserInformationPageElements(object):
    INPUT_SOCIAL_TITLE = '//input[@name="id_gender"]'
    INPUT_FIRSTNAME = '//input[@id="firstname"]'
    INPUT_LASTNAME = '//input[@id="lastname"]'
    INPUT_EMAIL = '//input[@id="email"]'
    DATE_OF_BIRTH_DAY = '//select[@id="days"]/option'  # 1 - 32
    DATE_OF_BIRTH_MONTH = '//select[@id="months"]/option'  # 1 - 13
    DATE_OF_BIRTH_YEAR = '//select[@id="years"]/option'  # a year between 1900 and 2022
    INPUT_CURRENT_PASSWORD = '//input[@id="old_passwd"]'
    INPUT_NEW_PASSWORD = '//input[@id="passwd"]'
    INPUT_NEW_PASSWORD_CONFIRMATION = '//input[@id="confirmation"]'
    NEWSLETTER_SIGN_UP = '//input[@id="newsletter"]'
    SPECIAL_OFFERS_OPT_IN = '//input[@id="optin"]'
    SAVE_INFORMATION = '//button[@name="submitIdentity"]'
    BUTTON_BACK_TO_YOUR_ACCOUNT = '//span[contains(. , "Back to your account")]//parent::a'
    BUTTON_HOME = '//span[contains(. , "Home")]//parent::a'


class UserInformationPage(Browser):
    def navigate_to_user_info_page(self):
        self.driver.get('http://automationpractice.com/index.php?controller=identity')

