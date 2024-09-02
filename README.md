# Project
Proyecto Programación 2024-1
## integrantes 
 * Kevin Daniel Castellanos Peña C.C. 1052338203
 * Julian Jacobo Gustin Moreno  T.I. 1081275973
 * Lucas Garcia Álvarez T.I. 1062434165
## Descripcion del proyecto
El Proyecto presente es una aplicación basada en la consola diseñada para pequeñas empresas. Permite gestionar productos, clientes y facturas, asegurando un control ágil y eficiente del inventario y la facturación. Incluye características avanzadas como cálculo de impuestos, manejo de descuentos, generación de reportes, y demás caracteristicas descritas en los siguientes apartados. El sistema es modular, ofreciendo una solución simple e intuitiva para la gestión diaria del negocio.
El siguiente proyecto fue escogido ya que nos enfocamos en hacer algo útil y practico para quien requiera usar el programa, además de tener un rango de mejora inmenso.
## Diagrama de concepto
## Code Project
```python
import sqlite3 as sql

def database():
    conn = sql.connect('database.db')
    c = conn.cursor()
    
    # Crear tabla Clientes
    c.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        ID INTEGER PRIMARY KEY,
        Nombre TEXT NOT NULL
    )""")
    
    # Crear tabla Presupuesto
    c.execute("""
    CREATE TABLE IF NOT EXISTS Presupuesto (
    Producto_id INTEGER,
    Inversion INTEGER,
    Unidades_AD INTEGER,
    Ventas INTEGER,
    Rendimiento REAL
    )""")

    # Crear tabla de Stock
    c.execute("""
    CREATE TABLE IF NOT EXISTS Stock (
        Producto_id INTEGER PRIMARY KEY,
        Nombre TEXT NOT NULL,
        Precio REAL,
        Stock INTEGER
    )""")

    conn.commit()
    conn.close()

def dataclient(a, b):
    conn = sql.connect('database.db')
    c = conn.cursor()
    
    # Uso de parámetros para evitar inyección de SQL
    c.execute("INSERT INTO Clientes (ID, Nombre) VALUES (?, ?)", (a, b))

    conn.commit()
    conn.close()

def datapress():
    conn = sql.connect('database.db')
    c = conn.cursor()

    while True:
        Producto_ID = input("ID del producto: ")
        if Producto_ID == "":
            break
        
        Inversion = float(input("Inversión: "))
        Unidades_AD = int(input("Unidades Compradas: "))
        
        # Obtener el precio del producto
        precio_producto = preciostock(Producto_ID)
        if precio_producto is None:
            print("El producto no existe. Intenta de nuevo.")
            continue
        unistock = ustock(Producto_ID)
        if unistock is None:
            print("No hay Stock, se vendieron todas las unidades")

        # Calcular rendimiento
        Ventas = Unidades_AD - unistock
        Rendimiento = (Ventas * precio_producto) - Inversion
        
        
        # Insertar datos en la tabla Presupuesto
        c.execute("INSERT INTO Presupuesto (Producto_id, Inversion, Unidades_AD, Ventas, Rendimiento) VALUES (?, ?, ?, ?,?)", 
                  (Producto_ID, Inversion, Unidades_AD, Ventas, Rendimiento))
        
        # Guardar cambios en la base de datos
        conn.commit()

    conn.close()

def preciostock(producto_id):
    conn = sql.connect('database.db')  # Conectar a la base de datos
    cursor = conn.cursor()  # Crear un cursor
    
    # Ejecutar la consulta para obtener el precio del producto por su ID
    cursor.execute("SELECT Precio FROM Stock WHERE Producto_id = ?", (producto_id,))
    
    # Obtener el resultado de la consulta
    resultado = cursor.fetchone()
    conn.close()  # Cerrar la conexión
    
    if resultado:
        return resultado[0]  # Retornar el precio si se encontró el producto
    else:
        return None  # Retornar None si no se encontró el producto

def ustock(producto_id):
    conn = sql.connect('database.db')  # Conectar a la base de datos
    cursor = conn.cursor()  # Crear un cursor
    
    # Ejecutar la consulta para obtener el precio del producto por su ID
    cursor.execute("SELECT Stock FROM Stock WHERE Producto_id = ?", (producto_id,))
    
    # Obtener el resultado de la consulta
    resultado = cursor.fetchone()
    conn.close()  # Cerrar la conexión
    
    if resultado:
        return resultado[0]  # Retornar el precio si se encontró el producto
    else:
        return None  # Retornar None si no se encontró el producto

def datastock():
    conn = sql.connect('database.db')  # Conectar a la base de datos
    cursor = conn.cursor()  # Crear un cursor
    
    while True:
        print("Ingrese los datos del producto (ID vacio para finalizar)(Stock):")
        
        producto_id = input("ID del Producto: ")
        if producto_id == "":
            break
        
        nombre = input("Nombre del Producto: ")
        if nombre == "":
            break
        
        precio = input("Precio: ")
        if precio == "":
            break
        
        stock = input("Cantidad en Stock: ")
        if stock == "":
            break
        
        # Insertar los datos en la tabla
        cursor.execute("INSERT INTO Stock (Producto_id, Nombre, Precio, Stock) VALUES (?, ?, ?, ?)", 
                       (producto_id, nombre, float(precio), int(stock)))
        
        # Guardar los cambios en la base de datos
        conn.commit()
    
    conn.close()  # Cerrar la conexión cuando termine

def menuint():
    print("Facturación [1]")
    print("Edición [2]")
    print("Estadísticas [3]")

def menuintx(a): 
    menuint()  # Llamada para mostrar el menú
    # Condicionales para cada opción del menú
    #if a == 1:
     #   menufact()
    #elif a == 2:
     #   edit()
    #elif a == 3:
     #   stats()
    #else:
     #   print("Opción Incorrecta, reinicia.")
      
def stats():
    print("Ventas[1]")
    print("Clientes[2]")
    print("Capital[3]")

def clientes_registrados():
    conn = sql.connect('database.db')  # Conectar a la base de datos
    c = conn.cursor()
    # Ejecutar la consulta SQL para contar filas
    c.execute(f"SELECT COUNT(*) FROM clientes")
    # Obtener el resultado de la consulta
    count = c.fetchone()[0]  # fetchone() devuelve una tupla, [0] accede al primer elemento
    conn.close()  # Cerrar la conexión a la base de datos
    return count  # Devolver el número de filas

# Llamar a la función para crear las tablas
if __name__ == "__main__":
    database()
    datastock()
    datapress()
```