

import unittest
import pytest
import alert
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import assertion
import pdb
import time
import random
import string

@pytest.fixture()
def setup():
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    driver = webdriver.Chrome(executable_path=r'C:\selenium\chromedriver.exe')
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver


"""first sign in button"""
def signin_button(setup):
    return setup.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()

"""account from database"""
def email(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("maximnudler4@gmail.com")

"""mail with name"""
def noemail(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys(random_char(7)+"@gmail.com")

"""mail with walla.co.il end"""
def email_walla(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallel1211@walla.co.il")

"""mail with hotmail.co.il"""
def hotmaili(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallel1211@hotmail.co.il")

"""password from database match to def email"""
def password(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("max123")

"""password match to all other mail"""
def password1(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("asdasd")

"""second sign in button"""
def sign_in_button(setup):
    return setup.find_element_by_xpath('//button[@class="btn btn-primary"]').click()

"""kids meal button"""
def kids_meal(setup):
    return setup.find_element_by_xpath('//*[text()="Kids Meal"]').click()

"""reserve button"""
def reserve(setup):
    return setup.find_element_by_xpath('//button[normalize-space()="Reserve"]').click()

"""scorling down"""
def footer(setup):
    return setup.find_element_by_xpath('//H2[text()="SVBURGER WEATHER"]').location_once_scrolled_into_view

"""send button in order page"""
def send_button(setup):
    return setup.find_element_by_xpath('//BUTTON[@class="btn btn-primary"][text()="Send"]/self::BUTTON').click()

"""find headline in reserve page"""
def headline(setup):
    return setup.find_element_by_xpath('//h1').is_displayed()

"""find table number in pop up"""
def table(setup):
    return setup.find_element_by_xpath('//h3[text()="0"]').text

"""find price in pop up to sanity test """
def price(setup):
    return setup.find_element_by_xpath('//*[text()="$ "]').text

"""find price in pop up to 'combo and kids product in cart' """
def price1(setup):
    return setup.find_element_by_xpath('//*[text() ="Total: 98$"]').text

"""find price in pop up after enter 2 in product field"""
def price2(setup):
    return setup.find_element_by_xpath('//*[text() ="Total: 78$"]').text

"""find price in pop up after add 3 to quantity"""
def price3(setup):
    return setup.find_element_by_xpath('//*[text() ="117"]').text

"""sign up first button"""
def sign_up(setup):
    return setup.find_element_by_xpath('//a[@href="#/SignUp"]').click()

"""create password"""
def passwords(setup):
    return setup.find_element_by_xpath('//input[@placeholder= "Create Password"]').send_keys("asdasd")

"""confirm password"""
def conf_pass(setup):
    return setup.find_element_by_xpath('//input[@placeholder= "Confirm Password"]').send_keys("asdasd")

"""sign up second button"""
def signup(setup):
    return setup.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()

"""first name field"""
def first_name(setup):
    return setup.find_element_by_xpath('//INPUT[@class="form-control"][1]').send_keys("hallel")

def first_name7_char(setup):
    return setup.find_element_by_xpath('//INPUT[@class="form-control"][1]').send_keys("hallell")
"""last name field"""
def last_name(setup):
    return setup.find_element_by_xpath('//INPUT[@class="form-control"][2]').send_keys("levi")
"""password in heb & eng chars"""
def heb_eng_pass(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Create Password"]').send_keys("שששששש")
"""password 5 char chars"""
def char_5_pass(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Create Password"]').send_keys("aaaaa")
def char_5_conf_pass(setup):
    return setup.find_element_by_xpath('//input[@placeholder= "Confirm Password"]').send_keys("aaaaa")
"""confirm password in heb & eng chars"""
def heb_eng_conf_pass(setup):
    return setup.find_element_by_xpath('//input[@placeholder= "Confirm Password"]').send_keys("שששששש")
"""combo meal displayed"""
def combo_meal(setup):
    return setup.find_element_by_xpath('//*[text()="Combo Meal"]').is_displayed()
"""combo meal button click"""
def combo_meal_click(setup):
    return setup.find_element_by_xpath('//*[text()="Combo Meal"]').click()
"""sides button click"""
def sides(setup):
    return setup.find_element_by_xpath('//*[text()="Sides"]').click()
"""vegan button click"""
def vegan(setup):
    return setup.find_element_by_xpath('//*[text()="Vegan"]').click()
"""burger button click"""
def burger(setup):
    return setup.find_element_by_xpath('//*[text()= "Burger"]').click()
"""random char for email"""
def random_char(y):
       return ''.join(random.choice(string.ascii_letters) for x in range(y))

"""send mail to mail field"""
def send_mail(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallel"+(random_char(1))+"@gmail.com")
"""send 11 chars"""
def send_char(setup):
    return setup.find_element_by_xpath('//INPUT[@class="form-control"][1]').send_keys(random_char(11))
"""swtich to alert"""
def alert(setup):
    return setup.switch_to.alert
"""send mail with co.il end"""
def send_mailil(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallel"+(random_char(1))+"@gmail.co.il")
"""send walla mail sign up"""
def send_mail_walla(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallel1211@walla.co.il")
"""log out button"""
def log_out(setup):
    return setup.find_element_by_xpath('//button[@variant="link"]').click()
"""send hotmail sign up"""
def hotmail(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallel1211@hotmail.co.il")
"""forgot password"""
def forgot_password(setup):
    return setup.find_element_by_xpath('//a[@id="forgotId"]').click
"""send worng password"""
def worng_password(setup):
    return setup.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("asdasdasdasd")
"""clear quaantity"""
def clear_quantity(setup):
    return setup.find_element_by_xpath('//input[@index="0"]').clear()
"""send keys to quantity"""
def quantity(setup):
        return setup.find_element_by_xpath('//input[@index="0"]').send_keys("2")

"""send worng keys to quantity"""
def worng_quantity(setup):
    return setup.find_element_by_xpath('//input[@index="0"]').send_keys("3")
"""clear table field"""
def clear_table(setup):
    return setup.find_element_by_xpath('(//INPUT[@min="1"])[2]').clear()
"""send keys to table field"""
def insert_table_field(setup):
    return setup.find_element_by_xpath('(//INPUT[@min="1"])[2]').send_keys("5")
"""find table text in popup"""
def table2(setup):
    return setup.find_element_by_xpath('//h3[text()="Table No "]').text
def clear_location(setup):
    return setup.find_element_by_xpath('//input[@id="location-name"]').clear()
def fill_location(setup):
    return setup.find_element_by_xpath('//input[@id="location-name"]').send_keys("Jerusalem")
def search_button(setup):
    return setup.find_element_by_xpath('//button[text()="Search"]').click()
def jerusalem(setup):
    return setup.find_element_by_xpath('//*[@id="root"]/div[2]/div[2]/div/div[2]/div/p[2]/strong').is_displayed()
