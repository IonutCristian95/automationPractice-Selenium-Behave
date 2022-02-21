from features.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SearchPageElements(object):
    SEARCH_BAR = '//form//input[@placeholder="Search"]'
    BUTTON_SEARCH_BAR = '//form[@id="searchbox"]//button'
    ALERT_NO_RESULTS = '//p[contains(text(), "No results")]'
    ALERT_EMPTY_SEARCH_INPUT = '//p[contains(text(), "Please enter a search keyword")]'
    NUMBER_OF_RETURNED_RESULTS = '//span[@class="heading-counter"]'


class SearchPage(Browser):
    def navigate_to_search_page(self):
        self.driver.get('http://automationpractice.com/index.php?controller=search')

    def check_search_page_title(self):
        if self.driver.title.find("Search") != -1:
            assert True
        else:
            assert False

    # The "product" parameter is the name of the product : string
    def search_bar_insert(self, product):
        search_bar = WebDriverWait(self.driver, 5000).until(
            EC.presence_of_element_located((By.XPATH, SearchPageElements.SEARCH_BAR))
        )
        search_bar.send_keys(product)

    def click_search_bar_button(self):
        self.driver.find_element_by_xpath(SearchPageElements.BUTTON_SEARCH_BAR).click()

    def results_alert_displayed(self):
        # Search for a warning that no results have been found
        alerts_list = self.driver.find_elements_by_xpath(SearchPageElements.ALERT_NO_RESULTS)
        if len(alerts_list) == 1:
            assert True
        else:
            assert False

    def returned_results_counter(self):
        results_counter_span = self.driver.find_elements_by_xpath(
            SearchPageElements.NUMBER_OF_RETURNED_RESULTS)
        results_counter_int = int((results_counter_span[0].text.strip().split(" "))[0])
        # Check for the presence of the span containing the results counter and
        # the results counter is a number bigger than 0
        if len(results_counter_span) == 1 and results_counter_int > 0:
            assert True
        else:
            assert False
