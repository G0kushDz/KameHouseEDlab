class Nodo:
    def __init__(self,valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def insertar(raiz, valor):
    if raiz is None:
        return Nodo(valor)
    
    if valor < raiz.valor:
        raiz.izquierdo = insertar(raiz.izquierdo, valor)

    if valor > raiz.valor:
        raiz.derecho = insertar(raiz.derecho, valor)

    return raiz

def mostrar_arbol(raiz, espacio=0):
    if raiz is None:
        return 
    espacio +=10

    mostrar_arbol(raiz.derecho, espacio)
    print("  " * espacio, raiz.valor)
    mostrar_arbol(raiz.izquierdo, espacio)

def busqueda(raiz, valor):
    nivel = 0
    padre = None
    actual = raiz
    lado = None

    while actual:
        if valor == actual.valor:
            print(f"\nNodo: {valor}")
            print(f"Nivel: {nivel}")

            if padre:
                print(f"Padre: {padre.valor}")
                if lado == 'izquierdo' and padre.derecho:
                    print(f"Hermano: {padre.derecho.valor}")
                elif lado == 'derecho' and padre.izquierdo:
                    print(f"Hermano: {padre.izquierdo.valor}")
                else:
                    print("Hermano: No hay")

            print(f"Hijo izquierdo: {actual.izquierdo.valor if actual.izquierdo else 'No hay'}")
            print(f"Hijo derecho: {actual.derecho.valor if actual.derecho else 'No hay'}")
            return

        padre = actual
        if valor < actual.valor:
            actual = actual.izquierdo
            lado = 'izquierdo'
        else:
            actual = actual.derecho
            lado = 'derecho'
        nivel += 1



datos = [8,3,10,1,6,14,4,7,13]

raiz = None
for dato in datos:
    raiz = insertar(raiz,dato)

print("°°° A R B O L   B I N A R I O °°°")
mostrar_arbol(raiz)

print("°°° B U S Q U E D A °°°")
busqueda(raiz,6)
busqueda(raiz,13)
busqueda(raiz,7)
