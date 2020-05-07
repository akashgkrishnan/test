from selenium import  webdriver
from time import  sleep

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

driver.find_element_by_xpath('//input[@placeholder = "Search for Vegetables and Fruits"]').send_keys('ber')
sleep(4)
products = driver.find_element_by_xpath('//div[@class = "products"]/div')


buttons = driver.find_elements_by_xpath('//div[@class="product-action"]/button')

#//div[@class='product-action']/button/parent::div/parent::div/h4
home_page = []
for button in buttons:
    #print(button.find_element_by_xpath("parent::div/parent::div/h4").text) #the above path already stored in button
    home_page.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()
driver.find_element_by_xpath('//a[@class="cart-icon"]').click()

driver.find_element_by_xpath('//button[text()="PROCEED TO CHECKOUT"]').click()

sleep(1)
items = driver.find_elements_by_xpath('//p[@class="product-name"]')

checkout_page = []

for item in items:
    checkout_page.append(item.text)


assert checkout_page == home_page

#print(f'checkout {checkout_page} home {home_page} ')

before_discount = driver.find_element_by_class_name('discountAmt').text
#copyin generated amount

all_amounts = driver.find_elements_by_xpath('//tr/td[5]/p')
#gets all the price from the total price table column


total_price = 0

for amount in all_amounts:
    total_price += int(amount.text)

print(f' total {total_price}')
print(f' before: {before_discount}')

assert total_price == int(before_discount)




driver.find_element_by_xpath('//input[@class="promoCode"]').send_keys('rahulshettyacademy')
driver.find_element_by_xpath('//button[@class="promoBtn"]').click()
sleep(7)
print(driver.find_element_by_xpath('//span[@class="promoInfo"]').text)

after_discount = driver.find_element_by_class_name('discountAmt').text

print(f'{float(after_discount)}')

assert float(after_discount) < int(before_discount)

driver.close()