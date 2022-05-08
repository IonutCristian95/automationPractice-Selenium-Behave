from features.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class CartPageElements(object):
    INCREASE_QUANTITY_BUTTON = '//a[@title="Add"]'
    DECREASE_QUANTITY_BUTTON = '//a[@title="Subtract"]'
    DELETE_PRODUCT_BUTTON = '//a[@title="Delete"]'
    ALERT_EMPTY_SHOPPING_CART = '//p[text()="Your shopping cart is empty."]'
    PRICE_REDUCTION = '//span[@class="price-percent-reduction small"]'
    PRODUCT_IN_CART = '(//tbody//tr)'
    PROCEED_TO_CHECKOUT = '//p[contains(@class, "cart_navigation")]//a[@title="Proceed to checkout"]'
    PROCESS_ADDRESS_BUTTON = '//button[@name="processAddress"]'
    PROCESS_CARRIER_BUTTON = '//button[@name="processCarrier"]'
    TERMS_OF_SERVICE_CHECKBOX = '//input[@id="cgv"]'
    PAYMENT_METHOD_BANKWIRE = '//a[@class="bankwire"]'
    PAYMENT_METHOD_CHEQUE = '//a[@class="cheque"]'
    CONFIRM_ORDER_BUTTON = '//span[contains(., "I confirm my order")]//parent::button'
    ORDER_CONFIRMATION = '//div[@class="box"]//ancestor::*[contains(text(), "complete") and contains(text(), "order")]'
    ALERT_TERMS_OF_SERVICE = '//*[@class="fancybox-error" and contains(. , "must agree to the terms of service")]'
    ALERT_TERMS_OF_SERVICE_CLOSE_BUTTON = '//a[@title="Close"]'
    BANKWIRE_PAYMENT_CONFIRMED = '//h3[@class="page-subheading" and contains(text(),"Bank-wire payment.")]'
    CHEQUE_PAYMENT_CONFIRMED = '//h3[@class="page-subheading" and contains(text(),"Check payment")]'


class CartPage(Browser):
    def navigate_to_checkout_cart_page(self):
        self.driver.get('http://automationpractice.com/index.php?controller=order')

    # The specific_product parameter is the position of the product in the cart
    def increase_quantity_of_a_specific_product(self, specific_product):
        self.driver.find_element_by_xpath(CartPageElements.PRODUCT_IN_CART + f'[{specific_product}]' +
                                          CartPageElements.INCREASE_QUANTITY_BUTTON).click()

    # The specific_product parameter is the position of the product in the cart
    def decrease_quantity_of_a_specific_product(self, specific_product):
        self.driver.find_element_by_xpath(CartPageElements.PRODUCT_IN_CART + f'[{specific_product}]' +
                                          CartPageElements.DECREASE_QUANTITY_BUTTON).click()

    def delete_a_specific_product(self, specific_product):
        self.driver.find_element_by_xpath(CartPageElements.PRODUCT_IN_CART + f'[{specific_product}]' +
                                          CartPageElements.DELETE_PRODUCT_BUTTON).click()

    def is_alert_active_empty_cart(self):
        alert_element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, CartPageElements.ALERT_EMPTY_SHOPPING_CART))
        )
        assert alert_element.is_displayed()

    def proceed_to_checkout_button(self):
        proceed_to_checkout_btn = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, CartPageElements.PROCEED_TO_CHECKOUT))
        )
        proceed_to_checkout_btn.click()

    def procees_address(self):
        process_address_btn = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, CartPageElements.PROCESS_ADDRESS_BUTTON))
        )
        process_address_btn.click()

    def procees_carrier(self):
        process_carrier_btn = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, CartPageElements.PROCESS_CARRIER_BUTTON))
        )
        process_carrier_btn.click()

    def accept_terms_of_service(self):
        checkbox = self.driver.find_element_by_xpath(CartPageElements.TERMS_OF_SERVICE_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()

    def select_payment_method(self, payment_method: str):
        """
        :param payment_method: "bankwire" or "cheque"
        If the parameter isn't one of the options above, it will assert False
        Select one of the payment methods to proceed.
        """
        if payment_method.lower() == "bankwire":
            payment_method_btn = WebDriverWait(self.driver, 5000).until(
                EC.presence_of_element_located((By.XPATH, CartPageElements.PAYMENT_METHOD_BANKWIRE))
            )
        elif payment_method.lower() == "cheque":
            payment_method_btn = WebDriverWait(self.driver, 5000).until(
                EC.presence_of_element_located((By.XPATH, CartPageElements.PAYMENT_METHOD_CHEQUE))
            )
        else:
            assert False
        payment_method_btn.click()

    def payment_method_confirmation_message(self, payment_method: str):
        """
        :param payment_method: "bankwire" or "cheque"
        Will check for the confirmation message if it is for bankwire or cheque
        Will assert False if the parameter provided is not one of the two options or
        if the confirmation message with the payment method provided is not found
        :return:
        """
        if payment_method.lower() == "bankwire":
            payment_confirmation = self.driver.find_elements_by_xpath(CartPageElements.BANKWIRE_PAYMENT_CONFIRMED)
        elif payment_method.lower() == "cheque":
            payment_confirmation = self.driver.find_elements_by_xpath(CartPageElements.CHEQUE_PAYMENT_CONFIRMED)
        else:
            assert False

        if payment_confirmation[0]:
            assert True
        else:
            assert False

    def delete_products_in_cart(self):
        products_delete_btn_list = self.driver.find_elements_by_xpath(CartPageElements.DELETE_PRODUCT_BUTTON)
        for product in products_delete_btn_list:
            try:
                product.click()
            except Exception as e:
                print(e)
                return
            sleep(3)

    def click_confirm_order_btn(self):
        confirm_btn = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, CartPageElements.CONFIRM_ORDER_BUTTON))
        )
        confirm_btn.click()

    def check_for_price_reduction(self):
        promotion = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, CartPageElements.PRICE_REDUCTION))
        )

        if promotion.is_displayed():
            assert True
        else:
            assert False
