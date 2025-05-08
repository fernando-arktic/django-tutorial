# Django Tutorial Project

- Este repositorio contiene un proyecto base de Django creado para aprender y practicar el framework.
- Se ha seguido este tutorial
    - [Tutotial 01](https://docs.djangoproject.com/es/5.2/intro/tutorial01/)
    - [Tutorial 02](https://docs.djangoproject.com/es/5.2/intro/tutorial02/)

## 📦 Requisitos

- Python 3.10+
- Git
- pip
---
## 🚀 Primeros pasos

1. Clona el repositorio:

   ```bash
   git clone https://github.com/fernando-arktic/django-tutorial.git
   cd django-tutorial
2. Crea y activa un entorno virtual:
- En Windows:
    ````shell
    python -m venv env
    .\env\Scripts\activate

- En macOS/Linux:
    ````bash
    python3 -m venv env
    source env/bin/activate
3. Instala las dependencias del proyecto:
    ```shell
    pip install -r requirements.txt
4. Ejecuta el servidor de desarrollo:
    ````bash
    python manage.py runserver
5. Abre el navegador y entra a:
    ```cpp
    http://127.0.0.1:8000/
---
## 📁 Estructura del proyecto

    django-tutorial/
    ├── manage.py
    ├── mysite/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    ├── requirements.txt
    └── .gitignore
---
## 🛡️ Notas
El entorno virtual ``env/`` está excluido del repositorio mediante ``.gitignore``.

Este proyecto está pensado para desarrollo y aprendizaje.