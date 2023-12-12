#Grupo: P12G01
import requests

#   To do:
#   fazer a lista das categorias mais bonita e fazer uma tabela para o output
#   o utilizador tem de poder meter vários tipos de atração
#   outras informações que possamos vir a considerar importantes 
#   distancia media, ordenação por distância maior ou menor, mostrar os mais perto e mais longe, (mais ideias)
#   verificar se o que a pessoa esta certo, tipo se as coordenadas que inseriu são um numero
#





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

# função que devolve apenas as categorias secundárias de uma categoria principal
# def subCategories(cat):
#     subCategories = []
#     for x in obterAtrações():
#         if cat in x:
#             subCategories.append(x)
#     return subCategories

def printList(lista):
    for x in lista:
        print(x)

def print_cleanWebResponse(webResponse):
    
    locations_found = 0
    clean_webResponse = webResponse["features"]
    
    for feature in clean_webResponse:
        if "name" in feature["properties"]:
            # O adress já inclui o nome, rua , cidade, país e código postal
            adress = feature["properties"]["formatted"]
            lat = feature["properties"]["lat"]
            lon = feature["properties"]["lon"]
            if "distance" in feature["properties"]:
                distance = feature["properties"]["distance"]
            else:
                distance = "0"
            print (adress,"|", lat,",",lon ,"|", distance,("m"))
            locations_found += 1
    print ("\nForam encontradas", locations_found, "atrações.")

    #print(clean_webResponse)
    


def main():
    
    # latitude = float(input("Localização (latitude): "))
    # longitude = float(input("Localização (longitude): "))
    # raio = float(input("Distância que pode viajar (km): "))
    
    # Forum aveiro (testes)
    # latitude = 40.64119
    # longitude = -8.65141
    # raio = 1.0

    #Coordenadas do stor
    latitude = 40.5
    longitude = -8.5
    raio = 5005
    
    print("Categorias de atrações disponíveis: \n")
    printList(mainCategories())
    while True:
        cat = str(input("Escolha as categorias das atrações que deseja visitar: "))
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

    #Criação do Url para o geoapify
    url = "https://api.geoapify.com/v2/places?"
    url += "categories=" + cat + "&filter=circle:" + str(longitude) + "," + str(latitude) + "," + str(raio) + "&bias=proximity:" + str(longitude) + "," + str(latitude) 
    url += "&apiKey=" + "34e316823d0044c4b9725dcd1af10809"
    #Resposta do servidor
    response = requests.get(url)
    webResponse = response.json()
    print_cleanWebResponse(webResponse)
    # with open("API_key.txt") as file:
    #     api_key = file.read()
    # api_key = api_key.strip()

if "_main_" == "_main_":
    main()