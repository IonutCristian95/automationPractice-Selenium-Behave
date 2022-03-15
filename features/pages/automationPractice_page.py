from time import sleep

from features.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutomationPracticeElements(object):
    MY_STORE_LOGO = '//div[@id="header_logo"]//a'
    SEARCH_BAR = '//form//input[@placeholder="Search"]'
    BUTTON_SEARCH_BAR = '//form[@id="searchbox"]//button'
    ADD_TO_WISHLIST_BUTTON = '(//a[contains(text(),"Add to Wishlist")])[1]'
    ADD_TO_COMPARE_BUTTON = '(//a[contains(text(),"Add to Compare")])[1]'
    LAYER_CART_CONTINUE_SHOPPING_BUTTON = '//span//following-sibling::*[contains(. ,"Continue")]'
    LAYER_CART_PROCEED_TO_CHECKOUT_BUTTON = '//a//span[contains(. , "Proceed to checkout")]'
    LAYER_CART_CLOSE = '//span[@title="Close window"]'
    CART_VIEW_BUTTON = '//a[@title="View my shopping cart"]'
    SIGN_IN_BUTTON = '//a[@class="login" and contains(text(), "Sign in")]'
    SIGN_OUT_BUTTON = '//a[@class="logout" and @title="Log me out"]'
    ACCOUNT_MANAGEMENT_BUTTON = '//a[@class="account"]'
    ADDED_TO_WISHLIST_POPUP = '//p[contains(text(), "Added to your wishlist")]'
    NEWSLETTER_INPUT_BOX = '//input[@id="newsletter-input"]'
    NEWSLETTER_BUTTON = '//input[@id="newsletter-input"]//following-sibling::button[@name="submitNewsletter"]'
    NEWSLETTER_CONFIRMATION = '//p[contains(text(), "You have successfully subscribed to this newsletter")]'
    NEWSLETTER_ALREADY_SUBSCRIBED_ALERT = '//p[contains(@class, "alert-danger") and contains(., "email address is ' \
                                          'already registered")] '
    NEWSLETTER_INVALID_EMAIL_ALERT = '//p[contains(text(), "Invalid email address.")]'


class AutomationPracticePage(Browser):
    def navigate_to_automationPractice_main_page(self):
        self.driver.get('http://automationpractice.com/index.php')

    def get_page_title(self):
        return self.driver.title

    # The "product" parameter is the product number in the list : integer
    def add_to_cart(self, product):
        add_to_cart_button = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, f'(//*[@id="homefeatured"]//li)[{product}]//ancestor::a['
                                                      f'@title="Add to cart"]'))
        )
        self.driver.execute_script("arguments[0].click();", add_to_cart_button)

    # Proceed to checkout after adding a product in cart
    def proceed_to_checkout(self):
        proceed_button = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.LAYER_CART_PROCEED_TO_CHECKOUT_BUTTON))
        )
        proceed_button.click()

    def click_continue_shopping_btn_layer_cart(self):
        continue_btn = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.LAYER_CART_CONTINUE_SHOPPING_BUTTON))
        )
        continue_btn.click()

    def click_view_cart_button(self):
        cart_btn = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.CART_VIEW_BUTTON))
        )
        cart_btn.click()

    def close_layer_cart(self):
        close_btn = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.LAYER_CART_CLOSE))
        )
        close_btn.click()

    def is_user_already_logged_in(self):
        sign_out_btn_present = self.driver.find_elements_by_xpath(AutomationPracticeElements.SIGN_OUT_BUTTON)
        if sign_out_btn_present[0]:
            assert True
        else:
            assert False

    def click_sign_in_button(self):
        sign_in_btn = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.SIGN_IN_BUTTON))
        )
        sign_in_btn.click()

    def click_account_management_button(self):
        account_btn = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.ACCOUNT_MANAGEMENT_BUTTON))
        )
        account_btn.click()

    def insert_email_newsletter(self, email):
        newsletter_input_box = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.NEWSLETTER_INPUT_BOX))
        )
        newsletter_input_box.clear()
        newsletter_input_box.send_keys(email)

    def click_subscribe_newsletter_button(self):
        self.driver.find_element_by_xpath(AutomationPracticeElements.NEWSLETTER_BUTTON).click()

    def newsletter_confirmation_message(self):
        confirmation_message_alert = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.NEWSLETTER_CONFIRMATION))
        )
        assert confirmation_message_alert.is_displayed()

    def newsletter_already_subscribed_alert(self):
        confirmation_message_alert = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.NEWSLETTER_ALREADY_SUBSCRIBED_ALERT))
        )
        assert confirmation_message_alert.is_displayed()

    def newsletter_invalid_email_error(self):
        invalid_email_message = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.NEWSLETTER_INVALID_EMAIL_ALERT))
        )
        assert invalid_email_message.is_displayed()

    def user_logged_out(self):
        """
        This function will disconnect the user if he is logged in
        """
        sign_out_btn = self.driver.find_elements_by_xpath(AutomationPracticeElements.SIGN_OUT_BUTTON)
        if len(sign_out_btn) > 0:
            sign_out_btn[0].click()
        # if sign_out_btn:
        #     sign_out_btn.click()

    def logged_in_facilities_present(self):
        """
            The log out button and account management button confirm that the user is logged in
        """
        account_management_btn = WebDriverWait(self.driver, 3000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.ACCOUNT_MANAGEMENT_BUTTON))
        )
        log_out_btn = WebDriverWait(self.driver, 3000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.SIGN_OUT_BUTTON))
        )
        if account_management_btn and log_out_btn:
            assert True
        else:
            assert False
