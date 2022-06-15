datos=[]
#Función grabar
def grabar(nif,nom,edad,fech,ueur,conyu):
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
                    print("Nombre",j)
                elif count == 3:
                    print("Edad:",j)
                elif count == 4:
                    print("Fecha de nacimiento:",j)
                elif count == 5:
                    print("Estado Civil:",j)
        else:
            print("La persona buscada no pertence a la Unión Europea.")

#Función imprimir
def imprimir():
    pass

#Verificar NIF
def verif_nif(nif,val=0):
    nif_leng=len(nif)
    for i in nif:
        if i == "-":
            val=+1
    if val == 1 and nif_leng == 12:
        return True