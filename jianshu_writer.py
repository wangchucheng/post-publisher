import time

import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from post import Post

def write(post, driver, timeout):
    write_link = 'https://www.jianshu.com/writer#/'
    driver.get(write_link)

    # 选择文集
    __set_corpus(post, driver, timeout)
    time.sleep(3)

    # 新建文章
    new_article = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div/div[1]'))
    new_article.click()
    article = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[1]/div/div/div/ul/li[1]'))
    article.click()
    time.sleep(3)

    # 添加标题
    title = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/input'))
    pyperclip.copy(post.title)
    title.clear()
    title.send_keys(Keys.CONTROL, 'v')
    time.sleep(3)
    
    # 添加正文
    content = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_id('arthur-editor'))
    pyperclip.copy(post.content)
    content.clear()
    content.send_keys(Keys.CONTROL, 'v')
    time.sleep(3)

    # 保存草稿
    driver.find_element_by_class_name('fa-floppy-o').click()

    # 发表文章
    # driver.find_element_by_xpath('//*[@id="root"]/div/div[2]/div[2]/div/div/div/div/ul/li[1]/a').click()

def __set_corpus(post, driver, timeout):
    corpora = WebDriverWait(driver, timeout).until(lambda d: d.find_elements_by_class_name('_3DM7w'))
    for c in corpora:
        corpus = c.get_attribute('title')
        if post.categories[0] == corpus:
            c.click()
            return
    driver.find_element_by_class_name('_1iZMb').click()
    new_corpus = driver.find_element_by_class_name('_1CtV4')
    pyperclip.copy(post.categories[0])
    new_corpus.clear()
    new_corpus.send_keys(Keys.CONTROL, 'v')
    driver.find_element_by_class_name('dwU8Q').click()