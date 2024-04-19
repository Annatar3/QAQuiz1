import unittest
from selenium import webdriver
from actions import MainPage, LoginPage, SignupPage, AccountPage

class TestSignup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationexercise.com')
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.signup_page = SignupPage(self.driver)
        self.account_page = AccountPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_signup_flow(self):
       
        self.main_page.click_signup_login_button()

        
        self.assertTrue(self.login_page.verify_new_user_signup_text())

        
        self.signup_page.enter_signup_details(
            name="John Doe",
            email="johndoe@example.com",
            password="Password123",
            dob="01/01/1990",
            first_name="John",
            last_name="Doe",
            company="ABC Company",
            address="123 Main St",
            address2="Apt 101",
            country="United States",
            state="California",
            city="Los Angeles",
            zipcode="90001",
            mobile_number="1234567890"
        )

        
        self.signup_page.click_create_account_button()

        
        self.assertTrue(self.signup_page.verify_account_info_text())

        
        self.assertTrue(self.signup_page.verify_account_created_text())

        
        self.signup_page.click_continue_button()

        
        self.assertTrue(self.account_page.verify_logged_in_as_text())

        
        self.account_page.click_delete_account_button()

        
        self.assertTrue(self.account_page.verify_account_deleted_text())

        
        self.account_page.click_continue_button()

if __name__ == "__main__":
    unittest.main()
