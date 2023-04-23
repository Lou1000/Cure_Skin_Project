from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC, wait



class SearchResultsPage(Page):

    PRODUCT_TOTAL = (By.ID, "ProductCount")
    def verifying_search_result (self, expected_behavior):
        actual_result = self.driver.find_element(*self.PRODUCT_TOTAL).text

        assert expected_behavior == actual_result, f'Expected {expected_behavior} but got actual {actual_result}'
        print('Test case passed')