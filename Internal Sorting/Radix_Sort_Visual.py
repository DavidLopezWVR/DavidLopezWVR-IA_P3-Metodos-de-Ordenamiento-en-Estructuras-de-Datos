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

    # Función para realizar el Radix Sort visual
    def radix_sort(arr_values, page):
        max_value = max(arr_values)  # Encontramos el valor máximo para determinar el número de dígitos
        place = 1  # Comenzamos con el primer dígito (las unidades)

        # Continuamos hasta que todos los dígitos hayan sido procesados
        while max_value // place > 0:
            counting_sort(arr_values, place, page)  # Ordenamos según el lugar actual (unidades, decenas, etc.)
            place *= 10  # Pasamos al siguiente dígito (decenas, centenas, etc.)

    # Función para realizar el Counting Sort de acuerdo a un dígito específico
    def counting_sort(arr_values, place, page):
        output = [0] * len(arr_values)
        count = [0] * 10  # Hay 10 posibles valores (0 a 9) para un dígito

        # Llenamos el arreglo de cuenta con las frecuencias de los dígitos
        for num in arr_values:
            index = num // place
            count[index % 10] += 1

        # Acumulamos las frecuencias
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Colocamos los números en el arreglo de salida ordenado por el dígito actual
        i = len(arr_values) - 1
        while i >= 0:
            num = arr_values[i]
            index = num // place
            output[count[index % 10] - 1] = num
            count[index % 10] -= 1
            i -= 1

        # Copiamos los resultados de vuelta al arreglo original
        for i in range(len(arr_values)):
            arr_values[i] = output[i]

        # Actualizamos los contenedores visualmente paso a paso
        update_containers(arr_values, page, place)

    # Función para actualizar los contenedores visualmente
    def update_containers(sorted_values, page, place):
        page.add(ft.Text(f"Ordenando por el lugar: {place}", size=20))  # Mostrar el lugar (unidades, decenas, etc.)
        for i, value in enumerate(sorted_values):
            arr[i].content.value = str(value)  # Actualizamos el valor
            if value % (place * 10) == 0:  # Resaltamos en naranja el contenedor que estamos ordenando
                arr[i].bgcolor = ft.colors.ORANGE
            else:
                arr[i].bgcolor = ft.colors.RED  # Volvemos a poner los demás contenedores en rojo
        page.update()
        time.sleep(2)

    # Iniciar el Radix Sort visualmente
    radix_sort(arr_values, page)

ft.app(target=main)
