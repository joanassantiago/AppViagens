#Grupo: P12G01

import requests


#serve para verifcar se a atração que a pessoa deseja esta contida na lista de categorias que foi dada pelos professores
def obter_atrações():
    atrações_existentes = []
    with open("categories.txt", "r") as atrações:
        for linhas in atrações.readlines():
            atrações_existentes.append(linhas.strip())

with open("API_key.txt") as file:
    api_key = file.read()
api_key = api_key.strip()

def main():

    localização = float(input("Localização (latitude, longitude): "))
    raio = float(input("Distância que pode viajar (km): "))
    atração = str(input("Tipo de atração que deseja: "))