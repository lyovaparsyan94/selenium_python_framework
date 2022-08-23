import logging
from pages.home.navigation_page import NavigationPage
from time import sleep
import utilities.custom_logger as cl
from base.basepage import BasePage


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "SIGN IN"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//input[@value='Login']"

    def click_login_link(self):
        self.element_click(locator=self._login_link, locatorType="link")

    def enter_email(self, email):
        self.send_keys_to_clicker(email, self._email_field)

    def enter_password(self, password):
        self.send_keys_to_clicker(password, self._password_field)

    def click_button(self):
        self.element_click(self._login_button, locatorType="xpath")

    def login(self, email='', password=''):
        self.click_login_link()
        sleep(5)
        self.clear_all_fields()
        self.enter_email(email=email)
        self.enter_password(password=password)
        self.click_button()

    def verify_success_login(self):
        result = self.is_element_present(locator='//*[@id="dropdownMenu1"]', locatorType="xpath")
        return result

    def verify_login_failed(self):
        result = self.is_element_present(
            locator="//span[contains(text(), 'Your username or password is invalid. Please try again.')]",
            locatorType="xpath")
        return result

    def clear_all_fields(self):
        email_field = self.get_element(locator=self._email_field)
        email_field.clear()
        password_field = self.get_element(locator=self._password_field)
        password_field.clear()

    def verify_login_title(self):
        return self.verify_page_title("My Courses")

    def logout(self):
        self.nav.navigate_to_user_settings()
        logout_link = self.wait_for_element(locator="//a[contains(text(),'Logout')]", locatorType="xpath", pollFrequency=1)
        self.element_click(element=logout_link)
