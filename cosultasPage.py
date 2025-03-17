import ddbb
import flet as ft
import datetime




def main(page: ft.Page):
    page.title = "Consultas"


    page.update()

    page.clean()


    def cargar_tabla(datos):
        tabla.rows = []
        for fila in datos:
            tabla.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(str(fila[0]))),  # ID
                    ft.DataCell(ft.Text(fila[1])),  # Nombre
                    ft.DataCell(ft.Text(fila[2])),  # Tipo
                    ft.DataCell(ft.Text(str(fila[3]))),  # Altura
                    ft.DataCell(ft.Text(str(fila[4]))),  # Fecha Plantación
                ])
            )
        page.update()

    def buscar(e):
        datos = ddbb.obtener_arboles_by_nombre(nombre_tf.value)
        cargar_tabla(datos)

    def volver(e):
        page.go("/inicio")

    # Crear la tabla para mostrar los árboles
    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Tipo")),
            ft.DataColumn(ft.Text("Altura (m)")),
            ft.DataColumn(ft.Text("Fecha Plantación")),
        ]
    )



    nombre_tf = ft.TextField(label="Nombre", width=300)
    btn_buscar = ft.ElevatedButton("BUCAR", on_click=buscar , width=300)

    btn_volver = ft.ElevatedButton("VOLVER", on_click=volver)

    # Estructura de la página
    columna_datos = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        width=page.width,
        height=page.height,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Text("CONSULTAS DE ÁRBOLES", size=40),
            nombre_tf,
            btn_buscar,
            tabla,
            btn_volver
        ]
    )

    datos = ddbb.obtener_arboles()
    cargar_tabla(datos)

    return columna_datos