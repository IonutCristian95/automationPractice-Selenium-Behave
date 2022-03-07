from features.browser import Browser


class OrderHistoryPageElements(object):
    BACK_TO_ACCOUNT_DETAILS_PAGE_BTN = '//span[contains(., "Back to your account")]//parent::a'
    HOME_PAGE_BTN = '//span[contains(., "Home")]//parent::a'
    PLACED_ORDERS_PAYMENTS = '//td[@class="history_method"]'


class OrderHistoryPage(Browser):
    def navigate_to_order_history_page(self):
        self.driver.get('http://automationpractice.com/index.php?controller=history')

    def click_back_to_account_details_btn(self):
        self.driver.find_element_by_xpath(OrderHistoryPageElements.BACK_TO_ACCOUNT_DETAILS_PAGE_BTN).click()

    def click_home_page_btn(self):
        self.driver.find_element_by_xpath(OrderHistoryPageElements.HOME_PAGE_BTN).click()

    def placed_orders_payments(self):
        """
        This function will assert True if both of the payment options are being used in the current orders
        """
        contains_cheque_payment, contains_bankwire_payment = False, False
        payments_list = self.driver.find_elements_by_xpath(OrderHistoryPageElements.PLACED_ORDERS_PAYMENTS)

        for i in range(len(payments_list)):
            if "check" in payments_list[i].text:
                contains_cheque_payment = True
            elif "Bank wire" in payments_list[i].text:
                contains_bankwire_payment = True

        if contains_cheque_payment is True and contains_bankwire_payment is True:
            assert True
        else:
            assert False





