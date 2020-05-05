import json

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

import post_reader
import jianshu_login
import jianshu_writer

base_url = 'https://jianshu.com/'
driver = webdriver.Chrome('')
driver.get(base_url)
driver.delete_all_cookies()

timeout = 5

try:
    with open('jianshu_cookies.json', 'r', encoding='utf-8') as f:
        cookies = json.loads(f.read())
except FileNotFoundError:
    cookies = json.loads(jianshu_login.qq(driver, timeout))

for cookie in cookies:
    driver.add_cookie({
        'name': cookie['name'],
        'value': cookie['value'],
        'path': cookie['path'],
        'domain': cookie['domain'],
        'secure': cookie['secure']
    })
driver.get('https://jianshu.com/')

mypost = post_reader.read_file('your_post.md')
jianshu_writer.write(mypost, driver, timeout)