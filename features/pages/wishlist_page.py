from features.browser import Browser
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class WishlistPageElements(object):
    NEW_WISHLIST_NAME = '//input[@id="name"]'
    NEW_WISHLIST_SAVE = '//button[@id="submitWishlist"]'
    WISHLIST = '(//tbody//tr)'
    # wishlist_view = (//tbody//tr)[1]//td[5]//a[contains(.,"View")]
    # wishlist_delete = (//tbody//tr)[1]//td[6]//a
    NO_PRODUCTS_IN_WISHLIST_ALERT = '//div[@id="block-order-detail"]//p[contains(text(), "No products")]'
    BACK_TO_USER_ACC_BTN = '//span[contains(., "Back to Your Account")]//parent::a'
    HOME_BTN = '//span[contains(., "Home")]//parent::a'



class WishlistPage(Browser):
    def navigate_to_wishlist_page(self):
        self.driver.get("http://automationpractice.com/index.php?fc=module&module=blockwishlist&controller=mywishlist")



