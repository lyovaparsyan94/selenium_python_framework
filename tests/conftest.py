import time

import pytest
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage


@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser=browser)
    driver = wdf.get_webdriver_instance()
    lp = LoginPage(driver)
    lp.login("levprotivlvov@gmail.com", "letskodeit")
    time.sleep(5)
    driver.get("https://courses.letskodeit.com/courses")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    # driver.quit()
    print("Running one time tearDown")


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")


@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")
