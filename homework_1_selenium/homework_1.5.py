from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.get("https://the-internet.herokuapp.com/typos")

paragraphs = driver.find_elements(By.TAG_NAME, "p")
assert len(paragraphs) >= 2

paragraph_text = paragraphs[1].text

allowed_texts = {
    "Sometimes you'll see a typo, other times you won't.",
    "Sometimes you'll see a typo, other times you wont.",
    "Sometimes you'll see a typo, other times you won,t.",
}

assert paragraph_text in allowed_texts

driver.quit()
