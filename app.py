import flet as ft

def main(page: ft.Page):
    # CONFIGURACIÓN GENERAL
    page.title = "Dashboard Moderno"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1200
    page.window_height = 700
    page.padding = 0
    page.bgcolor = "#0f172a"

    # SIDEBAR
    sidebar = ft.Container(
        width=250,
        bgcolor="#111827",
        padding=20,
        content=ft.Column(
            controls=[
                ft.Text(
                    "Mi Sistema",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color="white",
                ),

                ft.Divider(color="#374151"),

                ft.ListTile(
                    leading=ft.Icon(ft.Icons.DASHBOARD, color="white"),
                    title=ft.Text("Dashboard", color="white"),
                ),

                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PEOPLE, color="white"),
                    title=ft.Text("Usuarios", color="white"),
                ),

                ft.ListTile(
                    leading=ft.Icon(ft.Icons.SETTINGS, color="white"),
                    title=ft.Text("Configuración", color="white"),
                ),

                ft.ListTile(
                    leading=ft.Icon(ft.Icons.ANALYTICS, color="white"),
                    title=ft.Text("Reportes", color="white"),
                ),
            ]
        )
    )

    # TARJETA MODERNA
    def stat_card(title, value, icon, color):
        return ft.Container(
            width=250,
            height=140,
            border_radius=20,
            padding=20,
            bgcolor="#1e293b",
            content=ft.Column(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(
                                title,
                                size=16,
                                color="#94a3b8"
                            ),

                            ft.Icon(
                                icon,
                                color=color,
                                size=30
                            )
                        ]
                    ),

                    ft.Text(
                        value,
                        size=34,
                        weight=ft.FontWeight.BOLD,
                        color="white"
                    )
                ]
            )
        )

    # HEADER
    header = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            ft.Text(
                "Dashboard",
                size=32,
                weight=ft.FontWeight.BOLD,
                color="white"
            ),

            ft.Row(
                controls=[
                    ft.IconButton(
                        icon=ft.Icons.NOTIFICATIONS,
                        icon_color="white"
                    ),

                    ft.CircleAvatar(
                        content=ft.Text("A"),
                        bgcolor="blue"
                    )
                ]
            )
        ]
    )

    # INPUT MODERNO
    search_box = ft.TextField(
        hint_text="Buscar...",
        width=400,
        border_radius=15,
        filled=True,
        bgcolor="#1e293b",
        border_color="transparent",
        color="white",
    )

    # BOTÓN MODERNO
    modern_button = ft.ElevatedButton(
        "Agregar Usuario",
        icon=ft.Icons.ADD,
        style=ft.ButtonStyle(
            bgcolor="#2563eb",
            color="white",
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=15)
        )
    )

    # TABLA SIMPLE
    table = ft.DataTable(
        bgcolor="#1e293b",
        border_radius=15,
        columns=[
            ft.DataColumn(ft.Text("Usuario", color="white")),
            ft.DataColumn(ft.Text("Rol", color="white")),
            ft.DataColumn(ft.Text("Estado", color="white")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("Juan", color="white")),
                    ft.DataCell(ft.Text("Admin", color="white")),
                    ft.DataCell(ft.Text("Activo", color="green")),
                ]
            ),

            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text("María", color="white")),
                    ft.DataCell(ft.Text("Editor", color="white")),
                    ft.DataCell(ft.Text("Offline", color="red")),
                ]
            ),
        ]
    )

    # CONTENIDO PRINCIPAL
    content = ft.Container(
        expand=True,
        padding=30,
        content=ft.Column(
            controls=[

                header,

                ft.Container(height=20),

                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        search_box,
                        modern_button
                    ]
                ),

                ft.Container(height=30),

                ft.Row(
                    spacing=20,
                    controls=[
                        stat_card(
                            "Usuarios",
                            "1,245",
                            ft.Icons.PEOPLE,
                            "#3b82f6"
                        ),

                        stat_card(
                            "Ventas",
                            "$12K",
                            ft.Icons.ATTACH_MONEY,
                            "#10b981"
                        ),

                        stat_card(
                            "Pedidos",
                            "320",
                            ft.Icons.SHOPPING_CART,
                            "#f59e0b"
                        ),
                    ]
                ),

                ft.Container(height=30),

                ft.Text(
                    "Usuarios recientes",
                    size=22,
                    weight=ft.FontWeight.BOLD,
                    color="white"
                ),

                ft.Container(height=15),

                table
            ]
        )
    )

    # LAYOUT GENERAL
    page.add(
        ft.Row(
            expand=True,
            spacing=0,
            controls=[
                sidebar,
                content
            ]
        )
    )

ft.app(target=main)