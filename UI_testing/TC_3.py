'''
Navigate to http://www.uitestingplayground.com/

Go to Text Input, enter any text, click the button and check if the button text is the same as the entered text.

'''

from selenium.webdriver.common.by import By
from selenium import webdriver
from delete_files import delete_file
import time
import os

input_name = input("Please enter your button name: ")
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.uitestingplayground.com/")
driver.set_page_load_timeout(60)
time.sleep(2)

try:
    text_input = driver.find_element(By.XPATH, "//a[@href='/textinput']").click()
    time.sleep(2)

    new_button_name = driver.find_element(By.XPATH, "//input[@id='newButtonName']").send_keys(input_name)
    time.sleep(2)

    update_button = driver.find_element(By.XPATH, "//button[@id='updatingButton']")
    update_button.click()
    time.sleep(2)

    final_name = driver.find_element(By.XPATH, "//button[@id='updatingButton']")

    expected_result = str(input_name)
    actual_result = update_button.text

    if actual_result == expected_result:
        print(f"Test case is passed! New button name matches with button label: {actual_result}")
        driver.save_screenshot(os.path.join(os.path.dirname(__file__), "TC_3_screenshot.png"))
    else:
        print("Test case is failed")

except Exception as e:
    print(f"Error: {e}")

driver.close()

delete_file("TC_3_screenshot.png")
