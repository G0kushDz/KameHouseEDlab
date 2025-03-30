numeros = []
print("Ingresa un numero (Ingresa 0 para finalizar)")
while True:
    numero=int(input(f"Numero: "))
    if numero==0:
        break
    numeros.append(numero)

eliminar=int(input("Ingresa un numero que desees eliminar: "))
if eliminar in numeros:
    numeros.remove(eliminar)
    print(f"Se elimino el numero {eliminar} con exito.")
else:
    print(f"{eliminar} no se encuentra en la lista.")

suma=0
for n in numeros:
    suma += n
print(f"{suma} es la suma de los numeros en la lista.")

punta=int(input(f"Ingresa un numero, te mostrare los elemento menores a este en la lista: "))
numerosMenores=[]
for n in numeros:
    if n < punta:
        numerosMenores.append(n)
print(f"Esos son los numeros menores a {punta}.")
for n in numerosMenores:
    print(n)