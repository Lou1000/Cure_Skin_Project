from selenium.webdriver.common.by import By
from pages.base_page import Page


class MainPage(Page):

    CLOSE_POPUP = (By.XPATH, "//button[@class='popup-close']")

    def open_main_url(self):
        self.open_url('https://shop.cureskin.com')

    def remove_popup_banner(self):
        self.click(*self.CLOSE_POPUP)



