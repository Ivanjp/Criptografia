import random as rm
import math
import sympy as sp

# UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO FACULTAD DE CIENCIAS UNAM
# CRIPTOGRAFIA 2021-1
# ALUMNOS: Jorge Ivan Perez Perez 314211349
#          Dafne Michel Miranda Salazar 314212597

#--------------------------------------------------------------------------------------------------
#-----Codigos reutilizado de practicas pasadas, calculo del modulo inverso e implementacion de el algoritmo extendido de euclides.-----
#Se implementa el Algoritmo de Euclides Extendido para encontrar el inverso multiplicativo de 2 numeros
def egcd(a, b):
    if b == 0:
        return (1, 0, a)
    quo, rema = divmod(a, b)
    g, y, x = egcd(b,rema)
    return (y, g - quo * y, x)

#Funcion que calcula el Maximo comun Divisor
def mcd(x, y):

    while(y):
        x, y = y, x % y
    return x

#------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------
#---Funciones para los calculos de la curva---
#Funcion que realiza la suma eliptica de la curva
def sumaE(l1, l2, n1, n2):
    if l1[2] == 0:
        return l2 
    if l2[2] == 0:
        return l1
    if l1[0] == l2[0]:
        if (l1[1] + l2[1]) % n2 == 0:
            return 0, 1, 0
        a = (3 * l1[0] * l1[0] + n1) % n2
        b = (2 * l1[1]) % n2
    else:
        a = (l2[1] - l1[1]) % n2
        b = (l2[0] - l1[0]) % n2
    t, _, g = egcd(b, n2)
    if g > 1:
        return 0, 0, b
    res = (a * t * a * t - l1[0] - l2[0]) % n2
    return res, (a * t * (l1[0] - res) - l1[1]) % n2, 1

#Funcion que realiza la multilicacion elitptica de la curva 
def mulE(primo, l, e3,n2):
    #print("Si llego")
    res = (0, 1, 0)
    while primo > 0:
        if l[2] > 1:
            return l
        if primo % 2 == 1:
            res = sumaE(l, res, e3, n2)
        primo = primo // 2
        l = sumaE(l, l, e3, n2)
    return res

#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
#----Funciones principales----
# Funcion que realiza el algoritmo de Lenstra para factorizar    
def algLenstra(num_c):
    aux = num_c
    lista_primos = sp.primerange(0,num_c)#Lista de numeros primos que representa Z
    #Guardado de primos a utilizar
    ent1 = rm.randint(0, num_c - 1)
    #print(f"Esto es ent1: {ent1}")
    ent2 = rm.randint(0, num_c - 1)
    #print(f"Esto es ent2: {ent2}")
    ent3 = rm.randint(0, num_c - 1)
    #print(f"Esto es ent3: {ent3}")
    l = []#Lista que contendra 2 numeros primos aleatorios de Z
    l.append(ent1)
    l.append(ent2)
    l.append(1)
    while aux == num_c:
        #Ecuaciones
        b = (l[1] * l[1] - l[0] * l[0] * l[0] - ent3 * l[0]) % num_c
        #print(b)
        aux = mcd(4 * ent3**3 + 27 * b**2, num_c)
        #print(f"Esto es g: {aux}")
    if aux > 1:
        return (aux, num_c//aux)
    #Calculo de los factores    
    for p in lista_primos:
        aux2 = p
        while aux2 < num_c:
            l = mulE(p, l, ent3, num_c)
            if l[2] > 1:
                aux = mcd(l[2], num_c)
                return (aux, num_c//aux)
            aux2 = p * aux2
    return "No hay factorizacion para este numero"


def main():
    print("Criptosistema RSA")
    print("Alumnos:")
    print("\tJorge Ivan Perez Perez")
    print("\tDafne Michel Miranda Salazar\n")
    num_c = int(input("\nIngresa tu numero: "))
    print("\nCalculando....")
    print(algLenstra(num_c))
    print("\n")

main()

#------------------------------------------------------------------------------------------