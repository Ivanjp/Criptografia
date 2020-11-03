import math

# UNIVERSIDAD NACIONAL AUTONOMA DE MEXICO FACULTAD DE CIENCIAS UNAM
# CRIPTOGRAFIA 2021-1
# ALUMNOS: Jorge Ivan Perez Perez 314211349
#          Dafne Michel Miranda Salazar 314212597

#Funcion que normaliza la llave y el texto claro, quita los espacios y caracteres que no se encuentran en el abecedario Z27
def normaliza(texto):
    text = texto
    listaCaracteres = ["|", "°", "¬", "!", "#", "$", "%", "&", "/",
                       "(", ")", "=", "?", "¡", "¿", "+", "*", "{", "}", "[", "]", ",", ";", ".", ":", "-", "_", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "\""]
    for i in listaCaracteres:
        if i in texto:
            text = text.replace(i, "")

    return text.upper()

#Verifica si la llave genera una matriz cuadrada
def verifKey(n):
    x = math.sqrt(n)
    if n == x**2:
        return True
    else:
        return False

#Crea la matriz de cifrado o las matrices de el texto claro
def creaMatriz(texto, tipo, grado):
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    g = grado
    preMatriz = list(texto)
    matrizIndices = []
    for i in preMatriz:
        matrizIndices.append(abc.index(i))

    if tipo == "Llave":
     filas = g
     col = g
     M = [matrizIndices[col*i: col*(i+1)] for i in range(filas)]
     return M
    elif tipo == "Texto":
     filas = g
     col = 1
     M = [matrizIndices[col*i: col*(i+1)] for i in range(filas)]
     return M

#Saca el determinante de una matriz para verificar si la matriz tiene inversa
def determinante(m):
    orden = len(m[0])
    if orden == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    else:
        j = 0
        for i in range(orden):
            n = copia(m)
            for k in range(orden):
                n[k].pop(i)
            n.pop(0)
            j = j+m[0][i]*(-1)**(i+k)*determinante(n)

    return j

#Funcion que hace una copia de una matriz
def copia(m):
    result = []
    for f in m:
        result.append(f[:])
    return result

#Funcion que calcula el Maximo comun Divisor para ver si la llave tiene inversa y se puede utilizar para descifrar
def mcd(x, y):

    while(y):
        x, y = y, x % y
    return x

#Funcion que genera una matriz con los resultados de multiplicar la matriz de cifrado con los n-gramas
def multMatriz(mC, mT, grado):
    mM = []

    if grado == 2:
        for m in mT:
            for n in mC:
                mM.append(n[0]*m[0][0] + n[1]*m[1][0])
    elif grado == 3:
        for m in mT:
            for n in mC:
                mM.append(n[0]*m[0][0] + n[1]*m[1][0] + n[2]*m[2][0])
    elif grado == 4:
        for m in mT:
            for n in mC:
                mM.append(n[0]*m[0][0] + n[1]*m[1][0] + n[2]*m[2][0] + n[3]*m[3][0])
    elif grado == 5:
        for m in mT:
            for n in mC:
                mM.append(n[0]*m[0][0] + n[1]*m[1][0] + n[2]*m[2][0] + n[3]*m[3][0] + n[4]*m[4][0])
    elif grado == 6:
        for m in mT:
            for n in mC:
                mM.append(n[0]*m[0][0] + n[1]*m[1][0] + n[2]*m[2][0] + n[3]*m[3][0] + n[4]*m[4][0] + n[5]*m[5][0])
    elif grado == 7:
        for m in mT:
            for n in mC:
                mM.append(n[0]*m[0][0] + n[1]*m[1][0] + n[2]*m[2][0] + n[3]*m[3][0] + n[4]*m[4][0] + n[5]*m[5][0] + n[6]*m[6][0])
    elif grado == 8:
        for m in mT:
            for n in mC:
                mM.append(n[0]*m[0][0] + n[1]*m[1][0] + n[2]*m[2][0] + n[3]*m[3][0] + n[4]*m[4][0] + n[5]*m[5][0] + n[6]*m[6][0] + n[7]*m[7][0])
    elif grado == 9:
        for m in mT:
            for n in mC:
                mM.append(n[0]*m[0][0] + n[1]*m[1][0] + n[2]*m[2][0] + n[3]*m[3][0] + n[4]*m[4][0] + n[5]*m[5][0] + n[6]*m[6][0] + n[7]*m[7][0] + n[8]*m[8][0])
    
    return mM

#Genera el texto cifrado                
def genera(Matrix):

    aux = []
    textoCif = []
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

    for n in Matrix:
        aux.append(n%27)
 
    for a in aux:
        textoCif.append(abc[a])

    texto_cifrado = ''.join(textoCif)
    print(f"\nEl texto cifrado es: {texto_cifrado}\n")


#Funcion que cifra el texto claro del usuario
def cifrar(key,text):
    g = int(math.sqrt(len(key)))
    matrizCifrado = creaMatriz(key,"Llave",g)
    aux = determinante(matrizCifrado)
    aux1 = aux%27

    if verifKey(len(key)) == False:
        print("\nTu clave no genera una matriz nxn\n")
    elif len(text)%g == 1:
        print("\nLa longitud de tu texto no es multiplo de N\n")
    elif mcd(aux1,27) == 1:
     i = 0
     m = []
     mFinal = []

     while i < len(text):
         m.append(text[i:i+g])
         i+=g
    
     for let in m:
         mFinal.append(creaMatriz(let,"Texto",g))

     genera(multMatriz(matrizCifrado,mFinal,g)) 
    else:
        print("La matriz de cifrado no tiene inversa, escoge otra clave\n")

def main():
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
        key = input("\nIngresa tu llave >> ")
        txt = input("\nIngresa tu texto a cifrar >> ")

        keyN = normaliza(key) #Normaliza llave
        textN = normaliza(txt)  # Normaliza texto

        cifrar(keyN,textN)
       
    elif opcionMenu == "2":
       print("")

    elif opcionMenu == "0":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
