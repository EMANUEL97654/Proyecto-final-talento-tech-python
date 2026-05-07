import sqlite3
from database import conectar

def agregar_productos():
    conexion = None
    try:
        conexion = conectar()
        cursor = conexion.cursor()
        
        cursor.execute("BEGIN TRANSACTION")
        
        nombre_producto = input("Ingrese el nombre del producto: ").capitalize()
        descripcion_producto = input("Ingrese una breve descripcion del producto: ")
        stock_producto = int(input("Ingrese el stock del producto: "))
        categoria_producto = input("Ingrese la categoria del producto: ").capitalize()
        precio_producto = float(input("Ingrese el precio del producto: "))
        
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
    conexion = None
    try:
        categoria_producto = input("Ingrese la categoria del producto: ").strip()
        conexion = conectar()
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE categoria = ?",(categoria_producto.capitalize(),))
        producto = cursor.fetchone()
        
        if producto:
            print(f"ID: {producto[0]} | Nombre: {producto[1]} | Cantidad: {producto[3]}")
        else:
            print("Producto no encontrado.")
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()
        
def actualizar_productos():
    conexion = None
    try:
        id_producto = int(input("Ingrese el id del producto: "))
        nombre_producto = input("Ingrese el nombre del producto: ")
        descripcion_producto = input("Ingrese una breve descripcion del producto: ")
        stock_producto = int(input("Ingrese el stock del producto: "))
        categoria_producto = input("Ingrese la categoria del producto: ")
        precio_producto = float(input("Ingrese el precio del producto: "))
        
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
        print(f"Error: {e}")
    finally:
        if conexion:
            conexion.close()
    
def reporte_stock_bajo():
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
        