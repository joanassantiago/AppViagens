#Grupo: P12G01
import requests

#serve para verifcar se a atração que a pessoa deseja esta contida na lista de categorias que foi dada pelos professores
def obterAtrações():
    atraçõesExistentes = []
    with open("categories.txt", "r") as atrações:
        for linhas in atrações.readlines():
            atraçõesExistentes.append(linhas)
        atraçõesExistentes = [elemento.replace("\n", "") for elemento in atraçõesExistentes]
    return atraçõesExistentes
#função que devolve apenas as categorias principais
def mainCategories():
    mainCategories = []
    for x in obterAtrações():
        if "." not in x:
            mainCategories.append(x)
    return mainCategories

#função que devolve apenas as categorias secundárias de uma categoria principal
# def subCategories(cat):
#     subCategories = []
#     for x in obterAtrações():
#         if cat in x:
#             subCategories.append(x)
#     return subCategories

def printList(lista):
    for x in lista:
        print(x)

def main():
    '''
    latitude = float(input("Localização (latitude): "))
    longitude = float(input("Localização (longitude): "))
    raio = float(input("Distância que pode viajar (km): "))
    '''
    
    print("Categorias disponíveis: \n")
    printList(mainCategories())
    while True:
        cat = str(input("Escolha as categorias que deseja:"))
        if cat not in mainCategories():
            print("Escolha categorias válidas!")
            continue
        else:
            break
    
    # while True:
    #     choice = str(input("Deseja escolher uma subcategoria? (y/n)"))
    #     if choice != "y" and choice != "n":
    #         print("ERRO: Insere (y/n)!")
    #     else:
    #         break
    # if choice == "y":
    #     print("Subcategorias disponíveis: \n")
    #     printList(subCategories(cat))

    #Forum aveiro (testes)
    latitude = 40.641193
    longitude = -8.651418
    raio = 0.01
    cat = "commercial"

    #Criação do Url para o geoapify
    url = "https://api.geoapify.com/v2/places?"
    url += "categories=" + cat + "&filter=circle:" + str(longitude) + "," + str(latitude) + "," + str(raio) + "&bias=proximity:" + str(longitude) + "," + str(latitude) 
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

if "_main_" == "_main_":
    main()