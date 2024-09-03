# Programa Auxiliar de Negocios Kevlab
Proyecto de la Asignatura Programación de Computadores 2024-1
***

 [![Logo-equipo.webp](https://i.postimg.cc/Z5BYw1Tx/Logo-equipo.webp)](https://postimg.cc/9D2jMgwD)
 
## Integrantes 
 * Kevin Daniel Castellanos Peña C.C. 1052338203
 * Julian Jacobo Gustin Moreno  T.I. 1081275973
 * Lucas Garcia Álvarez T.I. 1062434165

## Descripción del problema
Es muy común que a la hora de empezar con tu propio emprendimiento o idea de negocios te encuentres con dificultades para llevar registro de los movimientos, inventario, e incluso clientes de tu empresa, por lo que no es de extrañar que debido a la confusión muchos de estos negocios principiantes tiendan a sufrir grandes pérdidas e incluso tener que abandonar su actividad al no poder sobrellevar esta problemática.


Es por esto que el presente proyecto se diseñó como una aplicación modular, ofreciendo una solución simple e intuitiva para la gestión diaria del negocio, esta basada en la consola orientada para estas pequeñas empresas y se propone gestionar productos, clientes y facturas, asegurando un control ágil y eficiente del inventario y la facturación. Incluyendo características avanzadas como Gestión de Inventario, Facturación, eneración de reportes y estadisticas, y demás caracteristicas que serán desarrolladas en el código y reflejadas en los siguientes apartados.


El siguiente proyecto fue escogido ya que nos enfocamos en hacer algo útil y practico para quien requiera usar el programa, además de tener un rango de mejora inmenso dependiendo de las necesidades de cada usuario, lo que permite que sea aplicable en diversos contextos y empresas con requerimientos diferentes a los de las demás.

## Cómo abordamos el problema
## Solución planteada
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
## Instrucciones de uso
***
Cómo todo programa, este tiene un método para poder ser utilizado efectivamente y así llevar un total registro de los movimientos económicos que la empresa requiera.
### Instalación del programa
Para instalar el programa hay que seguir los pasos descritos a continuación:
- **Primero**: Hay que instalar el lenguaje de programación "python" en el sistema operativo.
      Para esto se debe ingresar a la página oficial y [descargar python](https://www.python.org/downloads/) en la versión más actual posible para tu sistema operativo, ya que dentro del código se utilizan estructuras como la de "match case" las cuales solo funcionan con versiones recientes, esta por ejemplo funciona de python 3.10 en adelante.
  
  Si estas usando Windows puedes comprobar que la instalación haya funcionado abriendo la consola de Windows, presionando (win + r), y escribir "python --version", si funcionó debería responder con la versión descargada y ya se tendría al interprete instalado, no obstante, si no funcionó tendrás que descargalo directamente en la tienda de Microsoft para luego ya realizar comprobación y muy seguramente ya habrá funcionado.
  
- **Segundo**: Se necesita descargar el Editor de código "Visual Studio Code", puede ser en este [link](https://code.visualstudio.com/docs/?dv=win) o directamente en la tienda de Microsoft.

- **Tercero**: Se necesita instalar ciertas extensiones en el editor de códigoDebes buscar el icono a la izquierda de la interfaz con el nombre de "Extensions" o presionar (Ctrl + Shift + X), con ello buscarás las siguientes extensiones y así descargarlas en el editor:

    1. Python  (Que incluirá Pylance y Python Debugger)
    2. SQLite Viewer (Necesario para poder observar adecuadamente las tablas de información)

- **Finalmente**: Dentro de este repositorio encontrará el archivo que contiene el código del programa, esta nombrado como "ProyectoAuxiliarDeNegocios.py" y se accede a él en la parte superior del repositorio donde estan varios archivos adjuntos, allí se ha de seleccionar el archivo y en la parte derecha de la pantalla encontrará la opción llamada "Download Raw File" al seleccionarla lo descargará y ya se habrá terminado todo el proceso de instalación.
### Cómo utilizarlo
Para utilizar el programa es tan sencillo como ir a la parte superior izquierda de la interfaz del editor en donde se hallará el menú "File", allí se seleccionará la opción "Open New File" y deberás buscar el archivo del programa dentro de tu dispositivo y así seleccionarlo y abrirlo, después de esto, en la parte superior derecha se encontrará un simbolo conocido normalmente como "Reanudar" o "Play", aquí recibe el nombre de "Run Python Fyle", debes de hacer click en él y con eso el programa iniciará inmediatamente.

Al iniciar el programa se abrirá el menú dentro de la terminal de Python en la parte baja de la interfaz del editor, allí se presentarán varias opciones según los requerimientos del usuario y este debe seleccionar el número de la opción que desee seleccionar.

Luego de realizar cualquier acción dentro de este programa se redigirá al usuario al menú inmediatamente anterior, por lo que para salir de este y darle fin ha de seleccionar "Cancelar" hasta llegar al menú principal donde debe elegir "Cerrar el Programa", en caso contrario, puede seguir eligiendo otras opciones y llevar a cabo otras funciones hasta donde el usuario lo desee.
