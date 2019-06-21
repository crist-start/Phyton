#for c in range(100000):
#    print (c," ",bin(c)," ",oct(c)," ",hex(c))

'''Personal={"Homero":"Rodrigo","Maggie":"Vania","Bart":"Andres"}
print(Personal["Homero"])
print(Personal.keys())

llaves=Personal.keys()

for k in llaves:
    print(k,"será interpretado por",Personal[k])'''

##########################################################
'''#forma 1
dato=int(input("ingrese un dato"))
for c in range(dato):
    a=""
    for d in range (c+1):
        a+="*"
    print(a)

ast="*"

#forma 2
for c in range(dato):
    print(c+1,"*"*(c+1))'''

##########################################################

'''a=0
try:
    b=3/a
    print(b)
except ZeroDivisionError:
    print ("division por 0")

try:
    a=int(input("ingresa un numero"))
except ValueError:
    print("ingresaste un caracter no valido")'''

#########################################################

import math

a=math.cos(45*math.pi/180)
print(a)
print(math.pi)
print(math.e)
print(math.degrees(1))
print(math.factorial(9))
b=math.cos(math.radians(45))
print(math.tau)
