'''
Step 1) Open browser
Step 2) Navigate to python.org
Step 3) Search bla bla text
Step 4) Click on Go button
Step 5) Check that No results found. text display in page
Step 6) Close driver


Technical solution
Do the following in all type of browsers(Chrome and Firefox). Make for loop for sequence.
Handle exceptions
Use Logging

'''
from selenium import webdriver
import delete_log_file
import search_engine
import logging
import datetime

logging.info(f"The code started at: {datetime.datetime.now()}")

browsers = ["Chrome", "Safari"]

for browser in browsers:
    if browser == "Chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Safari()
    search_engine.search_function(driver)

logging.info(f"The code ended at: {datetime.datetime.now()}")

logging.shutdown()
delete_log_file.delete_file("lesson_22", "my_logs.log")
