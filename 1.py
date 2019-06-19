'''a=1
for c in range (10,0,-1):
    print (c)
    a=a*2
print(a)'''


'''for c in "Marcelo":
    print (c)'''

'''a=[4,4,3,7,8]

for c in a:
    print(c)'''

'''a=int(input("ingresa un numero en a: "))
b=int(input("ingresa un numero en b: "))
c=int(input("ingresa un numero en c: "))'''


'''if(a>b):
    if (a>c):
        print("a es mayor")
    else:
        print("c es mayor")
elif (b>c):
   print ("b es mayor")
else:
    print("c es el mayor")

def doble (a):
    return a*2
print (doble(2))
print (doble(3.5))
print (doble("hola"))'''

##############################################

'''def mayor2(v1,v2):
    if(v1>v2):
        return v1
    else:
        return v2

def mayor3(a,b,c):
    return mayor2(mayor2(a,b),c)

a=int(input("escribe un numero"))
b=int(input("escribe otro numero"))
c=int(input("escribe otro numero"))
print(mayor3(a,b,c))'''


#############################################
def paquetesCompletos(a):
    if (a in [1,2,3,4,6,7,9,11,12,14,17,19,22,27]):
        return False
    else:
        return True

z=int(input("ingresa un numero"))
print (paquetesCompletos(z))

#############################################

'''def factorial(n,v=False):
    fact =1
    for c in range (n):
        fact*=(c+1)
        if (v):
            print("resultado parcial :",fact)
    return fact

print(factorial(6,True))'''

#############################################

'''def factorialRecu(n):
    print("el valor de n:",n)
    if(n==0):
        return 1
    else:
        return (n*factorialRecu(n-1))

print (factorialRecu(6))'''

#############################################

'''def isPalindrome(cadena):
    if((len(cadena)==0) or len(cadena)==1):
        return True
    elif (cadena[0]==cadena[-1]) and isPalindrome(cadena[1:-1]):
        return True
    else:
        return False'''

'''def isPalindrome(cadena):
    return cadena==cadena[::-1]

print (isPalindrome("radar"))
print(isPalindrome("ana"))
print(isPalindrome("a"))
print(isPalindrome("oso"))
print (isPalindrome("true"))'''

############################################

def burbuja(arreglo):
    for d in range(len(arreglo)):
        for c in range (len(arreglo)-1):
            if (arreglo[c]>arreglo[c+1]):
                arreglo[c],arreglo[c+1]=arreglo[c+1],arreglo[c]
    return arreglo

arreglo=[1,9,4,7,8,2,5,6,3]
ordenado=burbuja(arreglo)
print (ordenado)
