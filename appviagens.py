#Grupo: P12G01
import requests
            from prettytable import PrettyTable

#   To do:
#   fazer a lista das categorias mais bonita e fazer uma tabela para o output
#   outras informações que possamos vir a considerar importantes 
#   distancia media, ordenação por distância maior ou menor, mostrar os mais perto e mais longe, (mais ideias)
#   verificar se o que a pessoa esta certo, tipo se as coordenadas que inseriu são um numero
#   ESTA A DAR ERRO NO COUNTRY


# Escreve todas as atrações disponíveis e tira o "\n" que vinha agarrado a todas para facilitar chamá-las
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

# Print de uma lista com setas atrás
def printList(lista):
    for value in lista:
        print("\t"+u"\u2192 " + " " + value)

    # print(f"{len(lista): >50}")
    # print("".format())

# Função que dá print do resultado obtido pelo Geoapify e o transforma numa tabela de dados
def print_cleanWebResponse(webResponse):
    
    tabela = PrettyTable(["Nome", "País", "Distrito", "Cidade", "Rua", "Código Postal", "Coordenadas", "Distância"])

    locations_found = 0

    distânciaTotal = 0

    clean_webResponse = webResponse["features"]

    print("\nAqui estão as atrações encontradas: \n")

    for feature in clean_webResponse:
        properties = feature["properties"]
        # Se não houver nome, não contará para o output
        if "name" in properties:
            name = properties["name"]

            # Para cada um dos valores, no caso de não estarem dados nenhuns disponíveis, apenas apresentar "sem dados" para não dar erro.

            if  "country" in properties:
                country = properties["country"]
            else: country = "Sem dados"
            
            if  "district" in properties:
                district = properties["district"]
            else: district = "Sem dados"
            
            if  "city" in properties:
                city = properties["city"]
            else: city = "Sem dados"
            
            if  "street" in properties:
                street = properties["street"]
            else: street = "Sem dados"
            
            if  "postcode" in properties:
                postcode = properties["postcode"]
            else: postcode = "Sem dados"
            
            # Não é necessário tornar a latitude e longitude error-proof, pois existem sempre dados.
            coordinates = properties["coordinates"]
            
            # No caso da distância, se não houverem dados é porque o local se encontra nas coordenadas introduzidas e a distância será 0
            if "distance" in properties:
                distance = properties["distance"]
                distânciaTotal += float(distance)
            else:
                distance = "0"
            

            tabela.add_row([name, country, district, city, street, postcode, coordinates, distance])
            
            locations_found += 1

    # tabela dos outputs
    print(tabela)

    # Outras informações adicionais
    print("\nForam encontradas", locations_found, "atrações.")
    print("A distância média às atrações próximas é de:", round(distânciaTotal / locations_found, 2))

    


def main():
    
    latitude = float(input("Localização (latitude): ")) #40.6379691
    longitude = float(input("Localização (longitude): ")) #-8.6509341
    raio = float(input("Distância que pode viajar (km): ")) * 1000 #0.2
    
    # Forum aveiro (testes)
    # latitude = 40.64119
    # longitude = -8.65141
    # raio = 10000

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
    #print(url)

    #Resposta do servidor
    response = requests.get(url)
    webResponse = response.json()
    #print (webResponse)
    print_cleanWebResponse(webResponse)
    # with open("API_key.txt") as file:
    #     api_key = file.read()
    # api_key = api_key.strip()

if "_main_" == "_main_":
    main()