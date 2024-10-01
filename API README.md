Pruebas de API con Postman
Requisitos:
 Postman instalado. 
 Acceso a la API. 

Ejecución de las Pruebas

Caso 1: Prueba de solicitud GET exitosa
API: https://jsonplaceholder.typicode.com
Endpoint: /users
Pasos para ejecutar:

1.	Abrir Postman
2.	Selecciona el método GET para ver registros
3.	Ingresar la API en el campo
4.	Utilizar el endpoint descrito arriba
5.	Click en Send
6.	Validar respuesta

Resultado Actual:
Muestra una respuesta 200 OK
Muestra el listado de usuarios existentes (10 usuarios)

Resultado Esperado:
Debería mostrar una respuesta 200 OK
Debería mostrar el listado de usuarios existentes

Conclusión:
La API funciona correctamente
Caso 2: Prueba de creación de usuario (POST)
API: https://jsonplaceholder.typicode.com
Endpoint: /users
JSON
{ "name": "Héctor Martínez", "email": "hector.martinez@example.com", "username": "hectormmh" }
Pasos para ejecutar:

1.	Abrir Postman
2.	Selecciona el método POST
3.	Ingresar la API en el campo
4.	Agregar los parámetros name, email y username
5.	Utilizar el endpoint y JSON descritos arriba
6.	Click en Send
7.	Validar respuesta

Resultado Actual:
Muestra una respuesta 201 Created
Muestra el ID del usuario creado y la fecha y hora de creación, sin embargo no crea el usuario

Resultado Esperado:
Debería mostrar una respuesta 201 Created
Debería mostrar la creación de usuario
El usuario debería guardarse y poder ser validado con el método GET
No debería ser posible crear un usuario sin el parámetro mandatorio email

Conclusión:
La API no funciona correctamente

Caso 3: Prueba de error en creación de usuario (POST)
API: https://jsonplaceholder.typicode.com
Endpoint: /users
JSON
{ "name": "Héctor Martínez", "email": "hector.martinez@example.com", "username": "hectormmh" }
Pasos para ejecutar:
1.	Abrir Postman
2.	Selecciona el método POST
3.	Ingresar la API en el campo
4.	Agregar los parámetros name y username, omitir el parámetro email
5.	Utilizar el endpoint y JSON descritos arriba
6.	Click en Send
7.	Validar respuesta

Resultado Actual:
Muestra una respuesta 201 Created
Muestra el ID del usuario creado y la fecha y hora de creación, sin embargo no crea el usuario
No valida que los parámetros name, email y username sean mandatorios para la creación de un usuario
Se muestra la respuesta como si el usuario hubiera sido creado pero pero no se guarda

Resultado Esperado:
Debería mostrar una respuesta 201 Created
Debería mostrar la creación de usuario
El usuario debería guardarse y poder ser validado con el método GET
No debería ser posible crear un usuario sin el parámetro mandatorio email
Conclusión:
La API no funciona correctamente
