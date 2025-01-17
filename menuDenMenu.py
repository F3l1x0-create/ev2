opc=0


while True :
    print("===menu===")
    print("[1]-mas opciones")
    print("[2]-opcion 2")
    print("[3]-salir ")


    try:
        opc=int(input("selecciona opcion: "))
        
    except ValueError:
        print("opcion no valida ")
        continue
    


    if opc== 1 :
        while True:
            print("===menu===")
            print("[1]-opcion 1")
            print("[2]-salir ")
    opc2=int(input("selecione una opcion : "))
    if opc2== 1:
        print("opcion menu del menu 1 ")
    elif  opc2==2:
        print("saliendo")
        break

 
              

    elif opc == 2:
        print("opcion 2 ")
    elif opc == 3:
        print("salir del menu")
    break
        