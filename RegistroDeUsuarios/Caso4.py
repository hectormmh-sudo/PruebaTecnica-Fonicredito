import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Curso.Clases import redireccionar

driver = webdriver.Chrome()
redireccionar(driver)

driver.implicitly_wait(5)

user_name = "Hector11"
last_name = "Martinez11"
email = "hector10@hector11.com"
phone = "1234567890"
password = "1111"
expected_length_password_error = "Password must be 8 Character Long!"


#Insertar nombre
driver.find_element(By.ID, "firstName").send_keys(user_name)
driver.find_element(By.ID, "lastName").send_keys(last_name)

#Insertar email y telefono
driver.find_element(By.ID, "userEmail").send_keys(email)
driver.find_element(By.ID, "userMobile").send_keys(phone)

#Seleccionar ocupacion
occupation_dropdown = Select(driver.find_element(By.CLASS_NAME,"custom-select"))
occupation_dropdown.select_by_visible_text("Engineer")

#Seleccionar genero
driver.find_element(By.CSS_SELECTOR, "input[value='Male']").click()

#Insertar contrasena y confirmar contrasena
driver.find_element(By.ID, "userPassword").send_keys(password)
driver.find_element(By.ID, "confirmPassword").send_keys(password)

#Check box de 18 anos
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()

#Click en registrar
driver.find_element(By.ID, "login").click()


#Validacion de contrasena menor a 8 caracteres
error_contrasena = driver.find_element(By.CSS_SELECTOR, "div[role='alert']").text
assert error_contrasena == expected_length_password_error

if error_contrasena == expected_length_password_error:
    print("Mensaje de contrasena menor a 8 caracteres presente - prueba exitosa")
else:
    print("Prueba fallida")

