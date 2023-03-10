from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then

click_search = (By.ID, "twotabsearchtextbox")
enter_item = (By.ID, "twotabsearchtextbox")
clicking_search_button = (By.ID,"nav-search-submit-text")
clicking_hat = (By.XPATH, "//span[@class='rush-component s-latency-cf-section']/div/div/div/div/div/div/div/div/h2/a")
all_color_options = (By.XPATH, "//ul[@class='a-unordered-list a-nostyle a-button-list a-declarative a-button-toggle-group a-horizontal a-spacing-top-micro swatches swatchesRectangle imageSwatches']/li")


@given ("Open Amazon webpage")
def open_amazon_page (context):
    context.driver.get("https://www.amazon.com/")


@when ("User clicks on search input box")
def clicking_on_search (context):
    clinking_search_input_feild = context.driver.find_element(*click_search)
    clinking_search_input_feild.click()


@when ("User enters {hat_name}")
def search_input_item (context, hat_name):
    entering_item_in_search = context.driver.find_element(*enter_item)
    entering_item_in_search.send_keys(hat_name)



@when ("User clicks on search button")
def clicking_search (context):
    search_button = context.driver.find_element(*clicking_search_button)
    search_button.click()


@when ("User clicks on item")
def clicking_on_hat (context):
    click_hat = context.driver.find_elements(*clicking_hat)
    click_hat[3].click()


@then ("User selects {num_options} different color variations of that item")
def selecting_colors (context, num_options):
    all_options = context.driver.find_elements(*all_color_options)
    actual_result = len(all_options)

    print(actual_result)

    for hat_option in all_options:
        hat_option.click()

    expected_result = num_options

    assert expected_result == str(actual_result), f'Expected {expected_result} but got actual {actual_result}'
    print('Test case passed')
