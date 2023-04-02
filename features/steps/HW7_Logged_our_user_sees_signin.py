from selenium.webdriver.common.by import By
from behave import given, when, then

@given ("Open Amazon Main Page")
def opening_amazon_url_page(context):
    context.app.main_page.open_main_url()


@when ("Click Amazon Orders link")
def click_returns_orders_tab(context):
    context.app.header.click_return_orders_tab()

@then ("Verify {expected_result} page is opened and shows text")
def verify_signin_header(context, expected_result):
    context.app.signin_page.loggedout_verify(expected_result)