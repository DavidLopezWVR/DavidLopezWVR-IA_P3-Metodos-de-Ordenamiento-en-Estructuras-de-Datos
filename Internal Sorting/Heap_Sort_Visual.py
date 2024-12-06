import flet as ft
import random
import time

# Función para "heapificar" el arreglo
def heapify(arr, n, i, page):
    largest = i  # Inicializamos el índice del mayor valor como la raíz
    left = 2 * i + 1  # Índice del hijo izquierdo
    right = 2 * i + 2  # Índice del hijo derecho

    # Verificamos si el hijo izquierdo es mayor que la raíz
    if left < n and arr[left].content.value > arr[largest].content.value:
        largest = left

    # Verificamos si el hijo derecho es mayor que el mayor encontrado hasta ahora
    if right < n and arr[right].content.value > arr[largest].content.value:
        largest = right

    # Si el mayor no es la raíz, intercambiamos y volvemos a aplicar heapify en el subárbol afectado
    if largest != i:
        arr[i].bgcolor = ft.colors.YELLOW  # Resaltamos el nodo raíz
        arr[largest].bgcolor = ft.colors.YELLOW  # Resaltamos el hijo mayor
        page.update()  # Actualizamos la visualización
        time.sleep(1)  # Pausa para ver los cambios

        # Intercambiamos los elementos
        arr[i].content.value, arr[largest].content.value = arr[largest].content.value, arr[i].content.value
        arr[i].bgcolor = ft.colors.RED  # Resaltamos el intercambio
        arr[largest].bgcolor = ft.colors.RED
        page.update()  # Actualizamos la visualización

        # Llamamos recursivamente para seguir manteniendo la propiedad de heap en el subárbol afectado
        heapify(arr, n, largest, page)

# Función para ordenar el arreglo utilizando Heap Sort
def heap_sort(arr, page):
    n = len(arr)

    # Construir un heap máximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, page)

    # Extraer elementos del heap uno por uno
    for i in range(n - 1, 0, -1):
        arr[i].bgcolor = ft.colors.GREEN  # Resaltamos el nodo ya ordenado
        page.update()  # Actualizamos la visualización
        time.sleep(1)

        # Intercambiamos el primer nodo (máximo) con el último nodo no ordenado
        arr[i].content.value, arr[0].content.value = arr[0].content.value, arr[i].content.value
        arr[0].bgcolor = ft.colors.RED  # Resaltamos la raíz durante el intercambio
        page.update()  # Actualizamos la visualización

        # Aplicamos heapify para restaurar la propiedad de heap en el subárbol
        heapify(arr, i, 0, page)

# Función principal de la aplicación
def main(page: ft.Page):
    # Crear una lista de contenedores con valores aleatorios
    def create_containers(number):
        container_list = []
        for _ in range(number):
            container_list.append(
                ft.Container(
                    content=ft.Text(value=str(random.randint(1, 100))),  # Números aleatorios entre 1 y 100
                    alignment=ft.alignment.center,
                    width=75,
                    height=75,
                    bgcolor=ft.colors.RED,
                    border_radius=50,
                )
            )
        return container_list

    # Crear una fila con los contenedores
    arr = create_containers(10)  # Generamos 10 contenedores con valores aleatorios
    row = ft.Row(controls=arr)
    page.add(row)

    # Ejecutar el Heap Sort visual
    heap_sort(arr, page)

ft.app(target=main)

