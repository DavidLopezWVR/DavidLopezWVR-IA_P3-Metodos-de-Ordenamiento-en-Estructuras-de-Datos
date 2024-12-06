def counting_sort(arr):
    # Encontrar el valor máximo en el arreglo
    max_val = max(arr)
    
    # Crear un arreglo de conteo con tamaño del valor máximo + 1
    count = [0] * (max_val + 1)
    
    # Contar la ocurrencia de cada número en el arreglo
    for num in arr:
        count[num] += 1
    
    # Reconstituir el arreglo ordenado
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])  # Agregar el número 'i' tantas veces como se haya contado
    
    return sorted_arr

# Lista de números a ordenar
arr = [4, 2, 2, 8, 3, 3, 1]

# Llamamos a la función de ordenamiento
sorted_arr = counting_sort(arr)

# Imprimimos el arreglo ordenado
print("Arreglo ordenado:", sorted_arr)
