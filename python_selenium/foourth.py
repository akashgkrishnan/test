from selenium import  webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.facebook.com/')

driver.find_element_by_xpath('//*[@id="email"]').send_keys('krishnanag1996@gmail.com')
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('Test@1996')
driver.find_element_by_xpath('//input[@type="submit"]').click()