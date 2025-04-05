import pytest
from unittest.mock import patch
from io import StringIO
from palindromo import verificar_capicua_palindromo, main  

# Casos de números capicúas
@pytest.mark.parametrize("entrada, resultado", [
    ("121", "121 es un **número capicúa**"),
    ("123", "123 no es un número capicúa"),
    ("12321", "12321 es un **número capicúa**"),
    ("0", "0 es un **número capicúa**"),
    ("123321", "123321 es un **número capicúa**"),
    ("123 321", "123 321 es un **número capicúa**"),
    ("123a21", "123a21 no es un número capicúa"),
    ("123.321", "123.321 no es un número capicúa"),
])
def test_capicua_numeros(entrada, resultado):
    assert verificar_capicua_palindromo(entrada) == resultado

# Casos de palíndromos (texto)
@pytest.mark.parametrize("entrada, resultado", [
    ("Madam", '"Madam" es un **palíndromo**'),
    ("Hola", '"Hola" no es un palíndromo'),
    ("A man a plan", '"A man a plan" es un **palíndromo**'),
    ("Able was I ere I saw Elba", '"Able was I ere I saw Elba" es un **palíndromo**'),
    ("¡Hola mundo!", '"¡Hola mundo!" no es un palíndromo'),
    ("A", '"A" es un **palíndromo**'),
    ("¡¡¡", '"¡¡¡" no es un palíndromo'),
])
def test_palindromos_texto(entrada, resultado):
    assert verificar_capicua_palindromo(entrada) == resultado

# Test de salida del programa
def test_salir_programa():
    with patch('sys.stdout', new=StringIO()) as fake_stdout:
        with patch('builtins.input', return_value='salir'):
            main()
            assert fake_stdout.getvalue() == "\nIngresa un texto o número (o 'salir' para terminar): \n"

# Test de entrada inválida
@pytest.mark.parametrize("entrada, resultado", [
    ("123a21", "123a21 no es un número capicúa"),
    ("123.321", "123.321 no es un número capicúa"),
    ("¡Hola!", '"¡Hola!" no es un palíndromo'),
])
def test_entradas_invalidas(entrada, resultado):
    assert verificar_capicua_palindromo(entrada) == resultado