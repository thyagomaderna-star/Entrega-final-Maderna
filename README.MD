# 🏆 Mi Aplicación Web: Gestión de Equipos & Blog

Esta plataforma es una solución integral desarrollada con **Python** y el framework **Django**. Permite la administración técnica de equipos deportivos y la publicación de artículos mediante un sistema de blog, integrando perfiles de usuario personalizados.

---

## 🚀 Características Principales

### ⚽ Gestión de Equipos (CRUD)
Administración completa de entidades deportivas:
* **Creación, visualización, edición y eliminación** de equipos.
* **Datos**: Nombre, año de fundación, partidos ganados y escudos.

### ✍️ Sistema de Blog (CRUD)
Un espacio para compartir contenido:
* **Publicación de posts**: Títulos, subtítulos y contenido enriquecido.
* **Editor Pro**: Integración de `django-ckeditor` para textos con formato.

### 👤 Usuarios y Perfiles
* **Autenticación**: Sistema completo de registro, inicio de sesión y cierre de sesión.
* **Personalización**: Perfiles con biografía, fecha de nacimiento, avatar y equipo favorito.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje**: Python (v3.13) 🐍
* **Framework**: Django 🎸
* **Gestor de Entorno**: Pipenv 📦
* **Base de Datos**: SQLite 🗄️
* **Librerías**:
    * `Pillow`: Procesamiento de imágenes (escudos y avatares).
    * `django-ckeditor`: Contenido enriquecido para posts.

---

## ⚙️ Instalación y Ejecución Local

Si querés clonar este proyecto y correrlo en tu máquina, seguí estos pasos:


Abrí tu terminal (se recomienda Git Bash) en el directorio deseado y ejecutá:
```bash
git clone [https://github.com/thyagomaderna-star/TuPrimeraPagina-Maderna.git](https://github.com/thyagomaderna-star/TuPrimeraPagina-Maderna.git)
cd TuPrimeraPagina-Maderna
code .
# Activar el entorno virtual
pipenv shell

# Ejecutar el servidor
python manage.py runserver


🎥 Video de Demostración
Podés ver el funcionamiento de la aplicación en el siguiente enlace:
