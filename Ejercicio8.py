def cuadrados(lista):
    for i in range(len(lista)):
        lista[i] = lista[i]**2
    return lista

if __name__ == "__main__":
    numeros = list(input("Ingrese una lista de numeros: "))
    resultado = cuadrados(numeros)
    print("La lista de cuadrados es: "+str(resultado))