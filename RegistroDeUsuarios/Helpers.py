import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



def redireccionar(_driver):
    driver = _driver
    driver.get("https://rahulshettyacademy.com/client/")
    driver.maximize_window()
    driver.find_element(By.LINK_TEXT, "Register").click()
    time.sleep(5)