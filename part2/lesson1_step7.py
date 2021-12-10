from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element_by_css_selector(
        '#treasure').get_attribute('valuex')

    input_element = browser.find_element_by_css_selector('#answer')
    input_element.send_keys(calc(x))

    browser.find_element_by_css_selector('#robotCheckbox').click()

    browser.find_element_by_css_selector('#robotsRule').click()

    button_submit_element = browser.find_element_by_css_selector('button')
    button_submit_element.click()

finally:

    time.sleep(30)
    browser.quit()

    pass
