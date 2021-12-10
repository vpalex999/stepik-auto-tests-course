import os
import time
import math
from selenium import webdriver

url = "http://suninjuly.github.io/file_input.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element_by_css_selector(
        '.form-group [name=firstname]').send_keys('oleg')

    browser.find_element_by_css_selector(
        '.form-group [name=lastname]').send_keys('bub')

    browser.find_element_by_css_selector(
        '.form-group [name=email]').send_keys('all@mail.com')

    my_dir = os.path.abspath(os.path.dirname(__file__))
    my_file = os.path.join(my_dir, 'my_file.txt')

    browser.find_element_by_css_selector('#file').send_keys(my_file)

    browser.find_element_by_css_selector('button').click()

finally:

    time.sleep(30)
    browser.quit()

    pass
