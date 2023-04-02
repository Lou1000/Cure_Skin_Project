from selenium.webdriver.common.by import By
from behave import given, when, then

CART_NUM = (By.XPATH, "//span[@id='nav-cart-count']")
@given ("Open Amazon Url")
def opening_amazon_url_page(context):
    context.app.main_page.open_main_url()


@when ("Click on cart icon")
def click_returns_orders_tab(context):
    context.app.cart_page.carted_item()

@then ("Verify 'Your Shopping Cart is empty.' text {expected_result} is present")
def verify_signin_header(context, expected_result):
    context.app.cart_page.number_of_cart_items(expected_result)