import time
import pytest
import unittest
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By
from utilities.teststatus import TestStatus
from pages.courses.register_courses import RegisterCoursesPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt()
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)


    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "123211111111111", "1225", 100),
          ("Complete Test Automation Bundle", "123211111111111", "1225", 100))
    @unpack
    def test_invalid_enrollment(self, cours_name, cc_num, cc_exp, cc_cvc):
        self.courses.enter_course_name(cours_name)
        self.courses.select_course_to_enroll(cours_name)
        self.courses.enroll_course(cc_num, cc_exp, cc_cvc)
        # self.courses.enroll_course(num=5470874098984444, exp=1225, cvc=100)
        # time.sleep(2)
        result = self.courses.verify_enroll_failed()
        self.ts.mark_final("test_invalid_enrollment", result, "Enrollment Failed Verification")
        a = self.driver.find_element(by=By.LINK_TEXT, value="ALL COURSES")
        a.click()