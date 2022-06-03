import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

s = Service("/home/natasha/PycharmProjects/Stepik_Python/Automation_testing/TEST-project/chromedriver")


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(service=s, options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()



