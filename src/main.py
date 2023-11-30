from selenium import webdriver

PATH = "/Users/tesla/driver/chromedriver" 

driver = webdriver.Chrome()
print("Starting Chrome...")
driver.get("https://www.briannewton.me")

print(driver.title)

driver.get("https://web.snapchat.com/")
