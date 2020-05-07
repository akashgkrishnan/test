from selenium import  webdriver
from time import  sleep

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://the-internet.herokuapp.com/windows')

driver.find_element_by_link_text('Click Here').click()
child_window = driver.window_handles[-1]

driver.switch_to.window(child_window)


assert driver.find_element_by_tag_name('h3').text == 'New Window'

driver.switch_to.window(driver.window_handles[0])

assert driver.find_element_by_tag_name('h3').text == 'Opening a new window'

sleep(2)


driver.close()
