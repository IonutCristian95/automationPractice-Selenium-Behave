from selenium.common.exceptions import NoSuchElementException

from features.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutomationPracticeElements(object):
    MY_STORE_LOGO = '*//div[@id="header_logo"]//a'
    SEARCH_BAR = '*//form//input[@placeholder="Search"]'
    BUTTON_SEARCH_BAR = '*//form[@id="searchbox"]//button'
    ADD_TO_WISHLIST_BUTTON = '(*//a[contains(text(),"Wishlist")])[1]'
    ADD_TO_COMPARE_BUTTON = '(*//a[contains(text(),"Compare")])[1]'
    ALERT_NO_RESULTS = '*//p[contains(text(), "No results")]'


class AutomationPracticePage(Browser):
    def navigate_to_automationPractice_main_page(self):
        self.driver.get('http://automationpractice.com/index.php')

    def get_page_title(self):
        return self.driver.title

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
        alerts_list = self.driver.find_elements_by_xpath(AutomationPracticeElements.ALERT_NO_RESULTS)
        if len(alerts_list) != 0:
            return True
        else:
            return False
