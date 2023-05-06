from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC, wait



class Header(Page):
  # SHOP_BY_PRODUCT = (By.XPATH, "//summary[@class='header__menu-item header__menu-item--top list-menu__item focus-inset']")
  SHOP_BY_PRODUCT = (By.XPATH, '//span[contains(text(), "Shop by Product")]')
  # FACE_WASHES = (By.XPATH, "//list-menu-item[@data-title='Face Washes']")
  FACE_WASHES = (By.CSS_SELECTOR, "a[href*='collections/face-wash']")
  HAMBURGER_BUTTON = (By.CSS_SELECTOR, '.menu-drawer-container')

  def shopping_by_product (self):
    # header_link = self.driver.find_elements(*self.SHOP_BY_PRODUCT)
    # header_link[1].click()
    self.wait_for_element_click(*self.SHOP_BY_PRODUCT)

  def hamburger(self):
    self.click(*self.HAMBURGER_BUTTON)

  def face_washes (self):
    self.click(*self.FACE_WASHES)