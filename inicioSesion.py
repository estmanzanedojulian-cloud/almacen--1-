import flet as ft
import subprocess
import sys
import os

def main(page: ft.Page):
    page.title = "Iniciar Sesión"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#0f172a"
    page.window_width = 1200
    page.window_height = 700
    page.padding = 0

    def iniciar_sesion(e):
        if usuario.value == "admin" and contraseña.value == "1234":

            ruta_app = os.path.join(
                os.path.dirname(os.path.abspath(__file__)),
                "inventario.py"
            )

            subprocess.Popen([sys.executable, ruta_app])

            page.window.destroy()

        else:
            mensaje.value = "Usuario o contraseña incorrectos"
            mensaje.color = "red"
            page.update()

    usuario = ft.TextField(
        label="Usuario",
        width=350,
        prefix_icon=ft.Icons.PERSON,
    )

    contraseña = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=350,
        prefix_icon=ft.Icons.LOCK,
        on_submit=iniciar_sesion,
    )

    mensaje = ft.Text(size=14)

    page.add(
        ft.Container(
            expand=True,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Card(
                        elevation=20,
                        content=ft.Container(
                            width=450,
                            padding=40,
                            content=ft.Column(
                                tight=True,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Icon(
                                        ft.Icons.ACCOUNT_CIRCLE,
                                        size=100,
                                        color="#3b82f6",
                                    ),
                                    ft.Text(
                                        "Iniciar Sesión",
                                        size=30,
                                        weight=ft.FontWeight.BOLD,
                                        color="white",
                                    ),
                                    ft.Text(
                                        "Ingresa tus credenciales",
                                        color="#94a3b8",
                                    ),
                                    ft.Container(height=20),
                                    usuario,
                                    contraseña,
                                    ft.Container(height=10),
                                    mensaje,
                                    ft.ElevatedButton(
                                        "Ingresar",
                                        icon=ft.Icons.LOGIN,
                                        width=350,
                                        height=50,
                                        on_click=iniciar_sesion,
                                    ),
                                ],
                            ),
                        ),
                    )
                ],
            ),
        )
    )

ft.app(target=main)