import flet as ft
from . import styles
from session.session_manager import SessionManager


def logo_container():
    logo_image_path = "assets/images/logo.png"  # Substitua pelo caminho real da imagem
    return ft.Container(
        content=ft.Image(src=logo_image_path, width=100, height=50),
    )


def expense_card(expense, on_edit_click, on_delete_click):
    return ft.Card(
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
                                        on_click=lambda e, id=expense.id: on_edit_click(
                                            id
                                        ),
                                    ),
                                    ft.IconButton(
                                        icon=ft.icons.DELETE,
                                        on_click=lambda e, id=expense.id: on_delete_click(
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


def add_expense_button(on_click):
    return ft.ElevatedButton(
        "Adicionar Despesa",
        on_click=on_click,
        style=styles.elevated_button_style(),
    )


def save_button(on_click):
    return ft.ElevatedButton(
        "Salvar",
        on_click=on_click,
        style=styles.elevated_button_style(),
    )


def app_bar(title, page, leading_icon=None):
    session = SessionManager.get_session(page)
    username = session.get("username") if session else "Usuário"

    def on_logout_click(e):
        SessionManager.clear_session(page)
        page.go("/login")

    return ft.AppBar(
        title=ft.Text(title),
        leading=leading_icon,
        actions=[
            ft.Text(username, style=ft.TextStyle(color=ft.colors.WHITE, size=16)),
            ft.IconButton(
                icon=ft.icons.LOGOUT,
                on_click=on_logout_click,
            ),
        ],
        bgcolor=styles.BACKGROUND_COLOR,
    )
