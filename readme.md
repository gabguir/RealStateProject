# Real State Site

_Sitio web de venta/alquiler de inmuebles desarrollado con Django_

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.


## Pre-requisitos 📋

_Esta es una lista de los paquetes que deben estar instalados previamente:_

* Python 3
	- Lenguaje de programación
	- [Ayuda - https://docs.microsoft.com/en-us/windows/python/beginners)](https://docs.microsoft.com/en-us/windows/python/beginners)
	- [Curso Django desde Cero en youtube](https://www.youtube.com/watch?v=vo4VF3neyrs)

* Pip
	- Gestor de instalación de paquetes PIP
	- [Ayuda - https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/](https://tecnonucleous.com/2018/01/28/como-instalar-pip-para-python-en-windows-mac-y-linux/)

* Virtualenv
	- Creador de entornos virtuales para Python
	- [Ayuda - https://techexpert.tips/es/windows-es/instalacion-del-entorno-virtual-de-python-en-windows/](https://techexpert.tips/es/windows-es/instalacion-del-entorno-virtual-de-python-en-windows/)


## Instalación pre-requisitos 🔧

Muchas veces tenemos ese problema común de no poder instalar ciertas librerías o realizar configuraciones para poder desarrollar en Windows para Web y es por ello que en éste tutorial vamos a ver los pasos para instalar Python y configurarlo con Pip y Virtualenv para así poder empezar a desarrollar aplicaciones basadas en éste lenguaje e instalar Django para crear aplicaciones web. [Ver video -> **https://www.youtube.com/watch?v=sG7Q-r_SZhA**](https://www.youtube.com/watch?v=sG7Q-r_SZhA)

1. Descargamos e instalamos Python 3.6 (o una versión superior) para Windows
	- [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Agregaremos Python a las variables de entorno de nuestro sistema si es que no se agregaron durante la instalación para que así podamos ejecutarlo desde la terminal `/cmd`
	- `C:\Python34 y C:\Python34\Scripts`

3. Ejecutamos Pip para verificar que esté instalado correctamente y también la versión
	- `pip --version`

4. Instalamos Virtualenv con
	- `pip install virtualenv`

5. Verificamos la versión de Virtualenv
	- `virtualenv --version`

6. Crearemos un entorno virtual con Python
	- `virtualenv test`

7. Iniciamos el entorno virtual
	- `.\test\Scripts\activate`

8. Finalmente desactivamos el entorno virtual
	- `deactivate`


## Instalación Local 🚀

Seguir los siguientes pasos para la instalación local.

1. Clonar el repositorio o subir/descargar los archivos.

	- `git clone https://github.com/gabguir/CoderProyectoFinal/tree/master`

2. Instalar los requerimientos.

	- `python3 -m pip install -r requirements.txt`

3. Revisar settings.py y .env
	- Revisar que la sección de base de datos esté configurada para que trabaje con la base de datos SQLite en local.

3. Realizar migraciones
	- Crear archivos de migración: `python3 manage.py makemigrations`
	- Realizar migraciones`python3 manage.py migrate`

4. Crear superusuario
	- `python3 manage.py createsuperuser`
	- Si se usa Cpanel es necesario indicar el encoding primero vía terminal: 
		-`export PYTHONIOENCODING="UTF-8"; python3.6 manage.py createsuperuser`

5. Obtener archivos estáticos
	- `python3 manage.py collectstatic`

6. Iniciar el servidor
	- `python3 manage.py runserver`
	- Iniciar en un puerto específico (:8000):`python3 manage.py runserver 8000`


## Datos de contexto 📦

_Datos de contexto para el uso del sitio web_


### Acceso a sección de administración de Django

URL de acceso: [http://localhost:8000/admin/](http://localhost:8000/admin/)
- Usuario: `admin`
	- Password: `abc123456`

### Usuarios panel de control
URL de acceso: [http://localhost:8000/panel/](http://localhost:8000/panel/)

- Usuario: `admin`
	- Password: `abc123456`

- Usuario: `donald`
	- Password: `user.123456`

- Usuario: `goofy`
	- Password: `user.123456`

- Usuario: `mickey`
	- Password: `user.123456`


### Funcionalidades Sitio Web
URL de acceso: [http://localhost:8000/](http://localhost:8000/)

1. Buscador de inmuebles desde la sección "Inicio"
	- Permite hacer una búsqueda que muestra todos los inmuebles disponibles coincidentes con los términos de búsqueda.

2. Sección "Propiedades"
	- Muestra los datos de de los inmuebles activos. 
	- Presenta un acceso a la vista de detalle de inmuebles.
	- Cada propiedad tiene un formulario de contacto para solicitar más información de ese inmueble.

3. Sección "Agentes"
	- Muestra los datos de los agentes activos. 

4. Sección "Nosotros"
	- Muestra el contenido de la página.

5. Sección "Blog"
	- Muestra los datos de los artículos activos. 
	- Presenta un acceso a la vista de detalle de artículos.

6. Opción "Contacto"
	- Muestra el contenido de la página y el formulario de contacto.


### Funcionalidades Panel de Administración 
URL de acceso: [http://localhost:8000/panel/](http://localhost:8000/panel/)


1. Acceso a través de formulario de login
	- Permite acceder al panel de administración.
	- Muestra información diferenciada entre usuarios del grupo "Agent" y "Admin"

2. Sección de búsqueda
	- Formulario de búsqueda de elementos en el panel de administración. 

3. Sección "Inmuebles"
	- Muestra una lista con los inmuebles activos. 
	- Pueden acceder usuarios de tipo Agente y Admin.
	- Se pueden realizar acciones de creación, ver detalle, modificación, eliminación.

4. Sección "Tipo de inmueble"
	- Muestra una lista con los tipos de inmueble. 
	- Pueden acceder sólo usuarios de tipo Admin.
	- Se pueden realizar acciones de creación, ver detalle, modificación, eliminación.

5. Sección "Agentes"
	- Muestra una lista con los agentes. 
	- Pueden acceder sólo usuarios de tipo Admin.
	- Se pueden realizar acciones de creación, ver detalle, modificación, eliminación.

6. Sección "Páginas"
	- Muestra una lista con las páginas. 
	- Pueden acceder usuarios de tipo Agente y Admin.
	- Se pueden realizar acciones de creación, ver detalle, modificación, eliminación.

7. Sección "Artículos"
	- Muestra una lista con los artículos activos. 
	- Pueden acceder usuarios de tipo Agente y Admin.
	- Se pueden realizar acciones de creación, ver detalle, modificación, eliminación.

8. Sección "Categorías"
	- Muestra una lista con las categorías de artículos. 
	- Pueden acceder usuarios de tipo Agente y Admin.
	- Se pueden realizar acciones de creación, ver detalle, modificación, eliminación.

9. Sección "Mensajes de agentes"
	- Muestra una lista con los mensajes de agentes. 
	- Pueden acceder usuarios de tipo Agente y Admin.
	- Se pueden realizar acciones de creación, ver detalle y eliminación.

10. Sección "Mensajes de propiedades"
	- Muestra una lista con los mensajes de propiedades. 
	- Pueden acceder usuarios de tipo Agente y Admin.
	- Se pueden realizar acciones de ver detalle y eliminación.

11. Sección "Mensajes de contacto"
	- Muestra una lista con los mensajes de contacto. 
	- Pueden acceder usuarios de tipo Agente y Admin.
	- Se pueden realizar acciones de ver detalle y eliminación.

12. Sección "Búsqueda de sitio web"
	- Muestra una lista con los términos de búsqueda del sitio web. 
	- Pueden acceder usuarios de tipo Agente y Admin.
	- Se pueden realizar acciones de ver detalle y eliminación.

13. Sección "Búsqueda de panel admin"
	- Muestra una lista con los términos de búsqueda del panel de administración. 
	- Pueden acceder usuarios de tipo Agente y Admin.
	- Se pueden realizar acciones de ver detalle y eliminación.

14. Sección "Perfil"
	- Muestra los datos del perfil de agente.
	- Pueden acceder usuarios de tipo Agente y Admin.
	- Se pueden realizar acciones de ver detalle y modificación de perfil.

15. Sección "Salir"
	- Permite cerrar la sesión y salir del panel de administración.


## Herramientas de construcción 🛠️

_Estas son las herramientas que hemos utilizado en nuestro proyecto_

* [Django](https://www.djangoproject.com/) - El framework web usado


## Autores ✒️

* **[Gabo Araya](https://github.com/Gabo-araya/)** - *Sitio web, panel de administración y documentación*



