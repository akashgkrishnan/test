from selenium import  webdriver
from selenium.webdriver import ActionChains
from time import sleep

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.familysearch.org/en/')
driver.maximize_window()
sleep(3)

action = ActionChains(driver)

driver.find_element_by_xpath('//*[@id="primaryNav"]/div[2]/button').click()

action.move_to_element(driver.find_element_by_link_text('Genealogies')).click().perform()