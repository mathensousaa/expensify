import flet as ft
from datetime import datetime
from controllers.expense_controller import (
    add_expense,
    get_all_expenses,
    update_expense,
    delete_expense,
)


<<<<<<< HEAD
def home_view(page: ft.Page):
=======
def all_expenses_view(page: ft.Page):
    expenses = get_all_expenses()

    def on_edit_expense_click(expense_id):
        page.views.append(edit_expense_view(page, expense_id, refresh_expenses))
        page.update()

    def on_delete_expense_click(expense_id):
        delete_expense(expense_id)
        refresh_expenses()

    def refresh_expenses():
        nonlocal expenses
        expenses = get_all_expenses()
        page.views[-1] = all_expenses_view(page)
        page.update()

    expense_items = [
        ft.Card(
            content=ft.Container(
                width=500,
                content=ft.Column(
                    [
                        ft.ListTile(
                            title=ft.Text(expense.description),
                            subtitle=ft.Text(
                                f"Valor: R${expense.amount} - Data: {expense.date.strftime('%d/%m/%Y')}"
                            ),
                            trailing=ft.Container(
                                width=100,  
                                padding=ft.padding.all(0),
                                content=ft.Row(
                                    controls=[
                                        ft.IconButton(
                                            icon=ft.icons.EDIT,
                                            on_click=lambda e: on_edit_expense_click(
                                                expense.id
                                            ),
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            on_click=lambda e: on_delete_expense_click(
                                                expense.id
                                            ),
                                        ),
                                    ],
                                    alignment=ft.MainAxisAlignment.END, 
                                    spacing=10, 
                                ),
                            ),
                        )
                    ],
                    spacing=0,
                ),
                padding=ft.padding.symmetric(vertical=10),
            )
        )
        for expense in expenses
    ]
>>>>>>> 38d4e101e645b397b90a79d766a97f51e1ccafd9

    def on_add_expense_click(e):
        page.views.append(add_expense_view(page, refresh_expenses))
        page.update()

    return ft.View(
        "/",
        [
            ft.AppBar(title=ft.Text("Expensify - Gerenciador de Gastos")),
            ft.ElevatedButton("Adicionar Despesa", on_click=on_add_expense_click),
            ft.Container(
                content=ft.Column(
                    controls=expense_items,
                    spacing=10,
                ),
                expand=True,
            ),
        ],
    )


def add_expense_view(page: ft.Page, on_success):
    description_input = ft.TextField(label="Descrição")
    amount_input = ft.TextField(label="Valor", keyboard_type=ft.KeyboardType.NUMBER)
    date_input = ft.TextField(label="Data", keyboard_type=ft.KeyboardType.DATETIME)

    def on_back_click(e):
        page.views.pop()
        page.update()

    def on_save_click(e):
        description = description_input.value
        try:
            amount = float(amount_input.value)
        except ValueError:
            snack_bar = ft.SnackBar(ft.Text("Valor inválido!"))
            page.open(snack_bar)
            return

        date_str = date_input.value
        try:
            date = datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            snack_bar = ft.SnackBar(ft.Text("Data inválida!"))
            page.open(snack_bar)
            return

        add_expense(description, amount, date)

        description_input.value = ""
        amount_input.value = ""
        date_input.value = ""

        page.views.pop()
        page.update()
        on_success()
        page.go("/")

    return ft.View(
        "/page4",
        [
            ft.AppBar(
                title=ft.Text("Adicionar Despesa"),
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=on_back_click),
            ),
            ft.Column(
                controls=[
                    description_input,
                    amount_input,
                    date_input,
                    ft.ElevatedButton("Salvar", on_click=on_save_click),
                ],
                spacing=10,
                expand=True,
            ),
        ],
    )


def edit_expense_view(page: ft.Page, expense_id: int, on_save_success):
    expense = next((exp for exp in get_all_expenses() if exp.id == expense_id), None)
    if not expense:
        return ft.View("/error", [ft.Text("Despesa não encontrada")])

    description_input = ft.TextField(label="Descrição", value=expense.description)
    amount_input = ft.TextField(
        label="Valor", value=str(expense.amount), keyboard_type=ft.KeyboardType.NUMBER
    )
    date_input = ft.TextField(label="Data", value=expense.date.strftime("%d/%m/%Y"))

    def on_back_click(e):
        page.views.pop()
        page.update()

    def on_save_click(e):
        description = description_input.value
        try:
            amount = float(amount_input.value)
        except ValueError:
            snack_bar = ft.SnackBar(ft.Text("Valor inválido!"))
            page.open(snack_bar)
            return

        date_str = date_input.value
        try:
            date = datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            snack_bar = ft.SnackBar(ft.Text("Data inválida!"))
            page.open(snack_bar)
            return

        updated_expense = update_expense(expense_id, description, amount, date)
        if updated_expense:
            page.views.pop()
            page.update()
            on_save_success()
        else:
            snack_bar = ft.SnackBar(ft.Text("Erro ao atualizar despesa!"))
            page.open(snack_bar)

    return ft.View(
        "/page5",
        [
            ft.AppBar(
                title=ft.Text("Editar Despesa"),
                leading=ft.IconButton(icon=ft.icons.ARROW_BACK, on_click=on_back_click),
            ),
            ft.Column(
                controls=[
                    description_input,
                    amount_input,
                    date_input,
                    ft.ElevatedButton("Salvar", on_click=on_save_click),
                ],
                spacing=10,
                expand=True,
            ),
        ],
    )
