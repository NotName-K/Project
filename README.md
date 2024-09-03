# Project D-3
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
        Metodo_Pago TEXT,                  
        Valor_Total_Compras REAL            
    )
    """)

    # Crear tabla de Stock
    c.execute("""
    CREATE TABLE IF NOT EXISTS Stock (
        Producto_id INTEGER PRIMARY KEY,
        Producto TEXT NOT NULL,
        Marca TEXT NOT NULL,
        Presentacion TEXT NOT NULL,
        PrecioU REAL,
        Stock INTEGER
    )""")
    # crear tabla facturas
    conn.commit()
    conn.close()

```

```python
def datafact():
    conn = sql.connect('database.db')
    c = conn.cursor()
    
    # Ingresar datos del cliente
    cc = int(input("C.C.: "))
    # Insertar datos del cliente en la tabla Clientes
    c.execute("INSERT INTO Clientes (ID) VALUES (?)", (cc,))
    
    total_factura = 0
    productos_comprados = []

    # Ingresar productos
    while True:
        codeprod = input("Codigo: ")
        if codeprod == "":  # Romper el bucle si el código está vacío
            break
        unit = int(input("Unidades: "))
        
        # Obtener los detalles del producto usando la función ustock
        datos_producto = ustock(codeprod)
        if datos_producto is None:
            print("Producto no encontrado.")
            continue
        
        datos_producto = ustock(codeprod) 
        
        if datos_producto[4] is None:
            print("Producto no encontrado.")
            continue
        
        # Calcular el total para este producto
        subtotal = datos_producto[4] * unit
        total_factura += subtotal
        
        # Guardar el producto comprado
        productos_comprados.append((codeprod, datos_producto[1],datos_producto[2],datos_producto[3],datos_producto[4] ,unit, subtotal))
        
        nuevo_stock = datos_producto[5] - unit
        
        if nuevo_stock < 0:
            print(f"No hay suficiente stock disponible para el producto {datos_producto[1],datos_producto[2],datos_producto[3]}.")
            conn.close()
            return
        
        # Actualizar el stock en la base de datos
        c.execute("UPDATE Stock SET Stock = ? WHERE Producto_id = ?", (nuevo_stock, codeprod))
    
    conn.commit()
    conn.close()
    
    print(f"ID CLIENTE: C.C. {cc}")
    print("ID, PRODUCTO, MARCA, PRESENTACION, PRECIO UNITARIO, UNIDADES, SUBTOTAL")
    for i in productos_comprados:
        print(i)
    print(f"Total: {total_factura}")
```

```python
def ustock(producto_id):
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT Producto_id, Producto, Marca, Presentacion, PrecioU, Stock FROM Stock WHERE Producto_id = ?", (producto_id,))
    resultado = cursor.fetchone()
    conn.close()
    
    if resultado:
        return resultado  # Retornar la tupla con Nombre, Marca, Presentación, Precio y Stock
    else:
        return None
    
```
```python
def datastock():
    conn = sql.connect('database.db')  # Conectar a la base de datos
    cursor = conn.cursor()  # Crear un cursor
    
    while True:
        print("Ingrese los datos del producto (ID vacio para finalizar)(Stock):")
        
        producto_id = input("ID del Producto: ")
        if producto_id == "":
            break
        
        Producto = input("Nombre del Producto: ")
        if Producto == "":
            break
        
        Marca = input("Marca: ")
        if Marca == "":
            break

        Presentacion = int(input("Presentacion(kg): "))
        if Presentacion == "":
            break
        
        PrecioU = input("Precio: ")
        if PrecioU == "":
            break

        stock = input("Cantidad en Stock: ")
        if stock == "":
            break
        
        # Insertar los datos en la tabla
        cursor.execute("INSERT INTO Stock (Producto_id, Producto, Marca, Presentacion, PrecioU, Stock) VALUES (?, ?, ?, ?, ?, ?)", 
                       (producto_id, Producto, Marca, Presentacion, float(PrecioU), int(stock)))
        
        # Guardar los cambios en la base de datos
        conn.commit()
    conn.close()  # Cerrar la conexión cuando termine
```
```python
def menu():
    k = ["    Interfaz  ", "Añadir Stock [1]", "Modo Facturacion [2]", "Estadisticas [3]"]
    while True:
        # Mostrar el menú
        for i in k:
            print(i)
        
        try:
            a = int(input("Ingrese una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue
        
        # Ejecutar la opción seleccionada
        if a == 1: 
            datastock()
        elif a == 2:
            datafact()
        elif a == 3:
            stats()
        elif a not in range(1, 4):
            print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")
```
```python
def stats(): # menu de estadisticas
    k = ["Estadisticas","Ventas[1]","Clientes[2]","Capital[3]"]
    while True:
        for i in k:
         print(i)

        try:
            a = int(input("Ingrese una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue
        
        if a == 1: 
            sellstats()
        elif a == 2:
            statsclients()
        elif a == 3:
            budgetstats()
        elif a not in range(1, 4):
            print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")
```
```python
def sellstats(): #
    k = ["Estadísticas de Ventas","[1] Producto más vendido","[2] Ingresos totales"," [3] Menu Principal"]
    for i in k:
         print(i)

    a = int(input("Seleccione una opción: "))
```
```python
def statsclients(): #
    k = ["Estadísticas de Clientes","[1] Cliente con mas compras","[2] gasto promedio","[3] Menu Principal"]
    for i in k:
        print(i)
    
    a = int(input("Seleccione una opción: "))
```
```python
def budgetstats(): #
    k = ["Estadísticas de Inventario","[1] Productos con bajo stock","[2] Valor total del inventario","[3] Volver al menú principal" ]
    for i in k:
        print(i)
    
    a = int(input("Seleccione una opción: "))
```
```python
# funciones
if __name__ == "__main__":
    database()
    menu()
```
