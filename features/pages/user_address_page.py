from features.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UserAddressPageElements(object):
    INPUT_FIRST_NAME = '//input[@id="firstname"]'
    INPUT_LAST_NAME = '//input[@id="lastname"]'
    INPUT_COMPANY = '//input[@id="company"]'
    INPUT_ADDRESS_LINE_1 = '//input[@id="address1"]'
    INPUT_ADDRESS_LINE_2 = '//input[@id="address2"]'
    INPUT_CITY = '//input[@id="city"]'
    INPUT_LIST_STATE = '//select[@id="id_state"]'
    INPUT_ZIPCODE = '//input[@id="postcode"]'  # 5 characters
    INPUT_COUNTRY = '//select[@id="id_country"]//option'  # There is only one option - United States
    INPUT_HOME_PHONE = '//input[@id="phone"]'
    INPUT_MOBILE_PHONE = '//input[@id="phone_mobile"]'
    INPUT_TEXTAREA_ADDITIONAL_INFORMATION = '//textarea[@id="other"]'
    INPUT_ADDRESS_ALIAS = '//input[@id="alias"]'
    BUTTON_SAVE_ADDRESS = '//button[@id="submitAddress"]'


class UserAddressPage(Browser):
    def navigate_to_address_page(self):
        self.driver.get('http://automationpractice.com/index.php?controller=address')

    def insert_first_name(self, first_name):
        input_first_name = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_FIRST_NAME))
        )
        input_first_name.clear()
        input_first_name.send_keys(first_name)

    def insert_last_name(self, last_name):
        input_last_name = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_LAST_NAME))
        )
        input_last_name.clear()
        input_last_name.send_keys(last_name)

    def insert_company(self, company):
        input_company = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_COMPANY))
        )
        input_company.clear()
        input_company.send_keys(company)

    def insert_address_line_1(self, address):
        input_address = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_ADDRESS_LINE_1))
        )
        input_address.clear()
        input_address.send_keys(address)

    def insert_address_line_2(self, address):
        input_address = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_ADDRESS_LINE_2))
        )
        input_address.clear()
        input_address.send_keys(address)

    def insert_city(self, city):
        input_city = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_CITY))
        )
        input_city.clear()
        input_city.send_keys(city)

    def choose_state(self, state_name):
        state_list = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_LIST_STATE+f"//option[contains("
                                                                                               f"text(), "
                                                                                               f"\"{state_name}\")]"))
        )
        state_list.click()

    def insert_zipcode(self, zipcode):
        """
        :param zipcode: 5 characters needed
        :return:
        """
        input_zipcode = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_ZIPCODE))
        )
        input_zipcode.clear()
        input_zipcode.send_keys(zipcode)

    def insert_country(self):
        """
        The only option in this list is the US
        """
        country_list = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_COUNTRY))
        )
        country_list.click()

    def insert_home_phone(self, home_phone):
        input_phone = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_HOME_PHONE))
        )
        input_phone.clear()
        input_phone.send_keys(home_phone)

    def insert_mobile_phone(self, mobile_phone):
        input_phone = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_MOBILE_PHONE))
        )
        input_phone.clear()
        input_phone.send_keys(mobile_phone)

    def insert_additional_info(self, info):
        insert_info = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_TEXTAREA_ADDITIONAL_INFORMATION))
        )
        insert_info.clear()
        insert_info.send_keys(info)

    def insert_address_alias(self, alias):
        insert_alias = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressPageElements.INPUT_ADDRESS_ALIAS))
        )
        insert_alias.clear()
        insert_alias.send_keys(alias)
