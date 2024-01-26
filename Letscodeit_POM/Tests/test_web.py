import sys
sys.path.append("/Users/Arusyak_Minasyan/Desktop/Python-auto/Letscodeit_POM")
from Lib import Helper
from Pages.google import GoogleSearch
from Pages.login import Login
from Pages.letscodeit import LetsCodeIt
import logging, datetime, data

logging.info(f"The code started at: {datetime.datetime.now()}")

driver = None
helper_obj = Helper() 
driver = helper_obj.driver()

helper_obj.navigate_to_page(driver, data.letskodeit_url)

lets_kod_it_page = LetsCodeIt(driver)
lets_kod_it_page.get_alert_text()
lets_kod_it_page.hide_element_check()
lets_kod_it_page.mouse_hover()
lets_kod_it_page.get_footer_text()

login_page = Login(driver)
login_page.try_to_login()

driver.execute_script("window.open('')")
logging.info("New tab is opened.")
before = driver.window_handles[0]
after = driver.window_handles[1]

driver.switch_to.window(after)
logging.info("Switched to the new tab.")

search_page = GoogleSearch(driver)
helper_obj.navigate_to_page(driver, data.google_url)
search_page.search_in_google(data.phrase)

helper_obj.close_browser(driver)
helper_obj.delete_file(data.delete_log_file)
helper_obj.delete_file(data.delete_txt_file)
helper_obj.delete_file(data.delete_screenshot_file)

print("Test is passed!")
logging.info(f"The code ended at: {datetime.datetime.now()}")
