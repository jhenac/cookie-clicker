from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(by=By.CSS_SELECTOR, value="#cookie")

end = time.time() + 300
while time.time() < end:
    cookie.click()
    if round(time.time(), 0) % 5 == 0:
        store_items = driver.find_elements(By.CSS_SELECTOR, '#store div')
        store_items.reverse()
        for n in range(len(store_items)):
            try:
                store_items[n].get_attribute('onclick')
                store_items[n].click()
            except:
                pass

time.sleep(1)
purchased_upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")
upgrades = [purchased_upgrades[n].text.split("\n")[0] for n in range(len(purchased_upgrades))]
print(upgrades)
print(f"Remaining cookies: {driver.find_element(By.CSS_SELECTOR, '#money').text}")
print(driver.find_element(By.CSS_SELECTOR, '#cps').text)

