import flet as ft
import random
import time

# Función para realizar el Counting Sort visual
def counting_sort(arr, page):
    # Encontrar el valor máximo en el arreglo
    max_val = max(arr, key=lambda container: int(container.content.value))
    max_val = int(max_val.content.value)  # Convertimos el valor máximo a entero

    # Crear un arreglo de conteo con tamaño del valor máximo + 1
    count = [0] * (max_val + 1)
    
    # Contar la ocurrencia de cada número en el arreglo
    for container in arr:
        num = int(container.content.value)
        count[num] += 1

    # Resaltamos el arreglo de conteo en la interfaz
    count_bars = []
    for i in range(len(count)):
        count_bars.append(
            ft.Container(
                content=ft.Text(value=str(count[i])),
                alignment=ft.alignment.center,
                width=50,
                height=75,
                bgcolor=ft.colors.BLUE,
                border_radius=5,
            )
        )
    row_bars = ft.Row(controls=count_bars)
    page.add(row_bars)

    # Pausa para visualizar el arreglo de conteo
    time.sleep(1)
    page.update()

    # Reconstruir el arreglo ordenado
    sorted_arr = []
    for i in range(len(count)):
        for _ in range(count[i]):
            sorted_arr.append(i)

    # Actualizar los contenedores con los valores ordenados
    for i, container in enumerate(arr):
        container.content.value = str(sorted_arr[i])
        container.bgcolor = ft.colors.GREEN  # Resaltamos en verde los valores ordenados
        page.update()
        time.sleep(0.5)  # Pausa para visualizar el cambio

# Función para crear los contenedores con números aleatorios
def create_containers(number):
    container_list = []
    for _ in range(number):
        container_list.append(
            ft.Container(
                content=ft.Text(value=str(random.randint(1, 10))),  # Números aleatorios entre 1 y 10
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

    # Ejecutar el Counting Sort visual
    counting_sort(arr, page)

ft.app(target=main)
