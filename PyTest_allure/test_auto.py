import logging, time, datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helpers import Helper

def test_search_auto(driver):
        
        logging.info(f"The code started at: {datetime.datetime.now()}")

        inp_search = (By.ID, "searchInp")
        submit = (By.ID, "submit_search")
        result_of_search = (By.XPATH, "//button[@id='research-btn']//span")
        url = "https://auto.am/"
        search_text = "kia"
        helper_obj = Helper(driver)

        helper_obj.navigate_to_page(url)
        helper_obj.find_and_send_keys(inp_search, search_text)
        time.sleep(2)
        
        helper_obj.wait_visibility(inp_search).send_keys(Keys.ENTER)
        logging.info(f"Performed search with data: {search_text}")
        search_result = helper_obj.wait_visibility(result_of_search)

        search_result = int(search_result.text)
        assert search_result > 1, "There is no such result."
        logging.info(f'Search result is: {search_result}')

        logging.info(f"The code ended at: {datetime.datetime.now()}")
# TODO, no need to put test scenario in  try except, use exception handling inside methods declaration.
#Nel, working code, good job