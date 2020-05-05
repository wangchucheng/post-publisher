import json

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import authorization


def qq(driver, timeout):
    qq_login = 'https://segmentfault.com/user/oauth/qq'
    driver.get(qq_login)
    authorization.qq(driver, timeout)
    
    # 等待跳转
    WebDriverWait(driver, timeout).until(EC.title_contains('思否'))
    cookies = driver.get_cookies()
    json_cookies = json.dumps(cookies)
    with open('segmentfault_cookies.json', 'w') as f:
        f.write(json_cookies)
    return json_cookies

