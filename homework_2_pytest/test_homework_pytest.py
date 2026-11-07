import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


@pytest.mark.smoke
def test_add_remove(browser):
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")

    add_button = browser.find_element(
        By.XPATH, "//button[text()='Add Element']"
    )
    add_button.click()
    add_button.click()

    delete_buttons = browser.find_elements(
        By.XPATH, "//button[text()='Delete']"
    )
    assert len(delete_buttons) == 2

    delete_buttons[0].click()

    delete_buttons = browser.find_elements(
        By.XPATH, "//button[text()='Delete']"
    )
    assert len(delete_buttons) == 1


@pytest.mark.smoke
def test_checkboxes(browser):
    browser.get("https://the-internet.herokuapp.com/checkboxes")

    checkbox_1 = browser.find_element(By.XPATH, "//input[1]")
    checkbox_2 = browser.find_element(By.XPATH, "//input[2]")

    assert not checkbox_1.is_selected()
    assert checkbox_2.is_selected()

    checkbox_1.click()
    checkbox_2.click()

    assert checkbox_1.is_selected()
    assert not checkbox_2.is_selected()


@pytest.mark.smoke
def test_dropdown(browser):
    browser.get("https://the-internet.herokuapp.com/dropdown")

    dropdown_element = browser.find_element(By.ID, "dropdown")
    dropdown = Select(dropdown_element)

    option_texts = [option.text for option in dropdown.options]
    assert option_texts == [
        "Please select an option",
        "Option 1",
        "Option 2",
    ]

    dropdown.select_by_visible_text("Option 1")
    assert dropdown.first_selected_option.text == "Option 1"

    dropdown.select_by_visible_text("Option 2")
    assert dropdown.first_selected_option.text == "Option 2"


@pytest.mark.regression
@pytest.mark.parametrize("symbol", ["a", "b", "x"])
def test_non_numeric_input(browser, symbol):
    browser.get("https://the-internet.herokuapp.com/inputs")

    input_field = browser.find_element(By.TAG_NAME, "input")
    input_field.send_keys(symbol)

    assert input_field.get_attribute("value") == ""


@pytest.mark.regression
@pytest.mark.parametrize("number", ["1.2", "5.55", "-10.005", "100"])
def test_numeric_input(browser, number):
    browser.get("https://the-internet.herokuapp.com/inputs")

    input_field = browser.find_element(By.TAG_NAME, "input")
    input_field.send_keys(number)

    assert input_field.get_attribute("value") == number


@pytest.mark.regression
@pytest.mark.parametrize(
    ("start_value", "value_after_up", "value_after_down"),
    [
        ("5", "6", "5"),
        ("12", "13", "12"),
    ],
)
def test_input_arrow_keys(
        browser, start_value, value_after_up, value_after_down
):
    browser.get("https://the-internet.herokuapp.com/inputs")

    input_field = browser.find_element(By.TAG_NAME, "input")
    input_field.send_keys(start_value)
    assert input_field.get_attribute("value") == start_value

    input_field.send_keys(Keys.ARROW_UP)
    assert input_field.get_attribute("value") == value_after_up

    input_field.send_keys(Keys.ARROW_DOWN)
    assert input_field.get_attribute("value") == value_after_down


@pytest.mark.regression
def test_typos(browser):
    browser.get("https://the-internet.herokuapp.com/typos")

    paragraphs = browser.find_elements(By.TAG_NAME, "p")
    assert len(paragraphs) >= 2

    allowed_texts = {
        "Sometimes you'll see a typo, other times you won't.",
        "Sometimes you'll see a typo, other times you wont.",
        "Sometimes you'll see a typo, other times you won,t.",
    }

    assert paragraphs[1].text in allowed_texts
