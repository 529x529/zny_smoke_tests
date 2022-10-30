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

    login_page_button = "//html/body/main/section[1]/div/header/nav/div[1]/ul[3]/li[1]/a"


    # Getters

    def get_login_page_button(self):
            return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_page_button)))


    # Actions

    def click_login_page_button(self):
        self.get_login_page_button().click()
        print("Click login button")


    # Methods

    def select_login_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_login_page_button()
