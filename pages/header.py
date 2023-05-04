from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC, wait



class Header(Page):
  SHOP_BY_PRODUCT = (By.XPATH, "//summary[@class='header__menu-item header__menu-item--top list-menu__item focus-inset']")
  FACE_WASHES = (By.XPATH, "//list-menu-item[@data-title='Face Washes']")
  def shopping_by_product (self):
    header_link = self.driver.find_elements(*self.SHOP_BY_PRODUCT)
    header_link[1].click()

  def face_washes (self):
    self.click(*self.FACE_WASHES)