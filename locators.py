from selenium.webdriver.common.by import By

class MainPageLocators:
    SIGNUP_LOGIN_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[4]/a")

class LoginPageLocators:
    NEW_USER_SIGNUP_TEXT = (By.XPATH, "//h2[contains(text(),'New User Signup!')]")

class SignupPageLocators:
    ACCOUNT_INFO_TEXT = (By.XPATH, "//h2[contains(text(),'ENTER ACCOUNT INFORMATION')]")
    TITLE_DROPDOWN = (By.ID, "title")
    NAME_INPUT = (By.ID, "name")
    EMAIL_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    DOB_INPUT = (By.ID, "dob")
    NEWSLETTER_CHECKBOX = (By.ID, "newsletter")
    SPECIAL_OFFERS_CHECKBOX = (By.ID, "offers")
    FIRST_NAME_INPUT = (By.ID, "firstname")
    LAST_NAME_INPUT = (By.ID, "lastname")
    COMPANY_INPUT = (By.ID, "company")
    ADDRESS_INPUT = (By.ID, "address1")
    ADDRESS2_INPUT = (By.ID, "address2")
    COUNTRY_DROPDOWN = (By.ID, "country")
    STATE_DROPDOWN = (By.ID, "state")
    CITY_INPUT = (By.ID, "city")
    ZIPCODE_INPUT = (By.ID, "zipcode")
    MOBILE_NUMBER_INPUT = (By.ID, "phone")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//*[@id='form']/div/div/div/div[1]/form/button")
    ACCOUNT_CREATED_TEXT = (By.XPATH, "//h2[contains(text(),'ACCOUNT CREATED!')]")

class AccountPageLocators:
    LOGGED_IN_AS_TEXT = (By.XPATH, "//p[contains(text(),'Logged in as')]")
    DELETE_ACCOUNT_BUTTON = (By.XPATH, "//*[@id='header']/div/div/div/div[2]/div/ul/li[5]/a")
    ACCOUNT_DELETED_TEXT = (By.XPATH, "//h2[contains(text(),'ACCOUNT DELETED!')]")
    CONTINUE_BUTTON = (By.XPATH, "//button[contains(text(),'Continue')]")
