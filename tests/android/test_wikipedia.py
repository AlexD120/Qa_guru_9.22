from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared.jquery_style import s, ss


def test_search_appium():
    with step('Skip wellcome screen'):
        s((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')).click()
    with step('Type search'):
        s((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        s((AppiumBy.ID, "org.wikipedia:id/search_src_text")).type('Appium')
    with step('Verify content found'):
        results = ss((AppiumBy.ID, "org.wikipedia:id/page_list_item_title"))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_search_appleinc():
    with step('Skip wellcome screen'):
        s((AppiumBy.ID, 'org.wikipedia:id/fragment_onboarding_skip_button')).click()
    with step('Type search'):
        s((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        s((AppiumBy.ID, "org.wikipedia:id/search_src_text")).type('Microsoft')
    with step('Verify content found'):
        results = ss((AppiumBy.ID, "org.wikipedia:id/page_list_item_title"))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Microsoft')).click()
        s((AppiumBy.XPATH, '//android.widget.TextView[@text="Microsoft"]')).should(
            have.text('Microsoft')
        )
