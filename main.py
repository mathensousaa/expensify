import flet as ft
from views.auth import login_view
from views.expenses import expense_view, home_view
from database.db_session import init_db
from views.user.register import register_view


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
        elif page.route == "/page5":
            page.views.append(expense_view(page))
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
