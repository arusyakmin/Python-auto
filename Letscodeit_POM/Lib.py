from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import shutil
import os, data
import logging

logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename=os.path.join(os.path.dirname(__file__), "my_logs.log"),
                    filemode='a',
                    encoding='utf-8'
                    )

class Helper:
    
    def driver(self): 
        try:
            driver = webdriver.Chrome()
            driver.maximize_window()
            return driver
        except Exception as e:
            print(f"Error creating driver: {e}")
    
    def navigate_to_page(self, driver, page_url):
        try:
            driver.get(page_url)
        except Exception as e:
            print(f"Error navigating to page: {e}")
        
    def move_to_element(self, driver, element):
        try:
            locator = driver.find_element(*element)
            driver.execute_script("arguments[0].scrollIntoView();", locator)
        except Exception as e:
            print(f"Error moving to element: {e}")


    def wait_and_click(self, driver, element):
        try:
            elem = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((element)))
            elem.click()
        except Exception as e:
            print(f"Error waiting and clicking: {e}")
    
    def find_elem_dom(self, driver, loc, sec=20):
        try:
            elem = WebDriverWait(driver, sec).until(
                EC.presence_of_element_located(loc))
            return elem
        except Exception as e:
            print(f"Error finding element in DOM: {e}")

    def wait_visibility(self, driver, element):
        try:
            elem = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(element))
            return elem
        except Exception as e:
            print(f"Error waiting for element visibility: {e}")
    
    def find_and_send_keys(self, driver, element, inp_text):
        try:
            elem = Helper().wait_visibility(driver, element)
            elem.send_keys(inp_text)
        except Exception as e:
            print(f"Error finding element and sending keys: {e}")
    
    def close_browser(self, driver):
        try:
            if driver:
                driver.quit()
        except Exception as e:
            print(f"An error occurred while closing the browser: {e}")

    def write_to_file(self, text_to_write):
        try:
            with open(os.path.join(os.path.dirname(__file__), data.file_name), 'a+') as f:
                f.write(f'{str(text_to_write)}\n')
        except Exception as e:
            print(f"Error writing to file: {e}")

    def create_screenshot(self, driver, screen): 
        folder_path = os.path.join(os.path.dirname(__file__), data.folder_name)       
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            driver.save_screenshot(os.path.join(folder_path, screen))
        except Exception as e:
            print(f"Error creating screenshot: {e}")

    def delete_file(self, files):
        file_path = os.path.join(os.path.dirname(__file__), files)
        try:
            if os.path.exists(file_path):
                if os.path.isdir(file_path):
                    confirm = input(f"Do you want to remove '{files}' folder and its contents? (yes/no): ")
                    if confirm.lower() == "yes":
                        shutil.rmtree(file_path)
                        print(f"'{files}' folder and its contents have been deleted.")
                    elif confirm.lower() == "no":
                        print(f"'{files}' folder hasn't been deleted.")
                    else:
                        print(f"'{files}' folder hasn't been deleted, because of incorrect input.")
                else:
                    confirm = input(f"Do you want to remove '{files}' file? (yes/no): ")
                    if confirm.lower() == "yes":
                        os.remove(file_path)
                        print(f"'{files}' file has been deleted.")
                    elif confirm.lower() == "no":
                        print(f"'{files}' file hasn't been deleted.")
                    else:
                        print(f"'{files}' file hasn't been deleted, because of incorrect input.")
            else:
                print(f"'{files}' does not exist.")
        except Exception as e:
            print(f"Error occurred while deleting '{files}'. Exception: {e}")