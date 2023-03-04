from selenium.webdriver.common.by import By
from behave import given, when, then

HAMBURGER_ICON = (By.ID, 'nav-hamburger-menu')
BESTSELLER_ICON = (By.XPATH, "//a[contains(@href, '/gp/bestsellers/?ref_=nav_em_cs_bestsellers_0_1_1_2')]")
SUB_HEADERS = (By.XPATH, "//div[@class='_p13n-zg-nav-tab-all_style_zg-tabs__EYPLq']/ul/li")




@given ("Open Amazon.com page")
def open_amazon_page (context):
    context.driver.get("https://www.amazon.com/")

@when ("Click on hamburger icon")
def click_hamburger_icon (context):
    hamburger_icon = context.driver.find_element(*HAMBURGER_ICON)
    hamburger_icon.click()

@when ("Click on best sellers")
def click_best_seller_icon (context):
    click_on_best_seller = context.driver.find_element(*BESTSELLER_ICON)
    click_on_best_seller.click()

@then ("Verify that there are {expected_result} links")
def verifying_subheaders_is_present (context, expected_result):

    actual_result = len(context.driver.find_elements(*SUB_HEADERS))
    print(actual_result)

    assert expected_result == str(actual_result), f'Expected {expected_result} but got actual {actual_result}'
    print('Test case passed')

