"""
Módulo de gestión de productos.

Este módulo contiene funciones para realizar operaciones CRUD
(Crear, Leer, Actualizar y Eliminar) sobre la tabla productos
de una base de datos SQLite, además de generar reportes de stock.
"""

import sqlite3
from database import conectar

def agregar_productos():
    """
    Agrega un nuevo producto a la base de datos solicitando los datos al usuario.
    Realiza validaciones sobre el nombre, stock y precio antes de insertar
    el registro en la tabla productos.
    """
    
    conexion = None
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("BEGIN TRANSACTION")
        
        nombre_producto = input("Ingrese el nombre del producto: ").capitalize()
        if nombre_producto == "":
            print("Error. El nombre no puede estar vacío.")
            return
        
        descripcion_producto = input("Ingrese una breve descripcion del producto: ")
        stock_producto = int(input("Ingrese el stock del producto: "))
        categoria_producto = input("Ingrese la categoria del producto: ").capitalize()
        precio_producto = float(input("Ingrese el precio del producto: "))
        
        if stock_producto < 0:
            print("Error: el stock no puede ser negativo. ")
            return

        if precio_producto <= 0:
            print("Error: el precio debe ser mayor a 0. ")
        
        cursor.execute("""
                    INSERT INTO productos (nombre, descripcion, cantidad, categoria, precio)
                    VALUES(?,?,?,?,?)""",(nombre_producto,descripcion_producto,stock_producto,categoria_producto,precio_producto))
        
        conexion.commit()
        print(f"{nombre_producto.capitalize()} agregado correctamente.")
    
    except ValueError:
        if conexion:
            conexion.rollback()
            print("ERROR: debe ingresar números validos en stock y precio.")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()

def mostrar_productos():
    """
    Muestra todos los productos almacenados en la base de datos,
    incluyendo ID, nombre, cantidad, categoría y precio.
    """
    
    conexion = None
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        
        for producto in productos:
            print(f"ID: {producto[0]} - Nombre: {producto[1]} - Cantidad: {producto[3]} - Categoria: {producto[4]} - Precio: {producto[5]} ")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()

def buscar_producto_por_id():
    """
    Busca un producto en la base de datos utilizando su ID.
    Si existe, muestra sus datos principales; de lo contrario,
    informa que el producto no fue encontrado.
    """
    
    conexion = None
    try:
        id_producto = int(input("Ingrese el id del producto: "))
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = ?",(id_producto,))
        producto = cursor.fetchone()
        
        if producto:
            print(f"ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[3]}")
        else:
            print("Producto no encontrado.")
    except ValueError:
        print("ERROR: el ID debe ser un numero.")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()
    
def buscar_producto_por_nombre():
    """
    Busca un producto por su nombre.
    Si encuentra una coincidencia exacta, muestra la información
    principal del producto.
    """
    
    conexion = None
    try:
        nombre_producto = input("Ingrese el nombre del producto: ").strip()
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE nombre = ?",(nombre_producto.capitalize(),))
        producto = cursor.fetchone()
        
        if producto:
            print(f"ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[3]}")
        else:
            print("Producto no encontrado")  
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()

def buscar_producto_por_categoria():
    """
    Busca y muestra todos los productos pertenecientes a una
    categoría específica ingresada por el usuario.
    """
    
    conexion = None
    try:
        categoria_producto = input("Ingrese la categoria del producto: ").strip()
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE categoria = ?",(categoria_producto.capitalize(),))
        productos = cursor.fetchall()
        
        if productos:
            print(f"\n PRODUCTOS ENCONTRADOS EN LA CATEGORIA {categoria_producto}")
            for producto in productos:
                print(
                    f"ID: {producto[0]} | "
                    f"Nombre: {producto[1]} | "
                    f"Cantidad: {producto[3]} | "
                    f"Precio: {producto[5]} | "
                )
            
        else:
            print("No se encontraron productos en esa categoria.")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()
        
def actualizar_productos():
    """
    Actualiza los datos de un producto existente utilizando su ID.
    Solicita los nuevos valores y valida que el stock y el precio
    sean correctos antes de guardar los cambios.
    """
    
    conexion = None
    try:
        id_producto = int(input("Ingrese el id del producto: "))
        nombre_producto = input("Ingrese el nombre del producto: ")
        if nombre_producto == "":
            print("ERROR: el nombre no puede estar vacío.")
            return
        descripcion_producto = input("Ingrese una breve descripcion del producto: ")
        stock_producto = int(input("Ingrese el stock del producto: "))
        categoria_producto = input("Ingrese la categoria del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        
        if stock_producto < 0:
            print("ERROR: el stock no puede ser negativo.")
            return

        if precio_producto <= 0:
            print("ERROR: el precio debe ser mayor a 0.")
            return    
        
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("BEGIN TRANSACTION")
        
        sentencia = "UPDATE productos SET nombre = ?, descripcion = ?, cantidad = ?, categoria = ?, precio = ? WHERE id = ?"
        
        cursor.execute(sentencia,(nombre_producto,descripcion_producto,stock_producto,categoria_producto,precio_producto,id_producto))
        
        conexion.commit()
        
        if cursor.rowcount > 0:
            print(f"Producto {id_producto} actualizado correctamente. ")
        else:
            print("No se encontro el ID especifico. ")
    
    except ValueError:
        if conexion:
            conexion.rollback()
            print("ERROR: ID, stock y precio deben ser numeros")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()
    

def eliminar_producto_segun_id():
    
    """
    Elimina un producto de la base de datos a partir de su ID.
    Antes de realizar la eliminación solicita confirmación
    al usuario.
    """
    
    conexion = None
    try:
        id_producto = int(input("Ingrese el id del producto a eliminar: "))
    
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("BEGIN TRANSACTION")
        
        cursor.execute("SELECT * FROM productos where id = ?", (id_producto,))
        producto = cursor.fetchone()
        
        if producto:
            print("Producto encontrado")
            print(producto)
            
            confirmacion = input("¿Está seguro que desea eliminar este producto? (s/n): ")
            
            if confirmacion.lower() == 's':
                cursor.execute("BEGIN TRANSACTION")
                cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
                conexion.commit()
                print("Producto eliminado correctamente.")
            else:
                print("Eliminacion cancelada.")
        else:
            print("Producto no encontrado.")
    except ValueError:
        if conexion:
            conexion.rollback()
            print("ERROR: el ID debe ser un numero.")
    except sqlite3.Error as e:
        if conexion:
            conexion.rollback()
        print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()
    
def reporte_stock_bajo():
    """
    Genera un reporte de productos cuyo stock sea menor o igual
    al límite indicado por el usuario.
    Permite identificar productos que requieren reposición.
    """
    
    conexion = None
    try:
        limite = int(input("Ingrese el limite de stock: "))
        
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (limite,))
        productos = cursor.fetchall()
        
        if productos:
            print("Productos con bajo stock:")
            for producto in productos:
                print(f"ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[3]}")
        else:
            print("No hay productos con bajo stock.")
    except ValueError:
        print("❌ Error: debe ingresar un número válido.")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    
    finally:
        if conexion:
            conexion.close()
        