import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching chrome browser..............")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="E:\\san_latest_2020\\grid\\geckodriver.exe")
        print("Launching firefox browser................")
    else:
        driver = webdriver.Chrome()
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## Pytest HTML report #################

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Sanjay'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("plugins", None)