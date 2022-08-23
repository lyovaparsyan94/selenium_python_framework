import logging
import time

import utilities.custom_logger as cl
from base.basepage import BasePage


class RegisterCoursesPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super(RegisterCoursesPage, self).__init__(driver)
        self.driver = driver

    ##############
    ## Locators ##
    ##############

    _search_box = ".input-group>input"  # id
    _search_course_icon = ".input-group>button"
    _course = "//h4[contains(text(),'{course_name}')]"
    _all_courses = "course-list"
    _enroll_button = '//*[@id="zen_cs_desc_with_promo_dynamic"]/div//button'
    _cc_num = "//input[contains(@autocomplete, 'cc-number') and contains(@placeholder, 'Card Number')]"
    _cc_exp = "//input[contains(@autocomplete, 'cc-exp') and contains(@name, 'exp-date')]"
    _cc_cvc = "//input[contains(@autocomplete, 'cc-csc') and contains(@name, 'cvc')]"
    _submit_enroll = "//button[contains(@class, 'zen-subscribe sp-buy btn btn-default btn-lg btn-block btn-gtw btn-submit checkout-button dynamic-button') and contains(@type, 'button')]"
    _enroll_error_message = '//*[@id="checkout-form"]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/ul/li/span'

    ##########################
    ## Element Interactions ##
    ##########################

    def enter_course_name(self, name):
        self.send_keys_to_clicker(data=name, locator=self._search_box, locatorType="css")
        self.element_click(self._search_course_icon, locatorType="css")

    def select_course_to_enroll(self, full_course_name):
        course_name = self._course.format(course_name=full_course_name)
        self.element_click(locator=course_name, locatorType="xpath")

    def click_on_enroll_button(self):
        self.element_click(locator=self._enroll_button, locatorType="xpath")

    def enter_card_number(self, num):
        # self.switch_to_some_frame(index=0) # not generic, primitive variant
        self.switch_frame_by_index(self._cc_num, locatorType="xpath")
        self.send_keys_to_clicker(num, locator=self._cc_num, locatorType="xpath")
        self.switch_to_default_content()

    def enter_card_exp(self, exp):
        self.switch_to_some_frame(index=1)
        # self.switch_frame_by_index(self._cc_exp, locatorType="xpath")
        self.send_keys_to_clicker(exp, locator=self._cc_exp, locatorType="xpath")
        self.switch_to_default_content()

    def enter_card_cvc(self, cvc):
        self.switch_to_some_frame(index=2)
        # self.switch_frame_by_index(self._cc_cvc, locatorType="xpath")
        self.send_keys_to_clicker(data=cvc, locator=self._cc_cvc, locatorType="xpath")
        self.switch_to_default_content()

    def click_on_enroll_submit_button(self):
        self.element_click(self._submit_enroll, locatorType="xpath")

    def enter_credit_card_information(self, num, exp, cvc):
        self.enter_card_number(num)
        self.enter_card_exp(exp)
        self.enter_card_cvc(cvc)

    def enroll_course(self, num="", exp="", cvc=""):
        self.click_on_enroll_button()
        time.sleep(2)
        self.scroll_browser(direction="down")
        self.enter_credit_card_information(num, exp, cvc)
        time.sleep(1)
        self.click_on_enroll_submit_button()

    def verify_enroll_failed(self):
        result = self.is_enabled(locator=self._submit_enroll, locatorType="xpath", info="Enroll Button")
        return not result
