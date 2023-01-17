# -*- coding: utf-8 -*-

'''
Created in 11/2020
@Author: Paulo https://github.com/alpdias
'''

# imported libraries
import random

def generator(tamanho):
    
    """
    -> Simple password generator\
    \n:param tamanho: Password length\
    \n:return: Password\
    """
    
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # list of numbers
    letrasMin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z'] # lowercase list
    letrasMax = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z'] # list of capital letters
    simbolos = ['!', '@', '#', '$', '%', '&', '*'] # symbol list

    lista = []

    lista.append(numeros + letrasMin + letrasMax + simbolos) # unique list for all characters

    senha = ''

    for i in range(tamanho):
        senha += random.choice(lista[0]) # choice of characters

    return senha


print(generator(25)) # generated password
