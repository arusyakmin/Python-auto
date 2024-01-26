'''
Navigate to http://www.uitestingplayground.com/

Go to Visibility, click the Hide button. Check in your program that buttons are hidden.

'''

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from delete_files import delete_file
import time
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.uitestingplayground.com/")
driver.set_page_load_timeout(60)
time.sleep(2)

def check_buttons_visibility():
        button_ids = ['removedButton', 'zeroWidthButton', 'overlappedButton',
                'transparentButton', 'invisibleButton', 'notdisplayedButton', 'offscreenButton']
        time.sleep(2)
        for button_id in button_ids:
            try:
                button = driver.find_element(By.XPATH, f"//button[@id='{button_id}']")
                
                if button.is_displayed():
                    print(f"The button with ID '{button_id}' is visible.")
                else:
                    print(f"The button with ID '{button_id}' is hidden.")
                               
            except NoSuchElementException:
                    print(f"The button with ID '{button_id}' is not found.")

            except Exception as e:
                    print(f"Error: {e}")


visibility = driver.find_element(By.XPATH, "//a[@href='/visibility']").click()
time.sleep(2)

check_buttons_visibility()

hide_button = driver.find_element(By.XPATH, "//button[@id='hideButton']").click()
time.sleep(2)

check_buttons_visibility()
driver.save_screenshot(os.path.join(os.path.dirname(__file__), "TC_1_screenshot.png"))

driver.close()

delete_file("TC_1_screenshot.png")
