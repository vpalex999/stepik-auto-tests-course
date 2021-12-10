from selenium import webdriver
import time
import math


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


url = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    x = browser.find_element_by_css_selector('.form-group #input_value').text

    input_element = browser.find_element_by_css_selector('#answer')
    input_element.send_keys(calc(x))

    robot_checkbox_element = browser.find_element_by_css_selector(
        '.form-check-custom .form-check-input')
    robot_checkbox_element.click()

    robots_rule_element = browser.find_element_by_css_selector(
        '.form-radio-custom .form-check-input')
    robots_rule_element.click()

    button_submit_element = browser.find_element_by_css_selector('button')
    button_submit_element.click()

finally:

    time.sleep(30)
    browser.quit()

    pass
