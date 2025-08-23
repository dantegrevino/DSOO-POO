num1 = int(input("Ingrese el primer entero: "))
num2 = int(input("Ingrese el segundo entero: "))
num3 = int(input("Ingrese el tercer entero: "))
num4 = int(input("Ingrese el cuarto entero: "))
num5 = int(input("Ingrese el quinto entero: "))

lista = [num1,num2,num3,num4,num5]


max = num1
for n in lista:
    if n >= max:
        max = n
print("El valor maximo es: "+ str(max))


min = num1
for n in lista:
    if n <= min:
        min = n
print("El valor minimo es: "+ str(min))