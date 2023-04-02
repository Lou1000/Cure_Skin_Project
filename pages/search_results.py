from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC, wait


class SearchResultsPage(Page):
    # SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    CLICK_ITEM = (By.XPATH, "//span[@class='rush-component s-latency-cf-section']/div/div/div/div/div/div/div/div/h2/a")

    # def verify_search_result(self, expected_text):
    #     self.verify_text(expected_text, *self.SEARCH_RESULT)

    def click_on_item(self):
        all_products = self.driver.find_elements(*self.CLICK_ITEM)
        self.driver.wait.until(EC.element_to_be_clickable((all_products[0])))
        all_products[0].click()