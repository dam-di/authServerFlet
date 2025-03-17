import flet as ft
import crontabService

import datetime

def main(page: ft.Page):
    page.title = "PROGRAMA WEB"

    # Función para cerrar el diálogo
    def close_dialog(e):
        dialog.open = False
        page.update()

    # Función para abrir el diálogo
    def open_dialog(mensaje):
        dialog.content = ft.Text(mensaje)
        dialog.open = True
        page.update()


    def abrir_selector_fecha(e):
        dp.open = True
        page.update()

    def seleccionar_fecha(e):
        if dp.value:  # Asegurar que se ha seleccionado una fecha
            txt_fecha.value = f"Fecha: {dp.value.day}/{dp.value.month}/{dp.value.year}"
        else:
            txt_fecha.value = "No se seleccionó ninguna fecha."

        page.update()

    def abrir_selector_hora(e):
        tp.open = True
        page.update()

    def seleccionar_hora(e):
        txt_hora.value = f"Hora seleccionada: {tp.value}"
        page.update()

    def get_minutos():
        # Crear una lista vacía para almacenar los objetos Option
        lista_minutos = []

        # Recorrer los valores del 1 al 59 (incluido)
        for i in range(1, 60):
            # Convertir el número en string para mostrarlo correctamente en el dropdown
            minuto_str = str(i).zfill(2)

            # Crear un objeto Option con el valor convertido
            opcion = ft.dropdown.Option(text=minuto_str, key=minuto_str)

            # Agregar la opción a la lista
            lista_minutos.append(opcion)

        # Retornar la lista completa de opciones
        return lista_minutos

    def get_hora():
        # Crear una lista vacía para almacenar los objetos Option
        lista_horas = []

        # Recorrer los valores del 1 al 59 (incluido)
        for i in range(0, 24):
            # Convertir el número en string para mostrarlo correctamente en el dropdown
            hora_str = str(i).zfill(2)

            # Crear un objeto Option con el valor convertido
            opcion = ft.dropdown.Option(text=hora_str, key=hora_str)

            # Agregar la opción a la lista
            lista_horas.append(opcion)

        # Retornar la lista completa de opciones
        return lista_horas

    def obtener_valores(e):
        hora = hora_drop.value
        minuto = minuto_drop.value
        dia = dp.value.day
        mes = dp.value.month
        evento = evento_tf.value

        mensaje = None
        if(hora is None):
            mensaje = "Debes seleccionar una hora"
        elif minuto is None:
            mensaje = "Debes indicar un minuto"
        elif evento is None:
            mensaje = "Indica un evento"
        if mensaje is not None:
            open_dialog(mensaje)
            return



        print(f"hora: {hora}, minuto: {minuto}, dia: {dia}, mes: {mes}, evento: {evento}")

        ok_crear = crontabService.crear_tarea(minuto, hora, dia, mes, evento)
        if(ok_crear):
            #ddbb.insertar_tarea(hora, minuto, dia, mes, "lunes" ,evento)
            open_dialog("Tarea creada con éxito")


    # Crear el contenedor con el texto dentro
    contenedor = ft.Container(
        padding=20,
        bgcolor=ft.Colors.BLACK,
        border_radius=20,
        width=page.width,
        height=page.height)  # Centra horizontal y verticalmente

    # Campos
    hora_drop = ft.Dropdown(label="Hora", options=get_hora(), max_menu_height=200, width=300,
                              border_color=ft.Colors.WHITE)
    #hora_tf = ft.TextField(label="Hora", hint_text="Please enter text here",border_color=ft.Colors.WHITE)
    #minuto_tf = ft.TextField(label="Minuto", icon=ft.Icons.LOCK_CLOCK, border_color=ft.Colors.WHITE)
    minuto_drop = ft.Dropdown(label="Minuto", options=get_minutos(), max_menu_height=200, width=300, border_color=ft.Colors.WHITE)
    dia_tf = ft.TextField(label="Día", border_color=ft.Colors.WHITE)
    mes_tf = ft.TextField(label="Mes", border_color=ft.Colors.WHITE)
    evento_tf = ft.TextField(label="Evento (descripción)", border_color=ft.Colors.WHITE)
    boton = ft.ElevatedButton("CREAR", on_click=obtener_valores, width=300)
    btn_hora = ft.ElevatedButton("Seleccionar Hora", on_click=abrir_selector_hora)
    txt_hora = ft.Text()
    tp = ft.TimePicker(on_change=seleccionar_hora)

    dp = ft.DatePicker(on_change=seleccionar_fecha, value=datetime.datetime.now())
    txt_fecha = ft.Text(f"Fecha: {dp.value.day}/{dp.value.month}/{dp.value.year}")
    btn_fecha = ft.ElevatedButton("Seleccionar Fecha", on_click=abrir_selector_fecha, animate_size=True)


    # Crear el AlertDialog
    dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Info"),
        content=ft.Text("Tarea creada con éxito"),
        actions=[
            ft.TextButton("Cerrar", on_click=close_dialog),
        ],
    )




    fila1 = ft.Row(alignment=ft.MainAxisAlignment.CENTER)

    fila_fecha = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,  # Centrar los elementos
        controls=[
            txt_fecha,  # Etiqueta de fecha
            btn_fecha  # Botón de selección de fecha
        ]
    )

    columna_datos = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        width=300,
        controls = [
            ft.Text("TAREAS CRON", size=40),
            hora_drop,
            minuto_drop,
            # dia_tf,
            # mes_tf,
            evento_tf,
            fila_fecha,
            boton
        ]
    )


    fila1.controls.append(columna_datos)
    #fila1.controls.append(columna_datos2)
    contenedor.content = fila1

    page.overlay.append(dp)
    page.overlay.append(dialog)
    return contenedor
