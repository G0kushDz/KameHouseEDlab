op =  input("Selecciona la opcion con el numero \n1) Paréntesis balanceados \n2) Número decimal a binario \n3) Verificación de palíndromos\n>")

if op == "1":
    def verificar(cadena):
        pila = []
        for char in cadena:
            if char == "(":
                pila.append(char)
            elif char == ")":
                if not pila:
                    return False
                pila.pop()
        return len(pila) == 0

    cadena1 = "(((())))"
    cadena2 = "(((())"
    cadena3 = "(())"

    print("La cadena", cadena1, "esta balanceada?", verificar(cadena1))
    print("La cadena", cadena2, "esta balanceada?", verificar(cadena2))
    print("La cadena", cadena3, "esta balanceada?", verificar(cadena3))

elif op == "2":
    class Converter:
        def __init__(self):
            self.pila = []

        def decimal_binario(self, numero):
            binario = ""
            while numero > 0:
                residuo = numero % 2
                self.pila.append(residuo)
                numero //=2
            while self.pila:
                binario += str(self.pila.pop())

            return binario
    
    conv = Converter()
    numero_decimal = int(input("Ingresa un numero en decimal: "))
    print(f"El numero binario es: ", conv.decimal_binario(numero_decimal))

elif op == "3":
    def palindromo(palabra):
        pila = []

        palabra = palabra.lower().replace(" ", "")

        for letra in palabra:
            pila.append(letra)

        for letra in palabra:
            if letra != pila.pop():
                return False
            
        return True

    palabra = input("ingresa una palabra: ")

    if palindromo(palabra):
        print("Es un palindromo")
    else:
        print("No es un palindromo")

else:
    print("Opcion no valida. Intenta de nuevo.")