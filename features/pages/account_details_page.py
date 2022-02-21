from features.browser import Browser


class AccountDetailsElements(object):
    ORDER_HISTORY = '(//ul[contains(@class, "myaccount")]//li)[1]'
    PERSONAL_INFORMATION = '(//ul[contains(@class, "myaccount")]//li)[4]'
    BACK_TO_ACCOUNT_MAIN_PAGE_BUTTON = '//span[contains(., "Back to your account")]'
    WISHLISTS = '//span[contains(., "wishlists")]//parent::a'
    NEW_WISHLIST_NAME_INPUT = '//input[@id="name"]'
    SAVE_NEW_WISHLIST_BUTTON = '//button[@id="submitWishlist"]'
    WISHLIST_NAME = '//a[contains(., "wishlist_test")]'
    DELETE_WISHLIST = '//a[contains(., "wishlist_test")]//parent::td/parent::tr//td[@class="wishlist_delete"]//a'
    PLACED_ORDERS_PAYMENTS = '//td[@class="history_method"]'

class AccountDetails(Browser):
    def navigate_to_account_details_page(self):
        self.driver.get('http://automationpractice.com/index.php?controller=my-account')

    def confirm_account_details_page_displayed(self):
        """
            This method will assert True if the current page displayed is the one for user's account
            otherwise it will assert False
        """
        assert "controller=my-account" in self.driver.current_url

    def confirm_wishlist_delete(self):
        self.driver.switch_to().alert().accept()

    def view_order_history(self):
        self.driver.find_element_by_xpath(AccountDetailsElements.ORDER_HISTORY).click()

    def placed_orders_payments(self):
        """
        This function will assert True if both of the payment options are being used in the current orders
        """
        contains_cheque_payment, contains_bankwire_payment = False, False
        payments_list = self.driver.find_elements_by_xpath(AccountDetailsElements.PLACED_ORDERS_PAYMENTS)

        for i in range(len(payments_list)):
            if "check" in payments_list[i].text:
                contains_cheque_payment = True
            elif "Bank wire" in payments_list[i].text:
                contains_bankwire_payment = True

        if contains_cheque_payment is True and contains_bankwire_payment is True:
            assert True
        else:
            assert False

