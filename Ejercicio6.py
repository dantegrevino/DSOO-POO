from Ejercicio5 import segundos
#def segundos(hor, min, seg):
#    resultado = seg + min*60 + hor*3600
#    return resultado

def segundos_inversa(segs):
    hor = segs // 3600
    min = (segs % 3600) // 60
    seg = segs % 60
    return hor,min,seg

h1 = int(input("Ingrese la cantidad de horas del primer intervalo: "))
m1 = int(input("Ingrese la cantidad de minutos del primer intervalo: "))
s1 = int(input("Ingrese la cantidad de segundos del primer intervalo: "))

h2 = int(input("Ingrese la cantidad de horas del segundo intervalo: "))
m2 = int(input("Ingrese la cantidad de minutos del segundo intervalo: "))
s2 = int(input("Ingrese la cantidad de segundos del segundo intervalo: "))


h, m, s = segundos_inversa( segundos(h1,m1,s1) + segundos(h2,m2,s2) )

print("La suma es: " +str(h)+" horas, "+str(m)+" minutos, "+str(s)+" segundos")
