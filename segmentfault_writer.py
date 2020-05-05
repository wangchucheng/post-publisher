import time

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from post import Post

def write(post, driver, timeout):
    write_link = 'https://segmentfault.com/write'
    driver.get(write_link)
    url = driver.current_url
    if 'howtowrite' in driver.current_url:
        driver.get('https://segmentfault.com/write?freshman=1')

    # 添加标题
    title = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_id('title'))
    pyperclip.copy(post.title)
    title.clear()
    title.send_keys(Keys.CONTROL, 'v')
    time.sleep(3)

    # 添加标签
    add_tag_button = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_id('add-tag-btn'))
    add_tag_button.click()
    search_tag = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_id('searchTag'))

    for tag in post.tags:
        pyperclip.copy(tag)
        search_tag.send_keys(Keys.CONTROL, 'v')
        search_result = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_id('tagSearchResult').find_element_by_tag_name('a'))
        if search_result.text == '找不到相关标签':
            pass
        else:
            search_result.click()
    ActionChains(driver).move_to_element(title).click().perform()
    time.sleep(3)

    # 添加正文
    content_click = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath('//*[@id="sfEditor"]/div/div[2]/div/div[1]/div[1]/div/div[6]/div[1]/div/div/div/div[5]/pre'))
    content_click.click()
    pyperclip.copy(post.content)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').perform()

    # 发表文章
    submit_button = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath('//*[@id="submitDiv"]/button'))
    submit_button.click()
    confirm_button = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_id('sureSubmitBtn'))
    confirm_button.click()