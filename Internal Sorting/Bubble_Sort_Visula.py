import flet as ft
import random
import time

# Función para realizar el Bubble Sort visual
def bubble_sort(arr, page):
    n = len(arr)
    
    # Pasamos por todos los elementos del arreglo
    for i in range(n):
        # Últimos i elementos ya están ordenados
        for j in range(0, n - i - 1):
            # Resaltamos el contenedor que estamos comparando
            arr[j].bgcolor = ft.colors.YELLOW
            arr[j + 1].bgcolor = ft.colors.YELLOW
            page.update()  # Actualizamos la página

            # Pausa para visualizar el cambio
            time.sleep(0.5)

            # Si el elemento actual es mayor que el siguiente, intercambiamos
            if int(arr[j].content.value) > int(arr[j + 1].content.value):
                arr[j].bgcolor = ft.colors.RED  # Resaltamos los contenedores que se van a intercambiar
                arr[j + 1].bgcolor = ft.colors.RED
                arr[j].content.value, arr[j + 1].content.value = arr[j + 1].content.value, arr[j].content.value
                page.update()  # Actualizamos la página
                time.sleep(0.5)  # Pausa para visualizar el intercambio

            # Restauramos el color a su valor original
            arr[j].bgcolor = ft.colors.RED
            arr[j + 1].bgcolor = ft.colors.RED
            page.update()  # Actualizamos la página

        # Resaltamos el elemento que ha sido colocado en su posición final
        arr[n - i - 1].bgcolor = ft.colors.GREEN
        page.update()  # Actualizamos la página
        time.sleep(0.5)

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

# Función principal de la aplicación
def main(page: ft.Page):
    # Crear una lista de contenedores con valores aleatorios
    arr = create_containers(10)  # Generamos 10 contenedores con valores aleatorios
    row = ft.Row(controls=arr)
    page.add(row)

    # Ejecutar el Bubble Sort visual
    bubble_sort(arr, page)

ft.app(target=main)
