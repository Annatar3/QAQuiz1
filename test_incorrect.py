import unittest
from selenium import webdriver
from actions import MainPage, LoginPage

class TestLoginWithIncorrectCredentials(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://automationexercise.com')
        self.main_page = MainPage(self.driver)
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_login_with_incorrect_credentials(self):
        # Step 1: Click on 'Signup / Login' button
        self.main_page.click_signup_login_button()

        # Step 2: Verify 'Login to your account' is visible
        self.assertTrue(self.login_page.verify_login_to_account_text())

        # Step 3: Enter incorrect email address and password
        self.login_page.login(email="incorrect@example.com", password="IncorrectPassword")

        # Step 4: Click 'login' button
        self.login_page.click_login_button()

        # Step 5: Verify error 'Your email or password is incorrect!' is visible
        self.assertTrue(self.login_page.verify_error_message("Your email or password is incorrect!"))

if __name__ == "__main__":
    unittest.main()
