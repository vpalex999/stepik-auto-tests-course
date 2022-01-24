import webbrowser
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def answer():
    return math.log(int(time.time()))


# @pytest.fixture(scope='module')
# def browser():
#     wd = webdriver.Firefox()
#     yield wd
#     wd.quit()


@pytest.mark.parametrize('url', [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
])
def test_pametrize(browser, url, answer):
    browser.get(url)

    text_area_element = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.TAG_NAME, 'textarea')))

    text_area_element.send_keys(str(answer))

    submit_element = browser.find_element_by_css_selector('.submit-submission')
    submit_element.click()

    is_correct = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint')))

    assert is_correct.text == 'Correct!', f'The text was {is_correct.text}'
