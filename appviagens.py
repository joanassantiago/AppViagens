#Grupo: P12G01

import requests


#serve para verifcar se a atração que a pessoa deseja esta contida na lista de categorias que foi dada pelos professores
# def obterAtrações():
#     atraçõesExistentes = []
#     with open("categories.txt", "r") as atrações:
#         for linhas in atrações.readlines():
#             atraçõesExistentes.append(linhas)
            


category = input()
lat = input()
lon = input()
radius = input()

url = "https://api.geoapify.com/v2/places?"

url += "categories=" + category + "&filter=circle:" + str(lon) + "," + str(lat) + "," + str(radius) + "&bias=proximity:" + str(lon) + "," + str(lat) 

url += "&apiKey=" + "34e316823d0044c4b9725dcd1af10809"

response = requests.get(url)
print(response.status_code)

#trocar variavel
a = response.json()
print (a)
print (a["type"])
# with open("API_key.txt") as file:
#     api_key = file.read()
# api_key = api_key.strip()

# def main():

#     latitude = float(input("Localização (latitude): "))
#     longitude = float(input("Localização (longitude): "))
#     raio = float(input("Distância que pode viajar (km): "))
#     atração = str(input("Tipo de atração que deseja: "))