personas = []
maximo= int(input("Ingrese el numero de personas a registar: "))

for i in range (maximo):
    nombre = input(f"Nombre de la persona {i+1}: " )
    identificacion = input(f"Identificacion para {nombre}: ")

    personas.append ([nombre, identificacion])

print("°PERSONAS REGISTRADAS°")
for i, persona in enumerate(personas, start=1):
    print(f"Persona {i}: Nombre: {persona[0]}, Identificacion: {persona[1]}")