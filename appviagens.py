#Grupo: P12G01
import requests
from prettytable import PrettyTable

# LER PRIMEIRO:
#   Para o programa funcionar corretamente, é necessário ser instalado o addon "pretty table" que pode ser feito com: 
#       python -m pip install -U prettytable
# 
#   Para uma melhor visibilidade da tabela, colocar o terminal em Fullscreen


# Escreve todas as atrações disponíveis e tira o "\n" que vinha agarrado a todas para facilitar chamá-las
def obterAtrações():
    atraçõesExistentes = []
    with open("categories.txt", "r") as atrações:
        for linhas in atrações.readlines():
            atraçõesExistentes.append(linhas)
        atraçõesExistentes = [elemento.replace("\n", "") for elemento in atraçõesExistentes]
    return atraçõesExistentes

# Função que devolve apenas as categorias principais
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


# Função que dá print do resultado obtido pelo Geoapify e o transforma numa tabela de dados
def print_cleanWebResponse(webResponse):

    tabela = PrettyTable(["Nome", "País", "Distrito", "Localidade", "Rua", "Código Postal", "Coordenadas", "Distância (m)"])

    locations_found = 0

    distânciaTotal = 0

    clean_webResponse = webResponse["features"]

    print("\nAqui estão as atrações mais próximas encontradas: \n")

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
                district = properties["county"]
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
            lat = properties["lat"]
            lon = properties["lon"]
            latlon = (lat, lon)
            
            # No caso da distância, se não houverem dados é porque o local se encontra nas coordenadas introduzidas e a distância será 0
            if "distance" in properties:
                distance = properties["distance"]
                distânciaTotal += float(distance)
            else:
                distance = "0"
            

            tabela.add_row([name, country, district, city, street, postcode, latlon, distance])

            locations_found += 1

    # Tabela dos outputs
    print(tabela)

    # Outras informações adicionais
    print("\nForam encontradas", locations_found, "atrações.")
    
    # Se não houverem atrações, não fazer a distância média
    if locations_found > 0:
        distânciaTotal = round(distânciaTotal / locations_found, 2)
        print("A distância média às atrações próximas é de:", distânciaTotal, "m")    
    
    # Para testes
    # print(webResponse)


def main():

    
    while True:
        latitude = input("Localização (latitude): ")
        # Serve para verificar se introduziu um número
        if latitude.isalpha():
            print("Introduza um número!")
        elif float(latitude) <= 90 and float(latitude) >= -90:
            latitude = float(latitude)
            break
        else:
            print("Introduza um valor válido (de -90 a 90)")

    while True:
        longitude = input("Localização (longitude): ")
        if longitude.isalpha():
            print("Introduza um número!")
        elif float(longitude) <= 180 and float(longitude) >= -180:
            longitude = float(longitude)
            break
        else:
            print("Introduza um valor válido (de -180 a 180)")
    
    while True:
        raio = float(input("Distância que pode viajar (km): ")) * 1000
        if raio < 0:
            print("Introduza uma distância válida!")
        else:
            break
        
    # Forum aveiro (testes)
    # latitude = 40.64119
    # longitude = -8.65141
    # raio = 10000
    
    print("\nCategorias de atrações disponíveis:")
    printList(mainCategories())
    categorias = []
    listaCategorias	= ""
    categoriasEscolhidas = 0
    print("\nEscolha as categorias das atrações que deseja visitar. Introduza uma de cada vez e quando terminar colocar \"end\":")
    while True:
        cat = str(input("\t> " ))
        # Serve para o utilizador terminar com as categorias que vai escolher
        if cat.lower() == "end" and categoriasEscolhidas >= 1:
            break
        elif cat.lower() not in mainCategories():
            print("\t\t!! Escolha categorias válidas !!")
            continue
        else:
            categorias.append(cat)
            categoriasEscolhidas += 1
            continue
    # Cria uma lista de categorias para se colocar na url
    for categoria in categorias:
        if categorias.index(categoria) == 0: listaCategorias += categoria
        else: listaCategorias += "," + categoria

    # Para testes
    # print(listaCategorias)

    #Criação do Url para o geoapif; Até 50 atrações
    
    apikey = "34e316823d0044c4b9725dcd1af10809"

    url = "https://api.geoapify.com/v2/places?"
    url += "categories=" + listaCategorias + "&filter=circle:" + str(longitude) + "," + str(latitude) + "," + str(raio) + "&bias=proximity:" + str(longitude) + "," + str(latitude) 
    url += "&limit=50&apiKey=" + apikey

    #Resposta do servidor
    response = requests.get(url)
    webResponse = response.json()
    #print (webResponsle)
    print_cleanWebResponse(webResponse)


if __name__ == "__main__":
    main()