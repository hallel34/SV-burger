import time

import alert
from telnetlib import EC
import pytest
import selenium
import image
from pages.lis_first_name import lis_first_name
from pages.lis_password import lis_password
from pages.lis_email import lis_emali_address
from pages.lis_last_name import lis_last_name
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


@pytest.fixture()
def setup():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(executable_path=r'C:\selenium\chromedriver.exe')
    driver.get("https://svburger1.co.il/#/HomePage")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver


"""sanity test"""

def test_sanity(setup):
    driver=setup
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("maximnudler4@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("max123")
    press_sign_in = driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    click_on_kids_meal = driver.find_element_by_xpath('//h5[@class="card-title"][text()="Kids Meal"]').click()
    click_on_reserve_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()= " Reserve "]').click()
    find_footer = driver.find_element_by_xpath('//H2[text()="SVBURGER WEATHER"]').location_once_scrolled_into_view
    driver.implicitly_wait(20)
    driver.find_element_by_xpath('//BUTTON[@class="btn btn-primary"][text()="Send"]/self::BUTTON').click()
    table_num0 = driver.find_element_by_xpath('//h3[text()="0"]').text
    print(table_num0)
    price = driver.find_element_by_xpath('//h2[text() ="39"]').text
    print(price)

"""sign up page"""

"""1.1 Functionality – register only with required field"""

def test_sign_up(setup):
    driver = setup
    sign_up_button = driver.find_element_by_xpath('//a[@href="#/SignUp"]').click()
    insert_mail__address = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("h4214134@gmail.com")
    insert_password = driver.find_element_by_xpath('//input[@placeholder= "Create Password"]').send_keys("asdasd")
    confirm_password = driver.find_element_by_xpath('//input[@placeholder= "Confirm Password"]').send_keys("asdasd")
    sign_up_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("First name must be in English letters only")
    except TimeoutException:
        print("alert does not Exist in page")



"""1.2 Functionality – register with 7 chars on First Name"""

def test_first_name(setup):
    driver = setup
    click_the_sign_up_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    insert_7_chars = driver.find_element_by_xpath('//input[@placeholder="Type your first name"]').send_keys("hallell")
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("halell22@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Create Password"]').send_keys('asdasd')
    confirm_password = driver.find_element_by_xpath('//input[@placeholder="Confirm Password"]').send_keys('asdasd')
    driver.implicitly_wait(30)
    driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("Last name must be in English letters only")
    except TimeoutException:
        print("alert does not Exist in page")
#
#

""" 1.3 Functionality - register with hebrew letters  in password field"""

def test_password_field(setup,):
    driver = setup
    click_the_sign_up_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    insert_name = driver.find_element_by_xpath('//INPUT[@class="form-control"][1]').send_keys("hallel")
    insert_lname = driver.find_element_by_xpath('//INPUT[@class="form-control"][2]').send_keys("levi")
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("agad3q35r32@gmail.com")
    insert_heb_letters_in_password_field = driver.find_element_by_xpath('//input[@placeholder="Create Password"]').send_keys("שששששש")
    insert_heb_letters_in_confirm_password_field = driver.find_element_by_xpath('//input[@placeholder="Confirm Password"]').send_keys("שששששש")
    click_the_sign_up_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    assert driver.find_element_by_xpath('//h5[text()="Combo Meal"]').is_displayed() is False
    print("password must be in English letters only")




"""1.4 Functionality - register with hebrew and english letters in password field"""

def test_password_field1(setup):
    driver = setup
    click_the_sign_up_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    insert_name = driver.find_element_by_xpath('//INPUT[@placeholder="Type your first name"]').send_keys("hallell")
    insert_lname = driver.find_element_by_xpath('//INPUT[@placeholder="Type your last name"]').send_keys("levi")
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("halell2322322@gmail.com")
    insert_heb_letters_in_password_field = driver.find_element_by_xpath('//input[@placeholder="Create Password"]').send_keys("ששששaa")
    insert_heb_letters_in_confirm_password_field = driver.find_element_by_xpath('//input[@placeholder="Confirm Password"]').send_keys("ששששaa")
    click_the_sign_up_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("password must be in english letters only")
    except TimeoutException:
        print("alert does not Exist in page")


""" 1.5 Functionality register with email address with .co.il ending:"""

def test_mail_field1(setup):
    driver = setup
    click_the_sign_up_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    insert_name = driver.find_element_by_xpath('//INPUT[@class="form-control"][1]').send_keys("hallell")
    insert_lname = driver.find_element_by_xpath('//INPUT[@class="form-control"][2]').send_keys("levi")
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("halell2225522@gmail.co.il")
    insert_heb_letters_in_password_field = driver.find_element_by_xpath('//input[@placeholder="Create Password"]').send_keys("asdasd")
    insert_heb_letters_in_confirm_password_field = driver.find_element_by_xpath('//input[@placeholder="Confirm Password"]').send_keys("asdasd")
    click_the_sign_up_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("Error: The email address is badly formatted.")
    except TimeoutException:
        print("alert does not Exist in page")

"""1.1 Error handilng - MISSING FIRST NAME"""

def test_01_missing_first_name(setup):
    driver = setup
    click_the_sign_up_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallel1331@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Create Password"]').send_keys('asdasd')
    confirm_password = driver.find_element_by_xpath('//input[@placeholder="Confirm Password"]').send_keys('asdasd')
    click_on_sign_up = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    alert = driver.switch_to.alert
    text = alert.text
    assert text == "First name must be in English letters only"
    alert.accept()


"""1.2 Error Handling -  Sign up with 11 characters on first name"""

def test_sign_up_with_11_char(setup):
    driver = setup
    click_the_sign_up_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    insert_11_char_to_name_field = driver.find_element_by_xpath('//INPUT[@class="form-control"][1]').send_keys("hallelevi10")
    insert_last_name = driver.find_element_by_xpath('//INPUT[@class="form-control"][2]').send_keys("levi")
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallelle434vi@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Create Password"]').send_keys('asdasd')
    confirm_password = driver.find_element_by_xpath('//input[@placeholder="Confirm Password"]').send_keys('asdasd')
    click_on_sign_up = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    alert = driver.switch_to.alert
    text = alert.text
    assert text == "First name must be between 2 and 10 characters"
    alert.accept()




"""sign_in page

2.1 Functionality - insert mail address with ".walla.co.il" ending"""

def test_mail_address_field(setup):
    driver = setup
    sign_up_button = driver.find_element_by_xpath('//a[@href="#/SignUp"]').click()
    insert_name = driver.find_element_by_xpath('//INPUT[@class="form-control"][1]').send_keys("hallell")
    insert_lname = driver.find_element_by_xpath('//INPUT[@class="form-control"][2]').send_keys("levi")
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallelkl4234kkl@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Create Password"]').send_keys('asdasd')
    confirm_password = driver.find_element_by_xpath('//input[@placeholder="Confirm Password"]').send_keys('asdasd')
    click_on_sign_up = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    click_on_log_out_button = driver.find_element_by_xpath('//button[@variant="link"]').click()
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallel@gmail.com")
    password_field = driver.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("asdasd")
    press_sign_in = driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    assert driver.find_element_by_xpath('//h5[text()="Combo Meal"]').is_displayed()

"""2.2 Functionality - insert mail address with ending"""


def test_mail_address_field_hotmail(setup):
    driver = setup
    sign_up_button = driver.find_element_by_xpath('//a[@href="#/SignUp"]').click()
    insert_name = driver.find_element_by_xpath('//INPUT[@class="form-control"][1]').send_keys("hallell")
    insert_lname = driver.find_element_by_xpath('//INPUT[@class="form-control"][2]').send_keys("levi")
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallel4234@hotmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Create Password"]').send_keys('asdasd')
    confirm_password = driver.find_element_by_xpath('//input[@placeholder="Confirm Password"]').send_keys('asdasd')
    click_on_sign_up = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    click_on_log_out_button = driver.find_element_by_xpath('//button[@variant="link"]').click()
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallel@hotmail.com")
    password_field = driver.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("asdasd")
    press_sign_in = driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()


"""2.3 Functionality - click on "forgot password" button"""

def test_forgot_password_button(setup):
    driver = setup
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    forgot_password_button = driver.find_element_by_xpath('//a[@id="forgotId"]').click


"""2.4 Functionality - enter wrong password with correct email address"""

def test_worng_password(setup):
    driver = setup
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("hallel34324@hotmail.com")
    password_field = driver.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("asdasdasdasd")
    press_sign_in = driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("Failed to log in")
    except TimeoutException:
        print("alert does not Exist in page")


"""2.5 Functionality - enter mail address without sign up first"""

def test_enter_mail_adrress(setup):
    driver = setup
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("moria4234@gmail.com")
    password_field = driver.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("asdasd")
    press_sign_in = driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    try:
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
        print("Failed to log in")
    except TimeoutException:
        print("alert does not Exist in page")


"""1.2 Error Handling -  enter email with hebrew letters"""

def test_email(setup):
    driver=setup
    sign_up_button = driver.find_element_by_xpath('//a[@href="#/SignUp"]').click()
    insert_name = driver.find_element_by_xpath('//INPUT[@class="form-control"][1]').send_keys("hallell")
    insert_lname = driver.find_element_by_xpath('//INPUT[@class="form-control"][2]').send_keys("levi")
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("הלל@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Create Password"]').send_keys('asdasd')
    confirm_password = driver.find_element_by_xpath('//input[@placeholder="Confirm Password"]').send_keys('asdasd')
    click_on_sign_up = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign Up"]').click()
    assert email == False, print("The email address is badly formatted")


"""SUit 3 Reservation and confirm reservation"""

# 1.1 Functionality – Select 2 meals
def test_select_2_meals(setup):
    driver = setup
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("maximnudler4@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("max123")
    press_sign_in = driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    click_on_kids_meal = driver.find_element_by_xpath('//h5[@class="card-title"][text()="Kids Meal"]').click()
    click_on_combo_meal = driver.find_element_by_xpath('//h5[text()="Combo Meal"]').click()
    find_footer = driver.find_element_by_xpath('//H2[text()="SVBURGER WEATHER"]').location_once_scrolled_into_view
    click_on_reserve_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()= " Reserve "]').click()
    driver.implicitly_wait(20)
    driver.find_element_by_xpath('//BUTTON[@class="btn btn-primary"][text()="Send"]/self::BUTTON').click()
    tablenum0 = driver.find_element_by_xpath('//h3[text()="0"]').text
    assert tablenum0
    print(tablenum0)
    price = driver.find_element_by_xpath('//h2[text() ="98"]').text
    assert price
    print(price)

"""1.2 Functionality – Select same meal twice to cancel order."""

def test_select_same_meal_twice(setup):
    driver = setup
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("maximnudler4@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("max123")
    press_sign_in = driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    click_on_kids_meal = driver.find_element_by_xpath('//h5[@class="card-title"][text()="Kids Meal"]').click()
    click_on_kids_meal = driver.find_element_by_xpath('//h5[@class="card-title"][text()="Kids Meal"]').click()


"""1.3 Functionality – press on “Log out”."""

def test_click_on_log_out_button(setup):
    driver = setup
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("maximnudler4@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("max123")
    press_sign_in = driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    press_log_out = driver.find_element_by_xpath('//button[@class = "btn btn-primary"] [1]').click()

"""1.4 Functionality – insert 4 in Product / Quantity field."""

def test_insert_4_in_product_field(setup):
    driver = setup
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("maximnudler4@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("max123")
    press_sign_in = driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    click_on_kids_meal = driver.find_element_by_xpath('//h5[@class="card-title"][text()="Kids Meal"]').click()
    click_on_reserve_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()= " Reserve "]').click()
    find_fotter = driver.find_element_by_xpath('//H2[text()="SVBURGER WEATHER"]').location_once_scrolled_into_view
    insert_4_in_product_field = driver.find_element_by_xpath('//input[@index="0"]').send_keys("4")
    click_on_send_button = driver.find_element_by_xpath('//BUTTON[@class="btn btn-primary"][text()="Send"]/self::BUTTON').click()
    price = driver.find_element_by_xpath('//h2[text() ="546"]').text
    assert price is False
    print(price)


"""1.5 Functionality - insert number 5 to table number field"""

def test_insert_5_to_table_number_field(setup):
    driver = setup
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("maximnudler4@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("max123")
    press_sign_in = driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    click_on_kids_meal = driver.find_element_by_xpath('//h5[@class="card-title"][text()="Kids Meal"]').click()
    click_on_reserve_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()= " Reserve "]').click()
    find_fotter = driver.find_element_by_xpath('//H2[text()="SVBURGER WEATHER"]').location_once_scrolled_into_view
    clear_table_number_field = driver.find_element_by_xpath('(//INPUT[@min="1"])[2]').clear()
    insert_5_in_product_field =driver.find_element_by_xpath('(//INPUT[@min="1"])[2]').send_keys("5")
    driver.implicitly_wait(30)
    time.sleep(45)
    driver.implicitly_wait(50)
    click_on_send_button = driver.find_element_by_xpath('//BUTTON[@class="btn btn-primary"][text()="Send"]/self::BUTTON').click()
    table_num = driver.find_element_by_xpath('//h3[text()="5"]').is_displayed()


"""1.6 Error Handling - insert number 123 to coupon field"""

def test_insert_number_123(setup):
    driver = setup
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("maximnudler4@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("max123")
    press_sign_in = driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    click_on_kids_meal = driver.find_element_by_xpath('//h5[@class="card-title"][text()="Kids Meal"]').click()
    click_on_reserve_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()= " Reserve "]').click()
    find_fotter = driver.find_element_by_xpath('//H2[text()="SVBURGER WEATHER"]').location_once_scrolled_into_view
    driver.implicitly_wait(20)
    coupon_field = driver.find_element_by_xpath('//input[@placeholder="XXX"]').send_keys("123")
    click_on_send_button = driver.find_element_by_xpath('//BUTTON[@class="btn btn-primary"][text()="Send"]/self::BUTTON').click()

"""1.7 Error Handling - choose all dishes """

def test_choose_all(setup):
    driver = setup
    sign_in_btn = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()="Sign In"]').click()
    email = driver.find_element_by_xpath('//input[@placeholder="Enter your email"]').send_keys("maximnudler4@gmail.com")
    password = driver.find_element_by_xpath('//input[@placeholder="Enter your password"]').send_keys("max123")
    press_sign_in = driver.find_element_by_xpath('//button[@class="btn btn-primary"]').click()
    choose_sides_dish = driver.find_element_by_xpath('(//DIV[@class="card text-center mb-3"])[4]').click()
    choose_vegan_dish = driver.find_element_by_xpath('(//DIV[@class="col-md-8"])[4]').click()
    choose_combo_dish = driver.find_element_by_xpath('(//DIV[@class="card-body"])[1]').click()
    choose_burger_dish = driver.find_element_by_xpath('(//DIV[@class="card-body"])[3]').click()
    choose_kids_dish = driver.find_element_by_xpath('//h5[@class="card-title"][text()="Kids Meal"]').click()
    click_on_reserve_button = driver.find_element_by_xpath('//button[@class="btn btn-primary"][text()= " Reserve "]').click()
    assert driver.find_element_by_xpath('//h1').is_displayed() == False

