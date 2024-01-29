from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging
class Helper():

    def __init__(self, driver):
        self.driver = driver

    def navigate_to_page(self, page_url):
        try:
            self.driver.get(page_url)
        except Exception as e:
            logging.info(f"Error navigating to page: {str(e)}")

    def wait_visibility(self, element):
        try:
            elem = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(element))
            return elem
        except TimeoutException:
            logging.info(f"Timeout waiting for element visibility: {str(element)}")
            return None

    def find_and_send_keys(self, element, inp_text):
        elem = self.wait_visibility(element)
        if elem:
            try:
                elem.send_keys(inp_text)
            except Exception as e:
                logging.info(f"Error sending keys to element: {str(e)}")