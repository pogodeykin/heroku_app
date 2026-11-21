from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable-notifications')
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/iframe")
iframe = driver.find_element(By.ID, "mce_0_ifr")
driver.switch_to.frame(iframe)
text_in_frame = driver.find_element(By.XPATH, "//p")
assert text_in_frame.text == "Your content goes here."
driver.switch_to.default_content()

driver.quit()