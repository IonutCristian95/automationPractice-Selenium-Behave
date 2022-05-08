from features.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountDetailsElements(object):
    ORDER_HISTORY = '(//ul[contains(@class, "myaccount")]//li)[1]'
    PERSONAL_INFORMATION = '(//ul[contains(@class, "myaccount")]//li)[4]'
    BACK_TO_ACCOUNT_MAIN_PAGE_BUTTON = '//span[contains(., "Back to your account")]'
    WISHLISTS = '//span[contains(., "My wishlists")]//parent::a'


class AccountDetails(Browser):
    def navigate_to_account_details_page(self):
        self.driver.get('http://automationpractice.com/index.php?controller=my-account')

    def confirm_account_details_page_displayed(self):
        """
            This method will assert True if the current page displayed is the one for user's account
            otherwise it will assert False
        """
        assert "controller=my-account" in self.driver.current_url

    def view_order_history(self):
        self.driver.find_element_by_xpath(AccountDetailsElements.ORDER_HISTORY).click()

    def view_wishlists(self):
        wishlist_btn = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, AccountDetailsElements.WISHLISTS))
        )
        wishlist_btn.click()
