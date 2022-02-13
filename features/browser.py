from selenium import webdriver


class Browser(object):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver98.exe")
    driver.implicitly_wait(15)
    driver.set_page_load_timeout(15)
    driver.maximize_window()

    def close(self):
        self.driver.close()
