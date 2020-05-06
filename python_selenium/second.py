from selenium import  webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.facebook.com/')

driver.find_element_by_name('firstname').send_keys('AKash')
driver.find_element_by_name('lastname').send_keys('krishnan')
driver.find_element_by_name('reg_email__').send_keys('krishnanag1999@gmail.com')
driver.find_element_by_name('reg_passwd__').send_keys('krishnanag1999@gmail.com')

driver.find_element_by_id('u_0_6').click()

driver.close()