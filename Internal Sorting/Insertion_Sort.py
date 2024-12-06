print("insert Sort")
def insertion_sort(arr):
    """
    Ordena un arreglo usando el método de Insertion Sort.

    :param arr: Lista de números a ordenar.
    :return: Lista ordenada.
    """
    # Recorremos el arreglo desde el segundo elemento (índice 1) hasta el final.
    for i in range(1, len(arr)):
        # Guardamos el valor actual que vamos a insertar en la posición correcta.
        key = arr[i]
        
        # Inicializamos j como el índice anterior al actual (i - 1).
        j = i - 1
        
        # Movemos los elementos que son mayores que 'key' una posición hacia adelante.
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Desplazamos el elemento hacia la derecha.
            j -= 1  # Avanzamos al índice anterior para seguir comparando.
        
        # Insertamos 'key' en la posición correcta dentro de los elementos ya ordenados.
        arr[j + 1] = key
    
    # Retornamos el arreglo ordenado.
    return arr

# Ejemplo de uso
lista = [5, 2, 9, 1, 5, 6]
print("Lista original:", lista)

# Ordenamos la lista usando insertion_sort.
lista_ordenada = insertion_sort(lista)
print("Lista ordenada:", lista_ordenada)
