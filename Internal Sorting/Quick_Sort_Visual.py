import flet as ft
import random
import time

def main(page: ft.Page):
    # Función para crear los contenedores con números aleatorios
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

    # Crear la fila de contenedores
    row = ft.Row(controls=create_containers(10))
    page.add(row)

    time.sleep(1)

    arr = row.controls  # Obtenemos los contenedores como un arreglo
    arr_values = [int(container.content.value) for container in arr]  # Lista de los valores

    # Función para realizar el Quick Sort visual
    def quick_sort(arr_values, low, high, page):
        if low < high:
            # Obtener la partición del arreglo
            pi = partition(arr_values, low, high, page)

            # Recursión para ordenar las dos particiones
            quick_sort(arr_values, low, pi - 1, page)  # Ordenar la partición izquierda
            quick_sort(arr_values, pi + 1, high, page)  # Ordenar la partición derecha

    # Función para realizar la partición
    def partition(arr_values, low, high, page):
        pivot = arr_values[high]  # Seleccionamos el último elemento como pivote
        i = low - 1  # Índice para el menor elemento

        # Resaltamos el pivote en amarillo
        arr[high].bgcolor = ft.colors.YELLOW
        update_containers(arr_values, page, "Pivote: {}".format(pivot))
        page.update()  # Forzamos la actualización de la página
        time.sleep(2)  # Esperamos 2 segundos para que se vea el pivote resaltado

        # Mover los elementos menores que el pivote a la izquierda
        for j in range(low, high):
            if arr_values[j] < pivot:
                i += 1
                arr_values[i], arr_values[j] = arr_values[j], arr_values[i]  # Intercambio

                # Actualizamos los contenedores visualmente después de cada intercambio
                update_containers(arr_values, page, "Intercambiando: {} con {}".format(arr_values[i], arr_values[j]))
                page.update()
                time.sleep(1)

        # Intercambiamos el pivote con el elemento en la posición correcta
        arr_values[i + 1], arr_values[high] = arr_values[high], arr_values[i + 1]
        update_containers(arr_values, page, "Intercambiando pivote con: {}".format(arr_values[i + 1]))
        page.update()
        time.sleep(1)

        # Restauramos el color de fondo de los contenedores a rojo después de la partición
        arr[high].bgcolor = ft.colors.RED

        return i + 1

    # Función para actualizar los contenedores visualmente
    def update_containers(sorted_values, page, message=""):
        page.controls.clear()
        page.add(ft.Text(message, size=20))  # Mostrar el mensaje de estado
        row = ft.Row(controls=create_containers_from_values(sorted_values))  # Crear los contenedores
        page.add(row)
        page.update()

    # Crear los contenedores de acuerdo con los valores ordenados
    def create_containers_from_values(values):
        container_list = []
        for value in values:
            container_list.append(
                ft.Container(
                    content=ft.Text(value=str(value)),
                    alignment=ft.alignment.center,
                    width=75,
                    height=75,
                    bgcolor=ft.colors.RED,  # Se pone rojo inicialmente
                    border_radius=50,
                )
            )
        return container_list

    # Iniciar el Quick Sort visualmente
    quick_sort(arr_values, 0, len(arr_values) - 1, page)

ft.app(target=main)



