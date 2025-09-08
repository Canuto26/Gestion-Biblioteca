# 📚 URLs Disponibles - Sistema de Gestión de Biblioteca

## 🌐 URLs Principales del Proyecto

### Página Principal
- **`/`** - Página principal con información de la API
  - **Método**: GET
  - **Descripción**: Muestra información general de la API, versión y todos los endpoints disponibles
  - **Ejemplo**: `http://127.0.0.1:8000/`

### Panel de Administración
- **`/admin/`** - Panel de administración de Django
  - **Método**: GET
  - **Descripción**: Interfaz web para administrar la base de datos
  - **Ejemplo**: `http://127.0.0.1:8000/admin/`

---

## 📖 API Endpoints - Gestión de Autores

### Listar y Crear Autores
- **`/api/autores/`**
  - **Métodos**: GET, POST
  - **GET**: Lista todos los autores con paginación
  - **POST**: Crea un nuevo autor
  - **Parámetros de búsqueda**: `?search=nombre`, `?ordering=nombre`
  - **Ejemplo**: `http://127.0.0.1:8000/api/autores/`

### Detalles de Autor
- **`/api/autores/{id}/`**
  - **Métodos**: GET, PUT, PATCH, DELETE
  - **GET**: Obtiene detalles de un autor específico
  - **PUT/PATCH**: Actualiza información del autor
  - **DELETE**: Elimina un autor (solo si no tiene libros asociados)
  - **Ejemplo**: `http://127.0.0.1:8000/api/autores/1/`

### Búsqueda Avanzada de Autores
- **`/api/autores/buscar/`**
  - **Método**: GET
  - **Parámetros**: `?nombre=valor`, `?nacionalidad=valor`
  - **Descripción**: Búsqueda avanzada por nombre y nacionalidad
  - **Ejemplo**: `http://127.0.0.1:8000/api/autores/buscar/?nombre=Gabriel`

---

## 🏢 API Endpoints - Gestión de Editoriales

### Listar y Crear Editoriales
- **`/api/editoriales/`**
  - **Métodos**: GET, POST
  - **GET**: Lista todas las editoriales
  - **POST**: Crea una nueva editorial
  - **Parámetros de búsqueda**: `?search=nombre`
  - **Ejemplo**: `http://127.0.0.1:8000/api/editoriales/`

### Detalles de Editorial
- **`/api/editoriales/{id}/`**
  - **Métodos**: GET, PUT, PATCH, DELETE
  - **GET**: Obtiene detalles de una editorial específica
  - **PUT/PATCH**: Actualiza información de la editorial
  - **DELETE**: Elimina una editorial (solo si no tiene libros asociados)
  - **Ejemplo**: `http://127.0.0.1:8000/api/editoriales/1/`

---

## 📚 API Endpoints - Gestión de Libros

### Listar y Crear Libros
- **`/api/libros/`**
  - **Métodos**: GET, POST
  - **GET**: Lista todos los libros con información de autor y editorial
  - **POST**: Crea un nuevo libro
  - **Parámetros de filtro**: `?genero=valor`, `?año_publicacion=valor`
  - **Parámetros de búsqueda**: `?search=titulo`
  - **Ejemplo**: `http://127.0.0.1:8000/api/libros/`

### Detalles de Libro
- **`/api/libros/{id}/`**
  - **Métodos**: GET, PUT, PATCH, DELETE
  - **GET**: Obtiene detalles de un libro específico
  - **PUT/PATCH**: Actualiza información del libro
  - **DELETE**: Elimina un libro (solo si no tiene préstamos activos)
  - **Ejemplo**: `http://127.0.0.1:8000/api/libros/1/`

### Búsqueda Avanzada de Libros
- **`/api/libros/buscar/`**
  - **Método**: GET
  - **Parámetros**: `?titulo=valor`, `?autor=valor`, `?editorial=valor`, `?genero=valor`, `?año_min=valor`, `?año_max=valor`
  - **Descripción**: Búsqueda avanzada con múltiples criterios
  - **Ejemplo**: `http://127.0.0.1:8000/api/libros/buscar/?genero=Novela&año_min=2020`

---

## 👥 API Endpoints - Gestión de Miembros

### Listar y Crear Miembros
- **`/api/miembros/`**
  - **Métodos**: GET, POST
  - **GET**: Lista todos los miembros
  - **POST**: Registra un nuevo miembro
  - **Parámetros de búsqueda**: `?search=nombre`
  - **Ejemplo**: `http://127.0.0.1:8000/api/miembros/`

### Detalles de Miembro
- **`/api/miembros/{id}/`**
  - **Métodos**: GET, PUT, PATCH, DELETE
  - **GET**: Obtiene detalles de un miembro específico
  - **PUT/PATCH**: Actualiza información del miembro
  - **DELETE**: Elimina un miembro (solo si no tiene préstamos activos)
  - **Ejemplo**: `http://127.0.0.1:8000/api/miembros/1/`

---

## 📋 API Endpoints - Gestión de Préstamos

### Listar y Crear Préstamos
- **`/api/prestamos/`**
  - **Métodos**: GET, POST
  - **GET**: Lista todos los préstamos con información de libro y miembro
  - **POST**: Registra un nuevo préstamo
  - **Parámetros de filtro**: `?estado=activo|completado|atrasado`
  - **Ejemplo**: `http://127.0.0.1:8000/api/prestamos/`

### Detalles de Préstamo
- **`/api/prestamos/{id}/`**
  - **Métodos**: GET, PUT, PATCH
  - **GET**: Obtiene detalles de un préstamo específico
  - **PUT/PATCH**: Actualiza información del préstamo
  - **Ejemplo**: `http://127.0.0.1:8000/api/prestamos/1/`

### Registrar Devolución
- **`/api/prestamos/{id}/devolucion/`**
  - **Método**: POST
  - **Descripción**: Registra la devolución de un libro
  - **Body**: `{"fecha_devolucion_real": "2025-09-07T21:00:00Z"}`
  - **Ejemplo**: `http://127.0.0.1:8000/api/prestamos/1/devolucion/`

### Búsqueda Avanzada de Préstamos
- **`/api/prestamos/buscar/`**
  - **Método**: GET
  - **Parámetros**: `?miembro=id`, `?estado=valor`, `?fecha_inicio=fecha`, `?fecha_fin=fecha`
  - **Descripción**: Búsqueda avanzada de préstamos
  - **Ejemplo**: `http://127.0.0.1:8000/api/prestamos/buscar/?estado=activo`

### Préstamos por Miembro
- **`/api/prestamos/miembro/{miembro_id}/`**
  - **Método**: GET
  - **Descripción**: Obtiene todos los préstamos de un miembro específico
  - **Ejemplo**: `http://127.0.0.1:8000/api/prestamos/miembro/1/`

### Préstamos Activos por Miembro
- **`/api/prestamos/miembro/{miembro_id}/activos/`**
  - **Método**: GET
  - **Descripción**: Obtiene solo los préstamos activos de un miembro específico
  - **Ejemplo**: `http://127.0.0.1:8000/api/prestamos/miembro/1/activos/`

---

## 🔧 Parámetros de Consulta Comunes

### Paginación
- **`?page=1`** - Número de página (20 elementos por página)
- **`?page_size=10`** - Tamaño de página personalizado

### Ordenamiento
- **`?ordering=campo`** - Ordenar por campo ascendente
- **`?ordering=-campo`** - Ordenar por campo descendente
- **Ejemplo**: `?ordering=-fecha_prestamo`

### Búsqueda
- **`?search=termino`** - Búsqueda general en campos específicos

### Filtros
- **`?campo=valor`** - Filtrar por valor exacto
- **`?campo__icontains=valor`** - Filtrar por contenido (insensible a mayúsculas)

---

## 📝 Ejemplos de Uso

### Crear un Autor
```bash
POST /api/autores/
Content-Type: application/json

{
    "nombre": "Gabriel García Márquez",
    "nacionalidad": "Colombiana",
    "fecha_nacimiento": "1927-03-06",
    "biografia": "Escritor colombiano, premio Nobel de Literatura"
}
```

### Crear un Libro
```bash
POST /api/libros/
Content-Type: application/json

{
    "titulo": "Cien años de soledad",
    "autor": 1,
    "editorial": 1,
    "isbn": "9788437604947",
    "genero": "Novela",
    "año_publicacion": 1967,
    "cantidad_disponible": 5
}
```

### Registrar un Préstamo
```bash
POST /api/prestamos/
Content-Type: application/json

{
    "libro": 1,
    "miembro": 1,
    "fecha_devolucion_esperada": "2025-09-14"
}
```

---

## 🚀 URLs de Prueba Rápida

1. **Página principal**: `http://127.0.0.1:8000/`
2. **Lista de autores**: `http://127.0.0.1:8000/api/autores/`
3. **Lista de libros**: `http://127.0.0.1:8000/api/libros/`
4. **Admin panel**: `http://127.0.0.1:8000/admin/`

---

## 📋 Notas Importantes

- **Base URL**: `http://127.0.0.1:8000`
- **Formato de respuesta**: JSON
- **Autenticación**: No requerida (configurado para desarrollo)
- **Paginación**: 20 elementos por página por defecto
- **Validaciones**: Todos los campos tienen validaciones apropiadas
- **Relaciones**: Los modelos están relacionados (Autor → Libro → Préstamo → Miembro)
