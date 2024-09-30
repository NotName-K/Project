# Programa Auxiliar de Negocios KeyFacT
Proyecto de la Asignatura Programación de Computadores 2024-1
***

![Logo-equipo.png](https://github.com/NotName-K/Project/blob/main/Imagenes/Logo.png?raw=true)
 
## Integrantes 
 * Kevin Daniel Castellanos Peña C.C. 1052338203
 * Julian Jacobo Gustin Moreno  T.I. 1081275973
 * Lucas Garcia Álvarez T.I. 1062434165

*Nota*: Este proyecto se llevó a cabo con la versión de python 3.12.5
## Descripción del problema
Es muy común que a la hora de empezar con tu propio emprendimiento o idea de negocios te encuentres con dificultades para llevar registro de los movimientos, inventario, e incluso clientes de tu empresa, por lo que no es de extrañar que debido a la confusión muchos de estos negocios principiantes tiendan a sufrir grandes pérdidas e incluso tener que abandonar su actividad al no poder sobrellevar esta problemática.

Es por esto que el presente proyecto se diseñó como una aplicación modular, ofreciendo una solución simple e intuitiva para la gestión diaria del negocio, esta basada en la consola orientada para estas pequeñas empresas y se propone gestionar productos, clientes y facturas, asegurando un control ágil y eficiente del inventario y la facturación. Incluyendo características avanzadas como calculo de impuestos, manejo de presupuesto, rentabilidad de venta, gastos de la empresa, generación de reportes y estadisticas, y demás caracteristicas que serán desarrolladas en el código y reflejadas en los siguientes apartados.

El siguiente proyecto fue escogido ya que nos enfocamos en hacer algo útil y practico para quien requiera usar el programa, además de tener un rango de mejora inmenso dependiendo de las necesidades de cada usuario, lo que permite que sea aplicable en diversos contextos y empresas con requerimientos diferentes a los de las demás.

## Cómo abordamos el problema
Primeramente, el programa debe funcionar en distintas ocasiones y debe guardar los datos ya registrados previamente para que se mantenga el seguimiento, por esto, se tuvo la necesidad de crear una base de datos para ello.

Esto puede llevarse a cabo de distintas formas, ya que inicialmente se probó con SQL, sin embargo, el equipo se decantó por usar archivos de texto con formato JSON debido a su mayor cercanía a los contenidos de la asignatura y su simpleza frente a otras alternativas; el funcionamiento se basa en que el programa lee un archivo llamado database.db, el cuál este mismo creará si no existe previamente, y en él se almancenan datos que al cargar se convierten en archivos JSON contenedores de las variables que requerimos y que se guardan en la misma base de datos.

```mermaid
 graph TD;
 A(Inicio);
    A -->F1[Se intenta abrir la base de datos];
    F1-->|Existe|G1[Se carga el contenido];
    F1-->|No existe|H1[Se crea diccionario con listas];
    G1-->I1;
    H1-->I1[Se convierte el diccionario en JSON];
    I1-->J1[Se escribe el JSON en el archivo];
    J1-->K1[Se guarda la información en el archivo];
```

Hecha la base de datos ya se pudo empezar a trabajar en la resolución de esta problemática, nos encargamos de detallar las funciones que como mínimo el programa debería cumplir, teniendo en cuenta los requerimientos más generales de cualquier empresa y los que más relevancia tiene el mantener seguimiento.

En ese sentido se creó el siguiente diagrama en donde se reflejan estas funciones básicas:

![Diagrama preliminar.jpg](https://github.com/NotName-K/Project/blob/main/Imagenes/Diagrama%20preliminar.jpg)

Como se puede observar el foco del proyecto va en torno a las ventas, el inventario, los clientes y las estadísticas que todo emprendimiento necesita, en ese sentido, se diseñó el programa con la idea de poder llevar a cabo cálculos y seguimientos de estos aspectos.

Teniendo eso en cuenta se creó un diseño modular en el que cada función se enuentra de un campo relativo al componente del que se relacione, por ejemplo, las opciones de ver el inventario o añadir algún producto a él están dentro del apartado "Inventario"; cada apartado tiene como acceso el menú principal desde donde inicia la interacción con el usuario y en donde terminará finalmente, puesto que la idea es que el usuario no tenga que ingresar repetidas veces en intervalos cortos de tiempo para, digamos, añadir 10 productos al inventario, de esta forma el usuario puede agregar estos productos o realizar cualquier otra acción las veces que desee y al final regresar al menú y cerrar el programa.

```mermaid
 graph TD;
 A(Inicio);
 A -->F1[Se carga/crea la base de datos];
    F1 -->B{Menú Principal};
       B -->|Opción 1|C{Inventario};
       B -->|Opción 2|R{Modo de Facturación};
       B -->|Opción 3|S{Estadísticas};
       B -->|Opción 4|C1[Terminar programa];
       C1 -->D1(Fin);
```
Posteriormente, se diseñó cada apartado teniendo en cuenta esas funciones que ya habíamos seleccionado y se aplicó el sistema modular propuesto al igual que se hizo con el menú principal.

- Inventario:

El apartado de Inventario debe incluir las opciones de añadir o eliminar productos, así como también de buscarlos bajo ciertos criterios, que posteriormente se definieron como el nombre o el ID de dichos productos; y finalmente el poder reflejarlos ordenados en la manera en que el usuario prefiera o necesite.

```mermaid
graph TD;
B{Menú} -->|Opción 1|C{Inventario};
          C -->|Opción 1|D{Editar Inventario};
             D-->zz{Ingreso de Contraseña}
              zz -->|Opción 1|E[Añadir Producto];
              E -->LL{Guardar cambios};
              zz -->|Opción 2|F[Eliminar Producto];
              F -->LL;
              D -->|Regresar|C
              LL --> C
          C -->|Opción 2|G{Ver Inventario};
              G -->H{Mostrar por:};
                 H -->|Opción 1|I[Precio];
                 H -->|Opción 2|J[Código];
                 H -->|Regresar|C;
                 I -->K;
              J -->K{Ver en Orden:};
                 K -->|Opción 1|L[Ascendente];
                 L -->KQ{Inventario Mostrado};
                 K -->|Opción 2|M[Descendente];
                 M -->KQ;
                 K -->|Regresar|C;
                 KQ --> C
          C -->|Opción 3|N{Buscar producto};
              N -->O{Buscar por:};
                 O -->|Opción 1|P[Nombre];
                 P -->KJ{Producto Mostrado};
                 O -->|Opción 2|Q[Código];
                 Q -->KJ;
                 KJ -->|Regresar|C;
          C -->|Regresar|B;
```
- Facturación:

Cómo tal no es un apartado, está dentro del menú principal debido a su indudable importancia a la hora de manejar negocios, ya que de ahí parten todas las demás funciones y estadísticas, y una buena parte del tiempo se empleará en facturar a los consumidores de los productos de la empresa.

```mermaid
graph TD;
B{Menú} -->|Opción 2|R[Modo de Facturación];
    R -->L1[Crear];
    R -->L2[Ver Factura por ID de Factura];
    R-->L3[Ver Factura por ID de Cliente];
    L1-->U1{ID del Cliente};
    U1-->|Si no esta registrado|M1[Se registra en la base de datos];
    M1 -->W1[Pedir Varios Datos mas al cliente]
    U1-->|Si esta registrado|N1;
    W1-->N1
    M1-->N1[Se ingresa el código de los productos];
    N1-->|Si no existe|N1;
    N1-->O1[Se ingresan las unidadades por comprar]
    O1-->P1[Unidades > Stock?];
    P1-->|Sí|N1;
    P1-->|No|Q1[Se registra la compra];
    Q1-->R1[Se restan las unidades del stock];
    R1-->S1[Se imprime la factura];
    S1-->T1[Se guarda la información en el archivo];
    T1-->B;

    L2 -->K2[Se muestran las facturas por ID de Factura]
    L3 -->K3[Se muestran las facturas por ID de Cliente]
    K2 -->B
    K3 -->B
```

- Estadísticas:

Para el apartado de estadísticas se planteó que el usuario pueda analizar el comportamiento de su empresa teniendo en cuenta variables como: el producto más vendido, Productos con bajo Stock o Gasto Promedio, utilizando el mismo sistema modular visto anteriormente dentro de las categorías "Ventas", "Clientes" y "Capital".
```mermaid
 graph TD;
B[Menú] -->|Opción 3|S{Estadísticas};
    S -->|Opción 1|T{Ventas};
        T -->|Opción 1|U[Producto más vendido];
        U -->L[Se muestra Producto] --> S;
        T -->|Opción 2|V[Ingresos Totales];
        V -->M[Se muestran Ingresos Totales] --> S;
        T -->|Regresar|S;
    S -->|Opción 2|W{Clientes};
        W -->|Opción 1|X{Cliente con más compras};
            X -->|Opción 1|N1[Por número de facturas];
            N1 -->R[Se muestra Cliente por número de facturas] --> S;
            X -->|Opción 2|N2[Por dinero gastado];
            N2 -->R2[Se muestra Cliente por dinero gastado] --> S;
        W -->|Opción 2|Y{Gasto promedio};
            Y -->|Opción 1|O1[Por cliente];
            O1 -->P1[Se muestra Gasto promedio por cliente] --> S;
            Y -->|Opción 2|O2[Por factura];
            O2 -->P2[Se muestra Gasto promedio por factura] --> S;
        W -->|Regresar|S;
    S -->|Opción 3|Z{Capital};
        Z -->|Opción 1|A1{Productos con bajo stock};
            A1 -->|Opción 1|P[cantidad de stock maxima requerida];
            P -->P3[Se muestra productos con stock menor a lo ingresado ] --> S;
        Z -->|Opción 2|B1[Valor total del inventario];
        B1 -->Q[Se muestra Valor total del inventario] --> S;
        Z -->|Regresar|S;
```
Al juntarse todos estos procesos se obtiene el siguiente resultado:
```mermaid
graph TD;
B{Menú} -->CCC{Inventario};
          CCC -->|Opción 1|DDD{Editar Inventario};
             DDD -->ZZZ{Ingreso de Contraseña}
              ZZZ -->|Opción 1|EEE[Añadir Producto];
              EEE -->|si ya está..|EEE
              EEE -->|si no está|LLL{Guardar cambios};
              ZZZ -->|Opción 2|FFF[Eliminar Producto];
              FFF -->LLL;
              DDD -->|Regresar|CCC
              LLL --> CCC
          CCC -->|Opción 2|GGG{Ver Inventario};
              GGG -->HHH{Mostrar por:};
                 HHH -->|Opción 1|III[Precio];
                 HHH -->|Opción 2|JJJ[Código];
                 HHH -->|Regresar|CCC;
                 III -->KKK;
              JJJ -->KKK{Ver en Orden:};
                 KKK -->|Opción 1|BBB[Ascendente];
                 BBB -->KQQ{Inventario Mostrado};
                 KKK -->|Opción 2|MMM[Descendente];
                 MMM -->KQQ;
                 KKK -->|Regresar|CCC;
                 KQQ --> CCC
          CCC -->|Opción 3|NNN{Buscar producto};
              NNN -->OOO{Buscar por:};
                 OOO -->|Opción 1|PPP[Nombre];
                 PPP -->KJJ{Producto Mostrado};
                 OOO -->|Opción 2|QQQ[Código];
                 QQQ -->KJJ;
                 KJJ -->|Regresar|CCC;

B[Menú] -->|Opción 3|SS{Estadísticas};
    SS -->|Opción 1|TT{Ventas};
        TT -->|Opción 1|UU[Producto más vendido];
        UU -->LL[Se muestra Producto] --> SS;
        TT -->|Opción 2|VV[Ingresos Totales];
        VV -->MM[Se muestran Ingresos Totales] --> SS;
        TT -->|Regresar|SS;
    SS -->|Opción 2|WW{Clientes};
        WW -->|Opción 1|XX{Cliente con más compras};
            XX -->|Opción 1|N1[Por número de facturas];
            N1 -->RR[Se muestra Cliente por número de facturas] --> SS;
            XX -->|Opción 2|N2[Por dinero gastado];
            N2 -->R2[Se muestra Cliente por dinero gastado] --> SS;
        WW -->|Opción 2|YY{Gasto promedio};
            YY -->|Opción 1|O1[Por cliente];
            O1 -->P1[Se muestra Gasto promedio por cliente] --> SS;
            YY -->|Opción 2|O2[Por factura];
            O2 -->P2[Se muestra Gasto promedio por factura] --> SS;
        WW -->|Regresar|SS;
    SS -->|Opción 3|ZZ{Capital};
        ZZ -->|Opción 1|A1{Productos con bajo stock};
            A1 -->|Opción 1|PP[cantidad de stock maxima requerida];
            PP -->P3[Se muestra productos con stock menor a lo ingresado] --> SS;
        ZZ -->|Opción 2|B1[Valor total del inventario];
        B1 -->QQ[Se muestra Valor total del inventario] --> SS;
        ZZ -->|Regresar|SS; 


B{Menú} -->|Opción 2|A{Modo de Facturación};
    A -->C[Crear];
    A -->D[Ver factura por ID de Factura];
    A -->E[Ver factura por ID de cliente];
    C -->F{ID del Cliente};
    F -->|Si no está registrado|H[Pedir Varios Datos más al cliente];
    H -->G[Se registra en la base de datos];
    F -->|Si está registrado|I;
    G -->I[Se ingresa el código de los productos];
    I -->|Si no existe el producto|I;
    I -->K[Se ingresan las unidades por comprar];
    K -->L[Unidades > Stock?];
    L -->|Sí|I;
    L -->|No|M[Se registra la compra];
    M -->N[Se restan las unidades del stock];
    N -->O[Se imprime la factura];
    O -->P[Se guarda la información en el archivo];
    P -->B;

    D -->Q[Se muestran las facturas por ID de Factura];
    E -->R[Se muestran las facturas por ID de Cliente];
    Q -->B;
    R -->B;
```

## Solución planteada

Luego de ya tener la idea de como llevar a cabo la solución de la problemática se inició la codificación de esta en el mismo orden en el que se planteó cada parte del programa.
### Inicializar, cargar y guardar datos en archivo JSON
En este caso, nos guiamos por los métodos dentro de la clase 18 de la asignatura "Diccionarios" y tal cómo se propuso en el diagrama de flujo, el programa lee, si existe o crea sino, el archivo de la base de datos y convierte sus datos a JSON para luego guardar cambios, si hubo, y utilizar la información de manera posterior.
```python
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
        print("Iniciando programa \n Agregue Contraseña de Administrador")
        # Se añade la contraseña y la pregunta de recuperación
        password = str(input("Nueva Contraseña: "))
        pregunta = str(input("Pregunta de Recuperación : "))
        respuesta = str(input("Respuesta: "))
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
        print("\nEl archivo JSON ya existe. No se realizaron cambios") 
```
***
### Interfaz Gráfica y sistema modular
Tal como se indicó desde el inicio, uno de los puntos clave del programa es ser sencillo de utilizar y permitir desplazarse entre cada módulo o apartado sin ningún problema, para esto se utilizó la estructura match case, en donde el usuario selecciona el número de una de las opciones impresas en la terminal y el programa lo redigirá al apartado o acción deseada.

Para facilitar la comprensión de la métodología propuesta el grupo llevó a cabo la creación de "Interfaces" guardadas en cadenas de caracteres, y estas a su vez en diccionarios para facilitar su ingreso a las funciones y acceso dentro de estas.

```python
# Ejemplo de módulo
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

# Ejemplo de Interfaz
I1 : str = """
Bienvenido al auxiliar de Negocios KeyFact \n
    |        Menú Principal       |
    |  1  |  Inventario           |
    |  2  |  Modo de Facturación  |
    |  3  |  Estadísticas         |
    |  4  |  Cerrar el programa   |
    """
```
***
### Funcion principal para acceso de administrador
En esta función se implementa el sistema de autenticación mediante contraseña para realizar acciones sensibles, como añadir y eliminar productos del stock. El proceso inicia solicitando al administrador del negocio una contraseña de acceso, posteriormente cuando se requiera añadir o eliminar un producto, se solicita que ingrese la contraseña. Si la contraseña es correcta, se procede a mostrar un menú de opciones para gestionar el inventario. Si la contraseña es incorrecta, se informa al usuario y se termina el proceso.
Esto tiene un metodo de recuperacion basado en pregunta respuesta definido por el administrador.
```python
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

```

***
### Funcion principal para gestionar la entrada de datos de una factura
En esta función se lleva a cabo el proceso de facturar una compra, para esto se carga el archivo y se obtiene el stock de cada producto del inventario, se ingresa el cliente y se registra si aún no lo está, luego se busca por el ID el producto y se digita las unidades que se desean adquirir, si cualquiera de estos datos no concuerda se regresa a ingresar el código y unas unidades aceptables, cuando ello suceda, se registrará la compra y la factura en la base de datos, se reducirá el stock del producto y se imprimirá la factura con la fecha exacta.

```python
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
        Nombre = str(input("Ingresa el nombre del cliente: "))
        Apellido = str(input("Y su primer apellido: "))
        data["Clientes"].append({"ID": cc, "Nombre": Nombre,"Apellido": Apellido,"Facturas": []})

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
    for cliente in data["Clientes"]:
        if cliente["ID"] == ultima_factura["Cliente_id"]:
            cliente = {"ID":cliente["ID"],"Nombre":cliente["Nombre"],"Apellido":cliente["Apellido"],"Facturas":cliente["Facturas"].append(ultima_factura["Factura_id"])}
    save_data("database.json", data)

    imprimir_factura(ultima_factura)
```
***
### Funciones para gestionar la entrada de datos de stock (agregar, eliminar)
Para agregar un dato al inventario se abre el archivo y cargan sus datos, luego se indican todos los datos asociados al producto (ID, Nombre, Marca, Presentación, Precio, Unidades en stock), se añade a la lista de stock y se guardan los cambios.

Por otra parte, para eliminar un producto se abre el archivo y esta misma lista donde se encuentra cada producto, se busca por el ID ingresado y se elimina de la lista.
```python
# Función para añadir un producto al inventario
def datastock():
    # Se carga la información del JSON
    data = load_data("database.json")
    while True:
        try:
            print("Ingrese los datos del producto (Digite ENTER para finalizar): ")
            # Se solicita el ID del producto
            producto_id = int(input("ID del Producto: "))

            #Verificar si la id ya está en uso
            id_encontrado = False
            for producto in data["Stock"]:
                if int(producto["Producto_id"]) == producto_id:
                    id_encontrado = True
                    break
            
            if id_encontrado:
                print(f"Error: El producto con ID {producto_id} ya existe")
                continue

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

```
```python
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
```
eliminar el producto ingresado en la función anterior
```python
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
```
***
### Funciones para ver y buscar en el inventario
Para poder visualizar el inventario primeramente se pregunta al usuario el criterio por el cual se van a ordenar los productos, en este caso se cuenta con dos, el precio y el ID, además de esto se debe ingresar si se desea un orden ascendente o descendente, esto dependiendo de cómo le sea más útil al usuario dicha información, para luego ordenar la lista de stock con base a los criterios seleccionados e imprimir los resultados.
```python
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
```
Función para mostrar el inventario según los criterios anteriores
```python
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

```
A su vez, para buscar algún producto se utiliza una estrategia similar, se carga la información del archivo y se obtiene la lista de stock, de donde por medio del nombre o del ID el usuario busca el producto deseado.
```python
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

```
* Funcion para Mostrar una Factura segun su ID o segun ID del Cliente
```python
def verfacturaCliente():
    # Se carga la información del JSON, y de ella se obtiene la lista de facturas
    data = load_data("database.json")
    listaDeClientes : list = data.get("Clientes", [])
    listaDeFacturas : list = data.get("Facturas", [])
    bandera: bool = False

    # Se imprimen los clientes
    print(f"{'ID':<10} {'Nombre':<20} {'Apellido':<20}")
    for cliente in listaDeClientes:
        bandera = True
        print(f"{cliente['ID']:<10} {cliente['Nombre']:<20} {cliente['Apellido']:<20}")
    if bandera == False:
        print("Actualmente no se tiene registrado ningún cliente")
    while True:
        try:
            ID = int(input("\nIngresa el ID del cliente para ver sus facturas: "))
            break
        except ValueError:
            print("ID inválida, por favor ingrese un valor numérico entero válido\n")
    bandera = False
    # Se imprimen las facturas que cumplan con estar dentro del intervalo
    print(f"{'ID':<10} {'Cliente':<15} {'Contacto':<25} {'Método de Pago':<15} {'Fecha':<15} {'Total':<20}")
    for factura in listaDeFacturas:
        if factura['Cliente_id'] == ID:
            bandera = True
            print(f"{factura['Factura_id']:<10} {factura['Cliente_id']:<15} {factura['Contacto']:<25} {factura['MetodoPago']:<15} {factura['Fecha']:<15} {factura['Total']:<20}")
    if bandera == False: # Si ninguna lo hace se imprime este mensaje
        print("No se encontraron facturas con dicho ID")
        return
    
    while True:
        try:
            Elección = int(input("Qué factura deseas ver? "))
                # Se hace un bucle para obtener la factura deseada
            for factura in listaDeFacturas:
                if Elección == factura['Factura_id']:
                    facturaSeleccionada = factura
            # Se llama a la función para imprimir la factura elegida
            imprimir_factura(facturaSeleccionada)
            break
        except ValueError:
            print("ID inválido, por favor ingrese un número entero\n")
            continue
        except UnboundLocalError:
            print("Factura no existente, por favor ingrese una válida\n")

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
```
***
### Funciones de estadisticas
Se implementa el diseño modular y la estructura match case para el funcionamiento del menú y la elección de opciones por el usuario.
```python
def stats(Interfaces: dict, bandera : bool): # Menu de estadisticas
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
```
Estadísticas de venta
```python
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
                producto_mas_vendido()
            case 2:
                IngresosTotales()
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")
```
estadísticas de clientes
```python
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
                clientemascompras()
            case 2:
                promxclcom()
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")
```
Estadísticas del inventario
```python
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
                bajostock()
            case 2:
                valtotinv()
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")
```
Dentro de este menú, cómo podemos apreciar contamos con las siguientes seis opciones para poder analizar el inventario, las ventas y los clientes.
- Ingresos Totales
```python
# Función para obtener los ingresos totales entre determinadas fechas
def IngresosTotales(): 
    data = load_data("database.json")
    IngresoNeto: int = 0
    fechas: list = []
    for i in data["Facturas"]:
       Ingreso = i.get("Total")
       IngresoNeto += Ingreso
       fechas.append(i.get("Fecha"))
    fechas.sort()
    print("Ingresos Totales: ")
    print(f"EL Total de Ingresos entre {fechas[0]} y {fechas[-1]} es {int(IngresoNeto)}")
```
- Producto más vendido
```python
# Función para mostrar el producto más vendido
def producto_mas_vendido():
    data = load_data("database.json")
    # Diccionario para contar las unidades vendidas por rproducto
    conteo_productos = {}
    #Iterar sobre todas las facturas
    for factura in data["Facturas"]:
        for producto in factura["Productos"]:
            id_producto = producto[0] # Indexar sobre las propiedades del producto
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
```
- Cliente con más compras
```python
# Función para obtener y guardar el ID de los clientes, sin repetirse
def idclientsord():
    data = load_data("database.json")
    idclientesfact : list = []
    for i in data["Facturas"]:
        idclientesfact.append(i.get("Cliente_id"))
    idfactn = set(idclientesfact)
    return idfactn
```
cantidad de facturas por cada cliente e imprimir el cliente con mayor cantidad de estas
```python
def clientemascompras():
    data = load_data("database.json") 
    while bandera == True:
        print(Interfaces["Clientbuy"])
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 

        match a:
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
```
- Promedio de compras por cliente:
```python
#Función para acumular el dinero invertido en todos los productos vendidos y al dividirlo por el número de clientes, se obtiene el promedio de compras por cliente
def promxclcom():
    data = load_data("database.json") 
    while bandera == True:
        print(Interfaces["Clientprom"])
        try:
            a = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
            continue 

        match a:
            case 1:
                 Invertido = 0
                 for i in idclientsord():
                  for j in data["Facturas"]:
                    if i == j["Cliente_id"]:
                      Invertido += j["Total"]
                 promxcl = Invertido / len(idclientsord())
                 print(f"El gasto promedio por cliente es {int(promxcl)}")

            case 2:
                 inv = 0
                 facturas = 0
                 for i in data["Facturas"]:
                     inv += i["Total"]
                     facturas += 1
                 print(f"El gasto promedio por cliente es {int(inv / facturas)}")
            case 3:
                break
            case _:
                print("Opción no válida. Por favor, ingrese un número entre 1 y 3.")
```
- Productos con Bajo Stock
```python
# Se ingresa un valor mínimo que debe tener de stock los productos, si alguno tiene menos se imprime
def bajostock():
    bandera: bool = False
    a = int(input("Ingrese el valor mínimo de stock para filtrar: "))
    data = load_data("database.json")
    # Almacenar los productos con bajo stock en una lista
    for i in data['Stock']:
        if i['Stock'] < a:
            bandera : bool = True
            producto_info = f"{i["Producto"]} {i["Marca"]} {i["Presentacion"]}"
            print(f"El producto {producto_info} está agotado o por agotarse, {i["Stock"]} unidades") 
             # Devuelve la lista de productos con bajo stock
    if not bandera:
        print("No hay ningún producto con stock por debajo de esa cantidad")
```
- Valor total del inventario
```python
# Función para mostrar el valor total del inventario actual
def valtotinv():
   # Se inicializan las variables
   vltotal : float = 0
   data = load_data("database.json") 

   # En el bucle se acumula el precio unitario de cada producto, multiplicado por su stock
   for i in data['Stock']:
       vltotal += i['Stock']*i['PrecioU']
   print(F"El valor Total del inventario es {float(vltotal)}")
       
```
***
### Función Main y Apartado Gráfico en detalle
Contiene las interfaces que ya se describieron, se llaman a las funciones para inicializar la base de datos y se imprime la interfaz del menú.
```python
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
        |  3  |    Ver por cliente    |
        |  4  |       Atrás           |
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

```
## Instrucciones de uso
***
Cómo todo programa, este tiene un método para poder ser utilizado efectivamente y así llevar un total registro de los movimientos económicos que la empresa requiera.
### Instalación del programa
Para instalar el programa hay que seguir los pasos descritos a continuación:
- **Primero**: Hay que instalar el lenguaje de programación "python" en el sistema operativo.
      Para esto se debe ingresar a la página oficial y [descargar python](https://www.python.org/downloads/) en la versión más actual posible para tu sistema operativo, ya que dentro del código se utilizan estructuras como la de "match case" las cuales solo funcionan con versiones recientes, esta por ejemplo funciona de python 3.10 en adelante.
  
  Si estas usando Windows puedes comprobar que la instalación haya funcionado abriendo la consola de Windows, presionando (win + r), y escribir "python --version", si funcionó debería responder con la versión descargada y ya se tendría al interprete instalado, no obstante, si no funcionó tendrás que descargalo directamente en la tienda de Microsoft para luego ya realizar comprobación y muy seguramente ya habrá funcionado.
  
- **Segundo**: Debes descargar el [programa](https://github.com/NotName-K/Project/blob/main/ProyectoAuxiliarDeNegocios.py) de python y abrirlo en un editor de código como puede ser [Visual Studio Code](https://code.visualstudio.com/download), o si prefieres descarga el archivo .exe desde [este enlace](https://github.com/NotName-K/Project/blob/main/ProyectoAuxiliarDeNegocios.exe) y ejecutalo. 

### Cómo utilizarlo

En caso de preferir el archivo .exe, simplemente ejecutalo después de descargarlo.

Si el usuario utiliza el editor de código, debe utilizar la opción "File" en el extremo superior izquierdo de la interfaz de Visual Studio y seleccionar "Open New File", en la venta emergente ha de ubicar y abrir el archivo "ProyectoAuxiliarDeNegocios.py", de ahí utiliza el símbolo de "Play" o "Resumir" en la esquina superior derecha del editor, esta tiene como nombre "Run Python File", al hacer click esta dará inicio al programa.

Al iniciar, el programa abrirá el menú dentro de la terminal de Python en la parte baja de la interfaz del editor, allí se presentarán varias opciones según los requerimientos del usuario y este debe seleccionar el número de la opción que desee seleccionar.

Luego de realizar cualquier acción dentro de este programa se redigirá al usuario al menú inmediatamente anterior, por lo que para salir de este y darle fin ha de seleccionar "Cancelar" hasta llegar al menú principal donde debe elegir "Cerrar el Programa", en caso contrario, puede seguir eligiendo otras opciones y llevar a cabo otras funciones hasta donde el usuario lo desee.

