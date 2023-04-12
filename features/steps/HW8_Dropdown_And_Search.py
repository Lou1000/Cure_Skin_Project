from selenium.webdriver.common.by import By
from behave import given, when, then

department_dropdown = (By.ID, "nav-search-dropdown-card")

@given ("Open Amazon page")
def opening_amazon_page(context):
    context.app.main_page.open_main_url()

@when ("Click on department toggle")
def select_department(context):
    context.app.header.department_toggle()

@then ("Enter {item_name} and click search button")
def verify_signin_header(context, item_name):
    context.app.header.input_search_text(item_name)
    context.app.header.click_search()