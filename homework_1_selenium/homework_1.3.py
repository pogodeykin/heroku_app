from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/dropdown")

dropdown_element = driver.find_element(By.ID, "dropdown")
dropdown = Select(dropdown_element)

option_texts = [option.text for option in dropdown.options]
assert "Option 1" in option_texts
assert "Option 2" in option_texts

dropdown.select_by_visible_text("Option 1")
assert dropdown.first_selected_option.text == "Option 1"

dropdown.select_by_visible_text("Option 2")
assert dropdown.first_selected_option.text == "Option 2"

driver.quit()
