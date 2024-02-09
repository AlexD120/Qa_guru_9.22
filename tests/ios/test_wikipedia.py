from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared.jquery_style import s, ss


def test_search():
    with step('Type search'):
        s((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        s((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')
    with step('Verify content found'):
        results = ss((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))
