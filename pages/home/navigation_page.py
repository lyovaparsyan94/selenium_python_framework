import logging
from time import sleep
import utilities.custom_logger as cl
from base.basepage import BasePage


class NavigationPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver = driver

    # Locators
    _my_courses = "MY COURSES"
    _all_courses = "ALL COURSES"
    _practice = "Practice" # Not found on current version of page
    _user_settings_icon = '//*[@id="dropdownMenu1"]'

    def navigate_to_all_courses(self):
        self.element_click(locator=self._all_courses, locatorType="link")

    def navigate_to_my_courses(self):
        self.element_click(locator=self._my_courses, locatorType="link")

    def navigate_to_practice(self):
        self.element_click(locator=self._practice, locatorType="link")

    def navigate_to_user_settings(self):
        user_settings_element = self.wait_for_element(locator=self._user_settings_icon, locatorType="xpath", pollFrequency=1)
        self.element_click(user_settings_element)

