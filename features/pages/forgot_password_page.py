from features.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ForgotPasswordElements(object):
    ALERT_CONFIRMATION_EMAIL_SENT = '//*[contains(text(), "confirmation email")]'
    EMAIL_INPUT = '//input[@id="email"]'
    RETRIEVE_PASSWORD = '//span[contains(text(), "Retrieve")]/parent::button'
    ALERT_NO_ACCOUNT_REGISTERED = '//div[@class="alert alert-danger"]//li[contains(text(), "no account")]'
    ALERT_INVALID_EMAIL = '//li[contains(text(), "Invalid email")]'


class ForgotPasswordPage(Browser):
    def navigate_to_forgot_pass_page(self):
        self.driver.get('http://automationpractice.com/index.php?controller=password')

    def is_alert_active_no_account(self):
        assert self.driver.find_element_by_xpath(ForgotPasswordElements.ALERT_NO_ACCOUNT_REGISTERED).is_displayed()

    def is_alert_active_invalid_email(self):
        assert self.driver.find_element_by_xpath(ForgotPasswordElements.ALERT_INVALID_EMAIL).is_displayed()

    def click_retrieve_password_button(self):
        self.driver.find_element_by_xpath(ForgotPasswordElements.RETRIEVE_PASSWORD).click()

    def insert_email(self, email):
        email_input = WebDriverWait(self.driver, 3000).until(
            EC.visibility_of_element_located((By.XPATH, ForgotPasswordElements.EMAIL_INPUT))
        )
        email_input.send_keys(email)
