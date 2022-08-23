from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager
from webdriver_manager.firefox import GeckoDriverManager


class WebDriverFactory():

    def __init__(self, browser):
        self.browser = browser

    def get_webdriver_instance(self):
        baseURL = "https://courses.letskodeit.com/"
        if self.browser == 'chrome':
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        elif self.browser == 'iexplorer':
            driver = webdriver.Ie(executable_path=IEDriverManager().install())
        elif self.browser == 'firefox':
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        else:
            driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.implicitly_wait(7)
        driver.maximize_window()
        driver.get(baseURL)
        return driver
