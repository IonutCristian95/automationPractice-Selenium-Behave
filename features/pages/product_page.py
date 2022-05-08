from features.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ProductPageElements(object):
    ERROR_NULL_QUANTITY = '//p[@class="fancybox-error" and contains(text(), "Null quantity")]'
    INPUT_QUANTITY = '//input[@id="quantity_wanted"]'
    BUTTON_DECREASE_QUANTITY = '//p[@id="quantity_wanted_p"]//ancestor::a[contains(@class, "quantity_down")]'
    BUTTON_INCREASE_QUANTITY = '//p[@id="quantity_wanted_p"]//ancestor::a[contains(@class, "quantity_up")]'
    SELECT_SIZE = '//select[@id="group_1"]'
    LIST_PRODUCT_COLOR = '//ul[@id="color_to_pick_list"]//li'
    BUTTON_ADD_TO_CART = '//span[contains(., "Add to cart")]//parent::button'
    BUTTON_ADD_TO_WISHLIST = '//a[@id="wishlist_button"]'
    ADDED_TO_WISHLIST_ALERT = '//p[@class="fancybox-error" and contains(text(), "Added to your wishlist")]'


class ProductPage(Browser):
    def increase_product_quantity(self):
        increase_quantity_btn = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, ProductPageElements.BUTTON_INCREASE_QUANTITY))
        )
        increase_quantity_btn.click()

    def decrease_product_quantity(self):
        decrease_quantity_btn = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, ProductPageElements.BUTTON_DECREASE_QUANTITY))
        )
        decrease_quantity_btn.click()

    def insert_desired_quantity(self, quantity):
        input_quantity = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, ProductPageElements.INPUT_QUANTITY))
        )
        input_quantity.clear()
        input_quantity.send_keys(quantity)

    def select_size(self, size):
        option = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, ProductPageElements.SELECT_SIZE +
                                            f'//option[contains(text(), "{size}")]'))
        )
        option.click()

    def select_color(self, option_number):
        color = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, ProductPageElements.LIST_PRODUCT_COLOR +
                                            f'[{option_number}]//a'))
        )
        color.click()

    def add_to_cart(self):
        add_to_cart_btn = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, ProductPageElements.BUTTON_ADD_TO_CART))
        )
        add_to_cart_btn.click()

    def add_to_wishlist(self):
        add_to_wishlist_btn = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, ProductPageElements.BUTTON_ADD_TO_WISHLIST))
        )
        add_to_wishlist_btn.click()

    def displayed_null_quantity_alert(self):
        self.driver.switch_to().alert().accept()

    def added_to_wishlist_alert(self):
        alert = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, ProductPageElements.ADDED_TO_WISHLIST_ALERT))
        )
        alert.is_displayed()
