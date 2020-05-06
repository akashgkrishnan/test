from selenium import  webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.makemytrip.com/')

driver.find_element_by_id('fromCity').click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys('del')
city_names = driver.find_elements_by_css_selector("p[class*='blackText'")

for city in city_names:
    if city.text == 'Bangkok, Thailand':
        city.click()