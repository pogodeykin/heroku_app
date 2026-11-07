from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/checkboxes")

checkbox_1 = driver.find_element(By.XPATH, "//input[1]")
checkbox_2 = driver.find_element(By.XPATH, "//input[2]")

assert not checkbox_1.is_selected()
assert checkbox_2.is_selected()

checkbox_1.click()
checkbox_2.click()

assert checkbox_1.is_selected()
assert not checkbox_2.is_selected()

driver.quit()
