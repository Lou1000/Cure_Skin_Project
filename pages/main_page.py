from pages.base_page import Page


class MainPage(Page):

    def open_main_url(self):
        self.open_url('https://www.amazon.com/')

    def product_link(self):
        self.open_url("https://www.amazon.com/gp/product/B074TBCSC8")