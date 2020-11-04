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
    preMatriz = list(texto)#Se guarda el texto ya se la llave o el texto claro en una matriz
    matrizIndices = [] #Se inicializa la matriz con los indices del alfabeto correspondientes a las letras de la llave o el texto
    for i in preMatriz:
        matrizIndices.append(abc.index(i))#Se llena la matriz con los indices

    if tipo == "Llave":
     filas = g #Filas que tendra la matriz de cifrado
     col = g #Columnas que tendra la matriz de cifrado
     M = [matrizIndices[col*i: col*(i+1)] for i in range(filas)] #Se crea la Matriz de cifrado
     return M
    elif tipo == "Texto":
     filas = g #Filas que tendra los n-gramas del texto
     col = 1 #Columna que tendra el n-grama
     M = [matrizIndices[col*i: col*(i+1)] for i in range(filas)]#Se crea una matriz que guarda los n-gramas del texto claro
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
def multMatriz(mC,mT,grado):
    mM = []
    i = 0

    for m in mT:
        for n in mC:
            for x in range (0,grado):
                i += n[x]*m[x][0]
         
            mM.append(i)
            i = 0

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
    return texto_cifrado

#Funcion que genera la matriz Transpuesta de una matriz 
def transpuesta(matriz):
    rows = len(matriz)
    cols = len(matriz[0])
    return [[matriz[j][i] for j in range(rows)] for i in range(cols)]

#Funcion que calcula el inverso modular del determinante de una matriz
def InversoModular(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

#Funcion que genera la matriz de cofactores de una matriz
def cofactores(M):
    S = []
    n = len(M)
    for i in range(0, n):
        fila = []
        for j in range(0, n):
            s = ((1 - i % 2) * 2 - 1) * ((1 - j % 2) * 2 - 1) * determinante(submatriz(M, i, j))
            fila.append(s)
        S.append(fila)
    return S

#Funcion que genera una submatriz eliminando la i-esima fila y la j-esima columna de la matriz original
def submatriz(M, i, j):
    n = len(M)
    S = []
    for a in range(0, n):
        if a == i:
            continue
            
        fila = []
        for b in range(0, n):
            if b == j:
                continue
            fila.append(M[a][b])
        S.append(fila)
        
    return S

#Funcion que genera la matriz de descifrado
def multMatrizModulo(M, grado,mod):
    
    aux = []#Matriz auxiliar que va a guardar la ultima matriz generada en el bucle que contendra los indices en modulo 27
    for m in M:
        for x in range (0,grado):
            m[x] = (m[x]*mod)%27
     
        aux = copia(M)
    
    return aux
     


#Funcion que cifra el texto claro del usuario
def cifrar(key,text):
    g = int(math.sqrt(len(key)))#Grado del que es la llave
    matrizCifrado = creaMatriz(key,"Llave",g)#Se crea la matriz de Cifrado
    aux = determinante(matrizCifrado)#Se calcula el determinante de la matriz de cifrado
    aux1 = aux%27#Se calcula el determinante en modulo 27

    if verifKey(len(key)) == False:
        print("\nTu clave no genera una matriz nxn\n")
    elif len(text)%g == 1:
        print("\nLa longitud de tu texto no es multiplo de N\n")
    elif mcd(aux1,27) == 1:#Verifica si el determinante es primo con el modulo
     i = 0
     m = []#Matriz auxiliar que guarda el texto separado por  multpilos de n
     mFinal = []#Matriz que guarda los n-gramas

     #Se crea una matriz con el texto dividido en multiplos de n para los n-gramas
     while i < len(text):
         m.append(text[i:i+g])
         i+=g
    #Se crea una lista que guarda los n-gramas del texto
     for let in m:
         mFinal.append(creaMatriz(let,"Texto",g))
     
     texto_cifrado = genera(multMatriz(matrizCifrado,mFinal,g))#Se hace el proceso de cifrado y se genera el texto cifrado
     print(f"\nEl texto cifrado es: {texto_cifrado}\n") 
    else:
        print("La matriz de cifrado no tiene inversa, escoge otra clave\n")

#Funcion que descifra un texto cifrado
def descifrar(key,text):
    g = int(math.sqrt(len(key)))#Grado del que es la llave
    matrizCifrado = creaMatriz(key,"Llave",g)#Se crea la matriz de Cifrado
    det = determinante(matrizCifrado)#Se calcula el determinante de la matriz de cifrado
    detM = det%27#Se calcula el determinante en modulo 27

    if verifKey(len(key)) == False:
        print("\nTu clave no genera una matriz nxn\n")
    elif len(text)%g == 1:
        print("\nLa longitud de tu texto no es multiplo de N\n")
    elif mcd(detM,27) == 1:#Verifica si el determinante es primo con el modulo
     mCF = cofactores(matrizCifrado)#Se crea la matriz de cofactores de la matriz de cifrado
     mTR = transpuesta(mCF)#Se crea la matriz transpuesta de la matriz de cofactores
     mKF = multMatrizModulo(mTR,g,InversoModular(detM,27))#Se crea la matriz generada a partir de la matriz transpuesta multiplicada por el determinante inverso en modulo 27
     i = 0
     m = []#Matriz auxiliar que guarda el texto separado por  multpilos de n
     mFinal = []#Matriz que guarda los n-gramas
    
    #Se crea una matriz con el texto dividido en multiplos de n para los n-gramas
     while i < len(text):
         m.append(text[i:i+g])
         i+=g
    #Se crea una lista que guarda los n-gramas del texto
     for let in m:
         mFinal.append(creaMatriz(let,"Texto",g))
     
     texto_descifrado = genera(multMatriz(mKF,mFinal,g)) #Se hace el proceso de descifrado y se genera el texto descifrado
     print(f"\nEl texto descifrado es: {texto_descifrado}\n") 
    else:
        print("La matriz de cifrado no tiene inversa, verifica que tu clave sea la correcta\n")

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
        key = input("\nIngresa tu llave >> ")
        txt = input("\nIngresa tu texto a descifrar >> ")

        keyN = normaliza(key) #Normaliza llave
        textN = normaliza(txt)  # Normaliza texto

        descifrar(keyN,textN)

    elif opcionMenu == "0":
        break
    else:
        print("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
