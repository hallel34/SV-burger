import pytest
import alert
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import screenshots
from URL import XPATH
from URL.XPATH import *
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager




@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get(Svburger)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver


"""first sign in button"""


def signin_button1(setup):
    return setup.find_element('xpath', sign_in_button1).click()


"""account from database"""


def email(setup):
    return setup.find_element('xpath', email_field).send_keys("maximnudler4@gmail.com")


"""mail with name"""


def noemail(setup):
    return setup.find_element('xpath', email_field).send_keys(random_char(7) + "@gmail.com")


"""mail with walla.co.il end"""


def email_walla(setup):
    return setup.find_element('xpath', email_field).send_keys("hallel1211@walla.co.il")


"""mail with hotmail.co.il"""


def hotmaili(setup):
    return setup.find_element('xpath', email_field).send_keys("hallel1211@hotmail.co.il")


"""password from database match to def email"""


def password(setup):
    return setup.find_element('xpath', password_field).send_keys("max123")


"""password match to all other mail"""


def password1(setup):
    return setup.find_element('xpath', password_field).send_keys("asdasd")


"""second sign in button"""


def sign_in_button(setup):
    return setup.find_element('xpath', sign_in_button2).click()


"""kids meal button"""


def kids_meal(setup):
    return setup.find_element('xpath', kids_meal_choice).click()


"""reserve button"""


def reserve(setup):
    return setup.find_element('xpath', reserve_button).click()


"""scorling down"""


def footer(setup):
    return setup.find_element('xpath', footer_scorll).location_once_scrolled_into_view


"""send button in order page"""


def send_button(setup):
    return setup.find_element('xpath', send_button1).click()


"""find headline in reserve page"""


def headline(setup):
    return setup.find_element('xpath', head_line).is_displayed()


"""find table number in pop up"""


def table(setup):
    return setup.find_element('xpath', table1).text


"""find price in pop up to sanity test """


def price(setup):
    return setup.find_element('xpath', prices).text


"""find price in pop up to 'combo and kids product in cart' """


def price1(setup):
    return setup.find_element('xpath', prices).text


"""find price in pop up after enter 2 in product field"""


def price2(setup):
    return setup.find_element('xpath', prices).text


"""find price in pop up after add 3 to quantity"""


def price3(setup):
    return setup.find_element('xpath', prices).text


"""sign up first button"""


def sign_up(setup):
    return setup.find_element('xpath', sign_up_button).click()


"""create password"""


def passwords(setup):
    return setup.find_element('xpath', password_sign_up_field).send_keys("asdasd")


"""confirm password"""


def conf_pass(setup):
    return setup.find_element('xpath', password_confirmation_field).send_keys("asdasd")


"""sign up second button"""


def signup(setup):
    return setup.find_element('xpath', sign_up_button2).click()


"""first name field"""


def first_name(setup):
    return setup.find_element('xpath', first_name_field).send_keys("hallel")


def first_name7_char(setup):
    return setup.find_element('xpath', first_name_field).send_keys("hallell")


"""last name field"""


def last_name(setup):
    return setup.find_element('xpath', last_name_field).send_keys("levi")


"""password in heb & eng chars"""


def heb_eng_pass(setup):
    return setup.find_element('xpath', password_sign_up_field).send_keys("שששששש")


"""password 5 char chars"""


def char_5_pass(setup):
    return setup.find_element('xpath', password_sign_up_field).send_keys("aaaaa")


def char_5_conf_pass(setup):
    return setup.find_element('xpath', password_confirmation_field).send_keys("aaaaa")


"""confirm password in heb & eng chars"""


def heb_eng_conf_pass(setup):
    return setup.find_element('xpath', password_confirmation_field).send_keys("שששששש")


"""combo meal displayed"""


def combo_meal_displey(setup):
    return setup.find_element('xpath', combo_meals).is_displayed()


"""combo meal button click"""


def combo_meal_click(setup):
    return setup.find_element('xpath', combo_meals).click()


"""sides button click"""


def sides(setup):
    return setup.find_element('xpath', sides_dish).click()


"""vegan button click"""


def vegan(setup):
    return setup.find_element('xpath', vegan_dish).click()


"""burger button click"""


def burger(setup):
    return setup.find_element('xpath', burger_dish).click()


"""random char for email"""


def random_char(y):
    return ''.join(random.choice(string.ascii_letters) for x in range(y))


"""send mail to mail field"""


def send_mail(setup):
    return setup.find_element('xpath', email_field).send_keys(
        "hallel" + (random_char(1)) + "@gmail.com")


"""send 11 chars"""


def send_char(setup):
    return setup.find_element('xpath', send_11_char).send_keys(random_char(11))


"""swtich to alert"""


def alert(setup):
    return setup.switch_to.alert


"""send mail with co.il end"""


def send_mailil(setup):
    return setup.find_element('xpath', email_field).send_keys(
        "hallel" + (random_char(1)) + "@gmail.co.il")


"""send walla mail sign up"""


def send_mail_walla(setup):
    return setup.find_element('xpath', email_field).send_keys("hallel1211@walla.co.il")


"""log out button"""


def log_out(setup):
    return setup.find_element('xpath', log_out_button).click()


"""send hotmail sign up"""


def hotmail(setup):
    return setup.find_element('xpath', email_field).send_keys("hallel1211@hotmail.co.il")


"""forgot password"""


def forgot_password(setup):
    return setup.find_element('xpath', forgot_password_button).click


"""send worng password"""


def worng_password(setup):
    return setup.find_element('xpath', password_sign_up_field).send_keys("asdasdasdasd")


"""clear quantity"""


def clear_quantity(setup):
    return setup.find_element('xpath', Quantity).clear()


"""send keys to quantity"""


def quantity(setup):
    return setup.find_element('xpath', Quantity).send_keys("2")


"""send worng keys to quantity"""


def worng_quantity(setup):
    return setup.find_element('xpath', Quantity).send_keys("3")


"""clear table field"""


def clear_table(setup):
    return setup.find_element('xpath', Table).clear()


"""send keys to table field"""


def insert_table_field(setup):
    return setup.find_element('xpath', Quantity).send_keys("5")


"""find table text in popup"""


def table2(setup):
    return setup.find_element('xpath', Table_text).text


def clear_location(setup):
    return setup.find_element('xpath', Location_field).clear()


def fill_location(setup):
    return setup.find_element('xpath', Location_field).send_keys("Jerusalem")


def search_button(setup):
    return setup.find_element('xpath', Location_field).click()


def jerusalem(setup):
    return setup.find_element('xpath', Jerusalem).is_displayed()
