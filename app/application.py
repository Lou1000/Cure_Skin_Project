from pages.main_page import MainPage
from pages.header import Header
from pages.search_results import SearchResultsPage
from pages.cart_page import CartPage
from pages.signin_page import SignedIn
from pages.new_arrivals import NewArrivals


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.header = Header(self.driver)
        self.search_results = SearchResultsPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.signin_page = SignedIn(self.driver)
        self.new_arrivals = NewArrivals(self.driver)