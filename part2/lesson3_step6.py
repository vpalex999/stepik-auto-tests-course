import os
import time
import math
from selenium import webdriver

url = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(url)

    browser.find_element_by_css_selector(
        'button[type=submit]').click()

    window2 = browser.window_handles[1]

    browser.switch_to.window(window2)

    x = browser.find_element_by_css_selector('#input_value').text

    browser.find_element_by_css_selector('#answer').send_keys(calc(x))

    browser.find_element_by_css_selector('.form-group button').click()

finally:

    time.sleep(10)
    browser.quit()

    pass
