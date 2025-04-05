def verificar_capicua_palindromo(entrada):
    entrada = str(entrada).lower()
    entrada_sin_espacios = entrada.replace(" ", "")
    
    if entrada_sin_espacios.isnumeric():
        if entrada_sin_espacios == entrada_sin_espacios[::-1]:
            return f"{entrada} es un **número capicúa**"
        else:
            return f"{entrada} no es un número capicúa"
    else:
        if entrada_sin_espacios == entrada_sin_espacios[::-1]:
            return f'"{entrada}" es un **palíndromo**'
        else:
            return f'"{entrada}" no es un palíndromo'

def main():
    while True:
        entrada = input("\nIngresa un texto o número (o 'salir' para terminar): ")
        if entrada.lower() == "salir":
            break
        print(verificar_capicua_palindromo(entrada))

if __name__ == "__main__":
    main()