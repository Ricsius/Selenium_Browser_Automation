import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WebAutomation():
    def __init__(self):
        self.website = "https://demoqa.com/login"
        chrome_options = Options()
        chrome_options.add_argument("--disable-search-engine-choice-screen")
        prefs = {"download.default_directory": os.getcwd()}
        chrome_options.add_experimental_option("prefs", prefs)
        service = Service("chromedriver-win64/chromedriver.exe")
        self.driver = webdriver.Chrome(options=chrome_options, service=service)

    def login(self, username, password):
        self.driver.get(self.website)

        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
        password_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "password")))
        login_button = self.driver.find_element(By.ID, "login")

        username_field.send_keys(username)
        password_field.send_keys(password)
        self.driver.execute_script("arguments[0].click();", login_button)

    def fill_form(self, fullname, email, current_address, permanent_address):
        elements_dropdown = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
        elements_dropdown.click()

        text_box_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "item-0")))
        text_box_element.click()

        fullname_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "userName")))
        email_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "userEmail")))
        current_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "currentAddress")))
        permanent_address_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "permanentAddress")))
        submit_button = self.driver.find_element(By.ID, "submit")

        fullname_field.send_keys(fullname)
        email_field.send_keys(email)
        current_address_field.send_keys(current_address)
        permanent_address_field.send_keys(permanent_address)
        self.driver.execute_script("arguments[0].click();", submit_button)

    def download_image(self):
        upload_download_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "item-7")))
        upload_download_element.click()

        download_button = self.driver.find_element(By.ID, "downloadButton")
        self.driver.execute_script("arguments[0].click();", download_button)
        time.sleep(3)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    webautomation = WebAutomation()
    webautomation.login(os.getenv("Tools_QA_User"), os.getenv("Tools_QA_Password"))
    webautomation.fill_form("John Smith", "john@gmail.com", "Street 1", "Street 2")
    webautomation.download_image()
    webautomation.close()