# MB6-Tarea 2 - TDD

## Historia
Esta función suma únicamente los números positivos de una lista.

## Código mínimo
def sumar_positivos(numeros):
    total = 0
    for num in numeros:
        if num > 0:
            total += num
    return total