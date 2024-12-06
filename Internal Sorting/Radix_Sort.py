def radix_sort(arr):
    # Encontramos el valor máximo para determinar el número de dígitos
    max_value = max(arr)
    place = 1  # Comenzamos con las unidades

    # Continuamos hasta que todos los dígitos hayan sido procesados
    while max_value // place > 0:
        counting_sort(arr, place)
        place *= 10  # Pasamos al siguiente dígito (decenas, centenas, etc.)

    return arr

def counting_sort(arr, place):
    output = [0] * len(arr)
    count = [0] * 10  # Hay 10 posibles valores (0 a 9) para un dígito

    # Llenamos el arreglo de cuenta con las frecuencias de los dígitos
    for num in arr:
        index = num // place
        count[index % 10] += 1

    # Acumulamos las frecuencias
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Colocamos los números en el arreglo de salida ordenado por el dígito actual
    i = len(arr) - 1
    while i >= 0:
        num = arr[i]
        index = num // place
        output[count[index % 10] - 1] = num
        count[index % 10] -= 1
        i -= 1

    # Copiamos los resultados de vuelta al arreglo original
    for i in range(len(arr)):
        arr[i] = output[i]

# Ejemplo de uso
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Arreglo original:", arr)
sorted_arr = radix_sort(arr)
print("Arreglo ordenado:", sorted_arr)
