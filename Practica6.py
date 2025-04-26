import numpy as np

ventas_np = np.array([
    [100,300,120],
    [400,200,200],
    [350,250,210],
    [280,300,200],
    [300,320,300],
    [250,300,350],
    [200,280,300],
    [180,300,400],
    [350,420,360],
    [694,500,800],
    [600,550,531],
    [500,400,300]
])

meses_np = [
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
    "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
]

departamentos=["Dulces", "Conservas", "Bebidas"]


cont=0
filas=12
mesMaxProdDulces=0
produccionMasAlta=0
for i in range (filas):
    if ventas_np[cont,0] > produccionMasAlta:
        produccionMasAlta = ventas_np[cont,0]
        mesMaxProdDulces = cont
    cont+=1
print(f"El mes con mayor produccion de dulces fue {meses_np[mesMaxProdDulces]} produciendo un total de {produccionMasAlta} dulces.")


sumaProdBebidas=0
cont=0
for i in range (filas):
    sumaProdBebidas+= ventas_np[cont,2]
    cont+=1
promedioProdBebidas= sumaProdBebidas/12
print(f"El promedio de produccion de bebidas al año es de {promedioProdBebidas}.")


cont=0
mesMaxProdBebidas=0
produccionMasAlta=0
mesMinProdBebidas=0
produccionMasBaja=10000
for i in range (filas):
    if ventas_np[cont,2] > produccionMasAlta:
        produccionMasAlta = ventas_np[cont,2]
        mesMaxProdBebidas = cont

    if ventas_np[cont,2] < produccionMasBaja:
        produccionMasBaja = ventas_np[cont,2]
        mesMinProdBebidas = cont
    cont+=1
print(f"El mes con mayor produccion de bebidas fue {meses_np[mesMaxProdBebidas]} produciendo un total de {produccionMasAlta} bebidas.")
print(f"El mes con menor produccion de bebidas fue {meses_np[mesMinProdBebidas]} produciendo un total de {produccionMasBaja} bebidas.")

cont=0
columnas=3
rubroMinCostProd=0
minCostProd=10000
for i in range (columnas):
    if ventas_np[11,cont] < minCostProd:
        minCostProd = ventas_np[11,cont]
        rubroMinCostProd = cont
    cont+=1
print(f"El rubro con el menor costo de produccion en Diciembre fue {departamentos[rubroMinCostProd]}, con un total de {minCostProd} de produccion.")
