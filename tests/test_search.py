from selenium import webdriver
from selenium.webdriver.common.by import By

SEARCH_FIELD = (By.NAME, 'search')
SEARCH_BUTTON = (By.CSS_SELECTOR, 'span.input-group-btn')
RESULT_HEADER = (By.CSS_SELECTOR, 'div#content > h1')


def test_search():
    driver = webdriver.Chrome('../drivers/chromedriver')
    driver.get('http://test.mojolab.tech/')
    driver.implicitly_wait(5)

    # Search for phone
    search_word = 'phone'
    search_field = driver.find_element(*SEARCH_FIELD)
    search_field.send_keys(search_word)
    driver.find_element(*SEARCH_BUTTON).click()

    # Verify search results header
    content_header = driver.find_element(*RESULT_HEADER)
    assert content_header.text == f'Search - {search_word}', \
        f"Expected text 'Search - {search_word}', but got {content_header.text}"
