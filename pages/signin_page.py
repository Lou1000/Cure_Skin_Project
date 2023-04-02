from selenium.webdriver.common.by import By
from pages.base_page import Page


class SignedIn(Page):

    SIGNING_IN = (By.XPATH, "//h1[@class='a-spacing-small']")


    def loggedout_verify(self, expected_test):
        actual_result = self.driver.find_element(*self.SIGNING_IN).text
        print(actual_result)

        assert expected_test == (actual_result), f'Expected {expected_test} but got actual {actual_result}'
        print('Test case passed')