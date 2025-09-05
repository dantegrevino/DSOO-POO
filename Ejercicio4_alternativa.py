lista = []

for i in range(5):
    j=i+1
    num = int(input("Ingrese el "+str(j)+"-esimo entero: "))
    lista.append(num)

if len(lista) != len(set(lista)):
    print("HAY DUPLICADOS")
else:
    print("SON TODOS DISTINTOS")