pacientes = [{
    'nombre' : 'Juan Luis',
    'edad' : 11,
    'sexo' : 'M',
    'domicilio' : 'Cuahutemoc #25, Zacatecas',
    'telefono' : 4924920506,
    'seguro' : 'FALSO'
},
{
    'nombre' : 'Valeria Rosalinda',
    'edad' : 23,
    'sexo' : 'F',
    'domicilio' : 'Altamira #240, Zacatecas',
    'telefono' : 4925542105,
    'seguro' : 'VERDADERO'
},
{
    'nombre' : 'Maria Guadalupe',
    'edad' : 27,
    'sexo' : 'F',
    'domicilio' : 'Condesa #122, Aguascalientes',
    'telefono' : 4928274756,
    'seguro' : 'VERDADERO'
},
{
    'nombre' : 'Roberto Carlos',
    'edad' : 40,
    'sexo' : 'M',
    'domicilio' : 'Orquideas #380, Zacatecas',
    'telefono' : 4921220304,
    'seguro' : 'VERDADERO'
}
]

def buscar_paciente(nombre):
    for paciente in pacientes:
        if paciente['nombre'] == nombre:
            return paciente 
    return None

def listar_nombres():
    for paciente in pacientes:
        print(paciente['nombre'])

def porcentaje_edad():
    total_niños=0
    total_jovenes=0
    total_adultos=0

    for paciente in pacientes:
        if paciente['edad'] <= 13:
            total_niños +=1
        if paciente['edad'] > 13 and paciente['edad'] <= 30:
            total_jovenes +=1
        if paciente['edad'] > 30:
            total_adultos +=1
    total_pacientes = total_niños + total_jovenes + total_adultos
    porcentaje_niños = (100/total_pacientes) * total_niños
    porcentaje_jovenes = (100/total_pacientes) * total_jovenes
    porcentaje_adultos = (100/total_pacientes) * total_adultos
    print(f"Niños:   {porcentaje_niños}%")
    print(f"Jovenes: {porcentaje_jovenes}%")
    print(f"Adultos: {porcentaje_adultos}%")

def porcentaje_sexo():
    total_masculinos=0
    total_femeninos=0

    for paciente in pacientes:
        if paciente['sexo'] == 'M':
            total_masculinos +=1
        if paciente['sexo'] == 'F':
            total_femeninos +=1
    total_pacientes = total_masculinos + total_femeninos
    porcentaje_masculinos = (100/total_pacientes) * total_masculinos
    porcentaje_femeninos = (100/total_pacientes) * total_femeninos
    print(f"Hombres:   {porcentaje_masculinos}%")
    print(f"Mujeres:   {porcentaje_femeninos}%")

def mostrar_paciente():
    nombre = input("Ingresa el nombre del paciente: ")
    paciente = buscar_paciente(nombre)

    if paciente:
        print(f"Nombre: {paciente['nombre']}")
        print(f"Edad: {paciente['edad']}")
        print(f"Sexo: {paciente['sexo']}")
        print(f"Domicilio: {paciente['domicilio']}")
        print(f"Telefono: {paciente['telefono']}")
        print(f"Seguro: {paciente['seguro']}")
    else:
        print("Paciente no encontrado")

def pacientes_con_seguro():
    con_seguro=0
    sin_seguro=0

    for paciente in pacientes:
        if paciente['seguro'] == 'VERDADERO':
            con_seguro +=1
        if paciente['seguro'] == 'FALSO':
            sin_seguro +=1
    total_pacientes = con_seguro + sin_seguro
    porcentaje_con_seguro = (100/total_pacientes) * con_seguro
    print(f"El {porcentaje_con_seguro}% de pacientes poseen seguro")

        


def menu():
    while True:
        print("°°°MENU PRINCIPAL°°°")
        print("(1) Lista de nombres de los pacientes")
        print("(2) Porcentaje de pacientes -Niños -Jovenes -Adultos")
        print("(3) Porcentaje de pacientes -Hombres -Mujeres")
        print("(4) Mostrar paciente")
        print("(5) Porcentaje de pacientes que poseen seguro")
        print("(0) Salir")

        opcion = input("Selecciona una opcion: ")
        if opcion == '1':
            listar_nombres()
        elif opcion == '2':
            porcentaje_edad()
        elif opcion == '3':
            porcentaje_sexo()
        elif opcion == '4':
            mostrar_paciente()
        elif opcion == '5':
            pacientes_con_seguro()
        elif opcion == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opcion invalida")

if __name__ == "__main__":
    menu()


