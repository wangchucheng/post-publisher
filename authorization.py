from selenium.webdriver.support.wait import WebDriverWait
 

def qq(driver, timeout):
    window_handles = driver.window_handles
    driver.switch_to_window(window_handles[-1])
 
    iframe = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_id('ptlogin_iframe'))
    driver.switch_to_frame(iframe)

    login = WebDriverWait(driver, timeout).until(lambda d: d.find_element_by_class_name('face'))
    login.click()