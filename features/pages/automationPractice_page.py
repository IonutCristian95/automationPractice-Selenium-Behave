from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
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
    ALERT_NO_RESULTS = '//p[contains(text(), "No results")]'
    NUMBER_OF_RETURNED_RESULTS = '//span[@class="heading-counter"]'
    LAYER_CART_CONTINUE_SHOPPING_BUTTON = '//span//following-sibling::*[contains(. ,"Continue")]'
    LAYER_CART_PROCEED_TO_CHECKOUT_BUTTON = '//a//span[contains(. , "Proceed to checkout")]'
    LAYER_CART_CLOSE = '//span[@title="Close window"]'
    CART_VIEW_BUTTON = '//a[@title="View my shopping cart"]'
    SIGN_IN_BUTTON = '//a[@class="login" and contains(text(), "Sign in")]'
    SIGN_OUT_BUTTON = '//a[@class="logout" and @title="Log me out"]'
    ACCOUNT_MANAGEMENT_BUTTON = '//a[@class="account"]'

class AutomationPracticePage(Browser):
    def navigate_to_automationPractice_main_page(self):
        self.driver.get('http://automationpractice.com/index.php')

    def get_page_title(self):
        return self.driver.title

    # The "product" parameter is the name of the product : string
    def search_bar_insert(self, product):
        search_bar = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.SEARCH_BAR))
        )
        search_bar.send_keys(product)

    def click_search_bar_button(self):
        self.driver.find_element_by_xpath(AutomationPracticeElements.BUTTON_SEARCH_BAR).click()

    def check_search_page_title(self):
        if self.driver.title.find("Search") != -1:
            assert True
        else:
            assert False

    def results_alert_displayed(self):
        # Search for a warning that no results have been found
        alerts_list = self.driver.find_elements_by_xpath(AutomationPracticeElements.ALERT_NO_RESULTS)
        if len(alerts_list) == 1:
            assert True
        else:
            assert False

    def returned_results_counter(self):
        results_counter_span = self.driver.find_elements_by_xpath(AutomationPracticeElements.NUMBER_OF_RETURNED_RESULTS)
        results_counter_int = int((results_counter_span[0].text.strip().split(" "))[0])
        # Check for the presence of the span containing the results counter and
        # the results counter is a number bigger than 0
        if len(results_counter_span) == 1 and results_counter_int > 0:
            assert True
        else:
            assert False

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
        sign_in_btn = WebDriverWait(self.driver, 7000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.SIGN_IN_BUTTON))
        )
        sign_in_btn.click()

    def click_account_management_button(self):
        account_btn = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, AutomationPracticeElements.ACCOUNT_MANAGEMENT_BUTTON))
        )
        account_btn.click()