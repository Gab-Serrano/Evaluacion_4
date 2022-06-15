datos=[]
#Función grabar
def grabar(nif,nom,edad,fech,ueur,conyu):
    datos.append([nif,nom,edad,fech,ueur,conyu])
    print(datos)
#Función buscar
def buscar():
    pass

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