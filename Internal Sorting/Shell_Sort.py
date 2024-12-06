def shell_sort(arr):
    n = len(arr)
    
    # Inicializar el intervalo (gap)
    gap = n // 2
    
    # Se van reduciendo los intervalos en cada iteración
    while gap > 0:
        # Realizar un Insertion Sort para el gap actual
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Mover los elementos del arreglo que son mayores que temp
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reducir el intervalo
    
    return arr

# Ejemplo de uso
arr = [34, 8, 50, 23, 3, 9, 1, 7]
print("Lista original:", arr)

sorted_arr = shell_sort(arr)

print("Lista ordenada:", sorted_arr)
