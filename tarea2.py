def sumar_positivos(numeros):
    """
    Suma únicamente los valores positivos de una lista.
    """
    total = 0
    for num in numeros:
        if num > 0:
            total += num
    return total



entrada = input("Ingresa varios números separados por espacio: ")
numeros = []


for valor in entrada.split():
    if valor.lstrip('-').isdigit():  
        numeros.append(int(valor))
    else:
        print(f"'{valor}' no es un número válido. Solo se aceptan números.")
        exit()  

# Calcular suma de positivos
resultado = sumar_positivos(numeros)
print("La suma de los números positivos es:", resultado)