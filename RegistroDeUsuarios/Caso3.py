import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from RegistroDeUsuarios.Helpers import redireccionar

driver = webdriver.Chrome()
redireccionar(driver)

user_name = "Hector11"
last_name = "Martinez11"
email = "hector10hector11.com"
phone = "1234567890"
password = "Pa$$w0rd"
expected_invalid_email_error = "*Enter Valid Email"


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

#Validacion del mensaje de error de formato incorrecto de email
error_email = (driver.find_element(By.XPATH, "(//div[@class='invalid-feedback'])[1]").text)
assert error_email == "*Enter Valid Email"
if error_email== expected_invalid_email_error:
    print("Mensaje de correo electrónico en formato incorrecto presente - prueba exitosa")
else:
    print("Prueba fallida")

time.sleep(5)


