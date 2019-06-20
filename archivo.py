'''arch=open('prueba'.txt,"w")
arch.write("prueba")
arch.close'''

#################################

class Persona:
    nombre=""
    edad=0
    estatura=0.0
    def __init__(self,n="",e=0,est=0.0):
        self.nombre=n
        self.edad=e
        self.estatura=est

arreglo=[]

arch=open('prueba.txt',"r")
'''for r in arch:
    print (r)
arch.close()'''
for r in arch:
    datos=r.split(",")
    if (len(datos)==3):
        arreglo.append(Persona(datos[0],int(datos[1]),float(datos[2])))
    
for c in arreglo:
    print(c.nombre,c.edad,c.estatura)
arch.close()

mayor=0

for e in arreglo:
    if e.edad>mayor:
        mayor=e.edad
        registro=e
print ("la mayor persona es ",registro.nombre, "y tiene una edad de ",registro.edad)
