from selenium import  webdriver
import  time
driver = webdriver.Chrome(executable_path='chromedriver.exe')

driver.get('https://rahulshettyacademy.com/AutomationPractice/')

checkboxes= driver.find_elements_by_xpath('//input[@type="checkbox"]')

for checkbox in checkboxes:
    checkbox.click()

time.sleep(2)

for checkbox in checkboxes:
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()
        break




time.sleep(1)
driver.close()

