# CineSpoilers - Aplicación Django REST

## 📺 Descripción General

CineSpoilers es una API REST desarrollada con Django y Django REST Framework para gestionar un catálogo de películas con géneros asociados, reseñas de usuarios, búsqueda avanzada y sistema de usuarios.

---

## 🎯 Funcionalidades Principales (Laboratorio del 26 de Abril de 2026)

### ✅ 1. Entidad Género

**Descripción:**
- Permite categorizar películas por géneros (Drama, Acción, Ciencia Ficción, etc.)
- Relación muchos a muchos (M2M) con Movie
- Cada película puede tener múltiples géneros

**Endpoints:**
```
GET    /api/genres/                  # Listar todos los géneros
POST   /api/genres/                  # Crear nuevo género
GET    /api/genres/{id}/             # Ver detalles del género
PUT    /api/genres/{id}/             # Actualizar género
PATCH  /api/genres/{id}/             # Actualización parcial
DELETE /api/genres/{id}/             # Eliminar género
```

**Ejemplo de Género:**
```json
{
  "id": 1,
  "name": "Acción",
  "description": "Películas de acción y aventura",
  "created_at": "2026-04-26T10:00:00Z",
  "updated_at": "2026-04-26T10:00:00Z"
}
```

**Captura de Pantalla:**
![Géneros en Admin](doc%20de%20capturas/CP1.PNG)

---

### ⭐ 2. Entidad Reseña

**Descripción:**
- Permite que usuarios califiquen películas del 1 al 5
- Asociadas directamente a cada película
- Incluye comentarios opcionales
- Visualización de calificación con estrellas (⭐)

**Endpoints:**
```
GET    /api/reseñas/                 # Listar todas las reseñas
POST   /api/reseñas/                 # Crear nueva reseña
GET    /api/reseñas/{id}/            # Ver detalles de reseña
PUT    /api/reseñas/{id}/            # Actualizar reseña
PATCH  /api/reseñas/{id}/            # Actualización parcial
DELETE /api/reseñas/{id}/            # Eliminar reseña
```

**Ejemplo de Reseña:**
```json
{
  "id": 1,
  "movie": 1,
  "rating": 5,
  "rating_stars": "⭐⭐⭐⭐⭐",
  "comment": "Película excelente, muy recomendada",
  "created_at": "2026-04-26T11:30:00Z",
  "updated_at": "2026-04-26T11:30:00Z"
}
```

**Captura de Pantalla:**
![Reseñas en API](doc%20de%20capturas/CP2.PNG)

---

### 🔍 3. Búsqueda por Filtros

**Descripción:**
- Búsqueda avanzada por título, sinopsis y géneros
- Filtrado por fecha de lanzamiento, estado activo y rating promedio
- Paginación automática para resultados grandes

**Endpoints:**
```
GET    /api/películas/?search=acción    # Búsqueda por texto
GET    /api/películas/?genre=1         # Filtrar por género
GET    /api/películas/?year=2020       # Filtrar por año
GET    /api/películas/?rating_min=4    # Rating mínimo
```

**Ejemplo de Búsqueda:**
```json
{
  "count": 25,
  "next": "http://127.0.0.1:8000/api/películas/?page=2",
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "Inception",
      "genres": ["Acción", "Ciencia Ficción"],
      "average_rating": 4.8,
      "release_date": "2010-07-16"
    }
  ]
}
```

**Captura de Pantalla:**
![Búsqueda y Filtros](doc%20de%20capturas/CP3.PNG)

---

### 👤 4. Sistema de Usuarios

**Descripción:**
- Autenticación de usuarios con JWT tokens
- Registro y login de usuarios
- Perfiles de usuario con reseñas personales
- Permisos para crear/editar reseñas

**Endpoints:**
```
POST   /api/auth/register/            # Registro de usuario
POST   /api/auth/login/               # Login y obtener token
GET    /api/auth/profile/             # Perfil del usuario
GET    /api/users/{id}/reviews/       # Reseñas del usuario
```

**Ejemplo de Login:**
```json
{
  "username": "usuario1",
  "password": "password123"
}
```

**Respuesta:**
```json
{
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...",
  "user": {
    "id": 1,
    "username": "usuario1",
    "email": "usuario1@example.com"
  }
}
```

**Captura de Pantalla:**
![Sistema de Usuarios](doc%20de%20capturas/CP4.PNG)

---

## 🎬 Entidad Película (Base)

Las películas incluyen todos los campos nuevos:

**GET /api/películas/{id}/**
```json
{
  "id": 1,
  "title": "Inception",
  "synopsis": "Un ladrón experto en extracción de secretos...",
  "duration_minutes": 148,
  "release_date": "2010-07-16",
  "is_active": true,
  "genres": [
    {
      "id": 1,
      "name": "Ciencia Ficción",
      "description": "Películas de ciencia ficción"
    },
    {
      "id": 3,
      "name": "Acción",
      "description": "Películas de acción"
    }
  ],
  "reviews": [
    {
      "id": 1,
      "user": "usuario1",
      "rating": 5,
      "rating_stars": "⭐⭐⭐⭐⭐",
      "comment": "Masterpiece"
    }
  ],
  "average_rating": 4.8,
  "created_at": "2026-04-26T09:00:00Z",
  "updated_at": "2026-04-26T09:30:00Z"
}
```

---

## 🌐 Endpoints Principales

### 🎥 Películas
```
GET    /api/películas/               # Listar películas (con filtros)
POST   /api/películas/               # Crear película
GET    /api/películas/{id}/          # Ver película
PUT    /api/películas/{id}/          # Actualizar película
DELETE /api/películas/{id}/          # Eliminar película
```

### 🏷️ Géneros
```
GET    /api/genres/                  # Listar géneros
POST   /api/genres/                  # Crear género
GET    /api/genres/{id}/             # Ver género
```

### ⭐ Reseñas
```
GET    /api/reseñas/                 # Listar reseñas
POST   /api/reseñas/                 # Crear reseña
GET    /api/reseñas/{id}/            # Ver reseña
```

### 👤 Autenticación
```
POST   /api/auth/register/           # Registro
POST   /api/auth/login/              # Login
GET    /api/auth/profile/            # Perfil
```

---

## 🚀 Instalación y Ejecución

### 1. Activar Entorno Virtual
```powershell
cd "c:\Tecsup\Django -proyects\Lab-05\cinespoilers\Cinespoller"
..\.venv\Scripts\Activate.ps1
```

### 2. Aplicar Migraciones
```powershell
python manage.py makemigrations movies
python manage.py migrate
```

### 3. Crear Superusuario
```powershell
python manage.py createsuperuser
```

### 4. Ejecutar Servidor
```powershell
python manage.py runserver
```

---

## 🌍 Acceso a la Aplicación

- **Admin Django:** `http://127.0.0.1:8000/admin/`
- **API Browsable:** `http://127.0.0.1:8000/api/`
- **Películas:** `http://127.0.0.1:8000/api/películas/`
- **Géneros:** `http://127.0.0.1:8000/api/genres/`
- **Reseñas:** `http://127.0.0.1:8000/api/reseñas/`

---

## 📝 Cómo Usar la Aplicación

### Crear un Género
```json
POST /api/genres/
{
  "name": "Comedia",
  "description": "Películas cómicas"
}
```

### Asignar Géneros a una Película
```json
PUT /api/películas/{id}/
{
  "genre_ids": [1, 3, 5]
}
```

### Crear una Reseña
```json
POST /api/reseñas/
{
  "movie_id": 1,
  "rating": 4,
  "comment": "Buena película"
}
```

### Búsqueda Avanzada
```json
GET /api/películas/?search=acción&genre=1&rating_min=4
```

---

## 🔍 Características Destacadas

✅ **Interfaz completamente en español**
✅ **Calificación con estrellas**
✅ **Búsqueda y filtrado avanzado**
✅ **Sistema de autenticación JWT**
✅ **API RESTful completa**
✅ **Admin Django personalizado**

---

## 📦 Dependencias

- Django 6.0.4
- Django REST Framework
- Django REST Framework Simple JWT
- Python 3.13.13

---

## 📅 Historial de Desarrollo

**26 de Abril de 2026 - Laboratorio**
- ✅ Agregada entidad Género con relación M2M
- ✅ Agregada entidad Reseña con calificación
- ✅ Implementada búsqueda por filtros
- ✅ Agregado sistema de usuarios con JWT
- ✅ Localización completa al español
- ✅ Visualización de calificación con estrellas

---

## 📸 Capturas de Pantalla

Todas las capturas están disponibles en la carpeta `doc de capturas/`:

- **CP1.PNG:** Gestión de Géneros en Admin
- **CP2.PNG:** API de Reseñas con estrellas
- **CP3.PNG:** Búsqueda y filtros avanzados
- **CP4.PNG:** Sistema de autenticación de usuarios

---

**Proyecto de Laboratorio - Abril 2026**