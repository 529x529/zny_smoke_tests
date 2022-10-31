import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.hoodies_page import Hoodies_page
from pages.login_page import Login_page
from pages.main_page import Main_page


def test_buy_hoodie_zny_together():
    driver = webdriver.Chrome(executable_path='/Users/mikhailrezchikov/PycharmProjects/resource/chromedriver')

    print("Start Test")

    mp = Main_page(driver)
    mp.get_driver()
    mp.select_login_page()

    login = Login_page(driver)
    login.autorization()

    mp.select_hoodies_page()

    hp = Hoodies_page(driver)
    hp.select_hoodie_stay_together()




    print("Finish test")
    time.sleep(5)