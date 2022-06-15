import funciones as fn
#Entrada programa
print("*"*3,"Bienvenido al sistema de registro de ciudadanos de Andalucía","*"*3)
while True:
    menu=int(input("¿Qué desea realizar?\n1. Grabar.\n2. Buscar.\n3. Imprimir.\n4. Salir.\n"))
    if menu == 1: #Grabar
        while True:
            nif_num=input("Ingrese el número NIF por registrar (incluir DV):\n")
            if fn.verif_nif(nif_num):
                break
            else:
                print("Debe ingresar un NIF correcto XXXXXXXX-ABC.")
        while True:
            nombre=input("Ingrese el nombre por registrar:\n")
            if len(nombre) >= 8:
                break
            else:
                print("Mínimo de carácteres incorrecto.")
        while True:
            try:
                edad=int(input("Ingrese la edad por registrar:\n"))
                if edad >= 0:
                    break
                else:
                    "Ingreso de edad incorrecta. Debe ser mayor que 0."
            except ValueError:
                print("Debe ingresar solo números.")
        fech_nac=input("Ingrese la fecha de nacimiento (dd/mm/aa):\n")
        conyu=input("¿Cuál es su estado civil?\n1. Soltero.\n2. Casado.\n3. Divorciado.\n4. Viudo.\n")
        fn.grabar(nif_num,nombre,edad,fech_nac,conyu)
    elif menu == 2: #Buscar
        while True:
            buscar_nif=input("Ingrese el NIF de la persona a buscar:\n")
            if fn.verif_nif(buscar_nif):
                break
            else:
                print("Debe ingresar un NIF correcto XXXXXXXX-ABC.")
        fn.buscar(buscar_nif)
    elif menu == 3: #Imprimir
        while True:
            try:
                option=int(input("¿Qué tipo de certificado desea imprimir?\n1. Certificado de nacimiento.\n2. Certificado de estado conyugal.\n3. Certificado de pertenencia a la Unión Europea.\n"))
                if option > 0 and option < 4:
                    break
                else:
                    print("Ingrese una opción correcta.")           
            except ValueError:
                print("Ingrese solo números.")
        while True:
            impr_nif=input("Ingrese el NIF de la persona:\n")
            if fn.verif_nif(impr_nif):
                break
            else:
                print("Debe ingresar un NIF correcto XXXXXXXX-ABC.")
        fn.imprimir(option,impr_nif)
    elif menu == 4: #Salir
        print("Muchas gracias. Saliendo del programa.")
        print("Programa desarrollado por Gabriel Serrano M.")
        print("Ver. 1.1.0.")
    else:
        print("Ingreso incorrecto.")



