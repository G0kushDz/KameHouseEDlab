##REQUERIMIENTOS PARA UN PROGRAMA SOBRE GESTION DE PRODUCTOS
#Agregar productos (se solicitara el identificador y nombre del producto)
#Actualizar el nombre de un producto (se agrega identificador a modificar y nombre del nuevo producto)
#Eliminar producto (Se agrega el identificador para eliminar el producto)
#Consultar la informacion de un producto (se solicitara identificador y se imprimira si existe el producto)

producto = {}

while True:
    print("\n°°°MENU°°°")
    print("(1) Agrega un producto")
    print("(2) Actualiza el nombre de un producto")
    print("(3) Elimina un producto")
    print("(4) Consulta la informacion de un producto")
    print("(5) Salir")

    opcion = input("Elige una opcion: ")

    #Agregar productos (se solicitara el identificador y nombre del producto)
    if opcion == "1":
        clave = input("Ingresa un identificador para el producto: ")
        nombre = input("Ingresa un nombre para el producto: ")
        if clave in producto:
            print("El identificador ya existe. Intenta con otro.")
        else:
            producto[clave] = nombre
            print(f"Producto '{nombre}' con clave '{clave}' se a agrgado con exito!.")
        

    #Actualizar el nombre de un producto (se agrega identificador a modificar y nombre del nuevo producto)
    elif opcion == "2":
        clave = input("Ingresa el identificador del producto que desea modificar: ")
        if clave in producto:
            nombre = input(f"Nuevo nombre para el producto {clave}: ")
            producto[clave] = nombre
            print("El producto a sido actualizado con exito!.")
        else:
            print("El identificador aun no existe en el diciionario.")

    #Eliminar producto (Se agrega el identificador para eliminar el producto)
    elif opcion == "3":
        clave = input("Ingresa el identificador del producto a eliminar: ")
        if clave in producto:
            nombre_eliminado = producto.pop(clave)
            print(f"Producto '{nombre_eliminado}' con clave '{clave}' ha sido eliminado.")
        else:
            print("El identificador no existe. No se puede eliminar.")
        
    #Consultar la informacion de un producto (se solicitara identificador y se imprimira si existe el producto)
    elif opcion == "4":
        clave = input("Ingresa el identificador del producto a consultar: ")
        if clave in producto:
            print(f"Producto encontrado: {clave} : {producto[clave]}")
        else:
            print("El producto no existe en el diccionario.")

    elif opcion == "5":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion no valida. Intenta de nuevo.")

