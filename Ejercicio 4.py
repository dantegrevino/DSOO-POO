num1 = int(input("Ingrese el primer entero: "))
num2 = int(input("Ingrese el segundo entero: "))
num3 = int(input("Ingrese el tercer entero: "))
num4 = int(input("Ingrese el cuarto entero: "))
num5 = int(input("Ingrese el quinto entero: "))

lista = [num1,num2,num3,num4,num5]


m = 0
while m <= 4:
    n = m+1
    while n <= 4:
        if lista[n] == lista[m]:
            print("HAY DUPLICADOS")
            n = 5
            m = 5
        n = n+1
    m = m+1

if m == 5:
    print("SON TODOS DISTINTOS")