alumnosPrimaria=[]
alumnosSecundaria=[]

print()
print("Agrega Alumnos de nivel Primaria")
while True:
    alumnoP=(input("Alumno: "))
    if alumnoP=="x":
        break
    alumnosPrimaria.append(alumnoP.upper())

print()
print("Agrega Alumnos de nivel Secundaria")
while True:
    alumnoS=(input("Alumno: "))
    if alumnoS=="x":
        break
    alumnosSecundaria.append(alumnoS.upper())

#Informar los nombres de todos los alumnos de nivel primaria
#  y los de nivel secundaria, sin repeticiones.
print()
print("Nombres de todos los alumnos (sin repeticiones)")
totalAlumnos= alumnosPrimaria + alumnosSecundaria
alumnosUnicos= set(totalAlumnos)
for n in alumnosUnicos:
    print(f"-{n}") 


#Informar qué nombres se repiten entre los alumnos de nivel 
# primaria y secundaria.
alumnosRepetidos=[]
for i in totalAlumnos:
    cont=0
    for j in totalAlumnos:
        if i ==j:
            cont+=1
        if cont > 1:
            alumnosRepetidos.append(i)

print()
print("Nombres que se repiten")
nombresRepetidos= set(alumnosRepetidos)
for n in nombresRepetidos:
    print(f"-{n}")


#Informar qué nombres de nivel primaria no se repiten 
# en los de nivel secundaria.
alumnosP=set(alumnosPrimaria)
alumnosS=set(alumnosSecundaria)
alumnosPLista=[]
alumnosR=[]
for i in alumnosP:
    alumnosPLista.append(i)
for i in alumnosP:
    for j in alumnosS:
        if i==j:
            alumnosR.append(i)
for i in alumnosR:
    if i in alumnosPLista:
        alumnosPLista.remove(i)

print()
print("Nombres de nivel primaria que no se repiten")
for i in alumnosPLista:
    print(f"-{i}")




