from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, SignupPageLocators, AccountPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def click_signup_login_button(self):
        signup_login_button = self.driver.find_element(*MainPageLocators.SIGNUP_LOGIN_BUTTON)
        signup_login_button.click()

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_new_user_signup_text(self):
        return self.driver.find_element(*LoginPageLocators.NEW_USER_SIGNUP_TEXT).is_displayed()

class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_account_info_text(self):
        return self.driver.find_element(*SignupPageLocators.ACCOUNT_INFO_TEXT).is_displayed()

    def enter_signup_details(self, name, email, password, dob, first_name, last_name, company, address, address2, country, state, city, zipcode, mobile_number):
        self.driver.find_element(*SignupPageLocators.TITLE_DROPDOWN).send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        self.driver.find_element(*SignupPageLocators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*SignupPageLocators.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*SignupPageLocators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*SignupPageLocators.DOB_INPUT).send_keys(dob)
        self.driver.find_element(*SignupPageLocators.NEWSLETTER_CHECKBOX).click()
        self.driver.find_element(*SignupPageLocators.SPECIAL_OFFERS_CHECKBOX).click()
        self.driver.find_element(*SignupPageLocators.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*SignupPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*SignupPageLocators.COMPANY_INPUT).send_keys(company)
        self.driver.find_element(*SignupPageLocators.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*SignupPageLocators.ADDRESS2_INPUT).send_keys(address2)
        self.driver.find_element(*SignupPageLocators.COUNTRY_DROPDOWN).send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        self.driver.find_element(*SignupPageLocators.STATE_DROPDOWN).send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        self.driver.find_element(*SignupPageLocators.CITY_INPUT).send_keys(city)
        self.driver.find_element(*SignupPageLocators.ZIPCODE_INPUT).send_keys(zipcode)
        self.driver.find_element(*SignupPageLocators.MOBILE_NUMBER_INPUT).send_keys(mobile_number)

    def click_create_account_button(self):
        self.driver.find_element(*SignupPageLocators.CREATE_ACCOUNT_BUTTON).click()

    def verify_account_created_text(self):
        return self.driver.find_element(*SignupPageLocators.ACCOUNT_CREATED_TEXT).is_displayed()

class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_logged_in_as_text(self):
        return self.driver.find_element(*AccountPageLocators.LOGGED_IN_AS_TEXT).is_displayed()

    def click_delete_account_button(self):
        self.driver.find_element(*AccountPageLocators.DELETE_ACCOUNT_BUTTON).click()

    def verify_account_deleted_text(self):
        return self.driver.find_element(*AccountPageLocators.ACCOUNT_DELETED_TEXT).is_displayed()

    def click_continue_button(self):
        self.driver.find_element(*AccountPageLocators.CONTINUE_BUTTON).click()
