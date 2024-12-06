import flet as ft   # Importamos el framework Flet para la interfaz gráfica
import random       # Importamos la librería random
import time         # Importamos la librería time

def main(page: ft.Page):  # Función principal que genera la ventana
    # Función para crear los contenedores
    def create_containers(number):
        container_list = []  # Lista para almacenar los contenedores
        for _ in range(number):  
            container_list.append(
                ft.Container(
                    content=ft.Text(value=random.randint(1, 100)),  # Número aleatorio entre 1 y 100
                    alignment=ft.alignment.center,  # Número centrado en el contenedor
                    width=75,  # Ancho del contenedor
                    height=75,  # Altura del contenedor
                    bgcolor=ft.colors.RED,  # Color inicial rojo
                    border_radius=50,  # Bordes redondeados
                )
            )
        return container_list

    # Crear y agregar una fila con 10 contenedores
    row = ft.Row(controls=create_containers(10))
    page.add(row)

    time.sleep(1)  # Pausa inicial para que los contenedores se muestren

    arr = row.controls  # Obtenemos los contenedores como un arreglo

    # Lógica de Insertion Sort
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Contenedor actual
        key_value = int(key.content.value)  # Valor del contenedor actual
        key.bgcolor = ft.colors.ORANGE  # Resaltar el contenedor actual en naranja
        page.update()
        time.sleep(0.5)

        j = i - 1
        # Comparación y movimiento de elementos mayores
        while j >= 0 and key_value < int(arr[j].content.value):
            arr[j].bgcolor = ft.colors.YELLOW  # Resaltar el contenedor comparado en amarillo
            page.update()
            time.sleep(0.5)

            arr[j + 1].content.value = arr[j].content.value  # Mover el valor al contenedor siguiente
            arr[j + 1].bgcolor = ft.colors.BLUE  # Resaltar el movimiento con azul
            page.update()
            time.sleep(0.5)

            arr[j + 1].bgcolor = ft.colors.RED  # Restaurar color original
            arr[j].bgcolor = ft.colors.RED  # Restaurar color original
            j -= 1

        # Insertar el valor en su posición correcta
        arr[j + 1].content.value = key_value
        arr[j + 1].bgcolor = ft.colors.GREEN  # Resaltar como ordenado en verde
        page.update()
        time.sleep(0.5)

    # Finalizar resaltando todos los elementos en verde
    for container in arr:
        container.bgcolor = ft.colors.GREEN
    page.update()
    time.sleep(0.5)

ft.app(target=main)  # Ejecutar la aplicación


