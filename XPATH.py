import pytest
from selenium import webdriver


# URL address
Svburger = "https://svburger1.co.il/#/HomePage"


# Button signin
sign_in_button1 = "//button[@class='btn btn-primary'][text()='Sign In']"


email_field = '//input[@placeholder="Enter your email"]'


password_field = '//input[@placeholder="Enter your password"]'


sign_in_button2 = '//button[@class="btn btn-primary"]'


kids_meal_choice = '//*[text()="Kids Meal"]'


reserve_button = '//button[normalize-space()="Reserve"]'


footer_scorll = '//H2[text()="SVBURGER WEATHER"]'


send_button1 = '//BUTTON[@class="btn btn-primary"][text()="Send"]/self::BUTTON'


head_line = '//h1'


table1 = '//h3[text()="0"]'


prices = '//*[text()="$ "]'


sign_up_button = '//a[@href="#/SignUp"]'


password_sign_up_field = '//input[@placeholder= "Create Password"]'


password_confirmation_field = '//input[@placeholder= "Confirm Password"]'


sign_up_button2 = '//button[@class="btn btn-primary"][text()="Sign Up"]'


first_name_field = '//INPUT[@class="form-control"][1]'


last_name_field = '//INPUT[@class="form-control"][2]'


combo_meals = '//*[text()="Combo Meal"]'


sides_dish = '//*[text()="Sides"]'


vegan_dish = '//*[text()="Vegan"]'


burger_dish = '//*[text()= "Burger"]'


send_11_char = '//INPUT[@class="form-control"][1]'


log_out_button = '//button[@variant="link"]'


forgot_password_button = '//a[@id="forgotId"]'

Quantity = '//input[@index="0"]'

Table = '(//INPUT[@min="1"])[2]'

Table_text = '//h3[text()="Table No "]'

Location_field = '//input[@id="location-name"]'

Search_Button = '//button[text()="Search"]'


Jerusalem = '//*[@id="root"]/div[2]/div[2]/div/div[2]/div/p[2]/strong'