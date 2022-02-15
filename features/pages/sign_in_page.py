from features.browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

class SignInPageElements(object):
    SIGN_IN_EMAIL = '//form[@id="login_form"]//label[@for="email"]//following-sibling::input'
    SIGN_IN_PASSWORD = '//form[@id="login_form"]//label[@for="passwd"]//following-sibling::span//input'
    SIGN_IN_BUTTON = '//button[@id="SubmitLogin"]'
    FORGOT_PASSWORD_REF = '//p[contains(@class, "lost_password")]'
    CREATE_ACCOUNT_EMAIL = '//input[@id="email_create"]'
    CREATE_ACCOUNT_BUTTON = '//button[@id="SubmitCreate"]'
    # Error encountered when creating an account
    ERROR_CREATE_ACCOUNT_EMAIL = '//*[contains(@id, "create_account_error")]'
    # Error encountered when signing in
    ERROR_INVALID_EMAIL = '//li[contains(text(), "Invalid email")]'

class SignInPage(Browser):
    def navigate_to_sign_in_page(self):
        self.driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')

    def sign_in_email_input(self, email):
        email_input = WebDriverWait(self.driver, 3000).until(
            EC.presence_of_element_located((By.XPATH, SignInPageElements.SIGN_IN_EMAIL))
        )
        email_input.clear()
        email_input.send_keys(email)
        
    def sign_in_password_input(self, password):
        password_input = WebDriverWait(self.driver, 3000).until(
            EC.presence_of_element_located((By.XPATH, SignInPageElements.SIGN_IN_PASSWORD))
        )
        password_input.clear()
        password_input.send_keys(password)

    def click_sign_in_btn(self):
        self.driver.find_element_by_xpath(SignInPageElements.SIGN_IN_BUTTON).click()

    def sign_in(self, email, password):
        self.sign_in_email_input(email)
        self.sign_in_password_input(password)
        sleep(2)
        self.click_sign_in_btn()

