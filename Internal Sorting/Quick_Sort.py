def quick_sort(arr):
    # Caso base: si la lista tiene 0 o 1 elemento, ya está ordenada
    if len(arr) <= 1:
        return arr

    # Elegir el pivote (usamos el último elemento de la lista)
    pivot = arr[-1]
    
    # Crear dos sublistas: una con elementos menores que el pivote
    # y otra con elementos mayores que el pivote
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursivamente ordenar las sublistas y combinar el resultado
    return quick_sort(left) + [pivot] + quick_sort(right)

# Ejemplo de uso
arr = [33, 10, 55, 71, 29, 5, 99, 14]
print("Lista original:", arr)

# Llamar al Quick Sort
sorted_arr = quick_sort(arr)

print("Lista ordenada:", sorted_arr)
