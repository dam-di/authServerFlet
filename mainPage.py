import ddbb
import flet as ft
from functools import partial


def main(page: ft.Page):
    page.title = "PROGRAMA WEB"

    def natigate_to(e, pageName):
        page.go(pageName)

    botonConsultas = ft.ElevatedButton(text="CONSULTAS",
                                       on_click = partial(natigate_to, pageName="/consultas"),
                                       width=300)
    botonFormulario = ft.ElevatedButton(text="FOMULARIO",
                                       on_click=partial(natigate_to, pageName="/formulario"),
                                       width=300)

    botonCron = ft.ElevatedButton(text="CRONTAB",
                                        on_click=partial(natigate_to, pageName="/crontab"),
                                        width=300)

    botonTareas = ft.ElevatedButton(text="TAREAS",
                                    on_click=partial(natigate_to, pageName="/tareas"),
                                    width=300)


    # Estructura simplificada
    columna_datos = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        width=page.width,
        height=page.height,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("ÁRBOLES", size=40),
            botonConsultas,
            botonFormulario,
            botonTareas,
            botonCron

        ]
    )

    return columna_datos
