from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Hoodies_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    hoodie_stay_together = "//a[@href='http://znyworldwide.com/hoodies/ohd-togetheraw22-blk']"

    #Getters

    def get_hoodie_stay_together(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.hoodie_stay_together)))


    #Actions


    def click_hoodie_stay_together(self):
        self.get_hoodie_stay_together().click()
        print("Click hoodie stay together")

    # Methods

    def select_hoodie_stay_together(self):
        self.get_current_url()
        self.click_hoodie_stay_together()