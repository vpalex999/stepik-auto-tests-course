import time
from selenium import webdriver
import math

url = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(url)

    button_submit_element = browser.find_element_by_css_selector('button')
    browser.execute_script(
        'return arguments[0].scrollIntoView(true);', button_submit_element)

    x = browser.find_element_by_css_selector('#input_value').text

    browser.find_element_by_css_selector('#answer').send_keys(calc(x))
    browser.find_element_by_css_selector('#robotCheckbox').click()
    browser.find_element_by_css_selector('#robotsRule').click()

    button_submit_element.click()

finally:

    time.sleep(30)
    browser.quit()

    pass
