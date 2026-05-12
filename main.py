"""
Archivo principal del sistema de inventario.

Este archivo inicia la aplicación:
- Crea la tabla si no existe.
- Ejecuta el menú principal.
"""

from database import crear_tabla
from menu import mostrar_menu

crear_tabla()
mostrar_menu()