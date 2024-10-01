Pruebas Automatizadas con Selenium + Python

Descripción
Este proyecto contiene pruebas automatizadas para el Test Tecnico, se utiliza Selenium y Python, para garantizar que la aplicación funcione correctamente y cumpla con los requisitos.

Objetivo
El objetivo de estas pruebas automatizadas es:
Caso 1: Validación de campos obligatorios
Caso 2: Registro exitoso
Caso 3: Error por correo electrónico inválido
Caso 4: Error por contraseña corta

Pre requisitos
•	Pycharm
•	Selenium
•	Python

### 1. Instalar Python

1. **Descargar Python**:
   - Visita el [sitio web oficial de Python](https://www.python.org/downloads/).
   - Descarga la última versión adecuada para tu sistema operativo (Windows, macOS, Linux).

2. **Instalar Python**:
   - Ejecuta el instalador y sigue los pasos.
   - Asegúrate de marcar la opción **"Add Python to PATH"** durante la instalación.

3. **Verificar la Instalación**:
   - Abre una terminal (Command Prompt en Windows o Terminal en macOS/Linux) y ejecuta:
     ```bash
     python --version
     ```
   - Deberías ver la versión de Python instalada.

### 2. Instalar PyCharm

1. **Descargar PyCharm**:
   - Ve al [sitio web de JetBrains PyCharm](https://www.jetbrains.com/pycharm/download/).
   - Descarga la versión Community (gratuita) o la versión Professional (de pago) según tus necesidades.

2. **Instalar PyCharm**:
   - Ejecuta el instalador y sigue las instrucciones para completar la instalación.

3. **Crear un Nuevo Proyecto**:
   - Abre PyCharm y selecciona **"New Project"**.
   - Elige la ubicación del proyecto y asegúrate de que se seleccione el intérprete de Python correcto.

### 3. Instalar Selenium

1. **Crear un Entorno Virtual (opcional pero recomendado)**:
   - Abre una terminal y navega al directorio de tu proyecto.
   - Crea un entorno virtual ejecutando:
     ```bash
     python -m venv venv
     ```
   - Activa el entorno virtual:
     - **Windows**:
       ```bash
       venv\Scripts\activate
       ```
     - **macOS/Linux**:
       ```bash
       source venv/bin/activate
       ```

2. **Instalar Selenium**:
   - Con el entorno virtual activado, ejecuta:
     ```bash
     pip install selenium
     ```

3. **Verificar la Instalación de Selenium**:
   - En PyCharm, crea un nuevo archivo Python y añade el siguiente código:
     ```python
     import selenium
     print(selenium.__version__)
     ```
   - Ejecuta el archivo. Si ves la versión de Selenium impresa, la instalación fue exitosa.


Ejecución:
1.	Abrir con Pycharm el archivo Caso1.py ubicado en el directorio RegistroDeUsuarios
2.	Click derecho sobre el archivo Caso1.py y seleccionar la opción Run
3.	Con esto se ejecutan las pruebas y los resultados se muestran en la consola

En el archivo llamado Caso1, se encuentra el código para el caso de prueba Validación de campos obligatorios
Cobertura: 
•	Verificar que los campos "Nombre", "Correo Electrónico" y "Contraseña" están presentes en la página.

En el archivo llamado Caso2, se encuentra el código para el caso de prueba Registro exitoso
Cobertura: 
•	Ingresar un nombre, correo electrónico válido y una contraseña de al menos 6 caracteres.
•	Verificar que, tras hacer clic en el botón de "Registro", aparece un mensaje de éxito o redirige a otra página.

En el archivo llamado Caso3, se encuentra el código para el caso de prueba Error por correo electrónico inválido
Cobertura: 
•	Ingresar un nombre, un correo electrónico en formato incorrecto (e.g. "test.com") y una contraseña válida.
•	Verificar que se muestra un mensaje de error indicando que el correo electrónico no es válido.

En el archivo llamado Caso4, se encuentra el código para el caso de prueba Error por contraseña corta
Cobertura: 
•	Ingresar un nombre, un correo electrónico válido y una contraseña de menos de 6 caracteres.
•	Verificar que se muestra un mensaje de error indicando que la contraseña es demasiado corta.

En el archivo llamado Helpers.py, se encuentra el código con la función redireccionar que sirve para poder llegar al formulario ya que no se puede acceder de manera directa mediante una URL, por lo tanto será necesario copiar ese archivo al proyecto.



