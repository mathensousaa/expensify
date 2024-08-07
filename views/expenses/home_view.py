import flet as ft

from controllers.expense_controller import add_expense
from . import styles


def home_view(page: ft.Page):

    def on_add_expense_click(e):
        page.views.append(add_expense_view(page))
        page.update()

    return ft.View(
        "/",
        [
            ft.Text("Expensify - Gerenciador de Gastos", style="headline4"),
            ft.ElevatedButton("Adicionar Despesa", on_click=on_add_expense_click),
        ],
    )


def add_expense_view(page: ft.Page):
    def on_back_click(e):
        page.views.pop()
        page.update()

    return ft.View(
        "/add_expense",
        [
            ft.AppBar(
                title=ft.Text("Adicionar Despesa"),
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=on_back_click),
            ),
            ft.TextField(label="Descrição"),
            ft.TextField(label="Valor", keyboard_type=ft.KeyboardType.NUMBER),
            ft.TextField(label="Data", keyboard_type=ft.KeyboardType.DATETIME),
            ft.ElevatedButton("Salvar", on_click=lambda e: add_expense()),
        ],
    )


def main(page: ft.Page):
    page.title = "Expensify"

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(home_view(page))
        elif page.route == "/add_expense":
            page.views.append(add_expense_view(page))
        page.update()

    def view_pop(view):
        page.views.pop()
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)
        else:
            page.go("/")

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(target=main)
