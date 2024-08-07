import flet as ft
from datetime import datetime
from controllers.expense_controller import (
    add_expense,
    get_all_expenses,
    update_expense,
    delete_expense,
)
from views.expenses.components import (
    logo_container,
    expense_card,
    add_expense_button,
    save_button,
    app_bar,
)
from session.session_manager import SessionManager
from . import styles


def all_expenses_view(page: ft.Page):
    logo = logo_container()
    session = SessionManager.get_session(page)
    user_id = session.get("user_id") if session else None

    if not user_id:
        page.go("/login")
        return

    expenses = get_all_expenses(user_id)

    def on_edit_expense_click(expense_id):
        page.views.append(edit_expense_view(page, expense_id, refresh_expenses))
        page.update()

    def on_delete_expense_click(expense_id):
        delete_expense(expense_id, user_id)
        refresh_expenses()

    def refresh_expenses():
        nonlocal expenses
        expenses = get_all_expenses(user_id)
        page.views[-1] = all_expenses_view(page)
        page.update()

    expense_items = [
        expense_card(expense, on_edit_expense_click, on_delete_expense_click)
        for expense in expenses
    ]

    def on_add_expense_click(e):
        page.views.append(add_expense_view(page, refresh_expenses))
        page.update()

    return ft.View(
        "/home",
        [
            app_bar("Expensify", page, logo),
            ft.Column(
                controls=[
                    add_expense_button(on_add_expense_click),
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
    session = SessionManager.get_session(page)
    user_id = session.get("user_id") if session else None

    if not user_id:
        page.go("/login")
        return

    description_input = ft.TextField(label="Descrição")
    amount_input = ft.TextField(label="Valor", keyboard_type=ft.KeyboardType.NUMBER)
    date_text = ft.Text(value="Data: (DD/MM/AAAA)", size=12)
    date_picker = ft.ElevatedButton("Escolher Data", icon=ft.icons.CALENDAR_MONTH)

    def handle_date_change(e):
        date_text.value = f"Data: {e.control.value.strftime('%d/%m/%Y')}"
        date_text.update()

    def handle_date_dismiss(e):
        page.add(ft.Text("DatePicker dismissed"))

    date_picker.on_click = lambda e: page.open(
        ft.DatePicker(
            first_date=datetime(year=1900, month=1, day=1),
            last_date=datetime(year=2024, month=12, day=31),
            on_change=handle_date_change,
            on_dismiss=handle_date_dismiss,
        )
    )

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

        date_str = date_text.value.replace("Data: ", "")
        try:
            date = datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            snack_bar = ft.SnackBar(ft.Text("Data inválida!"))
            page.open(snack_bar)
            return

        add_expense(description, amount, date, user_id)

        description_input.value = ""
        amount_input.value = ""
        date_text.value = "Data: (DD/MM/AAAA)"

        page.views.pop()
        page.update()
        on_success()
        page.go("/home")

    date_column = ft.Column([date_text, date_picker])

    return ft.View(
        "/add_expense",
        [
            app_bar(
                "Adicionar Despesa",
                page,
                leading_icon=ft.IconButton(
                    icon=ft.icons.ARROW_BACK, on_click=on_back_click, tooltip="Sair"
                ),
            ),
            ft.Column(
                controls=[
                    description_input,
                    amount_input,
                    date_column,
                    save_button(on_save_click),
                ],
                spacing=10,
                expand=True,
            ),
        ],
    )


def edit_expense_view(page: ft.Page, expense_id: int, on_save_success):
    session = SessionManager.get_session(page)
    user_id = session.get("user_id") if session else None

    if not user_id:
        page.go("/login")
        return

    expense = next(
        (exp for exp in get_all_expenses(user_id) if exp.id == expense_id), None
    )
    if not expense:
        return ft.View("/error", [ft.Text("Despesa não encontrada")])

    description_input = ft.TextField(label="Descrição", value=expense.description)
    amount_input = ft.TextField(
        label="Valor", value=str(expense.amount), keyboard_type=ft.KeyboardType.NUMBER
    )
    date_text = ft.Text(value=f"Data: {expense.date.strftime('%d/%m/%Y')}", size=12)
    date_picker = ft.ElevatedButton("Escolher Data", icon=ft.icons.CALENDAR_MONTH)

    def handle_date_change(e):
        date_text.value = f"Data: {e.control.value.strftime('%d/%m/%Y')}"
        date_text.update()

    def handle_date_dismiss(e):
        page.add(ft.Text("DatePicker dismissed"))

    date_picker.on_click = lambda e: page.open(
        ft.DatePicker(
            first_date=datetime(year=1900, month=1, day=1),
            last_date=datetime(year=2024, month=12, day=31),
            on_change=handle_date_change,
            on_dismiss=handle_date_dismiss,
        )
    )

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

        date_str = date_text.value.replace("Data: ", "")
        try:
            date = datetime.strptime(date_str, "%d/%m/%Y").date()
        except ValueError:
            snack_bar = ft.SnackBar(ft.Text("Data inválida!"))
            page.open(snack_bar)
            return

        updated_expense = update_expense(expense_id, user_id, description, amount, date)
        if updated_expense:
            page.views.pop()
            page.update()
            on_save_success()
        else:
            snack_bar = ft.SnackBar(ft.Text("Erro ao atualizar despesa!"))
            page.open(snack_bar)

    date_column = ft.Column([date_text, date_picker])

    return ft.View(
        "/edit_expense",
        [
            app_bar(
                "Editar Despesa",
                page,
                leading_icon=ft.IconButton(
                    icon=ft.icons.ARROW_BACK, on_click=on_back_click
                ),
            ),
            ft.Column(
                controls=[
                    description_input,
                    amount_input,
                    date_column,
                    save_button(on_save_click),
                ],
                spacing=10,
                expand=True,
            ),
        ],
    )
