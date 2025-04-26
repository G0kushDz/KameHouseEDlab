productos = [{
    'clave' : 'P01',
    'descripcion' : 'Laptop Dell F15',
    'existencia' : 25,
    'minimo' : 5,
    'precio' : 12500.00
},
{
    'clave' : 'P02',
    'descripcion' : 'Mouse',
    'existencia' : 50,
    'minimo' : 5,
    'precio' : 500.00
},
{
    'clave' : 'P03',
    'descripcion' : 'Teclado',
    'existencia' : 50,
    'minimo' : 5,
    'precio' : 700.00
}
]

def buscar_producto(clave):
    for producto in productos:
        if producto['clave'] == clave:
            return producto
    return None

def vender_producto():
    clave = input("Ingrese la clave del producto: ")
    producto = buscar_producto(clave)

    if producto:
        try: 
            cantidad_venta = int(input("Ingrese la cantidad vendida: "))
            if cantidad_venta <= 0:
                print("La cantidad debe ser positiva")
                return
            
            nueva_existencia_v = producto['existencia'] - cantidad_venta
            if nueva_existencia_v < 0:
                print("No hay suficiente existencia para la venta")
            elif nueva_existencia_v < producto['minimo']:
                producto['existencia'] = nueva_existencia_v
                print(f"Venta realizada, Advertencia: existencia baja ({nueva_existencia_v})")
            else:
                producto['existencia'] = nueva_existencia_v
                print(f"Venta realizada con exito. Nueva existencia ({nueva_existencia_v})")
        except ValueError:
            print("La cantidad debe ser un numero entero")
    else:
        print("Producto no encontrado")

def comprar_producto():
    clave = input("Ingrese la clave del producto: ")
    producto = buscar_producto(clave)

    if producto:
        try:
            cantidad_compra = int(input("Ingrese la cantidad comprada: "))
            if cantidad_compra <= 0:
                print("La cantidad debe ser positiva")
                return
            
            nueva_existencia_c = producto['existencia'] + cantidad_compra
            producto['existencia'] = nueva_existencia_c
            print(f"Compra realizada con exito. Nueva existencia ({nueva_existencia_c})")
        except ValueError:
            print("La cantidad debe ser un numero entero")
    else:
        print("Producto no encontrado")

def actualizar_precio():
    clave = input("Ingrese la clave del producto: ")
    producto = buscar_producto(clave)

    if producto:
        try:
            porcentaje = int(input("Ingresa el porcentaje(numero entero 1-100) que se le aumentara al precio: "))
            if porcentaje <= 0 or porcentaje > 100:
                print("El porcentaje debe estar entre 1 y 100")
                return
            nuevo_precio = producto['precio'] * (1 + porcentaje / 100)
            producto['precio'] = nuevo_precio
            print(f"El precio se modifico con exito. Nuevo precio ({nuevo_precio})")
        except ValueError:
            print("El porcentaje debe ser un numero entero")
    else:
        print("Producto no encontrado")

def mostrar_informacion():
    clave = input("Ingrese la clave del producto: ")
    producto = buscar_producto(clave)

    if producto:
        print(f"Clave: {producto['clave']}")
        print(f"Descripcion: {producto['descripcion']}")
        print(f"Existencia: {producto['existencia']}")
        print(f"Precio: {producto['precio']}")
    else:
        print("Producto no encontrado")

def agregar_producto():
    clave = input("Ingresa la clave del producto: ")
    if buscar_producto(clave):
        print("Ya existe un producto con esta clave")
        return
    descripcion = input("Ingresa la descripcion del producto: ")
    
    try:
        existencia = int(input("Ingresa la existencia inicial del producto: "))
        minimo = int(input("Ingresa la existencia minima del prodcuto: "))
        precio = float(input("Ingresa el precio del producto: "))

        if existencia < 0 or minimo < 0 or precio <=0:
            print("Error: los valores deben ser positivos")
            return
        
        nuevo_producto = {
            'clave' : clave,
            'descripcion' : descripcion,
            'existencia' : existencia,
            'minimo' : minimo,
            'precio' : precio
        }

        productos.append(nuevo_producto)
        print(f"Producto {descripcion} agregado exitosamente!")
    except ValueError:
        print("Error en algun valor, intentalo de nuevo")
    


def menu():
    while True:
        print("°°°MENU PRINCIPAL°°°")
        print("(1) Vender Producto")
        print("(2) Comprar Producto")
        print("(3) Actualizar Precio")
        print("(4) Mostrar Articulo")
        print("(5) Agregar Nuevo Producto")
        print("(0) Salir")

        opcion = input("Seleccione una opcion: ")
        if opcion == '1':
            vender_producto()
        elif opcion == '2':
            comprar_producto()
        elif opcion == '3':
            actualizar_precio()
        elif opcion == '4':
            mostrar_informacion()
        elif opcion == '5':
            agregar_producto()
        elif opcion == '0' :
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()