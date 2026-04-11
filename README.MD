Mi Aplicación Web - Gestión de Equipos y Blog
Este es un proyecto de aplicación web desarrollado con Python y el framework Django. La plataforma permite la gestión de equipos deportivos y la publicación de artículos mediante un sistema de blog, integrando perfiles de usuario personalizados.

Características
Gestión de Equipos (CRUD): Creación, visualización, edición y eliminación de equipos, incluyendo nombre, año de fundación, partidos ganados y escudos.

Sistema de Blog (CRUD): Publicación de posts con títulos, subtítulos y contenido enriquecido.

Autenticación de Usuarios: Sistema completo de registro, inicio de sesión y cierre de sesión.

Perfiles Personalizados: Cada usuario cuenta con un perfil donde puede agregar su biografía, fecha de nacimiento, avatar y seleccionar su equipo favorito.

Editor de Texto Enriquecido: Integración de django-ckeditor para la creación de posts con formato.

Tecnologías Utilizadas
Lenguaje: Python (v3.13)

Framework Web: Django

Gestor de Entorno: Pipenv

Base de Datos: SQLite

Librerías Adicionales:

Pillow: Para el procesamiento y carga de imágenes (escudos y avatares).

django-ckeditor: Para el manejo de contenido enriquecido en los posts.

Instalación y Ejecución Local
Si querés clonar este proyecto y correrlo en tu máquina, seguí estos pasos:

1. Clonar el repositorio
Abrí tu terminal (se recomienda Git Bash) en el directorio deseado y ejecutá:

Bash

git clone https://github.com/thyagomaderna-star/TuPrimeraPagina-Maderna.git
cd TuPrimeraPagina-Maderna
code .
2. Instalar dependencias y entorno virtual
Asegurate de tener Python instalado en tu sistema. Luego, en la terminal de Visual Studio Code, instalá pipenv y las dependencias del proyecto:

Bash

# Instalar pipenv si no lo tenés
pip install pipenv

# Instalar las dependencias desde el Pipfile
pipenv install
3. Ejecutar la aplicación
Una vez instaladas las librerías, activá el entorno y ejecutá el servidor de desarrollo:

Bash

# Activar el entorno virtual
pipenv shell

# Ejecutar el servidor
python manage.py runserver
La aplicación estará disponible en http://127.0.0.1:8000/.