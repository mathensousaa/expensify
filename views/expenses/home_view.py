import flet as ft
from datetime import datetime
from controllers.expense_controller import (
    add_expense,
    get_all_expenses,
    update_expense,
    delete_expense,
)

USER_ID = 1  # Define user_id as 1


def all_expenses_view(page: ft.Page):
    expenses = get_all_expenses(USER_ID)

    def on_edit_expense_click(expense_id):
        page.views.append(edit_expense_view(page, expense_id, refresh_expenses))
        page.update()

    def on_delete_expense_click(expense_id):
        delete_expense(expense_id, USER_ID)
        refresh_expenses()

    def refresh_expenses():
        nonlocal expenses
        expenses = get_all_expenses(USER_ID)
        page.views[-1] = all_expenses_view(page)
        page.update()

    expense_items = [
        ft.Card(
            content=ft.Container(
                width=500,
                bgcolor="#022c22",
                border_radius=8,
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
                                            on_click=lambda e, id=expense.id: on_edit_expense_click(
                                                id
                                            ),
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.DELETE,
                                            on_click=lambda e, id=expense.id: on_delete_expense_click(
                                                id
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
            ),
        )
        for expense in expenses
    ]

    def on_add_expense_click(e):
        page.views.append(add_expense_view(page, refresh_expenses))
        page.update()

    return ft.View(
        "/home",
        [
            ft.AppBar(
                title=ft.Text("Expensify - Gerenciador de Gastos"), bgcolor="#022c22"
            ),
            ft.Column(
                controls=[
                    ft.ElevatedButton(
                        "Adicionar Despesa",
                        on_click=on_add_expense_click,
                        bgcolor="#10b981",
                        color="#fafafa",
                    ),
                    ft.Container(
                        content=ft.Column(
                            controls=expense_items,
                            spacing=10,
                        ),
                        expand=True,
                    ),
                ],
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

        add_expense(description, amount, date, USER_ID)

        description_input.value = ""
        amount_input.value = ""
        date_input.value = ""

        page.views.pop()
        page.update()
        on_success()
        page.go("/")

    return ft.View(
        "/add_expense",
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
                    ft.ElevatedButton(
                        "Salvar",
                        on_click=on_save_click,
                        bgcolor="#10b981",
                        color="#fafafa",
                    ),
                ],
                spacing=10,
                expand=True,
            ),
        ],
    )


def edit_expense_view(page: ft.Page, expense_id: int, on_save_success):
    expense = next(
        (exp for exp in get_all_expenses(USER_ID) if exp.id == expense_id), None
    )
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

        updated_expense = update_expense(expense_id, USER_ID, description, amount, date)
        if updated_expense:
            page.views.pop()
            page.update()
            on_save_success()
        else:
            snack_bar = ft.SnackBar(ft.Text("Erro ao atualizar despesa!"))
            page.open(snack_bar)

    return ft.View(
        "/edit_expense",
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
