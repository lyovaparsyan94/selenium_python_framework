import os
import time
import logging
from traceback import print_stack
import utilities.custom_logger as cl
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumDriver:
    log = cl.customLogger(logging.DEBUG)

    def screenshot(self, result_message):
        """Takes screenshot of the current open web page"""
        filename = result_message + "." + str(round(time.time() * 1000)) + ".png"
        screenshot_directory = "../screenshots/"
        relative_file_name = screenshot_directory + filename
        current_dir = os.path.dirname(__file__)
        destination_file = os.path.join(current_dir, relative_file_name)
        destination_directory = os.path.join(current_dir, screenshot_directory)

        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info(f"relative_file_name={relative_file_name}, current_dir={current_dir},"
                          f"destination_file={destination_file}, destination_directory={destination_directory}")
            self.log.info(f"screenshot saved to directory: {destination_file}")
        except:
            self.log.error(f"### Exeption Occured")
            print_stack()

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def get_element(self, locator, locatorType="id"):
        element = None
        try:
            byType = self.get_by_type(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info(f"Element Found with Locator {locator} and locatorType {locatorType}")
        except:
            self.log.info(f"Element not found with Locator {locator} and locatorType {locatorType}")
        return element

    def get_element_list(self, locator, locatorType="id"):
        """ Get list of elements"""
        element = None
        try:
            byType = self.get_by_type(locatorType)
            element = self.driver.find_elements(byType, locator)
            self.log.info(f"Element list found with Locator {locator} and locatorType {locatorType}")
        except:
            self.log.info(f"Element list not found with Locator {locator} and locatorType {locatorType}")
        return element

    def element_click(self, locator="", locatorType="id", element=None):
        try:
            if locator: # if locator is not empty
                element = self.get_element(locator, locatorType)
            element.click()
            self.log.info(f"CLicked on the element with locator {locator}, locatorType {locatorType}")
        except Exception as e:
            self.log.info(f"Cannot click on the element with locator {locator}, locatorType {locatorType}")
            print(print_stack())

    def send_keys_to_clicker(self, data, locator="", locatorType="id", element=None):
        """ Send keys to an element """
        try:
            element = self.get_element(locator, locatorType)
            element.send_keys(data)
            self.log.info(f"Sent {data} data to element with locator {locator}, locatorType {locatorType}")
        except:
            self.log.info(f"Cannot send {data} data to the element with locator {locator}, locatorType {locatorType}")
            # print(print_stack())
            print(locator, locatorType, 55555555)

    def get_text(self, locator="", locatorType="id", element=None, info=""):
        """Get the text of an element"""
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.get_element(locator, locatorType)
            self.log.info("Before finding text")
            text = element.text
            self.log.info(f"After finding element, size is {str(len(text))}")
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info(f"Getting text on element :: {info}")
                self.log.info(f"The text is :: {text}")
                text = text.strip()
        except:
            self.log.error(f"Failed to get text on element :: {info}")
            print_stack()
            text = None
        return text

    def is_element_present(self, locator="", locatorType="id", element=None):
        """Check if element is present"""
        try:
            element = self.get_element(locator, locatorType)
            if element is not None:
                self.log.info(f"Element present with locator {locator} and locatorType {locatorType}")
                return True
            else:
                self.log.info(f"Element Not present with locator {locator} and locatorType {locatorType}")
                return False
        except:
            self.log.info("Element not found")
            return False

    def is_element_displayed(self, locator="", locatorType="id", element=None):
        """Check if element is displayed"""
        is_displayed = False
        try:
            if locator:
                element = self.get_element(locator, locatorType)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info(f"Element is displayed with locator {locator} and locatorType {locatorType}")
                return is_displayed
            else:
                self.log.info(f"Element Not displayed with locator {locator} and locatorType {locatorType}")
            return is_displayed
        except:
            self.log.info("Element not found")
            return False

    def element_presense_check(self, locator, byType):
        """Check if element is present"""
        try:
            elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Element Found")
                return True
            else:
                return False
        except:
            self.log.info("Element not found")
            return False

    def wait_for_element(self, locator, locatorType="id",
                         timeout=20, pollFrequency=0.5):
        element = None
        try:
            byType = self.get_by_type(locatorType)
            self.log.info("Waiting for maximum " + str(timeout) + " seconds for element to be visible")
            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            self.log.info("element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def scroll_browser(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -1000);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 1000);")

    def switch_to_some_frame(self, id='', name='', index=None):
        """
        Switch to iframe using element locator inside iframe
        Parameters:
            1. Required:
                None
            2. Optional:
                :param id:
                :param name:
                :param index:
        Returns:
            None
        :Exception
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        elif name:
            self.driver.switch_to.frame(name)
        else:
            self.driver.switch_to.frame(index)

    def switch_frame_by_index(self, locator, locatorType="xpath"):
        """
        Get iframe index using element locator inside iframe

        Parameters:
            1. Required:
                locator   - Locator of the element
            2. Optional:
                locatorType - Locator Type to find the element
        Returns:
            Index of iframe
        Exception:
            None
        """
        result = False
        try:
            iframe_list = self.get_element_list("//iframe", locatorType="xpath")
            self.log.info(f"Length of iframe list is {str(len(iframe_list))}")
            for i in range(len(iframe_list)):
                self.switch_to_some_frame(index=iframe_list[i])
                result = self.is_element_present(locator, locatorType)
                if result:
                    self.log.info(f"iframe index is {str(i)}")
                    break
                self.switch_to_default_content()
                return result
        except:
            print("iFrame index not found")
            return result

    def switch_to_default_content(self):
        """Switch to default content
        :parameter
            -None
        :return
            - None
        :exception
            -None
        """
        self.driver.switch_to.default_content()

    def get_element_attribute_value(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element

        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element

        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.get_element(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def is_enabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.get_element(locator, locatorType=locatorType)
        enabled = False
        try:
            attribute_value = self.get_element_attribute_value(element=element, attribute="disabled")
            if attribute_value is not None:
                enabled = element.is_enabled()
            else:
                value = self.get_element_attribute_value(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled