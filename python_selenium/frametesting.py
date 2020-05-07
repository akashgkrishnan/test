from selenium import  webdriver
from time import  sleep

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://the-internet.herokuapp.com/iframe')

driver.switch_to.frame("mce_0_ifr")
sleep(2)
driver.find_element_by_id('tinymce').clear()
driver.find_element_by_id('tinymce').send_keys('entering text via automation')

sleep(1)

driver.switch_to.default_content()
print(driver.find_element_by_tag_name('h3').text)