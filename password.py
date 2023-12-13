# La librería random nos permite de manera aleatoria elegir los caracteres que vamos a utilizar. 
import random

"""La primer variable nos solicitará el tamaño que deseamos de nuestra contraseña y la segunda es para 
    los caracteres de los que se va a elegir"""

longitud = input('Introduzca longitud de la clave: ')
base_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&?_'

"""Definamos la funcion que nos ayudará a hacer el trabajo de generar la cadena de texo."""

def generate(longitud):
    passwd = ''
    while len(passwd) != int(longitud):
        passwd += random.choice(base_char)
    print(passwd)

result = generate(longitud)