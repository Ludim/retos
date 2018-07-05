#!/usr/bin/python3.6
from sys import argv

"""Programar un algoritmo que detecte si, dentro de una cadena de caracteres, 
   los parentesis, corchetes y llaves se encuentran balanceados, esto es:
     - Todo parentesis, corchete o llave deben ser pares, es decir, 
     por cada simbolo de apertura debe existir su par de clausura. 
     - Usar solamente la entrada y salida estandar, esto es:

Ejemplo de entrada	   Salida esperada
(){}[]	   		   True
{[()]}			   True
([)])			   False
{{[[(())]]}}		   True
{({))})]		   False
[[()			   False
"""
def es_entrada_balanceada(entrada: str) -> bool:
    return False

entrada = argv[1]
print(es_entrada_balanceada(entrada))
