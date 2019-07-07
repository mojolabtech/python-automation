from behave import given, when, then
from selenium.webdriver.common.by import By


SEARCH_FIELD = (By.NAME, 'search')
SEARCH_BUTTON = (By.CSS_SELECTOR, 'span.input-group-btn')
RESULT_HEADER = (By.CSS_SELECTOR, 'div#content > h1')


@given('Open store page')
def open_base_url(context):
    context.driver.get('http://test.mojolab.tech/')

@when("Enter search word 'phone'")
def enter_search_word(context):
    search_field = context.driver.find_element(*SEARCH_FIELD)
    search_field.send_keys('phone')

@when('Click search button')
def click_search_btn(context):
    context.driver.find_element(*SEARCH_BUTTON).click()

@then("Verify search results contain 'phone'")
def verify_search_results(context):
    search_word = 'phone'
    content_header = context.driver.find_element(*RESULT_HEADER)
    assert content_header.text == f'Search - {search_word}', \
        f"Expected text 'Search - {search_word}', but got {content_header.text}"