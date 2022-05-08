from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from features.browser import Browser


class WishlistPageElements(object):
    NEW_WISHLIST_NAME = '//input[@id="name"]'
    NEW_WISHLIST_SAVE_BTN = '//button[@id="submitWishlist"]'
    NO_PRODUCTS_IN_WISHLIST_ALERT = '//div[@id="block-order-detail"]//p[contains(text(), "No products")]'
    BUTTON_BACK_TO_USER_ACCOUNT = '//span[contains(., "Back to Your Account")]//parent::a'
    BUTTON_HOME = '//span[contains(., "Home")]//parent::a'
    DEFAULT_WISHLIST = '//tr//a[contains(., "My wishlist")]'
    WISHLIST_NAMES = '//tbody//tr/td[1]'


class WishlistPage(Browser):
    def navigate_to_wishlist_page(self):
        self.driver.get("http://automationpractice.com/index.php?fc=module&module=blockwishlist&controller=mywishlist")

    def is_wishlist_page_currently_displayed(self):
        assert "mywishlist" in self.driver.current_url

    def default_wishlist_created(self):
        """
        When adding a product to a wishlist and there was none created beforehand,
        there will be created a default one called "My wishlist"
        """
        default_wishlist = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, WishlistPageElements.DEFAULT_WISHLIST))
        )
        default_wishlist.is_displayed()

    def create_new_wishlist(self, wishlist_name):
        input_wishlist = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, WishlistPageElements.NEW_WISHLIST_NAME))
        )
        input_wishlist.send_keys(wishlist_name)

        save_wishlist_btn = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, WishlistPageElements.NEW_WISHLIST_SAVE_BTN))
        )
        save_wishlist_btn.click()

    def view_wishlist(self, wishlist_name):
        wishlist = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, f'(//a[contains(., "{wishlist_name}")]'
                                            f'//ancestor::td//following-sibling::td//a[contains(., View)])[1]'))
        )
        wishlist.click()

    def delete_wishlist(self, wishlist_name):
        wishlist = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(
                (By.XPATH, f'//a[contains(., "{wishlist_name}")]'
                           f'//ancestor::td//following-sibling::td[@class="wishlist_delete"]//a'))
        )
        wishlist.click()

    def click_home_button(self):
        home_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, WishlistPageElements.BUTTON_HOME))
        )
        home_button.click()

    def click_back_to_account_button(self):
        account_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, WishlistPageElements.BUTTON_BACK_TO_USER_ACCOUNT))
        )
        account_button.click()

    def confirm_wishlist_delete(self):
        WebDriverWait(self.driver, 5).until(EC.alert_is_present(), 'Timed out waiting for simple alert to appear')
        alert = self.driver.switch_to.alert
        alert.accept()
        sleep(2)

    def no_products_alert_displayed(self):
        alert = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, WishlistPageElements.NO_PRODUCTS_IN_WISHLIST_ALERT))
        )
        alert.is_displayed()

    def search_for_wishlist(self, wishlist_name):
        """
        :return: returns True if the wishlist is in the list, otherwise returns False
        """
        wishlists = self.driver.find_elements_by_xpath(WishlistPageElements.WISHLIST_NAMES)
        for wishlist in wishlists:
            if wishlist_name in wishlist.text.strip():
                return True
        return False

