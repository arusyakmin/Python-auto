'''
Navigate to http://www.uitestingplayground.com/

Go to Progress Bar, click the Start button, then stop it.  Print Duration.

'''

from selenium.webdriver.common.by import By
from selenium import webdriver
from delete_files import delete_file
import time
import re
import os

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.uitestingplayground.com/")
driver.set_page_load_timeout(60)
time.sleep(2)

progress_bar = driver.find_element(By.XPATH, "//a[@href = '/progressbar']").click()
time.sleep(2)

try:
    start_button = driver.find_element(By.XPATH, "//button[@id = 'startButton']").click()
    time.sleep(2)

    stop_button = driver.find_element(By.XPATH, "//button[@id = 'stopButton']").click()
    time.sleep(2)

    result_duration = driver.find_element(By.XPATH, "//p[@id = 'result' and contains(text(), 'duration')]")
    time.sleep(2)

    duration = re.compile(r'duration:\s*(\d+)').search(result_duration.text)
    print(f"Progress duration is: {duration.group(1)}")
    
except Exception as e:
    print(f"Error: {e}")

driver.save_screenshot(os.path.join(os.path.dirname(__file__), "TC_2_screenshot.png"))

driver.close()

delete_file("TC_2_screenshot.png")
