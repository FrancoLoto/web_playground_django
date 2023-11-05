# Repositorio web_playground_django

Este repositorio contiene una aplicación web simple desarrollada con Django. La aplicación consta de dos páginas:

- Página principal: Muestra una lista de todos los usuarios registrados.
- Página de perfil: Muestra la información del perfil de un usuario específico.

La aplicación está desarrollada usando las siguientes tecnologías:

- Django: Framework web Python
- Python 3.8: Lenguaje de programación
- PostgreSQL: Base de datos relacional

## Instalación

Para instalar la aplicación, siga estos pasos:

1. Clone el repositorio:
   ```bash
   git clone https://github.com/FrancoLoto/web_playground_django.git

2. Instale las dependencias:
   pip install -r requirements.txt

3. Cree una base de datos PostgreSQL:
   createdb web_playground_django
4. Copie el archivo settings.example.py a settings.py y configure la conexión a la base de datos:
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'web_playground_django',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}

5. Migre las tablas de la base de datos:
   python manage.py migrate

6. Cree un superusuario:
   python manage.py createsuperuser

7. Inicie el servidor web:
   python manage.py runserver


Uso
Para acceder a la aplicación, abra un navegador web y vaya a la siguiente URL:

http://localhost:8000/

Documentación
La documentación de la aplicación está disponible en el siguiente enlace:

Documentación

Cambios recientes
2023-07-20: Se agregó la página de perfil.
2023-07-21: Se mejoró la validación de datos.
2023-07-22: Se agregó soporte para PostgreSQL.

La aplicación está dividida en dos partes principales:

La API
La API está desarrollada usando el framework Django REST Framework. Se compone de los siguientes modelos:

User: Representa un usuario registrado en la aplicación.
Profile: Representa el perfil de un usuario.
La API proporciona los siguientes endpoints:

/users: Devuelve una lista de todos los usuarios registrados.
/users/<pk>: Devuelve la información del perfil de un usuario específico.
/users/create: Crea un nuevo usuario.
/users/update/<pk>: Actualiza la información de un usuario.
/users/delete/<pk>: Elimina un usuario.
El frontend
El frontend está desarrollado usando el framework Bootstrap. Se compone de las siguientes vistas:

HomeView: Muestra una lista de todos los usuarios registrados.
ProfileView: Muestra la información del perfil de un usuario específico.
Tests
La aplicación incluye una serie de tests unitarios y de integración que se pueden ejecutar con el siguiente comando:
python manage.py test
