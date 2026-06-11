"""
Módulo principal del sistema de inventario.

Este módulo contiene el menú interactivo que permite al usuario
acceder a las distintas funcionalidades del sistema, como agregar,
consultar, actualizar y eliminar productos almacenados en la base de datos.
"""

from productos import (
    agregar_productos,
    mostrar_productos,
    buscar_producto_por_id,
    buscar_producto_por_categoria,
    buscar_producto_por_nombre,
    eliminar_producto_segun_id,
    actualizar_productos,
    reporte_stock_bajo
)

def mostrar_menu():
    
    """
    Muestra el menú principal del sistema de inventario y gestiona
    la interacción con el usuario.

    Permite acceder a las distintas operaciones disponibles:
    agregar productos, consultar información, actualizar registros,
    eliminar productos y generar reportes de stock.

    El menú permanece en ejecución hasta que el usuario seleccione
    la opción de salida o interrumpa el programa manualmente.
    """
    
    while True:
        try:
            # Muestra las opciones disponibles al usuario
            print("\n===== SISTEMA DE INVENTARIO =====")
            print("1. Agregar producto")
            print("2. Mostrar productos")
            print("3. Buscar producto por ID")
            print("4. Buscar producto por categoría")
            print("5. Buscar producto por nombre")
            print("6. Eliminar producto según ID")
            print("7. Actualizar producto")
            print("8. Reporte de stock bajo")
            print("9. Salir")

            # Solicita la opción seleccionada
            opcion = input("Seleccione una opción: ").strip()

            # Estructura match-case para ejecutar la acción correspondiente
            match(opcion):
                case "1":
                    agregar_productos()
                    continue
                case "2":
                    mostrar_productos()
                    continue
                case "3":
                    buscar_producto_por_id()
                    continue
                case "4":
                    buscar_producto_por_categoria()
                    continue
                case "5":
                    buscar_producto_por_nombre()
                    continue
                case "6":
                    eliminar_producto_segun_id()
                    continue
                case "7":
                    actualizar_productos()
                    continue
                case "8":
                    reporte_stock_bajo()
                    continue
                case "9":
                    print("Saliendo del programa...")
                    break
                case _:
                    print("ERROR. Ingrese un numero dentro del menú: ")
                    continue
        except KeyboardInterrupt:
            print("\n El programa fue interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"Ocurrio un error inesperado: {e}")
    