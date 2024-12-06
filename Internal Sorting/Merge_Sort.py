def merge_sort(arr):
    # Si el arreglo tiene un solo elemento o está vacío, ya está ordenado
    if len(arr) <= 1:
        return arr

    # Dividir el arreglo en dos mitades
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])  # Recursión en la mitad izquierda
    right = merge_sort(arr[mid:])  # Recursión en la mitad derecha

    # Fusionar las dos mitades ordenadas
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Mezclar los dos arreglos en orden ascendente
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Si quedan elementos en la mitad izquierda
    result.extend(left[i:])
    # Si quedan elementos en la mitad derecha
    result.extend(right[j:])
    
    return result

# Definir un arreglo de ejemplo
arr = [64, 25, 12, 22, 11]

print("Arreglo original:", arr)

# Realizamos el Merge Sort y mostramos los pasos
sorted_arr = merge_sort(arr)

print("Arreglo ordenado:", sorted_arr)
