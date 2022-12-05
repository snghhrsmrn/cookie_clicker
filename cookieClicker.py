from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()

driver.get("https://orteil.dashnet.org/cookieclicker/")

# you can add explicitly wait here instead of implicit wait. I just added implicit wait because I am lazy
driver.implicitly_wait(20)

# english language selection menu
language = driver.find_element_by_id("langSelect-EN")
language.click()

# finding the link of the big cookie to click
cookie = driver.find_element_by_id("bigCookie")

# counting the number of cookies
cookie_count = driver.find_element_by_id("cookies")

# sorting and creating the list of the product to purchase in order of their cost from highest to lowest
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

# action chains to click on cookie
actions = ActionChains(driver)
actions.click(cookie)

# for loop to click on cookie 500 times and purchase items as they are available
for i in range(500):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        print(value)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click().perform()

