import flet as ft
from views.auth import login_view
from views.expenses import home_view
from views.user.select_register import select_register_view
from views.user.register_with_email import register_with_email_view
from database.db_session import init_db


def main(page: ft.Page):
    page.fonts = {"Ubuntu": "/fonts/Ubuntu-Regular.ttf"}
    page.theme = ft.Theme(font_family="Ubuntu")
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.title = "Expensify"

    init_db()

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(home_view.all_expenses_view(page))
        elif page.route == "/page2":
            page.views.append(login_view(page))
        elif page.route == "/page3":
            page.views.append(home_view.all_expenses_view(page))
        elif page.route == "/page4":
            page.views.append(home_view.add_expense_view(page))
        elif page.route == "/select_register":
            page.views.append(select_register_view.select_register_view(page))
        elif page.route == "/register_with_email":
            page.views.append(register_with_email_view.register_with_email_view)
        page.update()

    def view_pop(view):
        page.views.pop()
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go("/")


ft.app(target=main)
