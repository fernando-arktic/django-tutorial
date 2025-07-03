# Django Tutorial Project

- Este repositorio contiene un proyecto base de Django creado para aprender y practicar el framework.
- Se ha seguido este tutorial
    - [Tutotial 01 - Instalación, Crear Proyecto, Crear Aplicación, Crear Vistas](https://docs.djangoproject.com/es/5.2/intro/tutorial01/)
    - [Tutorial 02 - Configuración de la BD, Crear Modelos, Activar Modelos, Migraciones, Uso de la API de Django, Sitio Administrativo de Django, Crear usuario Admin, Explorar sitio administrativo](https://docs.djangoproject.com/es/5.2/intro/tutorial02/)
    - [Tutorial 03 - Implementar más vistas, Vistas con contenido(lectura de plantillas HTML), manejo de errores, Atajos, Nombres de URL](https://docs.djangoproject.com/es/5.2/intro/tutorial03/)
    - [Tutorial 04 - Formulario de votaciones, Modificar las URLs, Modificar las vistas](https://docs.djangoproject.com/es/5.2/intro/tutorial04/)
    - [Tutorial 05 - Test automatizados](https://docs.djangoproject.com/es/5.2/intro/tutorial05/)
    - [Tutorial 06 - Añadir carpeta statics, CSS, Imágenes](https://docs.djangoproject.com/es/5.2/intro/tutorial06/)
    - [Tutorial 07 - ](https://docs.djangoproject.com/es/5.2/intro/tutorial07/)
    

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
    │   ├── settings.py
    │   ├── urls.py
    │   └── ...
    ├── polls/
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   ├── views.py
    │   └── ...
    ├── requirements.txt
    └── .gitignore
---
## 🗳️ App incluida: ``polls``
El proyecto incluye una app llamada ``polls``, desarrollada durante el tutorial oficial de Django.

### ¿Qué hace?
- Muestra preguntas de encuesta.
- Permite a los usuarios votar.
- Visualiza los resultados.

### Tecnologías usadas en ``polls``:
- Modelos (``Question``, ``Choice``)
- Admin de Django
- Vistas basadas en funciones
- Templates HTML
- Manejo de URLs
- Formularios básicos
- Tests

Puedes acceder a la app en:
```cpp
http://127.0.0.1:8000/polls/
```
---

## ✅ Estado del proyecto
✅ Entorno virtual configurado

✅ Django instalado

✅ Proyecto inicial creado

✅ App ``polls`` funcionando

---
## 🛡️ Notas
El entorno virtual ``env/`` está excluido del repositorio mediante ``.gitignore``.

Este proyecto está pensado para desarrollo y aprendizaje.