import math

operacion=input("Introduce la operacion a realizar (suma,resta,multiplicacion,division,exponente,raiz): ")


def suma():
    n1 = float(input("introduce un numero: "))
    n2 = float(input("introduce el otro numero: "))
    print("El resultado de la suma es:",n1+n2) 

def resta():
    n1 = float(input("introduce un numero: "))
    n2 = float(input("introduce el otro numero: "))
    print("El resultado de la resta es:",n1-n2)
    
def multiplicacion():
    n1 = float(input("introduce numero: "))
    n2 = float(input("introduce el otro numero: "))
    print("El resultado de la multiplicacion es:",n1*n2)
    
def division():		
    n1 = float(input("introduce numero: "))
    n2 = float(input("introduce numero: "))
    print("El resultado de la division es:",n1/n2)
    
def exponente():
    n1 = float(input("introduce numero: "))
    n2 = float(input("introduce exponente: "))
    print("El resultado del exponente es:",n1**n2)
    
def raiz():
    n1 = float(input("introduce numero: "))
    print("El resultado de la raiz es:",math.sqrt(n1))

if operacion=="suma":
    suma()

if operacion=="resta":
    resta()

if operacion=="multiplicacion":
    multiplicacion()

if operacion=="division":
    division()

if operacion=="exponente":
    exponente()

if operacion=="raiz":
    raiz()
