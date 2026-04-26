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

**Captura de Pantalla:**
- Jilder Alex 
![Géneros en Admin](doc%20de%20capturas/CP1.PNG)

- 
## Funcionalidad Agregada 

### 1. Entidad Reseña

- Vista de reseñas desde el navegador  
![Captura de pantalla](./doc%20de%20capturas/cap01.png)

#### Pruebas 
- POST  
![Captura POST](./doc%20de%20capturas/postj.png)

- GET  
![Captura GET](./doc%20de%20capturas/getj.png)

- PUT  
![Captura PUT](./doc%20de%20capturas/putj.png)

- DELETE  
![Captura DELETE](./doc%20de%20capturas/deletej.png)


### 2. Búsqueda por Filtros

Capturas de pantalla 

### 3. Perfil usuario 

Captutas de pantalla 


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