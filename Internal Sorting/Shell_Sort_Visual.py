import flet as ft
import random
import time

# Función para realizar el Shell Sort visual
def shell_sort(arr, page):
    n = len(arr)
    
    # Inicializar el intervalo (gap)
    gap = n // 2
    
    # Se van reduciendo los intervalos en cada iteración
    while gap > 0:
        # Realizar un Insertion Sort para el gap actual
        for i in range(gap, n):
            temp = int(arr[i].content.value)
            j = i
            # Resaltar el elemento que se está comparando
            arr[i].bgcolor = ft.colors.ORANGE
            arr[j].bgcolor = ft.colors.ORANGE
            page.update()
            time.sleep(0.5)
            
            # Mover los elementos del arreglo que son mayores que temp
            while j >= gap and int(arr[j - gap].content.value) > temp:
                arr[j].content.value = arr[j - gap].content.value
                arr[j].bgcolor = ft.colors.RED  # Resaltamos el elemento movido
                arr[j - gap].bgcolor = ft.colors.RED  # Resaltamos el elemento reemplazado
                page.update()
                time.sleep(0.5)
                j -= gap
            arr[j].content.value = str(temp)
            arr[j].bgcolor = ft.colors.GREEN  # Resaltamos el elemento insertado correctamente
            page.update()
            time.sleep(0.5)
        
        gap //= 2  # Reducir el intervalo (gap)
    
    return arr

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
    arr = create_containers(10)  # Generamos 10 contenedores con valores aleatorios entre 1 y 100
    row = ft.Row(controls=arr)
    page.add(row)

    # Ejecutar el Shell Sort visual
    shell_sort(arr, page)

ft.app(target=main)
