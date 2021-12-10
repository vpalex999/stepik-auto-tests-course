import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

url = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(url)

    element = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    browser.find_element_by_css_selector('#book').click()

    # time.sleep(30)
    x = browser.find_element_by_css_selector('#input_value').text
    browser.find_element_by_css_selector('#answer').send_keys(calc(x))
    browser.find_element_by_css_selector('.form-group button').click()


finally:

    time.sleep(10)
    browser.quit()

    pass
