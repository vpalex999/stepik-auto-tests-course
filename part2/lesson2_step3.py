import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

url = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(url)

    num1 = browser.find_element_by_css_selector('#num1').text
    num2 = browser.find_element_by_css_selector('#num2').text
    find_summ = int(num1) + int(num2)

    selectElement = browser.find_element_by_css_selector(
        'select.custom-select')

    Select(selectElement).select_by_value(str(find_summ))

    button_submit_element = browser.find_element_by_css_selector('button')
    button_submit_element.click()

finally:

    time.sleep(30)
    browser.quit()

    pass
