pasajeros = [
    ("Manuel Juarez", 19823451, "Liverpool"),
    ("Silvana Paredes", 22709128, "Buenos Aires"),
    ("Rosa Ortiz", 15123978, "Glasgow"),
    ("Luciana Hernandez", 38981374, "Lisboa")
]

ciudades = [
    ("Buenos Aires", "Argentina"),
    ("Glasgow", "Escocia"),
    ("Lisboa", "Portugal"),
    ("Liverpool", "Inglaterra"),
    ("Madrid", "España")
]

def consultarCiudadXDni(dni):
    for nombre, doc, ciudad in pasajeros:
        if doc == dni:
            return ciudad
    return None

def consultarPaisXCiudad(ciudad):
    for ciudad_nombre, pais in ciudades:
        if ciudad_nombre.lower() == ciudad.lower():
            return pais
    return None

def sumaPasajerosACiudad(ciudad):
    return sum(1 for _, _, destino in pasajeros if destino.lower() == ciudad.lower())


def sumaPasajerosAPais(pais_buscado):
    contador = 0
    for _, _, ciudad in pasajeros:
        pais = consultarPaisXCiudad(ciudad)
        if pais and pais.lower() == pais_buscado.lower():
            contador += 1
    return contador

def main():
    while True:
        print("\n°°° MENU °°° (selecciona la opcion con el numero)")
        print("1) Agregar pasajero")
        print("2) Agregar ciudad")
        print("3) Ver ciudad de destino por DNI")
        print("4) Ver cantidad de pasajeros a una ciudad")
        print("5) Ver país de destino por DNI")
        print("6) Ver cantidad de pasajeros a un país")
        print("7) Salir")

        opcion = input("> ")

        if opcion == "1":
            nombre = input("Nombre del pasajero: ")
            try:
                dni = int(input("DNI del pasajero: "))
            except ValueError:
                print("DNI inválido.")
                continue
            destino = input("Ciudad de destino: ")
            pasajeros.append((nombre, dni, destino))
            print("Pasajero agregado correctamente.")

        elif opcion == "2":
            ciudad = input("Nombre de la ciudad: ")
            pais = input("País al que pertenece la ciudad: ")
            ciudades.append((ciudad, pais))
            print("Ciudad agregada correctamente.")

        elif opcion == "3":
            try:
                dni = int(input("Ingresa el DNI del pasajero: "))
            except ValueError:
                print("DNI inválido.")
                continue
            ciudad = consultarCiudadXDni(dni)
            if ciudad:
                print(f"El pasajero viaja a {ciudad}.")
            else:
                print("Pasajero no encontrado.")

        elif opcion == "4":
            ciudad = input("Ingresa el nombre de la ciudad: ")
            cantidad = sumaPasajerosACiudad(ciudad)
            print(f"{cantidad} pasajero(s) viaja(n) a {ciudad}.")

        elif opcion == "5":
            try:
                dni = int(input("Ingresa el DNI del pasajero: "))
            except ValueError:
                print("DNI inválido.")
                continue
            ciudad = consultarCiudadXDni(dni)
            if ciudad:
                pais = consultarPaisXCiudad(ciudad)
                if pais:
                    print(f"El pasajero viaja a {pais}.")
                else:
                    print("País no encontrado para la ciudad.")
            else:
                print("Pasajero no encontrado.")

        elif opcion == "6":
            pais = input("Ingresa el nombre del país: ")
            cantidad = sumaPasajerosAPais(pais)
            print(f"{cantidad} pasajero(s) viaja(n) a {pais}.")

        elif opcion == "7":
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida. Intenta nuevamente.")

main()
