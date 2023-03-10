from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC, wait

click_search = (By.ID, "twotabsearchtextbox")
enter_item = (By.ID, "twotabsearchtextbox")
clicking_search_button = (By.ID,"nav-search-submit-text")
click_item = (By.XPATH, "//img[@alt='Marvel Avengers: Endgame Logo Super Heroes United T-Shirt']")
size_dropdown = (By.ID, "native_dropdown_selected_size_name")
size_selector = (By. XPATH, '//a[@id="native_dropdown_selected_size_name_5"]')
carting_item = (By.ID, 'add-to-cart-button')
cart = (By.XPATH, '//a[@href="/gp/cart/view.html?ref_=sw_gtc"]')
checking_cart_item = (By.XPATH, "//span[contains(@class, 'a-truncate sc-grid-item-product-title a-size-base-plus')]/span")


@given ("Open Amazon website")
def open_amazon_page (context):
    context.driver.get("https://www.amazon.com/")


@when ("click on search input field")
def clicking_on_search (context):
    clinking_search_input_feild = context.driver.find_element(*click_search)
    clinking_search_input_feild.click()


@when ("search for item {cart_item}")
def search_input_item (context, cart_item):
    entering_item_in_search = context.driver.find_element(*enter_item)
    entering_item_in_search.send_keys(cart_item)


@when ("click on search button")
def clicking_search (context):
    search_button = context.driver.find_element(*clicking_search_button)
    search_button.click()


@when ("click on the item")
def clicking_avengers_tshirt (context):
    avengers_tshirt = context.driver.find_element(*click_item)
    avengers_tshirt.click()


@when ("click on toggle button")
def clicking_on_toggle (context):
    dropdown = context.driver.find_element(*size_dropdown)
    select = Select(dropdown)
    select.select_by_visible_text("Large")


@when ("select a size")
def size_selecting (context):
    dropdown = context.driver.find_element(*size_dropdown)
    select = Select(dropdown)
    context.driver.wait.until(EC.element_located_to_be_selected((size_dropdown)))
    select.select_by_visible_text("Large")

    # sleep(5)

#     I don't know how to incorporate driver.wait.until() to replace sleep into this code without it breaking.
#     I tried adding it as: context.driver.wait.until(EC.element_located_to_be_selected((size_dropdown)))
#     But it's still breaking, I think it has to do with the particular item I selected.

@when ("add product to cart")
def adding_item_to_cart (context):
    adding_to_cart = context.driver.find_element(*carting_item)
    context.driver.wait.until(EC.element_to_be_clickable((carting_item)))
    adding_to_cart.click()


@when ("go to users amazon cart")
def going_to_cart_page (context):
    cart_page = context.driver.find_element(*cart)
    context.driver.wait.until(EC.element_to_be_clickable((cart)))
    cart_page.click()
    # sleep(4)


@given ("verify that there is {expected_result} item in the users Amazon cart")
def checking_item_added (context, expected_result):
    item_cart_locator = context.driver.find_elements(*checking_cart_item)
    single_locator = item_cart_locator[0]
    actual_result = single_locator.get_attribute("innerText")
    assert expected_result == actual_result, f'Expected {expected_result} but got actual {actual_result}'
    print('Test case passed')