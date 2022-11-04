from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Catalog_page_hoodies(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    hoodie_1 = "/html/body/main/section/div/section[1]/a"

    #Getters

    def get_hoodie_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hoodie_1)))

    #Actions

    def click_hoodie_1(self):
        self.get_hoodie_1().click()
        print("Click hoodie 1")

    # Methods

    def select_hoodie_1(self):
        self.get_current_url()
        self.click_hoodie_1()