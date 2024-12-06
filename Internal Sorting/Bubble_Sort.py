def bubble_sort(arr):
    n = len(arr)
    
    # Pasamos por todos los elementos del arreglo
    for i in range(n):
        # Últimos i elementos ya están ordenados
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente
            if arr[j] > arr[j + 1]:
                # Intercambiamos los elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
    return arr

# Lista de números a ordenar
arr = [64, 34, 25, 12, 22, 11, 90]

# Llamamos a la función de ordenamiento
sorted_arr = bubble_sort(arr)

# Imprimimos el arreglo ordenado
print("Arreglo ordenado:", sorted_arr)
