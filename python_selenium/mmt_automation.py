from selenium import  webdriver
import time
from selenium.common.exceptions import StaleElementReferenceException

driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://www.makemytrip.com/')

driver.find_element_by_id('fromCity').click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys('del')
time.sleep(2)
city_names = driver.find_elements_by_css_selector("p[class*='blackText'")

for city in city_names:
    try:
        if city.text == 'Del Rio, United States':
            city.click()
    except StaleElementReferenceException as e:
        pass


driver.find_element_by_css_selector("input[placeholder='To']").send_keys('del')
time.sleep(2)
# city_names = driver.find_elements_by_css_selector("p[class*='blackText'")
# for city in city_names:
#     try:
#         if city.text == 'Bangui, Central African Republic':
#             city.click()
#             break
#     except StaleElementReferenceException as e:
#         pass

driver.find_element_by_xpath("//p[text()='Delhi, India']").click()



driver.find_element_by_css_selector('a[class*="widgetSearchBtn"]').click()
time.sleep(2)
#driver.close()
