from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC, wait


class Header(Page):
    AMAZON_SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.ID, 'nav-search-submit-button')
    RETURN_ORDERS = (By.XPATH, "//a[@id='nav-orders']")
    DEPARTMENT_DROPDOWN = (By.ID, "nav-search-dropdown-card")
    DEPARTMENT_DROPDOWN2 = (By.ID, "searchDropdownBox")


    def input_search_text(self, text):
        # entering_item_in_search = self.driver.find_element(*self.AMAZON_SEARCH_FIELD)
        # entering_item_in_search.send_keys(text)
        self.input_text(text, *self.AMAZON_SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def click_return_orders_tab(self):
        self.click(*self.RETURN_ORDERS)

    def department_toggle(self):
        # dropdown = self.driver.wait.until(EC.element_located_to_be_selected((self.DEPARTMENT_DROPDOWN3)))
        # dropdown = self.driver.wait.until(EC.element_to_be_clickable((self.DEPARTMENT_DROPDOWN)))
        dropdown = self.driver.find_element(*self.DEPARTMENT_DROPDOWN2)
        select = Select(dropdown)
        select.select_by_visible_text("Prime Video")