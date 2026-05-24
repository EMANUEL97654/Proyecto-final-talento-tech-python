import sqlite3 as sql

"""
Módulo encargado de la conexión y creación
de la base de datos SQLite.

"""

def conectar():
    '''
    Crea y retorna una conexión a la base de datos.
    '''
    
    return sql.connect("inventario.db")

def crear_tabla():
    """
    Crea la tabla productos si todavía no existe.
    La tabla almacena:
    - ID
    - Nombre
    - Descripción
    - Cantidad
    - Precio
    - Categoría
    """
    conexion = None
    
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS productos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        descripcion TEXT,
                        cantidad INTEGER NOT NULL,
                        precio REAL NOT NULL,
                        categoria TEXT)''')
        conexion.commit()
    except sql.Error as e:
        print(f"ERROR: {e}")
    finally:
        if conexion:
            conexion.close()