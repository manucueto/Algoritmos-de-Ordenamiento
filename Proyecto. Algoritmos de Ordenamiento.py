#Manuel Cueto - C.i 30.241.203
#Raul Villanueva - C.I 30.094.013
#José Daniel Vergara - C.I 32.071.576

"""
Una empresa de desarrollo de software está desarrollando un sistema de
generación de reportes y te ha contratado a ti y tus compañeros para desarrollar los
siguientes requerimientos:
Desarrollo de una aplicación de gestión de productos en Python, que permite
crear, modificar, consultar y listar productos cuyas opciones se mostrarán en un
menú:
1. La aplicación deberá permitir la creación de productos con atributos como
nombre, descripción, categoría, precio, imagen, SKU, cantidad, peso,
dimensiones(alto y ancho en cm), fecha de creación y fecha de
actualización. Los productos deberán almacenarse en memoria en una lista.
(2 ptos)
2. La aplicación deberá permitir la actualización de los atributos de los
productos, actualizar el precio o la descripción, y modificar la imagen del
producto. (2 ptos)
3. La aplicación deberá permitir cargar la lista de productos de prueba desde el
inicio de la aplicación. Estos productos deberán estar guardados en un
archivo csv (2 ptos)
4. La aplicación deberá permitir realizar los siguientes reportes junto a sus
respectivos algoritmos de ordenamiento, que serán seleccionados a través de
un submenú (10 ptos 2 ptos c/u):
a. Listar productos según su cantidad de forma ascendente utilizando el
algoritmo de quicksort
b. Listar productos de forma descendente según su peso en un rango de
fecha de actualización introducido por el usuario, utilizando el
algoritmo de mergesort
c. Listar productos de forma ascendente o descendente según su fecha
de creación utilizando el algoritmo de shellsort. La opción de
ordenamiento será seleccionada por el usuario
d. Listar los productos de forma ascendente según su cantidad
utilizando el algoritmo de heapsort
"""

from datetime import datetime

# Clase producto, los atributos privados son los valores de cada producto
class Producto:
    def __init__(self,nombre,descripcion,categoria,precio,imagen,sku,cantidad,peso,alto,largo,fecha_creacion,fecha_actualizacion):
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria = categoria
        self.precio = precio
        self.imagen = imagen
        self.sku = sku
        self.cantidad = cantidad
        self.peso = peso
        self.dimensiones = [alto, largo]
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion

    # Metodo que imprime los los atributos del objeto
    def imprimir(self):
        print(f' - Nombre: {self.nombre} Descripcion: {self.descripcion} Categoria: {self.categoria} Precio: {self.precio} Imagen: {self.imagen} SKU: {self.sku} Cantidad: {self.cantidad} Peso: {self.peso} \n   Dimensiones: {self.dimensiones[0]}cm de Largo {self.dimensiones[1]}cm de Ancho Fecha de creacion: {self.fecha_creacion} Fecha de actualizacion: {self.fecha_actualizacion}')
    
    # Metodo que retorna la cantidad de producto
    def getCantidad(self):
        return int(self.cantidad)
    
    # Metodo que retorna el peso del producto
    def getPeso(self):
        return float(self.peso)
    
    # Metodo que retorna la fecha de actualizacion
    def getFechaActualizacion(self):
        return self.fecha_actualizacion

# Funcion del menú principal, donde se selecciona la opcion a escoger 
def menu():
    
    print(""" 
| SISTEMA DE CREACIÓN DE REPORTES | 

Eliga una Opción
[1] Crear Producto
[2] Modificar Productos
[3] Consultar Producto
[4] Listar Productos
[5] Cargar Productos
[6] Salir""")

    opc = int(input())
    # Se escoge la funcion segun sea el caso
    match opc:
        case 1: # Llama a la funcion para crear un producto
            crear()
        case 2: # Llama a la funcion para modificar un producto
            # Evaluamos la longitud de la lista de productos para saber si ya hay
            if len(lista_productos) == 0:
                print("No hay productos que modificar")
                return menu()
            else:
                modificar()
        case 3: # Llama la funcion para consultar los productos
            consultar()
        case 4: # Llama la funcion para listar los productos
            listar()
        case 5: # Llama la funcion para la carga de datos del .csv
            cargarProductos()
        case 6: # Llama la funcion para cerrar el programa
            quit()
        case _:
            print("Elegir un valor de la lista")
            return menu()



def crear():
    """
    La aplicación deberá permitir la creación de productos con atributos como
    nombre, descripción, categoría, precio, imagen, SKU, cantidad, peso,
    dimensiones(alto y ancho en cm), fecha de creación y fecha de
    actualización.
    """
    print("""
| CREAR PRODUCTO | 
""")
    # Ingreso de los datos
    nombre = input("Nombre: ")
    descripcion = input("Descripcion: ")
    categoria = input("Categoria: ")
    # Creamos el ciclo de validacion y verificamos si es un flotante
    while True:
        try:
            precio = float(input("Precio: "))
            break
        except:
            print("No ha ingresado un numero")
    imagen = input("Imagen: ")
    sku = input("SKU: ")
    # Verificamos si la cantidad es un entero
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            break
        except:
            print("No ha ingresado una cantidad valida")
    # Verificamos si el peso es un flotante
    while True:
        try:
            peso = float(input("Peso: "))
            break
        except:
            print("No ha ingresado un peso valido")
    # Verificamos si el alto es un flotante
    while True:
        try:
            alto = float(input("Alto en Centimetros: "))
            break
        except:
            print("No ha ingresado una cantidad valida")
    # Verificamos si el largo es un flotante
    while True:
        try:
            largo = float(input("Largo en Centimetros: "))
            break
        except:
            print("No ha ingresado una cantidad valida")
    # Obtenemos la fecha del sistema
    fecha_creacion = datetime.now().strftime("%d/%m/%y")[:19]
    # Creacion del objeto tipo producto
    producto = Producto(nombre,descripcion,categoria,precio,imagen,sku,cantidad,peso,alto,largo,fecha_creacion,fecha_creacion)
    # Agregando el objeto a la lista
    lista_productos.append(producto)

    print("\nProducto Creado Satisfactoriamente")
    # Reingresamos al menu
    menu()

def modificar():
    print(""" 
| MODIFICAR PRODUCTO | 

Eliga un Producto a Modificar
""")
    n = 1
    for producto in lista_productos:
        print(f"[{n}] {producto.sku} ({producto.nombre})")
        n += 1
    try:
        opc_prod = int(input())
    except:
        print("Ingrese la opción de producto que desea modificar")
        modificar()
    print(""" 
Elige un Valor a Modificar
[1] Nombre
[2] Descripcion
[3] Categoria
[4] Precio
[5] Imagen
[6] SKU
[7] Cantidad
[8] Peso
[9] Dimensiones""")
    # Leemos la opcion seleccionada
    try:
        opc_val = int(input())
    except:
        print("Ingrese un valor válido")
        modificar()

    match opc_val:
        case 1:
            nom = input("\nIngresa el nuevo valor del nombre: ")
            if len(nom) == 0 or len(nom) == 1:
                print("ingrese un nombre válido")
                
            lista_productos[opc_prod-1].nombre = nom
        case 2:
            descrip = input("\nIngresa el nuevo valor de la descripción: ")
            if len(descrip) == 0 or len(descrip) < 10:
                print("ingrese una descripción válida o más larga")
                
            lista_productos[opc_prod-1].descripcion = descrip
        case 3:
            catego = input("\nIngresa el nuevo valor de categoría: ")
            if len(catego) == 0 or len(catego) == 1:
                print("ingrese una categoría válida o más larga")
                
            lista_productos[opc_prod-1].categoria = catego
        case 4:
            while True:
                try:
                    precio = float(input("\nIngresa el nuevo valor del precio: "))
                    if precio < 0:
                        print("El precio que colocó no es válido")
                        break

                    lista_productos[opc_prod-1].precio = precio
                    break
                    
                except:
                    print("Ingrese una cantidad valida")
                    
        case 5:
            img = input("\nIngresa el nuevo valor de la imagen ej: img.jpg : ")
            try:
                img3 = img.split(".")
                if img3[-1] != "png" and img3[-1] != "jpeg" and img3[-1] != "jpg" and img3[-1] != "gif" and img3[-1] != "svg":
                    print("el formato de la url no es válido")
                    
            except:
                print("La url no es válida") 
            lista_productos[opc_prod-1].imagen = img
        case 6:
            new_sku = input("\nIngresa el nuevo valor del sku: ")
            if len(new_sku) == 0 or len(new_sku) == 1:
                print("ingresa un código sku válido: ")
                
            lista_productos[opc_prod-1].sku = new_sku
        case 7:
            while True:
                try:
                    lista_productos[opc_prod-1].cantidad = int(input("\nIngresa el nuevo valor de la cantidad: "))
                    break
                except:
                    print("Ha ingresado un valor invalido")
        case 8:
            while True:
                try:
                    peso = float(input("\nIngresa el nuevo valor del peso: "))
                    if peso < 0:
                        print("El peso no puede ser negativo:")
                        break
                        
                    lista_productos[opc_prod-1].peso = peso
                    break
                except:
                    print("Ha ingresado un caracter invalido")
        case 9:
            while True:
                try:
                    lista_productos[opc_prod-1].dimensiones[0] = float(input("\nIngresa el nuevo valor para el alto en cm: "))
                    break
                except:
                    print("Ha ingresado un valor invalido")
            while True:
                try:
                    lista_productos[opc_prod-1].dimensiones[1] = float(input("\nIngresa el nuevo valor para el ancho en cm: "))
                    break
                except:
                    print("Ha ingresado un valor invalido")
        case _:
            print("Elige un Valor de Entre la Lista de Opciones")
            return modificar()

    #Se actualiza la fecha con la última modificación
    lista_productos[opc_prod-1].fecha_actualizacion = datetime.now().strftime("%d/%m/%y")[:19] 
    
    menu()

# Funcion para la carga del producto
def cargarProductos():
    # Abrimos el archivo en modo lectura
    archivo = open("registros.csv","r")
    # Hacemos lectura de las lineas por un ciclo for
    for lineas in archivo:
        # Creamos una lista de los atributos del producto en una variable auxiliar
        aux = lineas.split(",")
        # Creamos un nuevo producto y lo añadimos a la lista de productos con sus datos respectivos
        lista_productos.append(Producto(aux[0],aux[1],aux[2],aux[3],aux[4],aux[5],aux[6],aux[7],aux[8],aux[9],aux[10],aux[11])) 
    # Cerramos el archivo
    archivo.close()

    print("Prouctos de Prueba Cargados Correctamente")
    # Volvemos a llamar a la funcion de menu
    menu()

def consultar():
    print(""" 
| CONULTAR PRODUCTO |

Ingresar el SKU del Producto a Consultar: """ )

    consulta = input("")
    #creamos un ontador para verificar que el sku ingresado se encuentre dentro de la lista de productos
    cont = 0
    for producto in lista_productos:
        if producto.sku == consulta:
            producto.imprimir()
            return menu()
        elif producto.sku != consulta:
            cont += 1
            if cont == len(lista_productos):
                print("No Existe Ningun Producto con este SKU")
        
    
    menu()

def listar():
    print("""
 | OPCIONES DE ORDENAMIENTO PARA EL REPORTE | 

Elegir Opción
[1] Listar productos según su cantidad de forma ascendente utilizando el
algoritmo de quicksort
[2] Listar productos de forma descendente según su peso en un rango de
fecha de actualización introducido por el usuario, utilizando el
algoritmo de mergesort
[3] Listar productos de forma ascendente o descendente según su fecha
de creación utilizando el algoritmo de shellsort. La opción de
ordenamiento será seleccionada por el usuario
[4] Listar los productos de forma ascendente según su cantidad
utilizando el algoritmo de heapsort""")
    
    print("""
| LISTA DE PRODUCTOS | 
""")
    try:
        opc = int(input())
    except:
        print("Elige un entero válido")
        listar()
        return

    lista_ordenada=[]
    # Creamos la lista donde se guardara la informacion ordenada, lo haremos de forma iterada
    # Para no vincular las dos listas bajo diferentes nombres
    for producto in lista_productos:
        lista_ordenada.append(producto)
    
    match opc:
        case 1:
            # Ordenamos Descendentemente
            lista_ordenada = quicksort(0,len(lista_ordenada)-1,lista_ordenada)
            # Mostramos con el orden invertido para que sea ascendente
            for k in range(len(lista_ordenada)-1,-1,-1):
                lista_ordenada[k].imprimir()
        case 2:
           
            # Creamos las listas
            try:
                 # Pedimos las fechas
                fecha1 = input("Ingrese la fecha menor para el rango(dd/mm/yy): ")
                fecha2 = input("Ingrese la fecha mayor para el rango(dd/mm/yy): ")
                fecha1=fecha1.split("/")
                fecha2=fecha2.split("/")
                # Creamos los objetos tipo fechas
                fecha1 = datetime(int(fecha1[2]),int(fecha1[1]),int(fecha1[0]))
                fecha2 = datetime(int(fecha2[2]),int(fecha2[1]),int(fecha2[0]))
                # Creamos el contador
                k=0
                # Evaluamos según la fecha menor recorriendo la lista, lo hacemos por un while
                # para ir actualizando la longitud de la lista ordenada en el encabezado
                while k < len(lista_ordenada):
                    # Recuperamos la fecha de actualizacion y quitamos el salto de línea
                    aux = lista_ordenada[k].getFechaActualizacion().replace("\n","")
                    # Si la fecha de modificacion es diferente a 'Sin modificacion' evaluamos, sino eliminamos
                    if aux != "Sin Modificaciones":
                        # Creamos una lista de los valores
                        fechaActualizacion = aux.split("/")
                        # Creamos el objeto tipo datetime para hacer las comparaciones
                        fechaActualizacion = datetime(int(fechaActualizacion[2]),int(fechaActualizacion[1]),int(fechaActualizacion[0]))
                        diferenciaFMen = fechaActualizacion - fecha1
                        
                        # Evaluamos si la diferencia de fechas entre la ingresada menos la del producto es menor que 0 para eliminarlas
                        if diferenciaFMen.days < 0:
                            lista_ordenada.pop(k)                            
                        diferenciaFmay = fechaActualizacion - fecha2
                        # Si la diferencia es negativa significa que esta en el rango
                        if diferenciaFmay.days > 0:
                            lista_ordenada.pop(k)
                    else:
                        lista_ordenada.pop(k)
                    k+=1
                # Ordenamos de forma ascendente
                lista_ordenada = mergesort(lista_ordenada)
                # Mostramos con el orden invertido para que sea descendente
                for k in range(len(lista_ordenada)-1,-1,-1):
                    lista_ordenada[k].imprimir()
            except:
                print("El formato de la fecha no es válido")
        case 3:
            
            shellsort(lista_ordenada, len(lista_ordenada))

            opc = int(input("""Listar de Forma:
[1] Ascendete
[2] Descendente
"""))
            match opc:
                case 1:
                    for producto in lista_ordenada:
                        producto.imprimir()
                case 2:
                    lista_ordenada = lista_ordenada[::-1]
                    for producto in lista_ordenada:
                        producto.imprimir()
                case _:
                    print("Elige un Valor de Entre la Lista de Opciones")
                    listar()
                    return
                    

        case 4:
            # Ordenamos de forma ascendente
            heapsort(lista_ordenada)
            # Mostramos de forma ordenada
            for k in range(len(lista_ordenada)):
                lista_ordenada[k].imprimir()
        case _:
            print("Elige un Valor de Entre la Lista de Opciones")
            listar()
            return
        
    menu()

"""
Funciones de Ordenamiento
"""
# QuickSort
def partition(izquierda, derecha, arreglo):
    # El ultimo elemento debe ser el pivote y el puntero el primero
    pivot, ptr = arreglo[derecha], izquierda
    for i in range(izquierda, derecha):
        if arreglo[i].getCantidad() >= pivot.getCantidad():
            # Se envian los valores mas pequeños que el ´pivote hacia al frente
            arreglo[i], arreglo[ptr] = arreglo[ptr], arreglo[i]
            ptr += 1
    # Por ultimo remplazamos el ultimo elemento en la posicion del puntero
    arreglo[ptr], arreglo[derecha] = arreglo[derecha], arreglo[ptr]
    return ptr

def quicksort(izquierda, derecha, arreglo):
    if len(arreglo) == 1:  # Condicion de finalizacion
        return arreglo
    if izquierda < derecha:
        pi = partition(izquierda, derecha, arreglo)
        quicksort(izquierda, pi - 1, arreglo)  # Arreglo recursivo de la parte izquierda
        quicksort(pi + 1, derecha, arreglo)  # Arreglo recursivo de la parte
    return arreglo

# MergeSort
def mergesort(arreglo):
    """
        Lo primero que se ve en el psudocódigo es un if que
        comprueba la longitud de la lista. Si es menor que 2, 1 o 0, se devuelve la lista.
        ¿Por que? Ya esta ordenada. 
    """
    if len(arreglo) == 1:
        return arreglo
    
    middle = len(arreglo) // 2
    right = mergesort(arreglo[:middle])
    left = mergesort(arreglo[middle:])
    return merge(left, right)

def merge(izquierda, derecha):
    """
        Merge se encargara de intercalar los elementos de las dos
        divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado
 
   # Intercalar ordenadamente
    while(i < len(izquierda) and j < len(derecha)):
        if izquierda[i].getPeso() < derecha[j].getPeso():
            result.append(izquierda[i])
            i += 1
        else:
            result.append(derecha[j])
            j += 1
 
   # Agregamos los resultados a la lista
    result.extend(izquierda[i:])
    result.extend(derecha[j:])
 
    # Retornamos el resultados
    return result

# ShellSort
def shellsort(array, n):
    #A diferencia de otros algoritmos de ordenamiento este da saltos más largos en sus pivotes para ordenar el arreglo
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i].fecha_creacion
            j = i
            while j >= interval and array[j - interval].fecha_creacion > temp:
                array[j].fecha_creacion = array[j - interval].fecha_creacion
                j -= interval
        array[j].fecha_creacion = temp
        interval //= 2

# HeadSort
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    if l < n and arr[i].getCantidad() < arr[l].getCantidad():
        largest = l
    if r < n and arr[largest].getCantidad() < arr[r].getCantidad():
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    """Va ordenando el arreglo de manera de árbol binario con el nodo padre en la punta o en
    la gerarquía más alta y sus hijos se distribuyen ordenadamente como las hojas del árbol"""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Funcion de inicio del programa
def start():
    # Se crea una variable global para la lista de productos
    global lista_productos
    lista_productos = []

    #Iniciamos el menu
    menu()

# Llamamos a la funcion principal
start()
