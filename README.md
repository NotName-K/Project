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
    )
    """)
    
    # Crear tabla Presupuesto
    c.execute("""
    CREATE TABLE IF NOT EXISTS Presupuesto (
        Presupuesto_Inicial INTEGER,
        Inversion TEXT,
        Ventas INTEGER
        Ganancia
    )
    """)

    # Crear tabla de Stock
    c.execute("""
    CREATE TABLE IF NOT EXISTS Stock (
        Producto_id INTEGER PRIMARY KEY,
        Nombre TEXT NOT NULL,
        Precio REAL,
        Stock INTEGER
    )
    """)

    conn.commit()
    conn.close()

def dataclient(a, b):
    conn = sql.connect('database.db')
    c = conn.cursor()
    
    # Uso de parámetros para evitar inyección de SQL
    c.execute("INSERT INTO Clientes (ID, Nombre) VALUES (?, ?)", (a, b))

    conn.commit()
    conn.close()

def datapress(a,b,c,d):
    conn = sql.connect('database.db')
    c = conn.cursor()
    
    # Uso de parámetros para evitar inyección de SQL
    c.execute("INSERT INTO Presupuesto (Presupuesto_Inicial, Inversion, Ventas, Ganancia) VALUES (?, ?, ?, ?)", (a, b, c, d))
    
    conn.commit()
    conn.close()

def datastock(a, b, c, d):
    conn = sql.connect('database.db')
    c = conn.cursor()
    while True: 
     c.execute("INSERT INTO Presupuesto (Producto_id, Nombre, Precio, Stock) VALUES (?, ?, ?, ?)", (a, b, c, d))
     if a == '':
      break
    conn.commit()
    conn.close()

def menuint():
    print("Facturación [1]")
    print("Edición [2]")
    print("Estadísticas [3]")

def menuintx(a): 
    menuint()  # Llamada para mostrar el menú
    # Condicionales para cada opción del menú
    if a == 1:
        menufact()
    elif a == 2:
        edit()
    elif a == 3:
        stats()
    else:
        print("Opción Incorrecta, reinicia.")
      
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

def statsx(a):
    stats()
    if a == 1:
        statsv()
    elif a == 2:
        statsc()
    elif a == 3:
        statsb()
    else:
        print("Opción Incorrecta, reinicia.")

# Llamar a la función para crear las tablas
if __name__ == "__main__":
    database()
    #a = int(input("ID: "))
    #b = input("Nombre: ")
    #dataclient(a, b)
    #print(f"Hay {clientes_registrados()} clientes registados")
    a = input("Codigo: ")
    b = input("Marca: ")
    c = input("tipo: ")
    d = float(input("stock: "))
    datastock(a,b,c,d)
```