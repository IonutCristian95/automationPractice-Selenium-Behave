from features.browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class UserAddressesPageElements(object):
    ADD_AN_ADDRESS_BUTTON = '//a[@title="Add an address"]'
    DELETE_ADDRESS_BUTTON = '(//a[@title="Delete"])'
    UPDATE_ADDRESS_BUTTON = '(//a[@title="Update"])'


class UserAddressesPage(Browser):
    def navigate_to_user_address(self):
        self.driver.get('http://automationpractice.com/index.php?controller=addresses')

    def click_add_an_address_button(self):
        add_an_address_button = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressesPageElements.ADD_AN_ADDRESS_BUTTON))
        )
        add_an_address_button.click()

    def click_update_address_button(self, address):
        """
        :param address: represents the address to be updated from the addresses list
        """
        address_to_update = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressesPageElements.UPDATE_ADDRESS_BUTTON+f"[{address}]"))
        )
        address_to_update.click()

    def click_delete_address_button(self, address):
        """
        :param address: represents the address to be deleted from the addresses list
        """
        address_to_delete = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, UserAddressesPageElements.DELETE_ADDRESS_BUTTON + f"[{address}]"))
        )
        address_to_delete.click()
