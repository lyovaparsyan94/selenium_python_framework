import unittest

from tests.home.login_tests import LoginTests
from tests.courses.register_courses_csv_data import RegisterCoursesCSVDataTests

# Get all tests from all tets classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesCSVDataTests)

# Create a test suite combining from all test classes
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)