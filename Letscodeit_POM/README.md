This project's main goal is to practise with selenium selectors, wait functions and POM format.
Installation

To run this project, you need to have Selenium installed. You can install it using the following command:
 - pip install selenium

Usage

- letscodeit.py
letscodeit.py contains the main code with the following steps:

1.Open Chrome browser
2.Navigate to https://www.letskodeit.com/practice
3.Click to open the Alert popup
4.Get text from the popup
5.Open txt file with live_coding_text.txt file name and write there popup text
6.Locate the following element, hide it, then add txt file the attribute and value based on which it shows up and hides
7.Scroll and click on the Mouse Hover button and Click on Top option to go to the top of the screen
8.Go to the footer and write text in the opened file


- login.py
login.py contains the main code with the following steps:

1.Click on the Sign In button
2.Fill the fields with incorrect email or password and click the Log In button
3.Get validation message and write in the txt file

- google.py
google.py contains the main code with the following steps:

1.Open a new tab, switch to the new tab
2.Get google.com on the second tab
3.Search the Automation word
4.Write in the opened file the results of the count and add in txt
5.Come back to the first tab
6.Close the driver with two tabs


- test.py
test.py contains all calls based on the provided scenario.

- Lib.py
Lib.py contains all helper functions, including:
1.navigate_to_page
2.move_to_element
3.wait_and_click
4.find_elem_dom
5.wait_visibility
6.find_and_send_keys
7.close_browser
8.delete_file

- letscodeit.py
letscodeit.py contains all locators and test cases for the 'Lets code it' website.

- login.py
login.py contains all locators and test cases for the 'Lets code it' website's login page.

 - google.py
google.py contains all locators and test cases for the 'Google' website.

