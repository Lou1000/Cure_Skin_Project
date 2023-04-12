from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page

class NewArrivals(Page):

    NEW_ARRIVALS = (By.CSS_SELECTOR, "a[href*='/New-Arrivals/']")
    OPTIONS = (By.XPATH, "//ul[@class='mm-category-list']/li[contains(text(), 'See More')]")
    def hovering_new_arrivals(self):
        new_arrivals_elements = self.driver.find_element(*self.NEW_ARRIVALS)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals_elements)
        actions.perform()

    def verifying_links(self, expected_links):
        elemens = self.driver.find_elements(*self.OPTIONS)
        actual_number_of_elements = len(elemens)
        assert actual_number_of_elements == int(
        expected_links), f'Expected {expected_links} but got {actual_number_of_elements}'