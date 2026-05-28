import flet as ft


def main(page: ft.Page):
    page.title = "Sistema de Ventas e Inventario"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 1280
    page.window_height = 760
    page.padding = 0
    page.bgcolor = "#0b1220"

    current_section = {"name": "Resumen"}

    products = [
        {"sku": "CAF-001", "name": "Cafe molido premium", "category": "Almacen", "stock": 48, "min_stock": 12, "cost": 2400, "price": 3900, "supplier": "Distribuidora Norte", "sold_today": 9},
        {"sku": "YER-014", "name": "Yerba organica 1kg", "category": "Almacen", "stock": 8, "min_stock": 15, "cost": 1900, "price": 3200, "supplier": "Campo Verde", "sold_today": 14},
        {"sku": "ACE-022", "name": "Aceite de oliva 500ml", "category": "Gourmet", "stock": 21, "min_stock": 10, "cost": 4100, "price": 6900, "supplier": "Sabores del Sur", "sold_today": 5},
        {"sku": "LIM-105", "name": "Detergente concentrado", "category": "Limpieza", "stock": 6, "min_stock": 10, "cost": 900, "price": 1600, "supplier": "LimpioMax", "sold_today": 11},
    ]

    suppliers = [
        {"name": "Distribuidora Norte", "contact": "Laura Perez", "phone": "+54 11 4321-1000", "status": "Activo"},
        {"name": "Campo Verde", "contact": "Martin Ruiz", "phone": "+54 341 555-8021", "status": "Reponer"},
        {"name": "Sabores del Sur", "contact": "Ana Gomez", "phone": "+54 299 441-0920", "status": "Activo"},
        {"name": "LimpioMax", "contact": "Sofia Diaz", "phone": "+54 351 210-7000", "status": "Activo"},
    ]

    def money(value):
        return f"${value:,.0f}".replace(",", ".")

    def sales_today():
        return sum(item["price"] * item["sold_today"] for item in products)

    def profit_today():
        return sum((item["price"] - item["cost"]) * item["sold_today"] for item in products)

    def total_units_today():
        return sum(item["sold_today"] for item in products)

    def low_stock_products():
        return [item for item in products if item["stock"] <= item["min_stock"]]

    def panel(content, padding=18, expand=False):
        return ft.Container(
            expand=expand,
            padding=padding,
            bgcolor="#111827",
            border_radius=8,
            content=content,
        )

    def status_badge(text, color):
        bg = {"#f97316": "#3a2412", "#f59e0b": "#3a2a0d", "#22c55e": "#12351f", "#60a5fa": "#132f4d"}.get(color, "#172033")
        return ft.Container(
            padding=ft.Padding(left=10, top=5, right=10, bottom=5),
            border_radius=8,
            bgcolor=bg,
            content=ft.Text(text, color=color, size=12, weight=ft.FontWeight.BOLD),
        )

    def action_button(text, icon, color, handler):
        return ft.ElevatedButton(
            text,
            icon=icon,
            on_click=handler,
            style=ft.ButtonStyle(
                bgcolor=color,
                color="#031012",
                shape=ft.RoundedRectangleBorder(radius=8),
            ),
        )

    status_text = ft.Text("", color="#5eead4", size=13)

    def show_message(message):
        status_text.value = message
        page.update()

    product_search = ft.TextField(
        hint_text="Buscar producto, SKU, categoria o proveedor",
        prefix_icon=ft.Icons.SEARCH,
        height=48,
        expand=True,
        border_radius=8,
        filled=True,
        bgcolor="#0f172a",
        border_color="#223044",
        focused_border_color="#14b8a6",
        color="#f8fafc",
        hint_style=ft.TextStyle(color="#64748b"),
    )

    sku_input = ft.TextField(label="SKU", height=46, width=130)
    name_input = ft.TextField(label="Producto", height=46, expand=True)
    category_input = ft.TextField(label="Categoria", height=46, width=150)
    stock_input = ft.TextField(label="Stock", height=46, width=100, keyboard_type=ft.KeyboardType.NUMBER)
    min_stock_input = ft.TextField(label="Minimo", height=46, width=100, keyboard_type=ft.KeyboardType.NUMBER)
    cost_input = ft.TextField(label="Costo", height=46, width=110, keyboard_type=ft.KeyboardType.NUMBER)
    price_input = ft.TextField(label="Precio", height=46, width=110, keyboard_type=ft.KeyboardType.NUMBER)
    supplier_input = ft.TextField(label="Proveedor", height=46, width=180)

    supplier_name_input = ft.TextField(label="Proveedor", height=46, expand=True)
    supplier_contact_input = ft.TextField(label="Contacto", height=46, width=180)
    supplier_phone_input = ft.TextField(label="Telefono", height=46, width=170)

    stats_row = ft.Row(spacing=14)
    sidebar_column = ft.Column(spacing=10)
    section_title = ft.Text(size=30, weight=ft.FontWeight.BOLD, color="#f8fafc")
    section_subtitle = ft.Text(color="#94a3b8", size=13)
    main_area = ft.Column(spacing=16, expand=True, scroll=ft.ScrollMode.AUTO)

    def stat_card(title, value, icon, color, subtitle):
        icon_bg = {"#14b8a6": "#103735", "#22c55e": "#12351f", "#60a5fa": "#132f4d", "#f59e0b": "#3a2a0d"}.get(color, "#182235")
        return ft.Container(
            expand=True,
            height=118,
            padding=18,
            bgcolor="#111827",
            border_radius=8,
            content=ft.Column(
                spacing=10,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text(title, size=13, color="#a7b0c0"),
                            ft.Container(width=38, height=38, border_radius=8, bgcolor=icon_bg, alignment=ft.Alignment.CENTER, content=ft.Icon(icon, color=color, size=22)),
                        ],
                    ),
                    ft.Text(value, size=28, weight=ft.FontWeight.BOLD, color="#f8fafc"),
                    ft.Text(subtitle, size=12, color="#8b97aa"),
                ],
            ),
        )

    def refresh_stats():
        stats_row.controls = [
            stat_card("Ventas del dia", money(sales_today()), ft.Icons.POINT_OF_SALE, "#14b8a6", f"{total_units_today()} unidades vendidas"),
            stat_card("Ganancia del dia", money(profit_today()), ft.Icons.TRENDING_UP, "#22c55e", "Margen calculado por producto"),
            stat_card("Productos", str(len(products)), ft.Icons.INVENTORY_2, "#60a5fa", f"{len(low_stock_products())} con stock bajo"),
            stat_card("Proveedores", str(len(suppliers)), ft.Icons.LOCAL_SHIPPING, "#f59e0b", "Contactos activos y pendientes"),
        ]

    def find_product(sku):
        return next((item for item in products if item["sku"] == sku), None)

    def sell_product(sku, qty=1):
        item = find_product(sku)
        if item is None:
            return
        if item["stock"] < qty:
            show_message(f"No hay stock suficiente para vender {item['name']}.")
            return
        item["stock"] -= qty
        item["sold_today"] += qty
        show_message(f"Venta registrada: {qty} x {item['name']}.")
        refresh_view()

    def restock_product(sku, qty=10):
        item = find_product(sku)
        if item is None:
            return
        item["stock"] += qty
        show_message(f"Stock actualizado: +{qty} unidades de {item['name']}.")
        refresh_view()

    def reduce_stock(sku, qty=1):
        item = find_product(sku)
        if item is None:
            return
        if item["stock"] <= 0:
            show_message(f"{item['name']} ya esta en cero.")
            return
        item["stock"] -= qty
        show_message(f"Ajuste aplicado: -{qty} unidad de {item['name']}.")
        refresh_view()

    def delete_product(sku):
        item = find_product(sku)
        if item is None:
            return
        products.remove(item)
        show_message(f"Producto eliminado: {item['name']}.")
        refresh_view()

    def toggle_supplier_status(name):
        supplier = next((item for item in suppliers if item["name"] == name), None)
        if supplier is None:
            return
        supplier["status"] = "Reponer" if supplier["status"] == "Activo" else "Activo"
        show_message(f"Estado actualizado para {supplier['name']}.")
        refresh_view()

    def delete_supplier(name):
        supplier = next((item for item in suppliers if item["name"] == name), None)
        if supplier is None:
            return
        suppliers.remove(supplier)
        show_message(f"Proveedor eliminado: {supplier['name']}.")
        refresh_view()

    def clear_product_inputs():
        for control in [sku_input, name_input, category_input, stock_input, min_stock_input, cost_input, price_input, supplier_input]:
            control.value = ""

    def clear_supplier_inputs():
        for control in [supplier_name_input, supplier_contact_input, supplier_phone_input]:
            control.value = ""

    def add_product(_):
        required = [sku_input, name_input, category_input, stock_input, min_stock_input, cost_input, price_input, supplier_input]
        if any(not control.value for control in required):
            show_message("Completa todos los campos del producto.")
            return
        try:
            sku = sku_input.value.strip().upper()
            if find_product(sku):
                show_message("Ya existe un producto con ese SKU.")
                return
            new_product = {
                "sku": sku,
                "name": name_input.value.strip(),
                "category": category_input.value.strip(),
                "stock": int(stock_input.value),
                "min_stock": int(min_stock_input.value),
                "cost": float(cost_input.value),
                "price": float(price_input.value),
                "supplier": supplier_input.value.strip(),
                "sold_today": 0,
            }
        except ValueError:
            show_message("Stock, minimo, costo y precio deben ser numeros.")
            return
        products.append(new_product)
        if not any(item["name"].lower() == new_product["supplier"].lower() for item in suppliers):
            suppliers.append({"name": new_product["supplier"], "contact": "Sin asignar", "phone": "-", "status": "Activo"})
        clear_product_inputs()
        show_message("Producto agregado correctamente.")
        refresh_view()

    def add_supplier(_):
        if not supplier_name_input.value or not supplier_contact_input.value:
            show_message("Completa nombre y contacto del proveedor.")
            return
        name = supplier_name_input.value.strip()
        if any(item["name"].lower() == name.lower() for item in suppliers):
            show_message("Ya existe un proveedor con ese nombre.")
            return
        suppliers.append({"name": name, "contact": supplier_contact_input.value.strip(), "phone": supplier_phone_input.value.strip() or "-", "status": "Activo"})
        clear_supplier_inputs()
        show_message("Proveedor agregado correctamente.")
        refresh_view()

    def product_rows():
        query = product_search.value.strip().lower() if product_search.value else ""
        visible = [
            item for item in products
            if query in " ".join([item["sku"], item["name"], item["category"], item["supplier"]]).lower()
        ]
        return [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(item["sku"], color="#dbeafe")),
                    ft.DataCell(ft.Text(item["name"], color="#f8fafc")),
                    ft.DataCell(ft.Text(item["category"], color="#cbd5e1")),
                    ft.DataCell(ft.Text(str(item["stock"]), color="#f87171" if item["stock"] <= item["min_stock"] else "#f8fafc")),
                    ft.DataCell(ft.Text(money(item["price"]), color="#f8fafc")),
                    ft.DataCell(ft.Text(item["supplier"], color="#cbd5e1")),
                    ft.DataCell(ft.Text(str(item["sold_today"]), color="#5eead4")),
                    ft.DataCell(
                        ft.Row(
                            spacing=6,
                            controls=[
                                ft.IconButton(icon=ft.Icons.POINT_OF_SALE, icon_color="#5eead4", tooltip="Vender 1", on_click=lambda e, sku=item["sku"]: sell_product(sku)),
                                ft.IconButton(icon=ft.Icons.ADD_BOX, icon_color="#93c5fd", tooltip="Sumar stock", on_click=lambda e, sku=item["sku"]: restock_product(sku)),
                                ft.IconButton(icon=ft.Icons.DELETE, icon_color="#f87171", tooltip="Eliminar", on_click=lambda e, sku=item["sku"]: delete_product(sku)),
                            ],
                        )
                    ),
                ]
            )
            for item in visible
        ]

    def inventory_rows():
        rows = []
        for item in sorted(products, key=lambda product: product["stock"] - product["min_stock"]):
            is_low = item["stock"] <= item["min_stock"]
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(item["name"], color="#f8fafc")),
                        ft.DataCell(ft.Text(str(item["stock"]), color="#f87171" if is_low else "#f8fafc")),
                        ft.DataCell(ft.Text(str(item["min_stock"]), color="#cbd5e1")),
                        ft.DataCell(status_badge("Stock bajo" if is_low else "Correcto", "#f97316" if is_low else "#22c55e")),
                        ft.DataCell(
                            ft.Row(
                                spacing=6,
                                controls=[
                                    ft.IconButton(icon=ft.Icons.ADD, icon_color="#5eead4", tooltip="Reponer 10", on_click=lambda e, sku=item["sku"]: restock_product(sku, 10)),
                                    ft.IconButton(icon=ft.Icons.REMOVE, icon_color="#fbbf24", tooltip="Ajustar -1", on_click=lambda e, sku=item["sku"]: reduce_stock(sku, 1)),
                                ],
                            )
                        ),
                    ]
                )
            )
        return rows

    def supplier_rows():
        return [
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(item["name"], color="#f8fafc")),
                    ft.DataCell(ft.Text(item["contact"], color="#cbd5e1")),
                    ft.DataCell(ft.Text(item["phone"], color="#cbd5e1")),
                    ft.DataCell(status_badge(item["status"], "#f59e0b" if item["status"] == "Reponer" else "#22c55e")),
                    ft.DataCell(
                        ft.Row(
                            spacing=6,
                            controls=[
                                ft.IconButton(icon=ft.Icons.SWAP_HORIZ, icon_color="#93c5fd", tooltip="Cambiar estado", on_click=lambda e, name=item["name"]: toggle_supplier_status(name)),
                                ft.IconButton(icon=ft.Icons.DELETE, icon_color="#f87171", tooltip="Eliminar", on_click=lambda e, name=item["name"]: delete_supplier(name)),
                            ],
                        )
                    ),
                ]
            )
            for item in suppliers
        ]

    def make_product_table():
        return ft.DataTable(
            bgcolor="#111827",
            border_radius=8,
            heading_row_color="#182235",
            column_spacing=20,
            columns=[
                ft.DataColumn(ft.Text("SKU", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Producto", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Categoria", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Stock", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Precio", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Proveedor", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Vendido hoy", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Acciones", color="#cbd5e1")),
            ],
            rows=product_rows(),
        )

    def make_inventory_table():
        return ft.DataTable(
            bgcolor="#111827",
            border_radius=8,
            heading_row_color="#182235",
            column_spacing=24,
            columns=[
                ft.DataColumn(ft.Text("Producto", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Stock actual", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Stock minimo", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Estado", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Acciones", color="#cbd5e1")),
            ],
            rows=inventory_rows(),
        )

    def make_supplier_table():
        return ft.DataTable(
            bgcolor="#111827",
            border_radius=8,
            heading_row_color="#182235",
            column_spacing=28,
            columns=[
                ft.DataColumn(ft.Text("Proveedor", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Contacto", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Telefono", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Estado", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Acciones", color="#cbd5e1")),
            ],
            rows=supplier_rows(),
        )

    def add_product_form():
        return panel(
            ft.Column(
                spacing=12,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("Agregar producto", size=18, weight=ft.FontWeight.BOLD, color="#f8fafc"),
                            action_button("Guardar", ft.Icons.ADD, "#14b8a6", add_product),
                        ],
                    ),
                    ft.Row(spacing=10, wrap=True, controls=[sku_input, name_input, category_input, stock_input, min_stock_input, cost_input, price_input, supplier_input]),
                ],
            )
        )

    def add_supplier_form():
        return panel(
            ft.Column(
                spacing=12,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Text("Agregar proveedor", size=18, weight=ft.FontWeight.BOLD, color="#f8fafc"),
                            action_button("Guardar", ft.Icons.PERSON_ADD, "#60a5fa", add_supplier),
                        ],
                    ),
                    ft.Row(spacing=10, wrap=True, controls=[supplier_name_input, supplier_contact_input, supplier_phone_input]),
                ],
            )
        )

    def alert_cards():
        low_items = low_stock_products()
        if not low_items:
            return [ft.Text("No hay alertas de inventario.", color="#94a3b8")]
        cards = []
        for item in low_items:
            needed = item["min_stock"] - item["stock"] + 1
            cards.append(
                ft.Container(
                    padding=12,
                    border_radius=8,
                    bgcolor="#2a1f12",
                    content=ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            ft.Column(
                                spacing=2,
                                controls=[
                                    ft.Text(item["name"], color="#fff7ed", weight=ft.FontWeight.BOLD),
                                    ft.Text(f"Stock {item['stock']} / minimo {item['min_stock']}", color="#fdba74", size=12),
                                ],
                            ),
                            ft.IconButton(icon=ft.Icons.ADD_SHOPPING_CART, icon_color="#fed7aa", tooltip=f"Reponer +{needed}", on_click=lambda e, sku=item["sku"], qty=needed: restock_product(sku, qty)),
                        ],
                    ),
                )
            )
        return cards

    def report_rows():
        rows = []
        for item in sorted(products, key=lambda product: product["sold_today"], reverse=True):
            revenue = item["price"] * item["sold_today"]
            profit = (item["price"] - item["cost"]) * item["sold_today"]
            rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(item["name"], color="#f8fafc")),
                        ft.DataCell(ft.Text(str(item["sold_today"]), color="#5eead4")),
                        ft.DataCell(ft.Text(money(revenue), color="#f8fafc")),
                        ft.DataCell(ft.Text(money(profit), color="#22c55e")),
                    ]
                )
            )
        return rows

    def make_reports_table():
        return ft.DataTable(
            bgcolor="#111827",
            border_radius=8,
            heading_row_color="#182235",
            column_spacing=34,
            columns=[
                ft.DataColumn(ft.Text("Producto", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Unidades", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Ventas", color="#cbd5e1")),
                ft.DataColumn(ft.Text("Ganancia", color="#cbd5e1")),
            ],
            rows=report_rows(),
        )

    def build_resumen():
        return [
            stats_row,
            ft.Row(
                spacing=16,
                vertical_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    panel(
                        ft.Column(
                            spacing=14,
                            controls=[
                                ft.Text("Productos con mas ventas hoy", size=18, weight=ft.FontWeight.BOLD, color="#f8fafc"),
                                make_reports_table(),
                            ],
                        ),
                        expand=True,
                    ),
                    ft.Container(
                        width=330,
                        content=panel(
                            ft.Column(spacing=14, controls=[ft.Text("Alertas de inventario", size=18, weight=ft.FontWeight.BOLD, color="#f8fafc")] + alert_cards())
                        ),
                    ),
                ],
            ),
        ]

    def build_productos():
        return [
            add_product_form(),
            panel(
                ft.Column(
                    spacing=14,
                    controls=[
                        ft.Row(controls=[product_search]),
                        ft.Column(scroll=ft.ScrollMode.AUTO, controls=[make_product_table()]),
                    ],
                )
            ),
        ]

    def build_inventario():
        return [
            panel(
                ft.Column(
                    spacing=14,
                    controls=[
                        ft.Text("Gestion de inventario", size=18, weight=ft.FontWeight.BOLD, color="#f8fafc"),
                        ft.Text("Usa + para reponer 10 unidades y - para ajustar stock manualmente.", color="#94a3b8", size=13),
                        ft.Column(scroll=ft.ScrollMode.AUTO, controls=[make_inventory_table()]),
                    ],
                )
            )
        ]

    def build_proveedores():
        return [
            add_supplier_form(),
            panel(ft.Column(spacing=14, controls=[ft.Text("Proveedores", size=18, weight=ft.FontWeight.BOLD, color="#f8fafc"), make_supplier_table()]))
        ]

    def build_reportes():
        return [
            stats_row,
            panel(
                ft.Column(
                    spacing=14,
                    controls=[
                        ft.Text("Reporte del dia", size=18, weight=ft.FontWeight.BOLD, color="#f8fafc"),
                        ft.Text(f"Total ganado hoy: {money(profit_today())} | Total vendido: {money(sales_today())}", color="#94a3b8", size=13),
                        make_reports_table(),
                    ],
                )
            ),
        ]

    sections = {
        "Resumen": {"icon": ft.Icons.DASHBOARD, "subtitle": "Vista general de caja, ventas y alertas", "builder": build_resumen},
        "Productos": {"icon": ft.Icons.INVENTORY_2, "subtitle": "Listado, busqueda, venta y alta de productos", "builder": build_productos},
        "Inventario": {"icon": ft.Icons.WAREHOUSE, "subtitle": "Reposicion, ajustes y estado de stock", "builder": build_inventario},
        "Proveedores": {"icon": ft.Icons.LOCAL_SHIPPING, "subtitle": "Contactos, estado y alta de proveedores", "builder": build_proveedores},
        "Reportes": {"icon": ft.Icons.ANALYTICS, "subtitle": "Ventas y ganancias calculadas del dia", "builder": build_reportes},
    }

    def sidebar_item(section_name):
        selected = current_section["name"] == section_name
        meta = sections[section_name]
        return ft.Container(
            height=46,
            padding=ft.Padding(left=12, top=0, right=12, bottom=0),
            border_radius=8,
            bgcolor="#1f2937" if selected else "transparent",
            on_click=lambda e, name=section_name: change_section(name),
            content=ft.Row(
                spacing=12,
                controls=[
                    ft.Icon(meta["icon"], color="#5eead4" if selected else "#cbd5e1", size=20),
                    ft.Text(section_name, color="#f8fafc" if selected else "#cbd5e1", size=14),
                ],
            ),
        )

    def rebuild_sidebar():
        sidebar_column.controls = [
            ft.Text("Mi Sistema", size=25, weight=ft.FontWeight.BOLD, color="#f8fafc"),
            ft.Text("Ventas e inventario", size=12, color="#7dd3fc"),
            ft.Divider(color="#223044", height=26),
        ]
        sidebar_column.controls.extend([sidebar_item(name) for name in sections])
        sidebar_column.controls.extend([
            ft.Container(expand=True),
            panel(
                ft.Column(
                    spacing=6,
                    controls=[
                        ft.Text("Caja abierta", color="#f8fafc", weight=ft.FontWeight.BOLD),
                        ft.Text(f"Ventas: {money(sales_today())}", color="#94a3b8", size=12),
                        ft.Text(f"Ganancia: {money(profit_today())}", color="#5eead4", size=12),
                    ],
                ),
                padding=14,
            ),
        ])

    def change_section(name):
        current_section["name"] = name
        refresh_view()

    def refresh_view():
        refresh_stats()
        section = sections[current_section["name"]]
        section_title.value = current_section["name"]
        section_subtitle.value = section["subtitle"]
        main_area.controls = section["builder"]()
        rebuild_sidebar()
        page.update()

    product_search.on_change = lambda _: refresh_view()

    header = ft.Row(
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=[
            ft.Column(spacing=4, controls=[section_title, section_subtitle]),
            ft.Row(
                spacing=10,
                controls=[
                    status_text,
                    ft.IconButton(icon=ft.Icons.NOTIFICATIONS, icon_color="#cbd5e1", bgcolor="#111827", tooltip="Ver alertas", on_click=lambda e: change_section("Inventario")),
                    ft.CircleAvatar(content=ft.Text("A", color="#031012"), bgcolor="#5eead4"),
                ],
            ),
        ],
    )

    sidebar = ft.Container(
        width=250,
        bgcolor="#0a0f1c",
        padding=22,
        content=sidebar_column,
    )

    content = ft.Container(
        expand=True,
        padding=26,
        content=ft.Column(spacing=18, controls=[header, main_area]),
    )

    page.add(ft.Row(expand=True, spacing=0, controls=[sidebar, content]))
    refresh_view()


ft.app(target=main)
