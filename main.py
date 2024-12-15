import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

WEBSITE = "https://demoqa.com/login"
USERNAME = os.getenv("Tools_QA_User")
PASSWORD = os.getenv("Tools_QA_Password")

def get_chrome_driver():
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    service = Service("chromedriver-win64/chromedriver.exe")
    driver = webdriver.Chrome(options=chrome_options, service=service)

    return driver

def login(driver):
    username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
    password_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = driver.find_element(By.ID, "login")

    username_field.send_keys(USERNAME)
    password_field.send_keys(PASSWORD)
    driver.execute_script("arguments[0].click();", login_button)

def navigate_to_form(driver):
    elements_dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
    elements_dropdown.click()

    text_box_element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "item-0")))
    text_box_element.click()

def fill_form(driver):
    fullname_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
    email_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "userEmail")))
    current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "currentAddress")))
    permanent_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "permanentAddress")))
    submit_button = driver.find_element(By.ID, "submit")

    fullname_field.send_keys("John Smith")
    email_field.send_keys("john@gmail.com")
    current_address_field.send_keys("John Street 100, New York, USA")
    permanent_address_field.send_keys("John Street 100, New York, USA")
    driver.execute_script("arguments[0].click();", submit_button)

driver = get_chrome_driver()

driver.get(WEBSITE)
login(driver)
navigate_to_form(driver)
fill_form(driver)

input("Press Enter to close the browser")
driver.quit()