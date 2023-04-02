from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    RETURN_ORDERS = (By.XPATH, "//a[@id='nav-orders']")

    def input_search_text(self, text):
        # entering_item_in_search = self.driver.find_element(*self.AMAZON_SEARCH_FIELD)
        # entering_item_in_search.send_keys(text)
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_return_orders_tab(self):
        self.click(*self.RETURN_ORDERS)
