from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re, logging, time
from Lib import Helper

class GoogleSearch(Helper):

    google_search = (By.NAME, "q")
    result_of_search = (By.XPATH, "//div[@id='result-stats']")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def search_in_google(self, phrase):
        try:
            self.find_and_send_keys(self.driver, self.google_search, phrase)
            self.find_elem_dom(self.driver, self.google_search).send_keys(Keys.ENTER)
            time.sleep(2)
            logging.info(f"Performed Google search with data: {phrase}")
            search_result = self.wait_visibility(self.driver, self.result_of_search).text
            logging.info(f"Found search result: {search_result}")
            print(search_result)

            match = re.search(r'\b([\d,]+)\b', search_result)

            if match:
                count = match.group(1).replace(',', '')
                self.write_to_file(count)
                logging.info(f"Match found. Count written to file: {count}")
            else:
                logging.warning("No match found in search result.")
                print("No match found.")   
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            self.create_screenshot(self.driver, f"{e}.png")