from selenium import  webdriver
from selenium.webdriver.support.select import Select
import  time


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://www.facebook.com/')
driver.maximize_window()
driver.find_element_by_css_selector("input[name='firstname']").send_keys('akash') #first name
driver.find_element_by_xpath('//input[@name="lastname"]').send_keys('new') #second name
driver.find_element_by_xpath('//*[@id="u_0_r"]').send_keys('akash.krishnan@nes.com') #email
driver.find_element_by_name('reg_email_confirmation__').send_keys('akash.krishnan@nes.com')
driver.find_element_by_xpath('//*[@id="u_0_w"]').send_keys('test@123wqei') #pass
driver.find_element_by_id('u_0_6').click() #gender radio

day_dropdown = Select(driver.find_element_by_xpath('//*[@id="day"]')) # for selecting from drop down. object of select created
month_dropdown = Select(driver.find_element_by_xpath('//*[@id="month"]'))
year_dropdown = Select(driver.find_element_by_xpath('//*[@id="year"]'))

day_dropdown.select_by_value('29')
month_dropdown.select_by_visible_text('Apr')
year_dropdown.select_by_visible_text('1996')
time.sleep(3)
driver.find_element_by_xpath("//button[@id='u_0_13']").click() #submit
