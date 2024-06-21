import time
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import os
from selenium.webdriver.common.keys import Keys

paths = r"\"C:\Users\jayasurya"
os.environ["PATH"] += os.pathsep + os.path.dirname(paths)
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver: WebDriver = webdriver.Chrome(options=chrome_options)

# Navigate to the CoWIN URL
driver.get("https://www.cowin.gov.in/")
driver.maximize_window()

# Wait for the page to load
time.sleep(5)
# Find the "FAQ" and "Partners" links
faq_link = driver.find_element(By.XPATH,
                               '/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[4]/a')
partners_link = driver.find_element(By.XPATH,
                                    '/html/body/app-root/app-header/header/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a')

# Open links in new tabs
ActionChains(driver).key_down(Keys.CONTROL).click(faq_link).key_up(Keys.CONTROL).perform()
ActionChains(driver).key_down(Keys.CONTROL).click(partners_link).key_up(Keys.CONTROL).perform()

# Wait for the new tabs to open
time.sleep(4)

# Get all window handles
window_handles = driver.window_handles

# Print the window handles
for index, handle in enumerate(window_handles):
    print(f"Window {index} Handle: {handle}")

# Switch to each window and print the title
for handle in window_handles:
    driver.switch_to.window(handle)
    print(f"Switched to window with handle: {handle}")
    print(f"Title: {driver.title}")
    driver.close()
    
