from time import sleep

from selenium import webdriver
driver=webdriver.Chrome()
driver.get(url="http://www.baidu.com")
driver.find_element_by_id('kw').send_keys('how to study Fiddler')
sleep(3)
driver.quit()