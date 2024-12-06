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

    # Función para realizar el merge sort
    def merge_sort(arr_values, page):
        if len(arr_values) <= 1:
            return arr_values

        # Dividir el arreglo
        mid = len(arr_values) // 2
        left = merge_sort(arr_values[:mid], page)
        right = merge_sort(arr_values[mid:], page)

        # Mezclar los arreglos
        return merge(left, right, page)

    def merge(left, right, page):
        result = []
        i = j = 0

        # Resaltamos los dos subarreglos antes de la fusión
        highlight_containers(left, right, page)
        
        # Fusionar dos listas ordenadas
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Agregar el resto de los elementos si quedan
        result.extend(left[i:])
        result.extend(right[j:])
        
        # Mostrar el estado actualizado
        update_containers(result, page)
        time.sleep(1)
        return result

    # Función para resaltar los contenedores mientras se fusionan
    def highlight_containers(left, right, page):
        # Resaltamos los contenedores correspondientes a las listas izquierda y derecha
        for container in arr:
            value = int(container.content.value)
            if value in left or value in right:
                container.bgcolor = ft.colors.YELLOW  # Resaltamos en amarillo
            else:
                container.bgcolor = ft.colors.RED  # Restablecemos a rojo

        page.update()
        time.sleep(1)  # Pausa para visualizar el resaltado

    # Función para actualizar los contenedores visualmente
    def update_containers(sorted_values, page):
        for i, value in enumerate(sorted_values):
            arr[i].content.value = str(value)  # Actualizamos el valor
            arr[i].bgcolor = ft.colors.GREEN  # Resaltamos en verde el valor ordenado
        page.update()

    # Ordenar visualmente paso a paso
    def visual_merge_sort(arr_values, page):
        sorted_values = merge_sort(arr_values, page)  # Realizar el merge sort
        update_containers(sorted_values, page)  # Actualizar la interfaz visualmente

    visual_merge_sort(arr_values, page)

ft.app(target=main)

