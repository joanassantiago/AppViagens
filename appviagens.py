#Grupo: P12G01
import requests


#   To do:
#   fazer a lista das categorias mais bonita e fazer uma tabela para o output
#   outras informações que possamos vir a considerar importantes 
#   distancia media, ordenação por distância maior ou menor, mostrar os mais perto e mais longe, (mais ideias)
#   verificar se o que a pessoa esta certo, tipo se as coordenadas que inseriu são um numero


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
        print("\t"+u"\u2192"+" "+x)

    # print(f"{len(lista): >50}")
    # print("".format())

def print_cleanWebResponse(webResponse):
    
    locations_found = 0
    clean_webResponse = webResponse["features"]
    print("Aqui estão as atrações encontradas: \n")

    for feature in clean_webResponse:
        properties = feature["properties"]
        if "name" in properties and "country" in properties:
            name = properties["name"]
            country = properties["country"]
            district = properties["county"]
            city = properties["city"]
            street = properties["street"]
            postcode = properties["postcode"]
            lat = properties["lat"]
            lon = properties["lon"]
            
            distance = "0"
            if "distance" in properties:
                distance = properties["distance"]
            
            print (name,"|",country,"|",district,"|",city,"|",street,"|",postcode,"|", lat,",",lon ,"|", distance,("m"))

            locations_found += 1

    print ("\nForam encontradas", locations_found, "atrações.")

    # print(clean_webResponse)
    


def main():
    
    latitude = float(input("Localização (latitude): ")) #40.6379691
    longitude = float(input("Localização (longitude): ")) #-8.6509341
    raio = float(input("Distância que pode viajar (km): ")) * 1000 #0.2
    
    # Forum aveiro (testes)
    # latitude = 40.64119
    # longitude = -8.65141
    # raio = 1.0

    #Coordenadas do stor
    # latitude = 40.5
    # longitude = -8.5
    # raio = 5005 * 1000
    
    print("Categorias de atrações disponíveis:")
    printList(mainCategories())
    categorias = []
    listaCategorias	= ""
    print("\nEscolha as categorias das atrações que deseja visitar. Introduza uma de cada vez e quando terminar colocar \"end\":")
    while True:
        cat = str(input("\t> " ))
        if cat.lower() == "end":
            break
        elif cat.lower() not in mainCategories():
            print("\t\t!! Escolha categorias válidas !!")
            continue
        else:
            categorias.append(cat)
            continue

    if len(categorias) == 0:
        print("\nERROR")
        return

    for categoria in categorias:
        if categorias.index(categoria) == 0: listaCategorias += categoria
        else: listaCategorias += "," + categoria

    # Para testes
    # print(listaCategorias)

    #Criação do Url para o geoapify
    url = "https://api.geoapify.com/v2/places?"
    url += "categories=" + listaCategorias + "&filter=circle:" + str(longitude) + "," + str(latitude) + "," + str(raio) + "&bias=proximity:" + str(longitude) + "," + str(latitude) 
    url += "&limit=50&apiKey=" + "34e316823d0044c4b9725dcd1af10809"
    print(url)
    #Resposta do servidor
    response = requests.get(url)
    webResponse = response.json()
    print_cleanWebResponse(webResponse)
    # with open("API_key.txt") as file:
    #     api_key = file.read()
    # api_key = api_key.strip()

if "_main_" == "_main_":
    main()