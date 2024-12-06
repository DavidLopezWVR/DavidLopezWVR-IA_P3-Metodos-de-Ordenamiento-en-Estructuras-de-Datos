def heapify(arr, n, i):
    largest = i  # Inicializamos el índice del mayor valor como la raíz
    left = 2 * i + 1  # Índice del hijo izquierdo
    right = 2 * i + 2  # Índice del hijo derecho

    # Verificamos si el hijo izquierdo es mayor que la raíz
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Verificamos si el hijo derecho es mayor que el mayor encontrado hasta ahora
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el mayor no es la raíz, intercambiamos y volvemos a aplicar heapify en el subárbol afectado
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Intercambiar
        heapify(arr, n, largest)  # Recursión para el subárbol afectado

def heap_sort(arr):
    n = len(arr)

    # Construimos un heap (reorganizamos el arreglo en un heap máximo)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraemos los elementos del heap uno a uno
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiamos la raíz del heap con el último elemento
        heapify(arr, i, 0)  # Aplicamos heapify en el heap reducido

# Ejemplo de uso
arr = [12, 11, 13, 5, 6, 7]
print("Lista original:", arr)

# Llamar a Heap Sort
heap_sort(arr)

print("Lista ordenada:", arr)
