import time
import unittest
import alert_msgs
from pytest_bdd import scenario
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import screenshots
from URL.XPATH import *
from URL.Functions import *




"""sanity test"""
def test_sanity(setup):
    signin_button1(setup)
    email(setup)
    password(setup)
    sign_in_button(setup)
    kids_meal(setup)
    footer(setup)
    reserve(setup)
    send_button(setup)
    table(setup)
    price(setup)
    try:
        assert table == "Table no 1"
    except:
        assert price == "Total: 42.9$"


"""sign up page"""
"""1.1 Functionality – register only with required field"""


def test_sign_up(setup):
    sign_up(setup)
    send_mail(setup)
    passwords(setup)
    conf_pass(setup)
    signup(setup)
    alert(setup)
    txt = setup.switch_to.alert
    text = txt.text
    assert text == "First name must be in English letters only"
    txt.accept()
    print(text)


"""1.2 Functionality – register with 7 chars on First Name"""


def test_first_name(setup):
    sign_up(setup)
    first_name7_char(setup)
    send_mail(setup)
    passwords(setup)
    conf_pass(setup)
    signup(setup)
    alert(setup)
    txt = setup.switch_to.alert
    text_mess = txt.text
    assert text_mess == "Last name must be in English letters only"
    txt.accept()
    print(text_mess)


""" 1.3 Functionality register with email address with .co.il ending:"""


def test_mail_field(setup):
    sign_up(setup)
    first_name(setup)
    last_name(setup)
    send_mailil(setup)
    passwords(setup)
    conf_pass(setup)
    signup(setup)


""" 1.4 Functionality - register with 5 char in password field"""


def test_password_field(setup):
    sign_up(setup)
    first_name(setup)
    last_name(setup)
    send_mail(setup)
    char_5_pass()
    char_5_conf_pass(setup)
    signup(setup)
    print("Password should be at least 6 characters")


"""1.5 Functionality -  Sign up with 11 characters on first name"""


def test_sign_up_with_11_char(setup):
    sign_up(setup)
    send_char(setup)
    last_name(setup)
    send_mail(setup)
    passwords(setup)
    conf_pass(setup)
    signup(setup)
    alert(setup)
    txt = setup.switch_to.alert
    text_mess = txt.text
    assert text_mess == "First name must be between 2 and 10 characters"
    alert(setup).accept()
    print(text_mess)


"""1.1 Error handling - register with hebrew letters in password field"""


def test_password_field1(setup):
    sign_up(setup)
    first_name(setup)
    last_name(setup)
    send_mail(setup)
    heb_eng_pass(setup)
    heb_eng_conf_pass(setup)
    signup(setup)
    combo_meal(setup)
    alert(setup)
    txt = setup.switch_to.alert
    text_mess = txt.text
    assert text_mess == "password must be in english letters only"
    print(text_mess)


"""1.2 Error handling - MISSING FIRST NAME"""


def test_01_missing_first_name(setup):
    sign_up(setup)
    send_mail(setup)
    last_name(setup)
    passwords(setup)
    conf_pass(setup)
    setup.implicitly_wait(10)
    signup(setup)
    alert(setup)
    text = alert(setup).text
    assert text == "First name must be in English letters only"
    alert(setup).accept()
    print(text)


"""sign_in page

2.1 Functionality - insert mail address with ".walla.co.il" ending"""


def test_mail_address_field(setup):
    sign_up(setup)
    first_name(setup)
    last_name(setup)
    send_mail_walla(setup)
    passwords(setup)
    conf_pass(setup)
    signup(setup)
    log_out(setup)
    signin_button(setup)
    email_walla(setup)
    password1(setup)
    sign_in_button(setup)
    combo_meal(setup)
    assert combo_meal(setup)


"""2.2 Functionality - insert mail address with hotmail ending"""


def test_mail_address_field_hotmail(setup):
    sign_up(setup)
    first_name(setup)
    last_name(setup)
    hotmail(setup)
    passwords(setup)
    conf_pass(setup)
    signup(setup)
    log_out(setup)
    signin_button(setup)
    hotmaili(setup)
    password1(setup)
    sign_in_button(setup)


"""2.3 Functionality - click on "forgot password" button"""


def test_forgot_password_button(setup):
    signin_button(setup)
    forgot_password(setup)


"""2.4 Functionality - enter wrong password with correct email address"""


def test_wrong_password(setup):
    signin_button(setup)
    email(setup)
    worng_password(setup)
    sign_in_button(setup)
    txt = alert(setup)
    text_mess = txt.text
    assert text_mess == "Failed to log in"
    print(text_mess)


"""3.5 Functionality – change location weather to Jerusalem"""


def test_weather_jerusalem(setup):
    signin_button(setup)
    clear_location(setup)
    fill_location(setup)
    search_button(setup)
    assert jerusalem(setup) == True


"""2.6 Error Handling - enter mail address without sign up first"""


def test_enter_mail_address(setup):
    signin_button(setup)
    noemail(setup)
    password(setup)
    sign_in_button(setup)
    txt = alert(setup)
    text_mess = txt.text
    assert text_mess == "Failed to log in"
    print(text_mess)


"""2.7 Error Handling -  enter email with no passworrd"""


def test_email(setup):
    signin_button(setup)
    email(setup)
    sign_in_button(setup)
    txt = alert(setup)
    text_mess = txt.text
    assert text_mess == "Failed to log in"
    print(text_mess)


"""SUit 3 Reservation and confirm reservation"""

"""1.1 Functionality – Select 2 meals"""


def test_select_2_meals(setup):
    signin_button(setup)
    email(setup)
    password(setup)
    sign_in_button(setup)
    kids_meal(setup)
    combo_meal_click(setup)
    footer(setup)
    reserve(setup)
    send_button(setup)
    assert table(setup)
    print(table(setup))
    assert price1(setup)
    print(price1(setup))


"""1.2 Functionality – Select same meal twice to cancel order."""


def test_select_same_meal_twice(setup):
    signin_button(setup)
    email(setup)
    password(setup)
    sign_in_button(setup)
    kids_meal(setup)
    kids_meal(setup)
    print("order canceled")


"""1.3 Functionality – press on “Log out”."""


def test_click_on_log_out_button(setup):
    signin_button(setup)
    email(setup)
    password(setup)
    sign_in_button(setup)
    log_out(setup)
    print("log out successful")


#
"""1.4 Functionality – insert 2 in Product / Quantity field."""


def test_insert_2_in_product_field(setup):
    signin_button(setup)
    email(setup)
    password(setup)
    sign_in_button(setup)
    kids_meal(setup)
    footer(setup)
    reserve(setup)
    clear_quantity(setup)
    time.sleep(5)
    quantity(setup)
    send_button(setup)
    assert price2(setup) is False
    print(price2, "is not true")


"""1.5 Functionality - insert number 5 to table number field"""


def test_insert_5_to_table_number_field(setup):
    signin_button(setup)
    email(setup)
    password(setup)
    sign_in_button(setup)
    kids_meal(setup)
    footer(setup)
    reserve(setup)
    clear_table(setup)
    time.sleep(5)
    insert_table_field(setup)
    send_button(setup)
    assert table2(setup) == "Table No 5"
    print(table2(setup))


"""1.6 Error Handling - insert 3 to quantity field"""


def test_insert_number_3(setup):
    signin_button(setup)
    email(setup)
    password(setup)
    sign_in_button(setup)
    kids_meal(setup)
    footer(setup)
    reserve(setup)
    clear_quantity(setup)
    time.sleep(5)
    worng_quantity(setup)
    send_button(setup)
    time.sleep(3)
    assert price3(setup) == "Total: 117$"
    print("Invalid value in quantity")


"""1.7 Error Handling - choose 4 dishes """


def test_choose_4_dish(setup):
    signin_button(setup)
    email(setup)
    password(setup)
    sign_in_button(setup)
    time.sleep(1)
    sides(setup)
    time.sleep(1)
    vegan(setup)
    time.sleep(1)
    kids_meal(setup)
    time.sleep(1)
    burger(setup)
    time.sleep(1)
    footer(setup)
    time.sleep(1)
    reserve(setup)
    time.sleep(1)
    assert headline(setup)
    print("order not be done")
