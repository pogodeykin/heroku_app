from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10)

driver.get("https://the-internet.herokuapp.com/add_remove_elements/")

add_element = driver.find_element(
    By.XPATH, "//button[text()='Add Element']"
)
add_element.click()
add_element.click()

wait.until(
    lambda d: len(d.find_elements(By.XPATH, "//button[text()='Delete']")) == 2
)

driver.find_element(By.XPATH, "//button[text()='Delete']").click()

wait.until(
    lambda d: len(d.find_elements(By.XPATH, "//button[text()='Delete']")) == 1
)

assert len(driver.find_elements(By.XPATH, "//button[text()='Delete']")) == 1

driver.quit()
