datos=[]
#Función grabar
def grabar(nif,nom,edad,fech,conyu):
    if conyu == 1:
        conyu="Soltero"
    elif conyu == 2:
        conyu="Casado"
    elif conyu == 3:
        conyu="Divorciado"
    else:
        conyu="Viudo"
    datos.append([nif,nom,edad,fech,conyu])
#Función buscar
def buscar(nif):
    for i in datos:
        if nif in i:
            count=0
            for j in i:
                count+=1
                if count == 1:
                    print("Número NIF:",j)
                elif count == 2:
                    print("Nombre:",j)
                elif count == 3:
                    print("Edad:",j)
                elif count == 4:
                    print("Fecha de nacimiento:",j)
                elif count == 5:
                    print("Estado Civil:",j)
        else:
            print("La persona buscada no pertence a la Unión Europea.")

#Función imprimir
def imprimir(submenu,nif):
    if submenu == 1:
        for i in datos:
            if nif in i:
                count=0
                print("*"*3,"Certificado de Nacimiento","*"*3)
                for j in i:
                    count+=1
                    if count == 1:
                        print("Número NIF:",j)
                    elif count == 2:
                        print("Nombre:",j)
                    elif count == 4:
                        print("Fecha de nacimiento:",j)
                print("")
                print("Firma: Registro Civil de Andalucía")
    elif submenu == 2:
        for i in datos:
            if nif in i:
                count=0
                print("*"*3,"Certificado de estado conyugal","*"*3)
                print("")
                for j in i:
                    count+=1
                    if count == 1:
                        nif_n=j
                    elif count == 2:
                        nombr=j
                    elif count == 5:
                        es_civ=j
                print("La persona de nombre",nombr,", número NIF",nif_n,"mantiene un estado civil",es_civ,".")
                print("")
                print("Firma: Registro Civil de Andalucía")
    else:
        for i in datos:
            if nif in i:
                count=0
                print("*"*3,"Certificado de Pertenencia a la Unión Europea","*"*3)
                print("")
                for j in i:
                    for j in i:
                        count+=1
                        if count == 1:
                            nif_n=j
                        elif count == 2:
                            nombr=j
                        elif count == 3:
                            edad=j
                print("La persona de nombre",nombr,", número NIF",nif_n,"de",edad,"años")
                print("Pertenece a la Unióin Europea ya que posee un NIF válido.")
                print("")
                print("Firma: Registro Civil de Andalucía")

#Verificar NIF
def verif_nif(nif,val=0):
    nif_leng=len(nif)
    for i in nif:
        if i == "-":
            val=+1
    if val == 1 and nif_leng == 12:
        return True