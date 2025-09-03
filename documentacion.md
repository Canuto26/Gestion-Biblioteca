# Requerimientos Funcionales
1. Gestión de Autores
* RF-001: Crear, leer, actualizar y eliminar autores

* RF-002: Cada autor debe tener: id, nombre, fecha de nacimiento, nacionalidad, biografía (opcional)

* RF-003: Búsqueda de autores por nombre o nacionalidad

2. Gestión de Editoriales
* RF-004: Crear, leer, actualizar y eliminar editoriales

* RF-005: Cada editorial debe tener: id, nombre, dirección, sitio web (opcional)

* RF-006: Búsqueda de editoriales por nombre

3. Gestión de Libros
* RF-007: Crear, leer, actualizar y eliminar libros

* RF-008: Cada libro debe tener: id, título, autor(es), editorial, ISBN, fecha de publicación, género, cantidad disponible

* RF-009: Relación muchos-a-muchos con autores (un libro puede tener múltiples autores)

* RF-010: Búsqueda de libros por: título, autor, editorial, género, ISBN

* RF-011: Filtrado por disponibilidad de libros

4. Gestión de Miembros
* RF-012: Crear, leer, actualizar y eliminar miembros

* RF-013: Cada miembro debe tener: id, nombre, email, teléfono, dirección, fecha de registro

* RF-014: Búsqueda de miembros por nombre o email

5. Gestión de Préstamos
* RF-015: Crear, leer, actualizar préstamos (no eliminar por historial)

* RF-016: Cada préstamo debe tener: id, libro, miembro, fecha de préstamo, fecha de devolución estimada, fecha de devolución real, estado (activo, devuelto, atrasado)

* RF-017: Al crear un préstamo, disminuir la cantidad disponible del libro

* RF-018: Al devolver un libro, aumentar la cantidad disponible

* RF-019: Validación de que el libro esté disponible antes del préstamo

* RF-020: Búsqueda de préstamos por: miembro, libro, estado, fechas

* RF-021: Endpoint para registrar devolución de libro

6. Endpoints Específicos
* RF-022: Endpoint para consultar libros disponibles

* RF-023: Endpoint para consultar préstamos activos de un miembro

* RF-024: Endpoint para consultar préstamos atrasados

# Requerimientos No Funcionales
1. Seguridad
* RNF-001: Autenticación por token (JWT) para operaciones sensibles

* RNF-002: Validación de datos de entrada en todos los endpoints

* RNF-003: Protección contra inyecciones SQL

2. Rendimiento
* RNF-004: Tiempo de respuesta inferior a 200ms para consultas simples

* RNF-005: Paginación en endpoints que devuelvan listas largas

* RNF-006: Uso de select_related y prefetch_related para optimizar consultas

3. Base de Datos
* RNF-007: Uso de PostgreSQL como motor de base de datos

* RNF-008: Configuración de conexión con PgAdmin 4 para administración

* RNF-009: Índices en campos de búsqueda frecuente

