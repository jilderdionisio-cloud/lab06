# CineSpoilers - Aplicación Django REST

## Descripción General

CineSpoilers es una API REST desarrollada con Django y Django REST Framework para gestionar un catálogo de películas con géneros asociados, reseñas de usuarios, búsqueda avanzada y sistema de usuarios.

---

## Funcionalidades Principales (Laboratorio del 26 de Abril de 2026)

### 1. Entidad Género ( SE PRESENTAN LAS CAPTURAS DE LOS 3 MIEMBROS )

**Descripción:**
- Permite categorizar películas por géneros (Drama, Acción, Ciencia Ficción, etc.)
- Relación muchos a muchos (M2M) con Movie
- Cada película puede tener múltiples géneros

### Captura de Pantalla pruebas:
## Jilder Alex Dionisio Rojas 
![Géneros en post](doc%20de%20capturas/postgenerosj.png)
![Géneros en get](doc%20de%20capturas/getgenerosj.png) 
![Géneros en put](doc%20de%20capturas/putgenerosj.png)
![Géneros en delete](doc%20de%20capturas/deletegeneros.png)

- 

## Adriana Chinchayhuara
![Géneros en post](doc%20de%20capturas/adriana-cap_post.png) 
![Géneros en get](doc%20de%20capturas/adriana-cap_get.png)
![Géneros en put](doc%20de%20capturas/adriana-cap_put.png)
![Géneros en delete](doc%20de%20capturas/adriana-cap_delete.png)

-

## Naomi Veliz
![Géneros en post](doc%20de%20capturas/naomi-crear-genero.png) 
![Géneros en get](doc%20de%20capturas/naomi-generos-get.jpeg)
![Géneros en put](doc%20de%20capturas/naomi-put-genero.png)
![Géneros en delete](doc%20de%20capturas/naomi-generos-delete.jpeg)


# Funcionalidad Agregada 

### 1. Entidad Reseña (JILDER ALEX DIONISO ROJAS)

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

- CAMBIO BASE DE DATOS 
![Captura BASE DE DATOS](./doc%20de%20capturas/dbreseña.png)

### 2. Búsqueda por Filtros Paginación y CRUD (NAOMI VELIZ PIE)

**Descripción:**
- Permite buscar películas por título o sinopsis
- Permite filtrar películas por género específico
- Sistema de paginación integrado (10 resultados por página)
- Endpoint personalizado para películas por género

#### Pruebas

- **POST Crear Película**  
![Crear película](doc%20de%20capturas/naomi-listar-peliculas.png)

- **GET Listar Películas**  
![Listar películas](doc%20de%20capturas/naomi-crear-pelicula.png)

- **GET Búsqueda por Título**  
![Búsqueda](doc%20de%20capturas/naomi-busqueda.png)

- **GET Filtrar por Género**  
![Filtro por género](doc%20de%20capturas/naomi-filtro-genero.png)

- **GET Endpoint Personalizado por Género**  
![Endpoint por género](doc%20de%20capturas/naomi-endpoint-genero.png)

- **GET Paginación**  
![Paginación](doc%20de%20capturas/naomi-paginacion.png)

- **GET Paginación 2**  
![Paginación 2](doc%20de%20capturas/naomi-paginacion2.png)

- **DELETE Eliminar Película**  
![Eliminar película](doc%20de%20capturas/naomi-delete-pelicula.png)

- **PUT Actualizar Género**  
![Actualizar género](doc%20de%20capturas/naomi-put-genero.png)

### 3. Perfil usuario (ADRIANA)

#### Pruebas 
- **POST Crear Usuarios** 
![Captura POST](./doc%20de%20capturas/adriana-usuarios-post.png)

- **GET Listar todos Usuarios**
![Captura GET](./doc%20de%20capturas/adriana-usuarios-get-todos.png)

- **GET Listar Usuario Específico**  
![Captura GET ID](./doc%20de%20capturas/adriana-usuarios-get-id.png)

- **PUT Cambiar ciudad** 
![Captura PUT](./doc%20de%20capturas/adriana-usuarios-put.png)

- **DELETE Eliminar Usuario** 
![Captura DELETE](./doc%20de%20capturas/adriana-usuarios-delete.png)

- **Cambio Base de Datos** 
![Captura DB](./doc%20de%20capturas/adriana-basededatos.png)

#### Validaciones
- **FALTA EDAD** 
![Captura FALTA EDAD](./doc%20de%20capturas/adriana-validacion1.png)

- **CORREO DUPLICADO**
![Captura CORREO DUPLICADO](./doc%20de%20capturas/adriana-validacion2.png)

## Características Destacadas 

- **Interfaz completamente en español**
- **Calificación con estrellas**
- **Búsqueda y filtrado avanzado**
- **Sistema de autenticación JWT**
- **API RESTful completa**
- **Admin Django personalizado**

---

## Dependencias

- Django 6.0.4
- Django REST Framework
- Django REST Framework Simple JWT
- Python 3.13.13

---

## Historial de Desarrollo

**26 de Abril de 2026 - Laboratorio**
-  Agregada entidad Género con relación M2M
-  Agregada entidad Reseña con calificación
-  Implementada búsqueda por filtros
-  Agregado sistema de usuarios con JWT
-  Localización completa al español
-  Visualización de calificación con estrellas

---

## Capturas de Pantalla

Todas las capturas están disponibles en la carpeta `doc de capturas/`:

- **CP1.PNG:** Gestión de Géneros en Admin
- **CP2.PNG:** API de Reseñas con estrellas
- **CP3.PNG:** Búsqueda y filtros avanzados
- **CP4.PNG:** Sistema de autenticación de usuarios

---

**Proyecto de Laboratorio - Abril 2026**
