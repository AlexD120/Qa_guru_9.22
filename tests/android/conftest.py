import allure
import pytest
import allure_commons
from appium.options.android import UiAutomator2Options
from selene import browser, support
import os
from appium import webdriver
import config
from qa_guru_922 import utils


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities(
        {
            # 'platformVersion': '9.0',
            'deviceName': 'Pixel_3a',
            # 'udid': 'emulator-5554',
            'appWaitActivity': 'org.wikipedia.*',

            'app': '/Users/aliya/PycharmProjects/Qa_guru_9.22/org.wikipedia-50466.apk'
        }
    )

    # browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    # browser.config.driver_options = options

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://127.0.0.1:4723/wd/hub', options=options
        )

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG,
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML,
    )

    # session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

