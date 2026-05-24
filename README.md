📦 Sistema de Inventario en Python

Proyecto final desarrollado en Python utilizando SQLite3 como base de datos.
La aplicación permite gestionar productos mediante una interfaz de consola.

🚀 Funcionalidades
✅ Registrar productos
✅ Mostrar productos registrados
✅ Buscar productos por ID
✅ Buscar productos por nombre
✅ Buscar productos por categoría
✅ Actualizar productos
✅ Eliminar productos con confirmación
✅ Reporte de productos con bajo stock
✅ Manejo de errores con try-except-finally
🛠️ Tecnologías utilizadas
Python 3
SQLite3
📂 Estructura del proyecto
proyecto_inventario/
│
├── main.py
├── database.py
├── productos.py
├── menu.py
└── inventario.db
🗄️ Base de datos

La aplicación utiliza una base de datos SQLite llamada:

inventario.db
| Campo       | Tipo                              |
| ----------- | --------------------------------- |
| id          | INTEGER PRIMARY KEY AUTOINCREMENT |
| nombre      | TEXT NOT NULL                     |
| descripcion | TEXT                              |
| cantidad    | INTEGER NOT NULL                  |
| categoria   | TEXT                              |
| precio      | REAL NOT NULL                     |

▶️ Cómo ejecutar el proyecto
1. Clonar el repositorio
git clone TU_URL_DEL_REPOSITORIO
2. Entrar en la carpeta del proyecto
cd proyecto_inventario
3. Ejecutar el programa
python main.py
📋 Menú principal
1. Agregar producto
2. Mostrar productos
3. Buscar producto por ID
4. Buscar producto por categoria
5. Buscar producto por nombre
6. Eliminar producto segun ID
7. Actualizar producto
8. Reporte de stock bajo
9. Salir
⚠️ Manejo de errores

El programa implementa manejo de errores utilizando:

try:
    # Código
except:
    # Manejo de errores
finally:
    # Cierre de conexión

Esto permite evitar cierres inesperados del sistema y asegurar el cierre correcto de la base de datos.

👨‍💻 Autor

Proyecto desarrollado por Emanuel Gonzalez Gartland
