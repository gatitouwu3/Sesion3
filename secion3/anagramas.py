def es_anagrama(palabra1, palabra2):
    # Eliminar espacios y convertir todo a minúsculas
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    
    # Comparar las letras ordenadas alfabéticamente
    return sorted(palabra1) == sorted(palabra2)

def main():
    # Pedir al usuario las palabras
    palabra1 = input("Ingresa la primera palabra: ")
    palabra2 = input("Ingresa la segunda palabra: ")

    # Verificar si son anagramas
    if es_anagrama(palabra1, palabra2):
        print(f"'{palabra1}' y '{palabra2}' son anagramas.")
    else:
        print(f"'{palabra1}' y '{palabra2}' no son anagramas.")

if __name__ == "__main__":
    main()