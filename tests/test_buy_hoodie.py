import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_total_page import Cart_total_page
from pages.catalog_page_hoodies import Catalog_page_hoodies
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.order_page import Order_page
from pages.product_page import Product_size_page

@allure.description("Test buy hoodie 1")
def test_buy_hoodie_1(set_up):
    driver = webdriver.Chrome(executable_path='/Users/mikhailrezchikov/PycharmProjects/resource/chromedriver')

    mp = Main_page(driver)
    mp.get_driver()
    mp.select_login_page()

    login = Login_page(driver)
    login.autorization()

    mp.select_hoodies_page()

    cph = Catalog_page_hoodies(driver)
    cph.select_hoodie_1()

    psp = Product_size_page(driver)
    psp.select_product()

    mp.select_cart_total_page()

    ctp = Cart_total_page(driver)
    ctp.checkout()

    op = Order_page(driver)
    op.create_order_payment_method_credit_card()

    driver.quit()