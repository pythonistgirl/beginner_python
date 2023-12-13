# Este programa me permitirá calcular las propinas de un restaurante

"""Este programa me permitirá calcular las propinas que los comensales deseen dejar, y también la calificaión del servicio"""

# Las primeras variables a ingresar son las siguientes
nombre = str(input("¿Cuál es su nombre? "))
mesa = int(input("¿Qué mesa ocupó? "))
mesero = str(input("¿Quién lo atendió? "))
servicio = int(input("Del 1 al 10 ¿Qué calificación le da al mesero? "))
cuenta = float(input("¿De cuánto es su cuenta? "))
pregunta = int(input("¿Desea dejar propina? \nEscriba 1 para Sí o 2 para NO "))

"""Aquí debemos escribir una función que nos permita hacer el calculo y aquí te dejo 2 formas, la primera puede ser que el mismo 
    comensal decida dejar propina, es la que esta a continuación """

def cal():
    if pregunta == 1:
        propina = int(input("Ingrese el porcentaje deseado: "))
        porcentaje = (cuenta * propina) / 100
        i = cuenta + porcentaje
        print(f'Gracias {nombre} por su consumo, lo atendió {mesero}, su total a pagar es {i} pesos.\nSu calificación es importante, gracias por los {servicio} puntos. Buen día')
    else:
        print(f'Gracias {nombre} por su consumo, lo atendió {mesero}, su total a pagar es {cuenta} pesos.\nSu calificación es importante, gracias por los {servicio} puntos. Buen día')
        
resultado = cal()

"""La siguiente función es si el restaurante decide elegir el procentaje de la propina, acorde a la calificación que le de al mesero"""

def calculate():
    if servicio > 8:
        porcentaje = (cuenta * 15) / 100
        i = cuenta + porcentaje
        print(f'Gracias {nombre} por su consumo, lo atendió {mesero}, 
              su total a pagar es {i} pesos.\nSu calificación es importante, gracias por los {servicio} puntos. Buen día')
        
    elif servicio > 4:
        porcentaje = (cuenta * 8) / 100
        i = cuenta + porcentaje
        print(f'Gracias {nombre} por su consumo, lo atendió {mesero}, 
              su total a pagar es {i} pesos.\nSu calificación es importante, gracias por los {servicio} puntos. Buen día')
    else:
        porcentaje = (cuenta * 2) / 100
        i = cuenta + porcentaje
        print(f'Gracias {nombre} por su consumo, lo atendió {mesero}, 
              su total a pagar es {i} pesos.\nSu calificación es importante, gracias por los {servicio} puntos. Buen día')

result = calculate()

"""Para ambos casos los resultados funcionan, pero si tienes dudas escribeme mensaje directo por IG: @pythonist_girl"""