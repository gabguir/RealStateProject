# NOTAS GENERALES

Notas generales para configuraciones del proyecto

## CONFIGURACIÓN LOCAL 
* Crear entorno virtual
	- `python3 -m venv /home/gabo/envs/coderhouse/env`
* Activar entorno virtual
    - `source /home/gabo/envs/coderhouse/env/bin/activate`
* Conocer los paquetes instalados en el env
	- `pip3 freeze > requirements.txt`
* Instalar los requerimientos
	- `python3 -m pip install -r requirements.txt`


## CONFIGURACIÓN DJANGO
* Instalar Django
	- `pip3 install django==3.2`
* Crear proyecto core 
	- `django-admin startproject core . `
* Realizar migraciones 
	- `python3 manage.py makemigrations`
    - `python3 manage.py makemigrations --check`
    - `python3 manage.py migrate`
* Crear un superusuario
	- `python3 manage.py createsuperuser`
* Instalar requerimientos
	- `python3 -m pip install -r requirements.txt`
* Correr servidor
	- `python3 manage.py runserver`


## APPS CREADAS
* contiene lógica de login y recuperacion de password
	- `python3 manage.py startapp login`
* contiene artículos de blog (FrontEnd)
	- `python3 manage.py startapp blog`
* contiene panel de administración (BackEnd)
	- `python3 manage.py startapp panel`


## INSTALAR PAQUETES
* Filtros automáticos en tablas
	- `pip3 install django-filter`
* Trabajar con imágenes
	- `python3 -m pip install Pillow`
* Usar mysql
	- `pip3 install mysqlclient`
* Trabajar con static files en el mismo servidor cpanel
	- `pip3 install whitenoise`
* Esconder datos importantes en github
	- `pip3 install python-decouple`
* Trabajar con Choices en selects
	- `pip3 install django-model-utils`


## ENTIDADES
 - Inmuebles
 - Clientes
 - Agentes
 - Paginas
 - Artículos
 - Categorías


## COMANDOS GIT
* git add -A
* git commit -m "commit"
* git push -u origin agrega_agentes


## ACCESO LOGIN ADMIN DJANGO
* Usuario: `admin`
* Password: `abc123456`
