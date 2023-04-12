from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# @given("Open Amazon page")
# def open_amazon_page (context):
#     context.driver.get("https://www.amazon.com/")

@when("Clicking on Returns and Orders tab")
def click_returns_tab (context):
    returns_button = context.driver.find_element(By.XPATH, '//a[@id="nav-orders"]')
    returns_button.click()

@then("Sign in text should be shown prompting user to sign in")
def show_signin_header (context):
    signin_header = context.driver.find_element(By.XPATH, 'h1[@class="a-spacing-small"]')
    signin_header.displayed()
