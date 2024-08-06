import flet as ft
from views.main_view import main_view
from database.db_session import init_db


def main(page: ft.Page):
    page.title = "Expensify"
    page.add(main_view())
    init_db()


ft.app(target=main)
