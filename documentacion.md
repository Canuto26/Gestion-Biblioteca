# Requerimientos Funcionales
1. Gestión de Autores
* RF01: Crear nuevo autor (nombre, nacionalidad, fecha de nacimiento, biografía)

* RF02: Listar todos los autores con paginación

* RF03: Ver detalles de un autor específico

* RF04: Actualizar información de un autor existente

* RF05: Eliminar un autor (solo si no tiene libros asociados)

* RF06: Buscar autores por nombre o nacionalidad


2. Gestión de Editoriales
* RF07: Crear nueva editorial (nombre, dirección, teléfono, email)

* RF08: Listar todas las editoriales

* RF09: Ver detalles de una editorial específica

* RF10: Actualizar información de una editorial

* RF11: Eliminar una editorial (solo si no tiene libros asociados)

* RF12: Buscar editoriales por nombre


3. Gestión de Libros
* RF13: Crear nuevo libro (título, autor, editorial, ISBN, género, año de publicación, cantidad disponible)

* RF14: Listar todos los libros con paginación

* RF15: Ver detalles de un libro específico

* RF16: Actualizar información de un libro

* RF17: Eliminar un libro (solo si no tiene préstamos activos)

* RF18: Buscar libros por título, autor o editorial

* RF19: Filtrar libros por género o año de publicación

4. Gestión de Miembros
* RF20: Registrar nuevo miembro (nombre, email, teléfono, dirección, fecha de registro)

* RF21: Listar todos los miembros

* RF22: Ver detalles de un miembro específico

* RF23: Actualizar información de un miembro

* RF24: Desactivar/eliminar miembro (solo si no tiene préstamos activos)

* RF25: Buscar miembros por nombre o email


5. Gestión de Préstamos
* RF26: Registrar nuevo préstamo (libro, miembro, fecha de préstamo, fecha de devolución esperada)

* RF27: Listar todos los préstamos (activos, históricos)

* RF28: Ver detalles de un préstamo específico

* RF29: Registrar devolución de libro (actualizar fecha de devolución real)

* RF30: Extender plazo de préstamo

* RF31: Listar préstamos activos de un miembro

* RF32: Listar préstamos por rango de fechas

* RF33: Ver historial de préstamos de un libro


# Requerimientos No Funcionales
1. Rendimiento
* NF01: Las operaciones CRUD básicas deben responder en menos de 200ms

* NF02: Las búsquedas y filtros deben responder en menos de 500ms

* NF03: La API debe soportar al menos 50 solicitudes concurrentes en entorno local


2. Seguridad
* NF04: Implementar autenticación por tokens (JWT) para todas las operaciones

* NF05: Validar todos los datos de entrada para prevenir inyecciones SQL

* NF06: Implementar permisos basados en roles (administrador, bibliotecario, miembro)

3. Base de Datos
* NF13: Usar PostgreSQL como motor de base de datos

* NF14: Implementar migraciones de base de datos con Django Migrations

* NF15: Configurar relaciones y constraints apropiadas en la base de datos

* NF16: Implementar índices para campos de búsqueda frecuentes

4. Configuracion
* NF17: Configuración para entorno local con variables de entorno

* NF18: Scripts para poblar la base de datos con datos de prueba

* NF19: Configuración de CORS para desarrollo local


