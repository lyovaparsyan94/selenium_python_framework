import time

import pytest
import unittest
from utilities.teststatus import TestStatus
from pages.courses.register_courses import RegisterCoursesPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalid_enrollment(self):
        self.courses.enter_course_name("JavaScript")
        self.courses.select_course_to_enroll("JavaScript for beginners")
        self.courses.enroll_course(num="123211111111111", exp="1225", cvc=100)
        result = self.courses.verify_enroll_failed()
        self.ts.mark_final("test_invalid_enrollment", result, "Enrollment Failed Verification")
