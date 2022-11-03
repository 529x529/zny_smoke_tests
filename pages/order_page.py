from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Order_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    customer_firstname = "//input[@id='customer_firstname']"
    customer_lastname = "//input[@id='customer_lastname']"
    customer_telephone = "//input[@id='customer_telephone']"
    customer_email = "//input[@id='customer_email']"
    shipping_address_country = "//select[@id='shipping_address_country_id']"
    country_id_russia = "//option[@value='176']"
    shipping_address_zone = "//select[@id='shipping_address_zone_id']"
    zone_id_moscow = "//option[@value='2761']"
    shipping_address_city = "//input[@id='shipping_address_city']"
    shipping_address_postcode = "//input[@id='shipping_address_postcode']"
    shipping_address = "//input[@id='shipping_address_address_1']"
    courier_delivery_radio_button = "//span[@class='order__radio__name radio__name' and contains(text(), 'Курьерская доставка по Москве')]"
    payment_method_credit_card = "//span[@class='order__radio__name radio__name' and text()='Банковская карта онлайн']"
    create_order_button = "//button[@id='orderButton']"

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

    def get_country_id_russia(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.country_id_russia)))

    def get_shipping_address_zone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_address_zone)))

    def get_zone_id_moscow(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.zone_id_moscow)))

    def get_shipping_address_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_address_city)))

    def get_shipping_address_postcode(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_address_postcode)))

    def get_shipping_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.shipping_address)))

    def get_courier_delivery_radio_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.courier_delivery_radio_button)))

    def get_payment_method_credit_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.payment_method_credit_card)))

    def get_create_order_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.create_order_button)))

    #Actions

    def input_customer_firstname(self, customer_firstname):
        self.get_customer_firstname().send_keys(customer_firstname)
        print("Input customer firstname")

    def input_customer_lastname(self, customer_lastname):
        self.get_customer_lastname().send_keys(customer_lastname)
        print("Input customer lastname")

    def input_customer_telephone(self, customer_telephone):
        self.get_customer_telephone().send_keys(customer_telephone)
        print("Input customer telephone")

    def input_customer_email(self, customer_email):
        self.get_customer_email().send_keys(customer_email)
        print("Input customer email")

    def select_country_id_russia(self):
        self.get_country_id_russia().click()
        print("Select shipping address russia")

    def select_zone_id_moscow(self):
        self.get_zone_id_moscow().click()
        print("Select zone id moscow")

    def input_shipping_address_city(self, shipping_address_city):
        self.get_shipping_address_city().send_keys(shipping_address_city)
        print("Input shipping address city")

    def input_shipping_address_postcode(self, shipping_address_postcode):
        self.get_shipping_address_postcode().send_keys(shipping_address_postcode)
        print("Input shipping address postcode")

    def input_shipping_address(self, shipping_address):
        self.get_shipping_address().send_keys(shipping_address)
        print("Input shipping address")

    def click_courier_delivery_radio_button(self):
        self.get_courier_delivery_radio_button().click()
        print("Click courier cdek radio button")

    def click_payment_method_credit_card(self):
        self.get_payment_method_credit_card().click()
        print("Click payment method credit card")

    def click_create_order_button(self):
        self.get_create_order_button().click()
        print("Click create order button")

    #Methods

    def create_order(self):
        self.get_current_url()
        # self.input_customer_firstname("Ivan")
        # self.input_customer_lastname("Ivan")
        # self.input_customer_telephone("70000000000")
        # self.select_country_id_russia()
        # self.select_zone_id_moscow()
        # self.input_shipping_address_city("Moscow")
        # self.input_shipping_address_postcode("123123")
        # self.input_shipping_address("Ivanovskaya street, 11")
        self.click_courier_delivery_radio_button()
        self.click_payment_method_credit_card()
        self.click_create_order_button()
