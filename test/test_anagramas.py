import pytest
import sys
import os
# Ajusta la ruta para que Python pueda encontrar anagramas.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from anagramas import es_anagrama

def test_anagramas_simples():
    assert es_anagrama("amor", "roma") == True

def test_anagramas_no_son_anagramas():
    assert es_anagrama("amor", "sol") == False

def test_anagramas_palabras_con_espacios():
    assert es_anagrama("a mor", "roma") == True

def test_anagramas_palabras_con_mayusculas():
    assert es_anagrama("AmOr", "RoMa") == True

def test_anagramas_palabras_vacias():
    assert es_anagrama("", "") == True

def test_anagramas_palabra_vacia_con_contenido():
    assert es_anagrama("", "hola") == False

def test_anagramas_palabras_con_caracteres_no_alfabeticos():
    assert es_anagrama("a1m2o3r", "r4o5m6a") == True

def test_anagramas_palabras_con_acentos():
    assert es_anagrama("ámor", "roma") == False  