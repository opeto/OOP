from selenium import webdriver #imports the necessary libraries: webdriver for browser automation,
from selenium.webdriver.common.by import By #for locating elements, 
from selenium.webdriver.chrome.options import Options #for Chrome configuration

# Deprecated - no longer needed
#chrome_driver_path = "/Users/philippmuellauer/Development/chromedriver" #commented out because it's no longer needed in this particular code setup

# keeps chrome open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chrome_options)

def test_eight_components():
    driver.get("https://www.selenium.dev/selenium/web/web-form.html") # Opens the specified URL in Chrome
    title = driver.title # Checks if the title matches the expected title ("Web form")
    assert title == "Web form"
    driver.implicitly_wait(0.5) #Waits for 0.5 seconds for elements to load
    text_box = driver.find_element(by=By.NAME, value="my-text") # Finds the element named "my-text" (text box)
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button") #For finding the element with the CSS selector "button" (submit button)
    text_box.send_keys("Selenium") # Enters text "Selenium" into the text box
    submit_button.click()  # Clicks the submit button
    message = driver.find_element(by=By.ID, value="message")  #Finds the element with the ID "message" (message box)
    value = message.text  #Gets the text of the message box
    assert value == "Received!" #Checks if the message text matches "Received!"

    # Closes Chrome
    # driver.quit()
    driver.close() #Closes the current Chrome window without quitting the entire browser


test_eight_components()
