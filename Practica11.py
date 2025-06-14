class Nodo:
    def __init__(self, pregunta, respuestas):
        self.pregunta = pregunta
        self.respuestas = respuestas

nodo_raiz = Nodo("¿Cómo está el clima? (selecciona la opción con el número)\n1) Soleado\n2) Nublado\n3) Lluvioso", {
    "1": Nodo("¿Humedad?\n1) Alta\n2) Normal", {
        "1": "No se puede jugar",
        "2": "Sí se puede jugar"
    }),
    "2": "Sí se puede jugar",
    "3": Nodo("¿Viento?\n1) Fuerte\n2) Suave", {
        "1": "No se puede jugar",
        "2": "Sí se puede jugar"
    })
})

def evaluar_clima(nodo_actual):
    respuesta = input(nodo_actual.pregunta + "\n> ")

    siguiente_nodo = nodo_actual.respuestas.get(respuesta)

    if siguiente_nodo is None:
        print("Respuesta no válida. Intenta nuevamente.\n")
        return evaluar_clima(nodo_actual)
    
    if isinstance(siguiente_nodo, Nodo):
        return evaluar_clima(siguiente_nodo)
    else:
        return siguiente_nodo

resultado = evaluar_clima(nodo_raiz)
print(f"\nResultado: {resultado}")
