from selenium import  webdriver


driver = webdriver.Chrome(executable_path='chromedriver.exe')
firediver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get('https://www.google.com')
driver.maximize_window()

print(driver.title)
print(driver.current_url)
driver.get('https://www.facebook.com')
driver.back() #to comeback from the pagge
driver.refresh() # to refresh the  webpage
driver.close()