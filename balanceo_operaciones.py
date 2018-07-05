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
{{[[(())]]}}	   True
{({))})]		   False
[[()			   False
"""
CERRADO = ['}', ')', ']']
CERRADO_ABIERTO = {'}':'{', ')':'(', ']':'['}

def es_entrada_balanceada(entrada: str) -> bool:
    # entrada impar
    if len(entrada) & 1:
        return False
    pila = []
    for i in entrada:
        if i in CERRADO and pila and (CERRADO_ABIERTO.get(i) != pila.pop()):
            return False
        else:
            continue
        pila.append(i)
    return True

if __name__ == '__main__':
    entrada = str(argv[1])
    print(es_entrada_balanceada(entrada))

