import os

import flet as ft
import cosultasPage
import formularioPage
import mainPage
import crontabPage


def main(page: ft.Page):
    page.title = "Aplicación con Páginas en Flet"

    #page.theme_mode = ft.ThemeMode.LIGHT

    # Imagen de fondo
    fondo = ft.Image(
        src="https://4.bp.blogspot.com/-E7bPPfQVr0w/T8bOZC8-XpI/AAAAAAAAeYI/lguz3krSlQk/s1600/Bosque-de-Pinos-Paisajes-Naturales-en-HD.jpg",  # Cambia esto por la ruta de tu imagen
        width=page.width,
        height=page.height,
        fit=ft.ImageFit.COVER,  # Ajusta la imagen para cubrir el espacio
    )

    def route_change(e):
        page.views.clear()  # Limpia las vistas antes de cargar la nueva

        if page.route == "/formulario":
            page.views.append(
                ft.View(
                    route="/formulario",
                    controls=[
                        ft.Stack(
                            [
                                fondo,  # Imagen de fondo
                                formularioPage.main(page)  # Contenido encima del fondo
                            ],
                            width=page.width,
                            height=page.height,
                        )
                    ]
                )
            )
        elif page.route == "/consultas":
            page.views.append(
                ft.View(
                    route="/consultas",
                    controls=[cosultasPage.main(page)]
                )
            )
        elif page.route == "/crontab":
            page.views.append(
                ft.View(
                    route="/crontab",
                    controls=[crontabPage.main(page)]
                )
            )
        elif page.route == "/inicio":
            page.views.append(
                ft.View(
                    route="/inicio",
                    controls=[ft.Stack(
                            [
                                fondo,  # Imagen de fondo
                                mainPage.main(page)  # Contenido encima del fondo
                            ],
                            width=page.width,
                            height=page.height,
                        )]
                )
            )
        else:
            page.go("/formulario")  # Página por defecto

        page.update()  # Importante actualizar la UI

    page.on_route_change = route_change
    page.go("/inicio")  # Carga la primera página automáticamente

if __name__ == '__main__':
    ft.app(target=main, view=ft.WEB_BROWSER, port=8000)
