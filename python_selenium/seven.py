from selenium import  webdriver
import  time
driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

driver.find_element_by_xpath('//*[@id="name"]').send_keys('test akash')
driver.find_element_by_xpath('//*[@id="alertbtn"]').click()
time.sleep(1)
alert = driver.switch_to.alert
alert.accept()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="name"]').send_keys('test akash cancel')
driver.find_element_by_xpath('//*[@id="confirmbtn"]').click()
time.sleep(1)
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(1)
driver.close()