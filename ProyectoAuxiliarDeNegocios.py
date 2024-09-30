# Se importan los módulos requeridos
import json
from datetime import datetime
import os

# Funcion para cargar datos desde un archivo JSON
def load_data(file_name):
    # Abre el archivo en modo de lectura
    with open(file_name, "r") as file: 
    # Carga el contendio del archivo y lo convierte en un diccionario
        return json.load(file)

# Funcion para guardar datos en un archivo JSON
def save_data(file_name, data):
    # Abre el archivo en modo de escritura
    with open(file_name, "w") as file: 
        # Convierte el diccionario a JSON y lo escribe en el archivo
        json.dump(data, file, indent=4) 
    print("Los datos fueron guardados con exito")

# Funcion para crear la estructura inicial de los diccionarios en JSON
def initialize_data():
    if not os.path.exists("database.json"): # Si no esta creada la base de datos
        print("Iniciando programa \n agregue una contraseña para el administrador")
        # Se añade la contraseña y la pregunta de recuperación
        password = str(input("Nueva Contraseña: "))
        pregunta = str(input("Ahora ingresa una pregunta para recuperar la contraseña: "))
        respuesta = str(input("Y su respuesta: "))
        # Crea un diccionario con listas vacias para clientes, stock, facturas, etc.
        data = {
            "Contrasena": [password],
            "Pregunta": [pregunta],
            "Respuesta": [respuesta],
            "Clientes": [],
            "Stock": [],
            "Facturas": [],
        }
        # Guarda el diccionario en un archivo JSON
        save_data("database.json", data)
        print("Datos inciales creados en database.json")
    else: # Si ya existe la base de datos se imprime el siguiente mensaje
        print("El archivo JSON ya existe. No se realizaron cambios") 

# Funcion para validar el acceso de un administrador
def accessoAdmin(funcion):
    # Se carga la información del JSON
    data = load_data("database.json")
    print("Tienes 3 intentos")
    # Se declaran e inicializan las variables
    password = str(input("Ingrese la contraseña: "))
    iteracion: int = 1
    acierto : bool = False
    # Si acierta la contraseña se actualiza la bandera "acierto"
    if password == data["Contrasena"][0]:
        acierto = True
    if acierto == False: # Sino, se dan 2 intentos más para ello
        while (iteracion < 3):
            iteracion += 1
            print("Contraseña incorrecta \nIntenta denuevo")
            password = str(input("Ingrese la contraseña: "))
            if password == data["Contrasena"][0]:
                acierto = True
                break

    # Si no se acertó la contraseña se dan 3 intentos para responder la pregunta de recuperación
    if acierto == False:
        iteracion = 1
        print("Acabaste los intentos permitidos, tienes 3 intentos para recuperar la contraseña con la pregunta de recuperación")
        while (iteracion < 4):
            iteracion += 1
            print(data["Pregunta"][0])
            respuesta = str(input("La respuesta es: "))
            if respuesta == data["Respuesta"][0]:
                print(f"Correcto, la contraseña guardada es: {data["Contrasena"][0]}, no la olvides")
                acierto = True # Si aciertan, se actualiza la bandera y se rompe el ciclo
                break
            else:
                print("Incorrecto")
                print("No se pudo recuperar la contraseña")
    if acierto == True: # Si en algún momento se acertó, al final se redirige a la función deseada
        funcion()       

# Función para obtener una lista no repetida de los id de los clientes
def idclientsord():
    # Se carga la información del JSON y se inicializan las variables
    data = load_data("database.json")
    idclientesfact : list = []
    for i in data["Facturas"]: # Para cada factura se toman los ID y se anexan a la lista de clientes
        idclientesfact.append(i.get("Cliente_id"))
    idfactn = set(idclientesfact) # Se usa set para eliminar ID's repetidos
    return idfactn # Se retornan los ID's de todas las facturas, sin repetirse

# Menú principal
def menu(Interfaces: dict, bandera: bool):
    while bandera == True:
        # Mostrar el menú
        print(Interfaces["General"])
        # Se elige una opción de la interfaz mostrada
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue
            
        # Ejecutar la opción seleccionada
        match a: # Se redirige a la función deseada por el usuario
            case 1:
                invent(Interfaces)
            case 2:
                facturas(Interfaces)
            case 3:
                stats(Interfaces)
            case 4:
                print("Fin del programa")
                bandera = False # Se actualiza la bandera para dar fin al bucle y al programa
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")

# Menú general Inventario 
def invent(Interfaces: dict):
    while True:
        print(Interfaces["Inventario"])
        # Se elige una opción de la interfaz mostrada
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue

        # Ejecutar la opción seleccionada
        match a: # Se redirige a la función deseada
            case 1:
                inventEdit(Interfaces)
            case 2:
                inventShow(Interfaces)
            case 3:
                # Menú de Búsqueda de productos
                print(Interfaces["Búsqueda"])
                buscar_criterio = int(input("Seleccione una opción: "))
                if buscar_criterio == 3: # Si se selecciona se retorna al menú anterior
                    break
                search_product(buscar_criterio)
                continue
            case 4:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")

# Menú para editar el Inventario
def inventEdit(Interfaces: dict):
    while True:
        print(Interfaces["Editar"])
        # Se elige una de las opciones mostradas
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 

    # Ejecutar la opción seleccionada
        match a: # Se redirige a la función deseada, pero primero llamando a la función para ingresar la contraseña
            case 1:
                accessoAdmin(datastock)
            case 2:
                accessoAdmin(deletestock)
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")

# Función para añadir un producto al inventario
def datastock():
    # Se carga la información del JSON
    data = load_data("database.json")
    while True:
        try:
            print("Ingrese los datos del producto (Digite ENTER para finalizar): ")
            # Se solicita el ID del producto
            producto_id = int(input("ID del Producto: "))

            # Se solicitan otros detalles del producto
            
            # Nombre
            Producto = input("Nombre del Producto: ")
            if Producto == "":
                break
            
            # Marca
            Marca = input("Marca: ")
            if Marca == "":
                break
            
            # Presentación
            Presentacion = input("Presentación: ")
            if Presentacion == "":
                break
            
            # Precio Unitario
            PrecioU = input("Precio: ")
            if PrecioU == "":
                break

            # Stock
            stock = input("Cantidad en Stock: ")
            if stock == "":
                break
            
            # Agregar el producto a la lista de Stock
            data["Stock"].append({
                "Producto_id": producto_id,
                "Producto": Producto,
                "Marca": Marca,
                "Presentacion": Presentacion,
                "PrecioU": float(PrecioU),
                "Stock": int(stock)
            })
        except ValueError:
            print("ID inválido, intenta denuevo")
            break
        #Guardar los cambios
    save_data("database.json", data)

# Función para eliminar un producto del inventario
def deletestock():
    while True:
        # Se busca el ID ingresado y se elimina el producto si existe, sino se reporta que no lo hace
        try:
            product_id= int(input("Ingrese el ID del producto a eliminar: "))
            data = load_data("database.json")
            if delete_product(product_id, data):
                save_data("database.json", data)
                print(f"El producto con ID {product_id} fue eliminado con exito")
            else:
                print(f"Producto con id {product_id} no encontrado")
        except ValueError:
            print("Valor inválido, por favor intente otra vez")

# Funcion para eliminar el producto ingresado en la función anterior
def delete_product(product_id, data):
    # Obtener la lista de stock
    stock_list = data.get("Stock", [])
    # Comprobar si la lista de stock es None y convertirla a una lista vacía si es necesario
    if stock_list is None:
        stock_list = []
    # Buscar el producto con el ID dado
    for i in range(len(stock_list)):
        if int(stock_list[i]["Producto_id"]) == product_id:
        # Eliminar el producto de la lista
            del stock_list[i]
            return True

# Menú para mostrar el inventario y seleccionar criterios
def inventShow(Interfaces: dict):
    while True:
        print(Interfaces["Visibilidad"])
        # Se escoge el criterio por el cuál mostrar el inventario
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue
        # Ejecutar la opción seleccionada
        match a: # Se confirma al usario el criterio seleccionado
            case 1:
                print("Filtro establecido: Por costo")
                a = 1
            case 2:
                print("Filtro establecido: Por ID")
                a = 2
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")
        
        print(Interfaces["Orden"])
        try:
        # Se elige el orden por el cuál se muestra el inventario
            b = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 
        # Ejecutar la opción seleccionada
        match b: # Se le confirma al usuario el orden seleccionado
            case 1:
                print("Orden establecido: Ascendente")
                b = 1
            case 2:
                print("Orden establecido: Descendente")
                b = 2
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")
        
        mostrarInvent(a, b) # Se llama a la función para mostrar el inventario con los criterios ya ingresados

# Función para mostrar el inventario según los criterios anteriores
def mostrarInvent(a:int, b:int):
    # Se carga la información del JSON, y de ella la lista de productos
    data = load_data("database.json")
    stock_list = data.get("Stock", [])
    
    # Se ordena la lista en función del criterio y el orden seleccionado
    if a == 1:
        stock_list.sort(key=lambda x: x["PrecioU"], reverse=(b==2))
    elif a == 2:
        stock_list.sort(key=lambda x: x["Producto_id"], reverse=(b==2))
    print(f"{'ID':<10} {'Producto':<20} {'Marca':<15} {'Presentación':<15} {'Precio Unitario':<15} {'Stock':<10}")
    for producto in stock_list:
        print(f"{producto['Producto_id']:<10} {producto['Producto']:<20} {producto['Marca']:<15} {producto['Presentacion']:<15} {producto['PrecioU']:<15} {producto['Stock']:<10}")

# Funcion para que el usuario busque un producto
def search_product(criterio):
    # Se carga la información del JSON y con ello la lista de productos
    data = load_data("database.json")
    stock_list = data.get("Stock", [])

    # Si se busca por el nommbre del producto
    if criterio == 1:
        nombre = input("Ingrese el nombre del producto: ").strip().lower()
        resultados = [producto for producto in stock_list if nombre in producto["Producto"].strip().lower()]

    # Si se busca por el ID del producto
    elif criterio == 2:
        try:
            producto_id = int(input("Ingrese el ID del producto: "))
            resultados = [producto for producto in stock_list if (producto["Producto_id"]) == producto_id]
        except ValueError:
            print("ID inválido, Debe ser un número entero")
            resultados = []

    # Si se encuentra el producto, se imprimen los resultados
    if resultados:
        print(f"{'ID':<10} {'Producto':<20} {'Marca':<15} {'Presentación':<15} {'Precio Unitario':<15} {'Stock':<10}")
        for producto in resultados:
            print(f"{producto['Producto_id']:<10} {producto['Producto']:<20} {producto['Marca']:<15} {producto['Presentacion']:<15} {producto['PrecioU']:<15} {producto['Stock']:<10}")
    else:
        print("No se encontraron productos que coincidan con los criterios de búsqueda.")

# Menú general Facturas
def facturas(Interfaces: dict):
    while True:
        print(Interfaces["Facturas"])
        # Se elige una opción de la interfaz mostrada
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue

        # Ejecutar la opción seleccionada
        match a: # Se redirige a la función deseada
            case 1:
                crearfact()
            case 2:
                verfacturas(Interfaces)
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")

# Función para crear una factura
def crearfact():
    # Cargar los datos desde el archivo JSON
    data = load_data("database.json")

    # Se solicitan los datos del cliente
    cc = int(input("C.C: "))
    mp = str(input("Pago en Efectivo o por Tarjeta: "))
    contacto = str(input("Se enviará la factura a (email o teléfono): "))
    fecha = datetime.now().strftime("%Y-%m-%d")

    # Agrega el cliente a la lista de Clientes si no está registrado
    if not any(cliente["ID"] == cc for cliente in data["Clientes"]):
        data["Clientes"].append({"ID": cc, "Ultimo_Metodo_Pago": None, "Valor_Total_Compras": 0})

    # Se declaran e inicializan las variables
    total_factura: float = 0 
    productos_comprados: list = []

    # Bucle para ingresar productos
    while True:
        codeprod = input("Codigo: ")
        if codeprod == "": 
            # Rompe el bucle si el codigo está vacio
            break
        codeprod = int(codeprod)

        # Se obtienen los detalles del producto
        datos_producto = ustock(codeprod, data)
        if datos_producto is None:
            print("Producto no encontrado.")
            continue
        
        # Se verifica si el producto tiene un stock válido
        if datos_producto['Stock'] is None:
            print("Producto no encontrado.")
            continue
        
        unit = int(input("Unidades: "))

        # Se verifica si hay suficiente stock
        if unit > datos_producto["Stock"]:
            print(f"Stock insuficiente para el producto {datos_producto['Producto']}, solo quedan {datos_producto['Stock']} unidades.")
            continue

        # Calcula el subtotal para este producto
        subtotal = datos_producto["PrecioU"] * unit
        total_factura += subtotal

        # Agrega el producto a la lista de productos comprados
        productos_comprados.append((codeprod, datos_producto["Producto"], datos_producto["Marca"], datos_producto["Presentacion"], datos_producto["PrecioU"],unit, subtotal))

        # Actualiza el stock del producto
        datos_producto["Stock"] -= unit
    
    save_data("database.json", data)

    # Agrega la factura a la lista de facturas
    data["Facturas"].append({
        "Factura_id": len(data["Facturas"]) + 1, # Incrementa en 1 el ID de factura
        "Cliente_id": cc,
        "Contacto": contacto,
        "MetodoPago": mp,
        "Fecha": fecha,
        "Total": total_factura,
        "Productos": productos_comprados
    })
    # Guarda los cambios en el archivo JSON
    save_data("database.json", data)

    # Se llama a la función para imprimir la última factura agregada
    ultima_factura = data["Facturas"][-1]  # Obtiene la última factura agregada
    imprimir_factura(ultima_factura)

# Función para ver todas las facturas
def verfacturas(Interfaces: dict):
    # Se carga la información del JSON, y de ella se obtiene la lista de facturas
    data = load_data("database.json")
    listaDeFacturas : list = data.get("Facturas", [])

    # Se crea el intervalo del que se tomaran las facturas
    print("Crea un intervalo de facturas para reducir la cantidad mostrada junta")
    min = int(input("Ingresa el valor mínimo: "))
    max = int(input("Ingresa el valor máximo: "))

    # Se imprimen las facturas que cumplan con estar dentro del intervalo
    print(f"{'ID':<10} {'Cliente':<15} {'Contacto':<25} {'Método de Pago':<15} {'Fecha':<15} {'Total':<20}")
    for factura in listaDeFacturas:
        if min <= factura["Factura_id"] and factura["Factura_id"] <= max :
            bandera = True
            print(f"{factura['Factura_id']:<10} {factura['Cliente_id']:<15} {factura['Contacto']:<25} {factura['MetodoPago']:<15} {factura['Fecha']:<15} {factura['Total']:<20}")
    if bandera == False: # Si ninguna lo hace se imprime este mensaje
        print("No se encontraron facturas con ID's entre dichos valores")
    Elección = int(input("Qué factura deseas ver? "))

    for factura in listaDeFacturas:
        if Elección == factura['Factura_id']:
            facturaSeleccionada = factura
    # Se llama a la función para imprimir la factura elegida
    imprimir_factura(facturaSeleccionada)

# Función para imprimir la información de la factura
def imprimir_factura(factura):

    # Se imprimen los datos de la factura de forma organizada
    print(f"\nFactura ID: {factura['Factura_id']}")
    print(f"Fecha: {factura['Fecha']}")
    print(f"Cliente ID: {factura['Cliente_id']}")
    print(f"Método de pago: {factura['MetodoPago']}")
    print(f"Se enviará la factura a: {factura['Contacto']}")
    print("\nDetalle de Productos:")
        
    # Encabezado
    print(f"{'ID':<10} {'Producto':<20} {'Marca':<15} {'Presentación':<15} {'Precio Unitario':<15} {'Unidades':<10} {'Subtotal':<10}")
    print("="*110)
    
    # Datos de productos
    for producto in factura['Productos']:
        print(f"{producto[0]:<10} {producto[1]:<20} {producto[2]:<15} {producto[3]:<15} {producto[4]:<15.2f} {producto[5]:<10} {producto[6]:<10.2f}")
        
    # Total
    print("\nTotal de la Factura:")
    print(f"Total: {factura['Total']:.2f}")

# Funcion para encontrar un producto en la lista de stock usando su ID
def ustock(codeprod, data):

    # Recorre cada producto en la lista de stock
    for producto in data.get("Stock", []):
        if int(producto["Producto_id"]) == int(codeprod): # Si encuentra un producto con la id correspondiente, lo retorna
            return producto
    return None # Si no lo encuentra, retorna None

# Menú general de Estadísticas
def stats(Interfaces: dict):
    while True:
        print(Interfaces["Estadísticas"])

        # Se elige una de las opciones mostradas
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue

        # Ejecutar la opción seleccionada
        match a: # Se redirige a la función deseada
            case 1:
                sellstats(Interfaces)
            case 2:
                statsclients(Interfaces)
            case 3:
                budgetstats(Interfaces)
            case 4:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 4.")

# Menú de Estadísticas de ventas
def sellstats(Interfaces: dict):
    while True:
        print(Interfaces["Ventas"])
        
        # Se elige una de las opciones mostradas
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 

    # Ejecutar la opción seleccionada
        match a: # Se redirige a la función deseada
            case 1:
                producto_mas_vendido()
            case 2:
                IngresosTotales()
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")

# Función para mostrar el producto más vendido
def producto_mas_vendido():
    # Se carga la información del JSON
    data = load_data("database.json")
    # Diccionario para contar las unidades vendidas por producto
    conteo_productos = {}
    # Itera sobre todas las facturas
    for factura in data["Facturas"]:
        for producto in factura["Productos"]:
            id_producto = producto[0] # Indexa sobre las propiedades del producto
            unidades = producto[5]
            if id_producto in conteo_productos:
                conteo_productos[id_producto] += unidades
            else:
                conteo_productos[id_producto] = unidades
    
    if conteo_productos:
        producto_mas_vendido_id = max(conteo_productos, key=conteo_productos.get)
        producto = ustock(producto_mas_vendido_id, data)
        
        if producto:
            print("Producto más vendido:")
            print(f"ID: {producto['Producto_id']}")
            print(f"Nombre: {producto['Producto']}")
            print(f"Marca: {producto['Marca']}")
            print(f"Presentación: {producto['Presentacion']}")
            print(f"Precio Unitario: {producto['PrecioU']}")
            print(f"Unidades Vendidas: {conteo_productos[producto_mas_vendido_id]}")
        else:
            print("El producto más vendido no se encuentra en el stock.")
    else:
        print("No se han registrado ventas o no hay productos en el stock.")

# Función para mostrar los ingresos totales registrados
def IngresosTotales():
    # Se carga la información del JSON
    data = load_data("database.json")
    IngresoNeto : float = 0
    fechas : list = []
    
    # Se inicia un bucle, donde por cada factura se va acumulando el ingreso, hasta obtener todos ellos
    for i in data["Facturas"]:
       Ingreso = i.get("Total")
       IngresoNeto += Ingreso
       fechas.append(i.get("Fecha"))
    fechas.sort()
    print("Ingresos Totales: ")
    print(f"EL Total de Ingresos entre {fechas[0]} y {fechas[-1]} es {float(IngresoNeto)}")

# Menú de Estadísticas de clientes
def statsclients(Interfaces: dict):
    while True:
        print(Interfaces["Clientes"])
        
        # Se elige una de las opciones mostradas
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 

    # Ejecutar la opción seleccionada
        match a: # Se redirige a la función deseada
            case 1:
                clientemascompras()
            case 2:
                promxclcom()
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")

# Función para mostrar al cliente con mayor cantidad de compras
def clientemascompras():
    # Se carga la información del JSON
    data = load_data("database.json") 
    while bandera == True:
        print(Interfaces["Clientbuy"])
        
        # Se elige una de las opciones mostradas
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 

        match a: # Mostrar el cliente con más compras por
            
            # Número de facturas
            case 1:
              cantfact = []
              for i in idclientsord():
                  facturas = 0
                  for j in data["Facturas"]:
                    if i == j["Cliente_id"]:
                      facturas += 1
                    cantfact.append([int(facturas), i])
              cantfact.sort(reverse=True)
              print(f"El cliente con mas facturas tiene ID {cantfact[0][1]} con un total de {cantfact[0][0]} facturas.")
            
            # Dinero gastado
            case 2:
              idtotal = []
              for i in idclientsord():
                  Invertido = 0
                  for j in data["Facturas"]:
                    if i == j["Cliente_id"]:
                      Invertido += j["Total"]
                  idtotal.append([int(Invertido), i])
              idtotal.sort(reverse=True) 
              print(f"El cliente que mas ha gastado tiene ID {idtotal[0][1]} con {idtotal[0][0]} gastados ")
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")

# Función para mostrar el promedio de compras por cliente
def promxclcom():
    # Se carga la información del JSON
    data = load_data("database.json") 
    while bandera == True:
        print(Interfaces["Clientprom"])
        try:
            # Se elige una de las opciones mostradas
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 

        match a: # Se mostrará el gasto promedio
            case 1: # Por el número de clientes
                 Invertido = 0
                 for i in idclientsord():
                  for j in data["Facturas"]:
                    if i == j["Cliente_id"]:
                      Invertido += j["Total"]
                 promxcl = Invertido / len(idclientsord())
                 print(f"El gasto promedio por cliente es {int(promxcl)}")

            case 2: # Por el número de facturas
                 inv = 0
                 facturas = 0
                 for i in data["Facturas"]:
                     inv += i["Total"]
                     facturas += 1
                 print(f"El gasto promedio por factura es {int(inv / facturas)}")
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")

# Menú de Estadísticas del inventario
def budgetstats(Interfaces: dict):
    while True:
        print(Interfaces["InvenStats"])
        try:
            # Se elige una de las opciones mostradas
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 

    # Ejecutar la opción seleccionada
        match a: # Se redirige a la función deseada
            case 1:
                bajostock()
            case 2:
                valtotinv()
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")

# Función para mostrar los productos con un stock más bajo que el ingresado
def bajostock():
    # Se inicializan las variables
    a = int(input("Ingrese el valor mínimo de stock para filtrar: "))
    data = load_data("database.json") # Se carga la información del JSON
    
    # En el bucle se almacenan los productos con stock por debajo de la cantidad ingresada en una lista
    for i in data['Stock']:
        if i['Stock'] < a:
            producto_info = f"{i["Producto"]} {i["Marca"]} {i["Presentacion"]}"
            print(f"El producto {producto_info} está agotado o por agotarse, {i["Stock"]} unidades") 
            # Devuelve la lista de productos con bajo stock

# Función para mostrar el valor total del inventario actual
def valtotinv():
   # Se inicializan las variables
   vltotal : float = 0
   data = load_data("database.json") 

   # En el bucle se acumula el precio unitario de cada producto, multiplicado por su stock
   for i in data['Stock']:
       vltotal += i['Stock']*i['PrecioU']
   print(F"El valor Total del inventario es {float(vltotal)}")
       
# Función main para dar inicio al programa
if __name__ == "__main__":

    # Se llama a la función para crear la base de datos si no existe
    initialize_data()

    # Se declaran e inicializan las variables que serán utilizadas
    bandera: bool = True
    I1 : str = """
Bienvenido al auxiliar de Negocios Keyfact \n
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
        |  4  |       Atrás           |
    """
    I3 : str = """
        Editar Inventario
        |    Seleccione una opción    |
        |  1  | Añadir Producto       |
        |  2  | Eliminar Producto     |
        |  3  |       Atrás           |
    """
    I4 : str = """
        Criterio de Organización
        |    Seleccione una opción    |
        |  1  | Por costo             |
        |  2  | Por ID                |
        |  3  |       Atrás           |
    """
    I5 : str = """
                  Orden
        |    Seleccione una opción    |
        |  1  | Ascendente            |
        |  2  | Descendente           |
        |  3  |       Atrás           |
    """
    I6 : str = """
        Opciones de Búsqueda:
        |    Seleccione una opción    |
        |  1  |  Por nombre           |
        |  2  |  Por ID               |
        |  3  |       Atrás           |
    """
    I7 : str = """
        |           Facturas          |
        |  1  |        Crear          |
        |  2  |    Ver por número     |
        |  3  |       Atrás           |
    """
    I8 : str = """
        |        Estadísticas         |
        |  1  |       Ventas          |
        |  2  |       Clientes        |
        |  3  |       Capital         |
        |  4  |       Atrás           |
    """
    I9 : str = """
        |   Estadísticas de Ventas    |
        |  1  | Producto más vendido  |
        |  2  |   Ingresos totales    |
        |  3  |       Atrás           |
    """
    I10 : str = """
        |  Estadísticas de Clientes   |
        |  1  |Cliente con más compras|
        |  2  |    Gasto promedio     |
        |  3  |       Atrás           |
    """
    I11 : str = """
        |   Estadísticas de Inventario   |
        |  1  | Productos con bajo stock |
        |  2  |Valor total del inventario|
        |  3  |         Atrás            |
    """
    I12 : str = """
        |   Clientes con más compras     |
        |  1  |  Por Numero de Facturas  |
        |  2  |  Por Dinero Gastado      |
        |  3  |         Atrás            |
    """ 
    I13 : str = """
        |           Gasto Promedio       |
        |  1  |      Por Cliente         |
        |  2  |      Por Factura         |
        |  3  |         Atrás            |
    """ 
    # Se guardan las interfaces en un diccionario para facilitar su transporte entre funciones
    Interfaces: dict = {"General": I1,"Inventario":I2, "Editar": I3,"Visibilidad": I4, "Orden": I5, "Búsqueda" : I6, "Facturas": I7}
    Interfaces.update({"Estadísticas": I8, "Ventas": I9, "Clientes": I10, "InvenStats": I11, "Clientbuy": I12, "Clientprom": I13})
    
    # Se llama a la función del menú y se ingresan las interfaces junto con la bandera
    menu(Interfaces, bandera)
