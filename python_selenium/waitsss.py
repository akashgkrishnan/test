from selenium import  webdriver
from time import  sleep

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

driver.find_element_by_xpath('//input[@placeholder = "Search for Vegetables and Fruits"]').send_keys('ber')
sleep(4)
products = driver.find_element_by_xpath('//div[@class = "products"]/div')


buttons = driver.find_elements_by_xpath('//div[@class="product-action"]/button')

for button in buttons:
    button.click()


driver.find_element_by_xpath('//a[@class="cart-icon"]').click()

driver.find_element_by_xpath('//button[text()="PROCEED TO CHECKOUT"]').click()

sleep(1)
driver.find_element_by_xpath('//input[@class="promoCode"]').send_keys('rahulshettyacademy')
driver.find_element_by_xpath('//button[@class="promoBtn"]').click()
sleep(7)
print(driver.find_element_by_xpath('//span[@class="promoInfo"]').text)