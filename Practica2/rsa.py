import random
import math
from sympy import *

# UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO FACULTAD DE CIENCIAS UNAM
# CRIPTOGRAFIA 2021-1
# ALUMNOS: Jorge Ivan Perez Perez 314211349
#          Dafne Michel Miranda Salazar 314212597

#Funcion que calcula el Maximo comun Divisor para ver si la llave tiene inversa y se puede utilizar para descifrar
def mcd(x, y):

    while(y):
        x, y = y, x % y
    return x

#Funcion que calcula entero positivo e menor que  phi(n), que sea coprimo con phi(n)    
def calculaE(phi):
    #Se escoge un entero al azar
    e = random.randrange(1, phi)

    #Algoritmo de Euclides para verificar que son coprimos
    g = mcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = mcd(e, phi)
    
    return e

#Se implementa el Algoritmo de Euclides Extendido para encontrar el inverso multiplicativo de 2 numeros y asi encontrar la clave privada
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m

#Funcion que genera todas las llaves para este criptosistema
def generaLlaves():
    val = []#Lista donde se guardaran las llaves
    #Rango de numeros de donde se sacaran los 2 numeros primos de 50 digitos
    a = 10000000000000000000000000000000000000000000000000 
    b = 99999999999999999999999999999999999999999999999999
    #Se escoge un numero primo al azar en el rango de a y b
    p = randprime(a, b)
    q = randprime(a, b)
    #Se calcula el modulo
    n = p*q
    #Se calcula phi
    phi = (p-1)*(q-1)
    #Se escoge el entero positivo e, es decir la llave publica
    e = calculaE(phi)
    #Se calcula la llave privada
    d = modinv(e,phi)
    #Agregamos las llaves a la lista
    val.append(n)
    val.append(e)
    val.append(d)

    return val

#Funcion que encripta el mensaje dado por el usuario
def encripta(n,e,msg):
  ctext = [pow(ord(char),e,n) for char in msg]
  return ctext

#Funcion que descencripta el mensaje previamente cifrado
def descencripta(n,d,msg_cryp):

    try:
        text = [chr(pow(char,d,n)) for char in msg_cryp]
        return "".join(text)
    except TypeError as e:
        print(e)

llaves = generaLlaves()#Se guardan las llaves para utilizarlas despues en el main
menc = []#Se guarda el texto cifrado para poder descifrarlo posteriormente

def main():
    print("Criptosistema RSA")
    print("Alumnos:")
    print("\tJorge Ivan Perez Perez")
    print("\tDafne Michel Miranda Salazar\n")
    print("Selecciona una opción")
    print("\t1 - Cifrar.")
    print("\t2 - Descifrar")
    print("\t0 - Salir")


while True:
    # Mostramos el menu
    main()

    # solicituamos una opción al usuario
    opcionMenu = input("\nIngresa la opcion >> ")

    if opcionMenu == "1":
        msg = input("\nIngresa el mensaje que quieres encriptar: ")
        print("\nEncriptando....")
        encryp = encripta(llaves[0],llaves[1],msg)
        print("\nTu mensaje cifrado es: ",encryp)
        print("\n")
        menc = encryp#Asignamos  el texto cifrado a la lista global para acceder a el en la opcion de descifrado
       
    elif opcionMenu == "2":
        
        print("\nDesencriptando....")
        des = descencripta(llaves[0],llaves[2],menc)
        print("\nTu mensaje descifrado es: ",des)
        print("\n")

    elif opcionMenu == "0":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
