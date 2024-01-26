from selenium.webdriver.common.by import By
import time, logging
from Lib import Helper


class LetsCodeIt(Helper):

    alert_btn = (By.ID, "alertbtn")
    hide_textbox = (By.ID, "hide-textbox")
    diplayed_txt = (By.ID, "displayed-text")
    mouse_hover_elem = (By.XPATH, "//button[@id = 'mousehover']")
    top_option = (By.XPATH, "//div[@class='mouse-hover-content']/a[text()='Top']")
    footer_style = (By.CLASS_NAME, "footer-style")
    copyright_txt = (By.XPATH, "//p[@class='small dynamic-text jqCopyRight']")

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        
    def get_alert_text(self):
        try:
            self.wait_and_click(self.driver, self.alert_btn)
            popup = self.driver.switch_to.alert

            self.write_to_file(popup.text)
            logging.info(f"Alert Text: {popup.text}")
            popup.accept()

        except Exception as e:
            logging.error(f"Error in handling alert - {e}")
            self.create_screenshot(self.driver, f"{e}.png")

    def hide_element_check(self):
        try:
            self.wait_and_click(self.driver, self.hide_textbox)
            time.sleep(2)
            style_attribute = self.find_elem_dom(self.driver, self.diplayed_txt).get_attribute('style')

            self.write_to_file(f'Hidden attribute is - {style_attribute}')
            logging.info(f"Textbox Style Attribute: {style_attribute}")

        except Exception as e:
            logging.error(f"Error in handling textbox - {e}")
            self.create_screenshot(self.driver, f"{e}.png")
                
    def mouse_hover(self):
        try:
            self.move_to_element(self.driver, self.mouse_hover_elem)
            self.wait_and_click(self.driver, self.mouse_hover_elem)
            self.wait_and_click(self.driver, self.top_option)
            logging.info("Successfully performed mouse hover and clicked on top option.")

        except Exception as e:
            logging.error(f"Error in handling top-option - {e}")
            self.create_screenshot(self.driver, f"{e}.png")

    def get_footer_text(self):
        try:
            self.wait_visibility(self.driver, self.footer_style)
            footer_txt = self.find_elem_dom(self.driver, self.copyright_txt).text
            self.write_to_file(footer_txt)
            logging.info(f"Footer Text: {footer_txt}")

        except Exception as e:
            logging.error(f"Error in handling footer - {e}")
            self.create_screenshot(self.driver, f"{e}.png")