import flet as ft
import random
import time

def main(page: ft.Page):
    # Función para crear los contenedores
    def create_containers(number):
        container_list = []
        for _ in range(number):
            container_list.append(
                ft.Container(
                    content=ft.Text(value=random.randint(1, 100)),  # Número aleatorio entre 1 y 100
                    alignment=ft.alignment.center,  # Alinear texto al centro
                    width=75,  # Ancho del contenedor
                    height=75,  # Altura del contenedor
                    bgcolor=ft.colors.RED,  # Color inicial rojo
                    border_radius=50,  # Bordes redondeados
                )
            )
        return container_list

    # Crear y agregar una fila de contenedores
    row = ft.Row(controls=create_containers(10))
    page.add(row)

    time.sleep(1)  # Pausa inicial para que los contenedores se muestren

    arr = row.controls  # Obtenemos los contenedores como un arreglo

    # Lógica del Selection Sort
    n = len(arr)
    for i in range(n):
        # Encontrar el índice del elemento más pequeño
        min_index = i
        arr[min_index].bgcolor = ft.colors.ORANGE  # Resaltar el valor mínimo inicial
        page.update()
        time.sleep(0.5)

        for j in range(i + 1, n):
            arr[j].bgcolor = ft.colors.YELLOW  # Resaltar el elemento que se compara
            page.update()
            time.sleep(0.5)

            if int(arr[j].content.value) < int(arr[min_index].content.value):
                # Restaurar el color del elemento anterior más pequeño
                arr[min_index].bgcolor = ft.colors.RED if min_index != i else ft.colors.ORANGE
                min_index = j
                arr[min_index].bgcolor = ft.colors.BLUE  # Resaltar el nuevo mínimo
                page.update()
                time.sleep(0.5)

            arr[j].bgcolor = ft.colors.RED  # Restaurar color después de comparar
            page.update()

        # Intercambiar el elemento más pequeño con el elemento inicial
        if min_index != i:
            arr[min_index].bgcolor = ft.colors.GREEN  # Resaltar el intercambio
            arr[i].bgcolor = ft.colors.GREEN

            # Intercambio visual
            arr[min_index].content.value, arr[i].content.value = (
                arr[i].content.value,
                arr[min_index].content.value,
            )
            page.update()
            time.sleep(0.5)

        # Marcar el elemento ordenado como verde
        arr[i].bgcolor = ft.colors.GREEN
        page.update()

    # Finalizar resaltando todos los elementos en verde
    for container in arr:
        container.bgcolor = ft.colors.GREEN
    page.update()
    time.sleep(0.5)

ft.app(target=main)
