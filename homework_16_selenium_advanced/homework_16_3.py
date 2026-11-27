from pathlib import Path

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
driver.get("https://the-internet.herokuapp.com/upload")
file_path = Path("789.txt").resolve()
driver.find_element(By.ID, "file-upload").send_keys(str(file_path))
driver.find_element(By.ID, "file-submit").click()
wait = WebDriverWait(driver, 10)
file_name = wait.until(expected_conditions.visibility_of_element_located((By.ID, "uploaded-files")))
assert file_name.text == "789.txt"

driver.quit()