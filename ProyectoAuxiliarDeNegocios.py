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
    

def datastock():
    conn = sql.connect('database.db')  # Conectar a la base de datos
    cursor = conn.cursor()  # Crear un cursor
    
    while True:
        print("Ingrese los datos del producto (ID vacio para finalizar)(Stock):")
        
        try:
            producto_id = input("ID del Producto: ")
            if producto_id == "":
                break
        except:
            print("ID ya registrado")
            return menu()
        
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

def menu(Interfaces: dict):
    while True:
        # Mostrar el menú
        print(Interfaces["General"])
        
        try:
            a = int(input("Ingrese una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue
        
        # Ejecutar la opción seleccionada
        if a == 1: 
            datastock(Interfaces)
        elif a == 2:
            datafact(Interfaces)
        elif a == 3:
            stats(Interfaces)
        elif a not in range(1, 4):
            print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")


def stats(InterfazEstads: str): # menu de estadisticas
    while True:
        print(Interfaces["Estadísticas"])

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

def sellstats(): #
    k = ["Estadísticas de Ventas","[1] Producto más vendido","[2] Ingresos totales"," [3] Menu Principal"]
    for i in k:
         print(i)

    a = int(input("Seleccione una opción: "))


def statsclients(): #
    k = ["Estadísticas de Clientes","[1] Cliente con mas compras","[2] gasto promedio","[3] Menu Principal"]
    for i in k:
        print(i)
    
    a = int(input("Seleccione una opción: "))
 

def budgetstats(): #
    k = ["Estadísticas de Inventario","[1] Productos con bajo stock","[2] Valor total del inventario","[3] Volver al menú principal" ]
    for i in k:
        print(i)
    
    a = int(input("Seleccione una opción: "))

# funciones
if __name__ == "__main__":

    I1 : str = """
Bienvenido al auxiliar de Negocios Kevlab \n
    |    Seleccione una opción    |
    |  1  |  Inventario           |
    |  2  |  Modo de Facturación  |
    |  3  |  Estadísticas         |
    """
    I2 : str = """
        Opciones de Inventario:
        |    Seleccione una opción    |
        |  1  |  Editar inventario    |
        |  2  |  Ver inventario       |
        |  3  |  Buscar producto      |
    """

    I3 : str = """
        Mostrar inventario
        |    Seleccione una opción    |
        |  1  | Por costo             |
        |  2  | Por ID                |
    """
    I4 : str = """
        Mostrar inventario
        |    Seleccione una opción    |
        |  1  | Ascendente            |
        |  2  | Descendente           |
    """

    I5 : str = """
        Opciones de Búsqueda:
        |    Seleccione una opción    |
        |  1  |  Por nombre           |
        |  2  |  Por ID               |
    """

    I6 : str = """
        |        Estadísticas         |
        |  1  |       Ventas          |
        |  2  |       Clientes        |
        |  3  |       Capital         |
    """
    Interfaces: dict = {"General": I1,"Inventario":I2, "Visibilidad": I3, "Orden": I4, "Búsqueda" : I5, "Estadísticas": I6}

    database()
    menu(Interfaces)