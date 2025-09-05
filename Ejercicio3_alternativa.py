
lista = []

for i in range(5):
    num = int(input("Ingrese un entero: "))
    lista.append(num)


min = min(lista)
max = max(lista)

print("El valor minimo es: "+ str(min))
print("El valor maximo es: "+ str(max))