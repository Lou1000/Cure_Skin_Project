from selenium.webdriver.common.by import By
from pages.base_page import Page


class CartPage(Page):

    CARTING_ITEM = (By.ID, 'add-to-cart-button')
    CART = (By.XPATH, '//a[@href="/gp/cart/view.html?ref_=sw_gtc"]')
    CART_COUNT = (By.ID, "nav-cart-count")
    CART_ICON = (By.XPATH, "//span[@id='nav-cart-count']")
    CART_ICON_BTN = (By.XPATH, "//span[@class='nav-cart-icon nav-sprite']")


    def cart_item(self):
        self.click(*self.CARTING_ITEM)

    def carted_item(self):
        self.click(*self.CART_ICON_BTN)
    def users_cart(self):
        self.click(*self.CART)


    def verify_cart_item(self, expected_text):
        actual_result = self.driver.find_element(*self.CART_COUNT).text
        print(actual_result)

        assert expected_text == (actual_result), f'Expected {expected_text} but got actual {actual_result}'
        print('Test case passed')

    def number_of_cart_items(self, expected_text):
        actual_result = self.driver.find_element(*self.CART_COUNT).text
        print(actual_result)

        assert expected_text == (actual_result), f'Expected {expected_text} but got actual {actual_result}'
        print('Test case passed')



