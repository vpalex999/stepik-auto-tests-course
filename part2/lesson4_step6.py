import os
import time
import math
from selenium import webdriver

url = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser.get(url)

    browser.find_element_by_css_selector('#button')

finally:

    time.sleep(0)
    browser.quit()

    pass
