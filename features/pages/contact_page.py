from features.browser import Browser


class ContactPageElements(object):
    SUBJECT_HEADING_LIST = '//select[@id="id_contact"]//option'
    EMAIL_ADDRESS_INPUT = '//input[@id="email"]'
    ORDER_REFERENCE_LIST = '//select[@name="id_order"]//option'
    ATTACH_FILE_INPUT = '//input[@id="fileUpload"]'
    MESSAGE_INPUT = '//textarea[@id="message"]'
    SEND_MESSAGE_BUTTON = '//button[@id="submitMessage"]'
    BLANK_MESSAGE_ERROR = '//div[contains(@class, "alert alert-danger")]' \
                          '//ancestor::li[contains(., "The message cannot be blank")]'
    NO_SUBJECT_HEADING_ERROR = '//div[contains(@class, "alert alert-danger")]' \
                               '//ancestor::li[contains(., "Please select a subject from the list provided")]'


class ContactPage(Browser):
    def navigate_to_contact_page(self):
        self.driver.get("http://automationpractice.com/index.php?controller=contact")



