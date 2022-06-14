import funciones as fn
#Entrada programa
print("*"*3,"Bienvenido al sistema de registro de ciudadanos de Andalucía","*"*3)
while True:
    menu=int(input("¿Qué desea realizar?\n1. Grabar.\n2. Buscar.\n3. Imprimir.\n4. Salir.\n"))
    if menu == 1: #Grabar
        pass
        fn.grabar()
    elif menu == 2: #Buscar
        pass
        fn.buscar()
    elif menu == 3: #Imprimir
        pass
        fn.imprimir()
    elif menu == 4: #Salir
        break
    else:
        print("Ingreso incorrecto.")



