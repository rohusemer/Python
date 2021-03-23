#TEMA: Funciones cónicas
    #Encontrar las dimensiones de los tirantes de un puente
    #conociendo la geometríaparabólica que este tiene

    #Si sabemos que el cable superior tiene forma parabólica,
    #conocemos la altura de las dos torres yde uno de los tirantes,
    #y sabemos que la distancia de torre a torre es de 120 m, con distanciasentre tirantes iguales,
    #¿cuál sería la altura para cada uno de los tirantes que se encuentran entrelas dos torres?

Y = ax^2 + bx + c       #Como el cable superior es de forma parabólica
L = Dt / Nt+1           #Separación entre tirantes:

I=0

for l in  L:
    Dt = 120
    Nt = 14
    print(L)
while I<4 :
    A = int(input("Igrese distacia "))
    B = int(input("Igrese Altura "))
    if A==0 && B==20:
        for x in Y:
            print("constante c",B)
            I++



A_ = int(input("Ingrese numero"))
for i in range(A):
    if (A%i)==0 && A<1:
        print("No primo")
    if (A%i)!= 0 && A==2:
	print("Es Primo")