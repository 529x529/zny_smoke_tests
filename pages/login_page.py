from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    email = "//input[@id = 'input-email']"
    password = "//input[@id = 'input-password']"
    login_button = "//button[@class = 'login__button button button--black']"

    #Getters

    def get_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.email)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    #Actions

    def input_email(self, email):
        self.get_email().send_keys(email)
        print("Input email")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    # Methods

    def autorization(self):
        Logger.add_start_step(method="autorization")
        self.get_current_url()
        self.input_email("ttesttestov9789@gmail.com")
        self.input_password("Testtest1234")
        self.click_login_button()
        Logger.add_end_step(url=self.driver.current_url, method="autorization")



