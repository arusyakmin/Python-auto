from selenium.webdriver.common.by import By
import time
import logging
import os

logging.basicConfig(
                    level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s',
                    datefmt='%d-%m-%Y %H:%M:%S',
                    filename=os.path.join(os.path.dirname(__file__), "my_logs.log"),
                    filemode='a',
                    encoding='utf-8'
                    )

def search_function(driver):

    driver.maximize_window()

    driver.get("https://www.python.org/")

    search_box = driver.find_element(By.NAME, "q")
    search_box.clear()
    time.sleep(1)

    search_box.send_keys("bla bla")
    time.sleep(1)

    search_box.submit()
    time.sleep(1)  

    try:
        no_results_message = driver.find_element(By.CSS_SELECTOR, "ul.list-recent-events.menu p")
        time.sleep(1)
        if no_results_message.text == "No results found.":
            print("No results found message displayed")
            logging.info("No results found message displayed")
            logging.info("Test is done successfully!")
        else:
            print(f"Unexpected result found: {no_results_message.text}")
            logging.warning(f"Unexpected result found: {no_results_message.text}")
            
    except Exception as e:
        logging.error("Error: 'No results found.' message not found")

    driver.close()
    time.sleep(1)
