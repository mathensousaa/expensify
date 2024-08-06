import flet as ft


def main_view():
    return ft.Column(
        [
            ft.Text("Expensify - Gerenciador de Gastos"),
            ft.ElevatedButton("Adicionar Despesa", on_click=add_expense_view),
        ]
    )


def add_expense_view(e):
    # Logic to display add expense form
    pass
