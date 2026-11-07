from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.TAG_NAME, "input")

input_field.send_keys("123")
assert input_field.get_attribute("value") == "123"

input_field.send_keys(Keys.ARROW_UP)
assert input_field.get_attribute("value") == "124"

input_field.send_keys(Keys.ARROW_DOWN)
assert input_field.get_attribute("value") == "123"

input_field.clear()
input_field.send_keys("abc")
assert input_field.get_attribute("value") == ""

driver.quit()
