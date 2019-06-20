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
'''def paquetesCompletos(a):
    if (a in [1,2,3,4,6,7,9,11,12,14,17,19,22,27]):
        return False
    else:
        return True

z=int(input("ingresa un numero"))
print (paquetesCompletos(z))'''

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
'''import time
import random

def burbuja(arreglo):
    for d in range(len(arreglo)):
        for c in range (len(arreglo)-1):
            if (arreglo[c]>arreglo[c+1]):
                arreglo[c],arreglo[c+1]=arreglo[c+1],arreglo[c]
    return arreglo

n=2350000
a=[]
for c in range (n):
    a.append(random.randint(0,n))

inicio=time.time()
#b=burbuja(a)
b=a.sort()
fin=time.time()
print("el tiempo fue: ", fin-inicio)'''

##############################################

'''import tkinter
import tkinter.ttk as ttk

def despedir():
    #print("Adios Prras", en.get())
    if (var_chk.get()):
        print("si")
        print(combo.get())
        #en.insert(0,combo.get())
    else:
        print ("nope")
    valor=var_radio.get()
    print(nombres[valor])

ventana=tkinter.Tk()
ventana.title("IG")
et=tkinter.Label(ventana,text="Hola Mundo")
et['text']="FES Aragón"
et.pack()
bn=tkinter.Button(ventana,text="Despedir", command=despedir)
bn.pack()
en=tkinter.Entry(ventana,text="default")
en.pack()
combo=ttk.Combobox(ventana)
combo['values']=[1.2,2,3,4,5,6,7,8,9,0,"hola",'adios']
combo.pack()
var_chk=tkinter.BooleanVar()
chk=tkinter.Checkbutton(ventana,text='selecciona', variable=var_chk)
chk.pack()
nombres=["Moisés","Mónica","Sebas","Jessica","Marcelo"]
var_radio=tkinter.IntVar()
for c in range(len(nombres)):
    r=tkinter.Radiobutton(ventana,text=nombres[c],value=c, variable=var_radio)
    r.pack()
ventana.mainloop()'''

#############################################

'''suma = 0.0
for c in range(10):
    suma =suma+0.1

if(suma==1.0):
    print ("la suma es 1.0")
else:
    print ("la suma no es 1!")'''

#############################################
    
class Persona:
    nombre=""
    edad=0
    estatura=0.0
    def __init__(self,n="",e=0,est=0.0):
        self.nombre=n
        self.edad=e
        self.estatura=est

Persona1=Persona()
Persona2=Persona()
Persona1.nombre="Fulanito"
Persona1.edad=20
Persona1.estatura=1.70
Persona2.nombre="Erick"
Persona2.edad=22
Persona2.estatura=1.65
print (Persona1.nombre)

Per1=Persona("Pedro",30,1.73)
Per2=Persona("Pablo",32,1.75)
print (Per2.nombre)
print (Per1.edad)

arreglo=[]
arreglo.append(Persona("Maria",19,1.60))
arreglo.append(Persona("Carlos",21,1.68))
arreglo.append(Persona("Javier",34,1.68))
arreglo.append(Persona("Jorge",25,1.78))
arreglo.append(Persona("Manuel",22,1.68))
arreglo.append(Persona("Josue",21,1.72))
for c in arreglo:
    print (c.nombre,c.edad,c.estatura)

prueba=arreglo[1]
prueba.nombre="Julieta"
for c in arreglo:
    print (c.nombre,c.edad,c.estatura)
