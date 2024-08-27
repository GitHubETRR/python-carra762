def main() :
    dictionary = pilot('Pilot.txt')

    if dictionary :
        menu(dictionary)


def pilot(file) :
    dictionary = []
    try :
        with open (file, 'r', encoding = 'utf-8') as f :
            for linea in f : 
                nom_ap, apo, an = linea.strip().split('"')
                
                palabras = nom_ap.split()
                nom2 = palabras[1] if len(palabras) == 3 else ""
                nom, ap = palabras[0], palabras[-1]

                an = list(map(int, an.strip().split()))
                
                dictionary.append({
                    'nom y ap' : nom_ap,
                    'nom' : nom,
                    'nom2' : nom2,
                    'ap' : ap,
                    'apo' : apo,
                    'an' : an,
                })
            
            return dictionary              

    except OSError :
        print("no se pudo abrir el archivo.")
        return None


def repeatedWords(apellido) :
    opciones = {
        'rosberg' : ["keke" , "nico"],
        'hill' : ["phil", "graham", "damon"],
    }

    if apellido in opciones :
        while True :
            election = input(f"{' , ' .join(opciones[apellido])} {[apellido]}").strip().lower()
            if election in opciones[apellido] :
                return election
            else : 
                print("piloto no válido")
    
    return apellido


def searchByName(dictionary, search) :
    namef = ["juan", "manuel", "fangio"] #fangio
    nameh = ["hakinen", "hakkinen", "hakinnen", "hakkinnen"] #hakkinen
    namek = ["raikonen", "raikkonen", "raikonnen", "raikkonnen"] #raikkonen

    j = 0
    for d in dictionary :
        if search == 'rosberg' :
            pregunta = input("Keke o Nico Rosberg?: ").strip().lower()
            if pregunta == 'keke' :
                search = 'keke' 
            elif pregunta == 'nico' :
                search = 'nico'
            else : 
                print("no se encontró piloto")
                return "no se encontró piloto" , j
        
        if search == 'hill' :
            pregunta = input("Phil, Graham o Damon Hill?: ").strip().lower()
            if pregunta == 'phil' :
                search = 'phil' 
            elif pregunta == 'graham' :
                search = 'graham'
            elif pregunta == 'damon' :
                search = 'damon'
            else : 
                print("no se encontró piloto")
                return "no se encontró piloto" , j

        if search == namek : #raikkonen
            if d['ap'] == 'Räikkönen' :
                print(f"{d['nom']} {d['ap']} ganó en {d['an']}")
                j += 1
        
        if search in nameh : #hakkinen
            if d['ap'] == 'Häkkinen' :
                print(f"{d['nom']} {d['ap']} ganó en {d['an']}")
                j += 1

        if search == d['nom'].lower() or search == d['nom2'].lower() or search == d['ap'].lower() or search == d['apo'].lower() :
            j += 1
            if search == namef : #fangio
                print(f"{d['nom']} {d['nom2']} {d['ap']} ganó en {d['an']}")
            else : 
                print(f"{d['nom']} {d['ap']} ganó en {d['an']}")

            return d['nom y ap'] , j

    return "no se encontró piloto", j  


def searchByNumber(dictionary, search) :
    yearsf = [1951, 1954, 1955, 1956, 1957] #fangio 

    j = 0
    for d in dictionary :
        if search in d['an'] :
            if search == yearsf :
                print(f"{d['nom']} {d['nom2']} {d['ap']} ganó en {d['an']}")
                j += 1
            else : 
                print(f"{d['nom']} {d['ap']} ganó en {d['an']}")
                j += 1

            return d['nom y ap'], j
        
    return "no se encontró piloto", j

    

def DatoInteresante(file, i) :
    i = i.lower().strip()
    try :
        with open (file , 'r', encoding = 'utf-8') as f :
            for linea in f : 
                linea = linea.strip()

                nom_ap, info = linea.split(':')

                info = info.strip()

                if i.lower() in nom_ap.lower() :
                    print(info) 
                    break


    except OSError :
        print("no se pudo abrir el archivo.")


def continuar() :
    while True :
        continuar = input("¿continuar? si/no: ").strip().lower()
        if continuar in ["no", "n"] :
            return False , 'e'
        elif continuar in ["si", "s"] :
            return True , ''
        print("ingrese 'si' o 'no' ")


def menu(dictionary) :
    n = ["n", "nombre", "apellido"]
    y = ["y", "año", "anio"]
    e = ["e", "exit", "salir"]

    option = ''
    while option != 'e' :
        while True :
            option = input ("ingrese 'n' para nombre o apellido, ingrese 'y' para un año o 'e' para salir: ").strip().lower()
            j = 0
            if option in n :
                while j == 0 :
                    search = input("Nombre o apellido: ").strip().lower()
                    i = ""
                    i , j = searchByName(dictionary, search)
                    if i == 'no se encontró piloto' and j == 0:
                        print("intente nuevamente.")
                        j = 0
                    else :
                        DatoInteresante('datos.txt', i)

            elif option in y :
                while j == 0 :
                    try :
                        search = int(input("año: ")) 
                        i , j = searchByNumber(dictionary, search)
                        if i == 'no se encontró piloto' and j == 0:
                            print("intente nuevamente.")
                            j = 0
                        else :
                            DatoInteresante('datos.txt', i)

                    except ValueError :
                        print("no es un año válido, por favor, volver a ingresarlo")
                        j = 0
            
            if option in n or option in y :
                continuar_respuesta , new_answer = continuar()
                if not continuar_respuesta :
                    option = new_answer 
                    print("muchas gracias")
                    break
            elif option in e :
                print("muchas gracias")
                break
            else :
                print("opción incorrecta")    
      

main()