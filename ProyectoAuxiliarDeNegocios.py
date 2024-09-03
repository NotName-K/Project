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

def menu(Interfaces: dict, bandera : bool):
    while bandera == True:
        # Mostrar el menú
        print(Interfaces["General"])
         
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue
            
        # Ejecutar la opción seleccionada
        match a:
            case 1:
                invent(Interfaces, bandera)
            case 2:
                datafact()
            case 3:
                stats(Interfaces, bandera)
            case 4:
                print("Fin del programa")
                bandera = False
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")

def invent(Interfaces: dict, bandera : bool): # menu de estadisticas
    while bandera == True:
        print(Interfaces["Inventario"])
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue

        # Ejecutar la opción seleccionada
        match a:
            case 1:
                inventEdit(Interfaces, bandera)
            case 2:
                inventShow(Interfaces, bandera)
            case 3:
                budgetstats(Interfaces, bandera)
            case 4:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")

def inventEdit(Interfaces: dict, bandera : bool):
    while bandera == True:
        print(Interfaces["Editar"])
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 

    # Ejecutar la opción seleccionada
        match a:
            case 1:
                datastock()
            case 2:
                print("Funcion aún por diseñar")
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")

def inventShow(Interfaces: dict, bandera : bool):
    while bandera == True:
        print(Interfaces["Visibilidad"])
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue
        # Ejecutar la opción seleccionada
        match a:
            case 1:
                print("Filtro establecido: Por costo")
            case 2:
                print("Filtro establecido: Por ID")
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")
        
        print(Interfaces["Orden"])
        try:
            b = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 
        # Ejecutar la opción seleccionada
        match b:
            case 1:
                print("Orden establecido: Ascendente")
            case 2:
                print("Orden establecido: Descendente")
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")
        return mostrarInvent(a,b)

def mostrarInvent(a:int, b:int):
    print("Funcion aún por diseñar")

def stats(Interfaces: dict, bandera : bool): # menu de estadisticas
    while bandera == True:
        print(Interfaces["Estadísticas"])
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue

        # Ejecutar la opción seleccionada
        match a:
            case 1:
                sellstats(Interfaces, bandera)
            case 2:
                statsclients(Interfaces, bandera)
            case 3:
                budgetstats(Interfaces, bandera)
            case 4:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")

def sellstats(Interfaces: dict, bandera : bool):
    while bandera == True:
        print(Interfaces["Ventas"])
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 

    # Ejecutar la opción seleccionada
        match a:
            case 1:
                print("Funcion aún por diseñar")
            case 2:
                print("Funcion aún por diseñar")
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")

def statsclients(Interfaces: dict, bandera : bool):
    while bandera == True:
        print(Interfaces["Clientes"])
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 

    # Ejecutar la opción seleccionada
        match a:
            case 1:
                print("Funcion aún por diseñar")
            case 2:
                print("Funcion aún por diseñar")
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")

def budgetstats(Interfaces: dict, bandera : bool):
    while bandera == True:
        print(Interfaces["InvenStats"])
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 

    # Ejecutar la opción seleccionada
        match a:
            case 1:
                print("Funcion aún por diseñar")
            case 2:
                print("Funcion aún por diseñar")
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")

# Se declaran las variables contenedoras de interfaces y se llaman a las funciones
if __name__ == "__main__":
   
    bandera : bool = True
    I1 : str = """
Bienvenido al auxiliar de Negocios Kevlab \n
    |        Menú Principal       |
    |  1  |  Inventario           |
    |  2  |  Modo de Facturación  |
    |  3  |  Estadísticas         |
    |  4  |  Cerrar el programa   |
    """
    I2 : str = """
        Opciones de Inventario:
        |    Seleccione una opción    |
        |  1  |  Editar inventario    |
        |  2  |  Ver inventario       |
        |  3  |  Buscar producto      |
        |  4  |       Cancelar        |
    """
    
    I3 : str = """
        Editar Inventario
        |    Seleccione una opción    |
        |  1  | Añadir Producto       |
        |  2  | Eliminar Producto     |
        |  3  |       Cancelar        |
    """

    I4 : str = """
        Mostrar inventario
        |    Seleccione una opción    |
        |  1  | Por costo             |
        |  2  | Por ID                |
        |  3  |       Cancelar        |
    """
    I5 : str = """
        Mostrar inventario
        |    Seleccione una opción    |
        |  1  | Ascendente            |
        |  2  | Descendente           |
        |  3  |       Cancelar        |
    """

    I6 : str = """
        Opciones de Búsqueda:
        |    Seleccione una opción    |
        |  1  |  Por nombre           |
        |  2  |  Por ID               |
        |  3  |       Cancelar        |
    """

    I7 : str = """
        |        Estadísticas         |
        |  1  |       Ventas          |
        |  2  |       Clientes        |
        |  3  |       Capital         |
        |  4  |       Cancelar        |
    """
    I8 : str = """
        |   Estadísticas de Ventas    |
        |  1  | Producto más vendido  |
        |  2  |   Ingresos totales    |
        |  3  |       Cancelar        |
    """
    I9 : str = """
        |  Estadísticas de Clientes   |
        |  1  |Cliente con más compras|
        |  2  |    Gasto promedio     |
        |  3  |       Cancelar        |
    """
    I10 : str = """
        |   Estadísticas de Inventario  |
        |  1  | Productos con bajo stock |
        |  2  |Valor total del inventario|
        |  3  |         Cancelar         |
    """

    Interfaces: dict = {"General": I1,"Inventario":I2, "Editar": I3,"Visibilidad": I4, "Orden": I5}
    Interfaces.update({"Búsqueda" : I6, "Estadísticas": I7, "Ventas": I8, "Clientes": I9, "InvenStats": I10})
    database()
    menu(Interfaces, bandera)