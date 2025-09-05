def media(lista):
    resultado = float(sum(lista)) / float(len(lista)) #float() because python 2
    return resultado

if __name__ == "__main__":
    numeros = list(input("Ingrese una lista de numeros: ")) #list() allows tuples: 1,2,2 e.g.
    promedio = media(numeros)
    print("La media es: "+str(promedio))