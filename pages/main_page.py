import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):

    url = 'https://znyworldwide.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    zny_logo = "//a[@class='header__logo']"
    login_page_button = "//html/body/main/section[1]/div/header/nav/div[1]/ul[3]/li[1]/a"
    hoodies_page_button = "/html/body/header/nav/div[1]/ul[1]/li[3]/a"
    cart_total_button = "//span[@id='cart-total']"

    # Getters

    def get_zny_logo(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.get_zny_logo)))

    def get_login_page_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_page_button)))

    def get_hoodies_page_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hoodies_page_button)))

    def get_cart_total_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_total_button)))

    # Actions

    def click_zny_logo(self):
        self.get_zny_logo().click()
        print("Click zny logo")

    def click_login_page_button(self):
        self.get_login_page_button().click()
        print("Click login page button")

    def click_hoodies_page_button(self):
        self.get_hoodies_page_button().click()
        print("Click hoodies page button")

    def click_cart_total_button(self):
        self.get_cart_total_button().click()
        print("Click cart total button")

    # Methods

    def get_driver(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def select_login_page(self):
        self.get_current_url()
        self.click_login_page_button()

    def select_hoodies_page(self):
        self.get_current_url()
        self.click_hoodies_page_button()
