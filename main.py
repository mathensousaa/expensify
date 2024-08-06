import flet as ft
from views.main_view import main_view
from database.db_session import init_db
from views.user.register.register_view import register_view


def main(page: ft.Page):
    page.title = "Expensify"
    register_view(page)
    init_db()


ft.app(target=main)
