"""
@package utilities

CheckPoint class implementation
It provides functionality to assert the result

Example:
    self.check_point.markFinal("Test Name", result, "Message")
"""
import logging
import utilities.custom_logger as cl
from base.seleniumdriver import SeleniumDriver


class TestStatus(SeleniumDriver):
    log = cl.customLogger(logging.INFO)

    def __init__(self, driver):
        """Inits Checkpoint class"""
        super(TestStatus, self).__init__(driver)
        self.resultlist = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.resultlist.append("PASS")
                    self.log.info(f"### VERIFICATION SUCCESSFULL :: + {result_message}")
                else:
                    self.resultlist.append(f"FAIL")
                    self.log.info(f"### VERIFICATION FAILED :: + {result_message}")
                    self.screenshot(result_message)
            else:
                self.resultlist.append("FAIL")
                self.log.error(f"### VERIFICATION FAILED :: + {result_message}")
                self.screenshot(result_message)
        except:
            self.resultlist.append("FAIL")
            self.log.error(f"### Exeption Occured !!! ")
            self.screenshot(result_message)

    def mark(self, result, result_message):
        """mark the result of the verification point in a test case"""
        self.set_result(result, result_message)

    def mark_final(self, testname, result, result_message):
        """
        Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result, result_message)
        if "FAIL" in self.resultlist:
            self.log.error(f"{testname} ### TEST FAILED ")
            self.resultlist.clear()
            assert True == False
        else:
            self.log.info(f"{testname} ### TEST SUCCESSFULL ")
            self.resultlist.clear()
            assert True == True