from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('http://a2staging.innovationm.com/')
driver.maximize_window()

driver.find_element_by_link_text('Employer Sign Up').click()
time.sleep(6)

child_window = driver.window_handles[-1]
driver.switch_to.window(child_window)

driver.find_element_by_xpath('//label[@class="has-float-label"]').send_keys('akash krishnan company')
driver.find_element_by_xpath('//input[@name="fullName"]').send_keys('akash krishnan')
driver.find_element_by_xpath('//input[@name="email"]').send_keys('akash@email.com')
driver.find_element_by_xpath('//input[@name="password"]').send_keys('Test@123')
driver.find_element_by_xpath('//input[@name="confirmPassword"]').send_keys('Test@123')
driver.find_element_by_xpath('//button[@type="submit"]').click()



