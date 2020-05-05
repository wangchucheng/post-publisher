import json

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import authorization


def qq(driver, timeout):
    qq_login = 'https://www.jianshu.com/users/auth/qq_connect'
    driver.get(qq_login)
    authorization.qq(driver, timeout)
    
    # 等待跳转
    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element_by_class_name('write-btn'))
    cookies = driver.get_cookies()
    json_cookies = json.dumps(cookies)
    with open('jianshu_cookies.json', 'w') as f:
        f.write(json_cookies)
    return json_cookies
