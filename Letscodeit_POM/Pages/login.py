from selenium.webdriver.common.by import By
from Lib import Helper
import logging, data
from faker import Faker
fake = Faker()

email_data = fake.email()
password_data = fake.password()

class Login(Helper):    
        signin = (By.XPATH, "//a[text()='Sign In']")
        email = (By.XPATH, "//input[@id='email']")
        passwd = (By.XPATH, "//input[@id='login-password']")
        login_btn = (By.ID, "login")
        error_msg = (By.XPATH, "//span[@class='error']")

        def __init__(self, driver):
                super().__init__()
                self.driver = driver
    
        def try_to_login(self):
                self.move_to_element(self.driver, self.signin)
                self.wait_and_click(self.driver, self.signin) 
                self.find_and_send_keys(self.driver, self.email, data.email_data)   
                self.find_and_send_keys(self.driver, self.passwd, data.password_data)
                self.wait_and_click(self.driver, self.login_btn)

                error_message = self.wait_visibility(self.driver, self.error_msg)

                self.write_to_file(error_message.text)
                logging.info(f"Login Error Message: {error_message}")

