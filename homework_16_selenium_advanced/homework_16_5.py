from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable-notifications')
options.add_experimental_option("prefs", {"download.default_directory": str(Path(__file__).resolve().parent)})

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/download")
link = driver.find_element(By.XPATH, "//a[text()='demo-upload.txt']")
link.click()

file = Path(__file__).resolve().parent / "demo-upload.txt"

WebDriverWait(driver, 30).until(lambda _: file.is_file())

assert file.is_file()
driver.quit()