from selenium import webdriver


class Browser(object):
    driver = webdriver.Chrome(executable_path="C:\\chromedriver100.exe")
    driver.implicitly_wait(30)
    driver.set_page_load_timeout(30)
    driver.maximize_window()

    def close(self):
        self.driver.close()
