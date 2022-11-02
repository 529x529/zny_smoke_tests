from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Cart_total_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    customer_firstname = "//input[@id='customer_firstname']"
    customer_lastname = "//input[@id='customer_lastname']"
    customer_telephone = "//input[@id='customer_telephone']"
    customer_email = "//input[@id='customer_email']"
    shipping_address_country = "//select[@id='shipping_address_country_id']"
    shipping_address_zone = "//select[@id='shipping_address_zone_id']"
    shipping_address_city = "//input[@id='shipping_address_city']"
    shipping_address_postcode = "//input[@id='shipping_address_postcode']"
    shipping_address = "//input[@id='shipping_address_address_1']"

    #Getters

    def get_customer_firstname(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.customer_firstname)))

    def get_customer_lastname(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.customer_lastname)))

    def get_customer_telephone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.customer_telephone)))

    def get_customer_email(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.customer_email)))

    def get_shipping_address_country(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_address_country)))

    def get_shipping_address_zone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_address_zone)))

    def get_shipping_address_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_address_city)))

    def get_shipping_address_postcode(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_address_postcode)))

    def get_shipping_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_address)))

    #Actions

    def input_customer_firstname(self, customer_firstname):
        self.get_user_name().send_keys(customer_firstname)
        print("Input customer firstname")

    def input_customer_lastname(self, customer_lastname):
        self.get_user_name().send_keys(customer_lastname)
        print("Input customer lastname")

    def input_customer_telephone(self, customer_telephone):
        self.get_user_name().send_keys(customer_telephone)
        print("Input customer telephone")

    def input_customer_email(self, customer_email):
        self.get_user_name().send_keys(customer_email)
        print("Input customer email")

    def input_customer_email(self, customer_email):
        self.get_user_name().send_keys(customer_email)
        print("Input customer email")

    # Methods

    def checkout(self):
        self.get_current_url()
        self.click_checkout_button()