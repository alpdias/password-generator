import random

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letrasMin = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'w', 'y', 'z']
letrasMax = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'W', 'Y', 'Z']
simbolos = ['!', '@', '#', '$', '%', '&', '*']

lista = []

lista.append(numeros + letrasMin + letrasMax + simbolos)

senha = ''

for i in range(8):
    senha += random.choice(lista[0])

print(senha)
