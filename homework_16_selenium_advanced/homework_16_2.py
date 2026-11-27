from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable-notifications')
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/dynamic_controls")

remove_btn = driver.find_element(By.XPATH, "//button[text()='Remove']")
enable_btn = driver.find_element(By.XPATH, "//button[text()='Enable']")
input_field = driver.find_element(By.XPATH, "//input[@type='text']")

remove_btn.click()
wait = WebDriverWait(driver, 10)
message = wait.until(expected_conditions.visibility_of_element_located((By.ID, "message")))
assert message.text == "It's gone!"
assert not driver.find_elements(By.ID, "checkbox")

assert not input_field.is_enabled()

enable_btn.click()
message = wait.until(expected_conditions.visibility_of_element_located((By.ID, "message")))
assert input_field.is_enabled()

driver.quit()