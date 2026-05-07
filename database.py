import sqlite3 as sql

def conectar():
    return sql.connect("inventario.db")

def crear_tabla():
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
    conexion.close()