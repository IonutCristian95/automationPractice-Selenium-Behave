from features.browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class WishlistPageElements(object):
    NEW_WISHLIST_NAME = '//input[@id="name"]'
    NEW_WISHLIST_SAVE = '//button[@id="submitWishlist"]'
    NO_PRODUCTS_IN_WISHLIST_ALERT = '//div[@id="block-order-detail"]//p[contains(text(), "No products")]'
    BUTTON_BACK_TO_USER_ACCOUNT = '//span[contains(., "Back to Your Account")]//parent::a'
    BUTTON_HOME = '//span[contains(., "Home")]//parent::a'


class WishlistPage(Browser):
    def navigate_to_wishlist_page(self):
        self.driver.get("http://automationpractice.com/index.php?fc=module&module=blockwishlist&controller=mywishlist")

    def view_wishlist(self, wishlist_position):
        """
        :param wishlist_position: This parameter is the position of the wishlist counting from top
        """
        wishlist = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, f'(//tbody//tr)[{wishlist_position}]//ancestor::a[contains(., "View")]'))
        )
        wishlist.click()

    def delete_wishlist(self, wishlist_position):
        """
        :param wishlist_position: This parameter is the position of the wishlist counting from top
        """
        wishlist = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(
                (By.XPATH, f'(//tbody//tr)[{wishlist_position}]//td[@class="wishlist_delete"]//a'))
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
        self.driver.switch_to().alert().accept()

