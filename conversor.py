print("¡Bienvenido al banco conversor de monedas!")
m1 = input("Ingresa el numero de la divisa que deseas convertir \n1.Dolares \n2.Euros \n3.Pesos Mexicanos \n4.Libras Inglesas \n5.Yen \n")



if m1 == '1':  # DOLARES
    m2 = input("Ingresa el numero al que deseas convertir tus divisas \n1.Euros \n2.Pesos Mexicanos \n3.Libras Inglesas \n4.Yen \n")
    if m2 == "1":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = cash * 0.913448
        print(f'Tienes {conv} euros')
    elif m2 == "2":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = cash * 17.1234
        print(f'Tienes {conv} pesos mexicanos')
    elif m2 == "3":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = cash * 0.793147
        print(f'Tienes {conv} libras inglesas')
    elif m2 == "4":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = cash * 149.484
        print(f'Tienes {conv} yenes')

elif m1 == "2":  # EUROS
    m2 = input("Ingresa el numero al que deseas convertir tus divisas \n1.Dolares \n2.Pesos Mexicanos \n3.Libras Inglesas \n4.Yen \n")
    if m2 == "1":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 1.1)
        print(f'Tienes {conv} dolares')
    elif m2 == "2":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 18.7329)
        print(f'Tienes {conv} pesos mexicanos')
    elif m2 == "3":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 0.868401)
        print(f'Tienes {conv} libras inglesas')
    elif m2 == "4":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 163.607)
        print(f'Tienes {conv} yenes')

elif m1 == "3":  # PESOS MEXICANOS
    m2 = input("Ingresa el numero al que deseas convertir tus divisas \n1.Dolares \n2.Euros \n3.Libras Inglesas \n4.Yen \n")
    if m2 == "1":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 0.0584337)
        print(f'Tienes {conv} dolares')
    elif m2 == "2":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 0.0533802)
        print(f'Tienes {conv} pesos mexicanos')
    elif m2 == "3":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 0.0463458)
        print(f'Tienes {conv} libras inglesas')
    elif m2 == "4":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 8.73434)
        print(f'Tienes {conv} yenes')

elif m1 == "4":  #LIBRAS ESTERLINAS
    m2 = input("Ingresa el numero al que deseas convertir tus divisas \n1.Dolares \n2.Euros \n3.Pesos Mexicanos \n4.Yen \n")
    if m2 == "1":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 1.26078)
        print(f'Tienes {conv} dolares')
    elif m2 == "2":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 1.15178)
        print(f'Tienes {conv} euros')
    elif m2 == "3":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 21.5753)
        print(f'Tienes {conv} pesos mexicanos')
    elif m2 == "4":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 188.460)
        print(f'Tienes {conv} yenes')

elif m1 == "5":  # YENES
    m2 = input("Ingresa el numero al que deseas convertir tus divisas \n1.Dolares \n2.Euros \n3.Pesos Mexicanos \n4.Libras Inglesas \n")
    if m2 == "1":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 0.00668996)
        print(f'Tienes {conv} dolares')
    elif m2 == "2":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 0.00611125)
        print(f'Tienes {conv} euros')
    elif m2 == "3":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 0.114508)
        print(f'Tienes {conv} pesos mexicanos')
    elif m2 == "4":
        cash = float(input("Ingresa la cantidad de dinero a convertir "))
        conv = (cash * 0.00530703)
        print(f'Tienes {conv} libras inglesas')

else:
    print("Gracias por usar este conversor!")