from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


sub_nav = (By.XPATH, "//div[@id='nav-subnav']/a")
new_arrivals = (By.CSS_SELECTOR, "a[href*='/New-Arrivals/']")
# hidden_submenu = (By.XPATH, "//div[@id='nav-subnav']/a")
clothing_subheader = (By.CSS_SELECTOR, "#nav-subnav[data-category='apparel']" )
second_subnav = (By.ID, "nav-flyout-aj:https://m.media-amazon.com/images/G/01/Softlines/Store/MegaMenu/megamenucreator_removeps_en_US.json:subnav-sl-megamenu-8:0")
options = (By.XPATH, "//ul[@class='mm-category-list']/li[contains(text(), 'See More')]")

@given ("Open Amazon product link")
def opening_amazon_link(context):
    context.app.main_page.product_link()

@when ("Hover over new arrivals tab")
def hover_new_arrivals(context):
    context.app.new_arrivals.hovering_new_arrivals()


@then ("Verify user can see new arrivals {expected_number_of_links} links")
def hover_products(context, expected_number_of_links):
    context.app.new_arrivals.verifying_links(expected_number_of_links)
