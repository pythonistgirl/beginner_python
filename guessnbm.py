import random

rdm_nmb = random.randint(0,2)
number = int(input("Adivina el numero "))

# print(rdm_nmb)

while number != rdm_nmb:
    number = int(input("No has adivinado el numero intentalo otra vez "))
    if number == rdm_nmb:
        print(f'{number} es la respuesta ¡FELICIDADES! \nGracias por participar')
        break


