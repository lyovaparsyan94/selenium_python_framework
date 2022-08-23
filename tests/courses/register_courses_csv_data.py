import time
import pytest
import unittest
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By
from pages.home.navigation_page import NavigationPage
from utilities.read_data import get_csv_data
from utilities.teststatus import TestStatus
from pages.courses.register_courses import RegisterCoursesPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt()
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.navigate_to_all_courses()

    @pytest.mark.run(order=1)
    @data(*get_csv_data('/home/lyova/work/selelnium_framework/testdata.csv'))
    @unpack
    def test_invalid_enrollment(self, cours_name, cc_num, cc_exp, cc_cvc):
        self.courses.enter_course_name(cours_name)
        time.sleep(2)
        self.courses.select_course_to_enroll(cours_name)
        time.sleep(2)
        self.courses.enroll_course(cc_num, cc_exp, cc_cvc)
        time.sleep(2)
        result = self.courses.verify_enroll_failed()
        self.ts.mark_final("test_invalid_enrollment", result, "Enrollment Failed Verification")
