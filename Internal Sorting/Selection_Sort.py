def selection_sort(arr):
    # Recorrer todos los elementos del arreglo
    for i in range(len(arr)):
        min_index = i  # Inicializamos el índice del valor más pequeño
        print(f"Paso {i+1}: Buscar el valor mínimo en el arreglo")

        # Encuentra el elemento más pequeño en el arreglo
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j  # Actualizamos el índice del valor más pequeño
        
        # Intercambiar el valor mínimo con el valor en la posición i
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(f"Intercambiamos {arr[i]} y {arr[min_index]}")
        print(f"Arreglo en este paso: {arr}")

    return arr

# Definir un arreglo
arr = [64, 25, 12, 22, 11]

print("Arreglo original:", arr)
# Llamamos a la función de ordenamiento
sorted_arr = selection_sort(arr)
print("Arreglo ordenado:", sorted_arr)
