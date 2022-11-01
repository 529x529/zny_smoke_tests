from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Product_size_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    size_m_button = "//span[@class='product__size__name' and contains(text(),'M')]"
    cart_button = "//button[@id='button-cart']"

    #Getters

    def get_size_button_m(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.size_m_button)))
    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    #Actions

    def click_size_button_m(self):
        self.get_size_button_m().click()
        print("Click size button M")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Click cart button")

    # Methods

    def select_product_size_m(self):
        self.get_current_url()
        self.click_size_button_m()
        self.click_cart_button()
