from selenium import  webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.facebook.com/')

driver.find_element_by_css_selector("input[name='firstname']").send_keys('akash') #first name
driver.find_element_by_xpath('//input[@name="lastname"]').send_keys('new') #second name
driver.find_element_by_xpath('//*[@id="u_0_r"]').send_keys('akash.krishnan@nes.com') #email
driver.find_element_by_xpath('//*[@id="u_0_w"]').send_keys('test@123wqei') #pass
driver.find_element_by_id('u_0_6').click() #gender radio
driver.find_element_by_xpath("//button[@id='u_0_13']").click() #submit



print(driver.find_element_by_xpath('//*[@id="u_0_12"]/p').text)

