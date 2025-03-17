import ddbb
import flet as ft
import datetime


def main(page: ft.Page):
    page.title = "PROGRAMA WEB"

    def menu(e):
        page.go("/inicio")

    def crear_arbol(e):
        nombre = nombre_tf.value
        tipo = tipos_drop.value
        altura = altura_tf.value
        fecha = dp.value

        ddbb.insertar_arbol(nombre, tipo, altura, fecha)

    def abrir_selector_fecha(e):
        dp.open = True
        page.update()

    def seleccionar_fecha(e):
        txt_fecha.value = f"Fecha: {str(dp.value.day).zfill(2)}/{str(dp.value.month).zfill(2)}/{dp.value.year}"
        page.update()

    def get_tipos():
        # Crear una lista vacía para almacenar los objetos Option
        lista_tipos = []
        lista_tipos.append(ft.dropdown.Option(text="Perenne", key="Perenne"))
        lista_tipos.append(ft.dropdown.Option(text="Caduca", key="Caduca"))

        return lista_tipos

    # Declarar objetos
    nombre_tf = ft.TextField(label="Nombre", width=300, bgcolor="black")
    altura_tf = ft.TextField(label="Altura", width=300, bgcolor="black")
    tipos_drop = ft.Dropdown(label="Tipo", options=get_tipos(), max_menu_height=200, width=300,
                             border_color=ft.Colors.WHITE,
                             bgcolor=ft.Colors.BLACK, fill_color=ft.Colors.BLACK, filled=True,
                             color=ft.Colors.GREY, focused_bgcolor=ft.Colors.RED,

                             focused_color=ft.Colors.BLUE)

    dp = ft.DatePicker(on_change=seleccionar_fecha, value=datetime.datetime.now())
    txt_fecha = ft.Text(f"Fecha: {str(dp.value.day).zfill(2)}"
                        f"/{str(dp.value.month).zfill(2)}"
                        f"/{str(dp.value.year).zfill(2)}", bgcolor="black")
    btn_fecha = ft.FilledButton("Seleccionar Fecha", on_click=abrir_selector_fecha, width=300)

    btn_crear = ft.FilledButton("Crear Arbol", on_click=crear_arbol, width=300)

    btn_papge2 = ft.FilledButton("VOLVER", on_click=menu, width=300)
    # Estructura simplificada
    columna_datos = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        width=page.width,
        height=page.height,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("ÁRBOLES", size=40),
            nombre_tf,
            altura_tf,
            tipos_drop,
            txt_fecha,
            btn_fecha,
            btn_crear,
            btn_papge2

        ]
    )


    page.overlay.append(dp)
    # Agregar la columna directamente a la página
    #page.add(columna_datos)

    return columna_datos

