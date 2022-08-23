import pytest
import unittest
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self):
        self.ts = TestStatus(self.driver)
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.lp.login("levprotivlvov@gmail.com", "letskodeit")
        result1 = self.lp.verify_login_title()
        self.test_status.mark(result1, result_message="Title Verified")
        result2 = LoginPage(driver=self.driver).verify_success_login()
        self.ts.mark_final("test_valid_login", result2, "Login was successful")

    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        LoginPage(driver=self.driver).logout()
        LoginPage(driver=self.driver).login("levprotivlvov@gmail.com", "letskodeit22212121")
        result = self.lp.verify_login_failed()
        assert result == True
