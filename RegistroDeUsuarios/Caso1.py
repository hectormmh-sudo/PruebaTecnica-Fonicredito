import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from Curso.Clases import redireccionar

driver = webdriver.Chrome()
redireccionar(driver)


#Caso 1: Validación de campos obligatorios
#Verificar que los campos "Nombre", "Correo Electrónico" y "Contraseña" están presentes en la página.

#Validacion Nombre presente
nombre = (driver.find_element(By.XPATH, "//label[text()='First Name']").text)
assert nombre == "First Name"
if nombre == "First Name":
    print("Nombre presente en la pagina - prueba exitosa")
else:
    print("Prueba fallida")


#Validacion Correo presente
correo = (driver.find_element(By.XPATH, "//label[text()='Email']").text)
assert correo == "Email"
if correo == "Email":
    print("Correo presente en la pagina - - prueba exitosa")


#Validacion Contrasena presente
contrasena = (driver.find_element(By.XPATH, "//label[text()='Password']").text)
assert contrasena == "Password"
if contrasena == "Password":
    print("Contrasena presente en la pagina - prueba exitosa")

