from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC, wait


# enter_item = (By.ID, "twotabsearchtextbox")
# clicking_search_button = (By.ID,"nav-search-submit-text")
# click_item = (By.XPATH, "//span[@class='rush-component s-latency-cf-section']/div/div/div/div/div/div/div/div/h2/a")
# carting_item = (By.ID, 'add-to-cart-button')
# cart = (By.XPATH, '//a[@href="/gp/cart/view.html?ref_=sw_gtc"]')
# checking_cart_item = (By.XPATH, '//img[@alt="Hefty Party On Disposable Plastic Cups, Red, 18 Ounce, 30 Count, Opens in a new tab"]')
# cart_count = (By.ID, "nav-cart-count")


@given ("Open Amazon.com website")
def open_amazon_page (context):
    # context.driver.get("https://www.amazon.com/")
    context.app.main_page.open_main_url()


@when ("search for item {red_cup}")
def search_input_item (context, red_cup):
    # entering_item_in_search = context.driver.find_element(*enter_item)
    # entering_item_in_search.send_keys(red_cup)
    context.app.header.input_search_text(red_cup)


@when ("click on the search button")
def clicking_search (context):
    # search_button = context.driver.find_element(*clicking_search_button)
    # search_button.click()
    context.app.header.click_search()


@when ("click on item")
def clicking_cup (context):
    context.app.search_results.click_on_item()
    # sleep(3)


@when ("add the item to cart")
def adding_item_to_cart (context):
    # adding_to_cart = context.driver.find_element(*carting_item)
    # adding_to_cart.click()
    context.app.cart_page.cart_item()


@when ("go to the users amazon cart")
def going_to_cart_page (context):
    # cart_page = context.driver.find_element(*cart)
    # cart_page.click()
    context.app.cart_page.users_cart()


@given ("verify that there is only {expected_result} item in the users Amazon cart")
def checking_item_added (context, expected_result):
    # actual_result = context.driver.find_element(*cart_count).text
    # print(actual_result)
    #
    # assert expected_result == (actual_result), f'Expected {expected_result} but got actual {actual_result}'
    # print('Test case passed')

    context.app.cart_page.verify_cart_item(expected_result)
