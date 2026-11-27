from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--start-maximized')
options.add_argument('--disable-notifications')
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/context_menu")

actions = ActionChains(driver)
context_menu = driver.find_element(By.ID, "hot-spot")
actions.context_click(context_menu).perform()
alert = driver.switch_to.alert
assert alert.text == "You selected a context menu"
alert.dismiss()

driver.quit()