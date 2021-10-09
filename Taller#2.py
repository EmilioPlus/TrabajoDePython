

#Que mostrara el siguente ejercicio...
'''def fred():
    print("Zap")
def jane():
    print("ABC")


jane()
fred()
jane()'''


#Escriba un programa que pida la anchura y altura...
'''anchura = int(input("Anchura del rectángulo: "))
altura = int(input("Altura del rectángulo: "))

for i in range(altura):
    for j in range(anchura):
        print("* ", end="")
    print()'''

#Escriba un programa que pida la anchura de un triángulo y lo dibuje.
'''anchuraTrian = int(input("Anchura del triangulo: "))

for i in range(1, anchuraTrian + 1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(1, anchuraTrian):
    for j in range(anchuraTrian - i):
        print("*", end="")
    print()'''

#Solicitar al usuario que ingrese su dirección email...
'''def validar(email):
    CaracteraBuscar="@"
    emailValido=False
    for Eml in email:
        if Eml==CaracteraBuscar:
        return True
    return False

#programa principal
Email=input("Ingrese su email: ")
if validar(Email):
    print("El Email es corecto")
else:
    print("El Email es incorrecto")'''

#Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar...
'''def sumaDigitos(Numero):
    suma=0
    while Numero!=0:
        digito=Numero%10
        suma=suma+digito
        Numero=Numero//10
    return suma

#programa principal
Sumar=0
num=int(input("Numero a digitar: "))
while num!=0:
    print("Suma:",sumaDigitos(num))
    Sumar=Sumar+num
    num=int(input("Numero a digitar: "))
print("Sumatoria:", Sumar)
print("Dígitos:", sumaDigitos(Sumar))'''


'''from Funciones import *

#programa principal 
num=int(input("Numero: ")) 
un_digito=int(input("Dígito: "))
print("Frecuencia del dígito en el numero:",frecuencia(num,un_digito))'''

#Escribir una función que calcule el total de una factura tras aplicarle el IVA....
'''def invoice(amount, vat=21):#Función que aplica el IVA a una factura. Parametros, 
    #amount: Es la cantidad sin IVA, vat: Es el porcentaje de IVA, 
    # Devuelve el total de la factura una vez aplicado el IVA.
    return amount + amount*vat/100

print(invoice(25411,10))
print(invoice(13568))'''

#Escribir un programa que pregunte al usuario su nombre, edad, dirección...
'''Nombre = input("¿Como te llamas? ")
Edad = input("¿Cuantos años tienes?")
Direccion = input("¿Cuál es tu dirección?")
Telefono = input("¿Cuál es tu número de teléfono?")
persona = {"nombre": Nombre, "edad": Edad, "direccion": Direccion, "telefono": Telefono}
print(persona["nombre"], "tiene", persona["edad"], "años, vive en",
persona["direccion"], "y su numero de teléfono es", persona["telefono"])'''

'''#Escribir una función que calcule el máximo común divisor de dos números y otra 
#que calcule el mínimo común múltiplo.
def mcd(a, b):
	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a

# solicitamos los dos números
Num1 = int(input("Ingrese el primer numero: "))
Num2 = int(input("Ingrese el segundo numero: "))

print("El maximo común divisor de ", Num1," y ", Num2," es ", mcd(Num1, Num2))

#segundo ejercicio Minimo comun multiplo
def maximo_comun_divisor(a, b):
    temporal = 0
    while b != 0:
        temporal = b
        b = a % b
        a = temporal
    return a


def minimo_comun_multiplo(a, b):
    return (a * b) / maximo_comun_divisor(a, b)


a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))

mcm = minimo_comun_multiplo(a, b)
print(f"El minimo comun multiplo de {a} y {b} es {mcm}")'''


#Escribir un programa que almacene el diccionario con los créditos de las...
'''Curso = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
Credito = 0
for materia, creditos in Curso.items():
    print(materia, 'Solo Tiene', creditos, 'Créditos')
    Credito += creditos
print("")
print("Total de créditos del curso: " + str(Credito))'''

#Escribir un programa que almacene las asignaturas de un curso: por ejemplo...
'''Calculo = ["Calculo", "Física", "Química", "Istoria", "Lenguas estrangeras"]
for i in Calculo:
    print(f"Mis estudios son: {i}")'''

# Escribir un programa que pregunte al usuario los números ganadores de la...
'''NumeroGanador = []
for i in range(6):
    NumeroGanador.append(int(input("Introduce un numero ganador: ")))
NumeroGanador.sort()
print("Los numeros ganadores son: " + str(NumeroGanador))'''

# Escribir un programa que pida al usuario una palabra y muestre por pantalla si...
'''equal = 0 
alreves = 0
word = input("Digite la palabra: ")
for i in reversed(range(0, len(word))):
    if word[i].lower() == word[alreves].lower():
        equal += 1
    alreves += 1
    if len(word) == equal:
        print("Es palindromo!")
else:
    print("No es palindromo!")'''


