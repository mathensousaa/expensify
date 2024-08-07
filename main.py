import flet as ft
from views.auth.login import login_view
from views.expenses import expense_view, home_view
from views.user.select_register import select_register_view
from views.user.register_with_email import register_with_email_view
from database.db_session import init_db
from session.session_manager import SessionManager


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
        session = SessionManager.get_session(page)
        if session and page.route == "/login":
            page.go("/home")
        elif page.route == "/home":
            page.views.append(home_view.all_expenses_view(page))
        elif page.route == "/add_expense":
            page.views.append(home_view.add_expense_view(page))
        elif page.route == "/edit_expense":
            page.views.append(home_view.edit_expense_view(page))
        elif page.route == "/select_register":
            page.views.append(select_register_view(page))
        elif page.route == "/register_with_email":
            page.views.append(register_with_email_view(page))
        elif page.route == "/login":
            page.views.append(login_view(page))

        page.update()

    def view_pop(view):
        page.views.pop()
        if page.views:
            top_view = page.views[-1]
            page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop

    session = SessionManager.get_session(page)
    if session:
        page.go("/home")
    else:
        page.go("/login")


ft.app(target=main)
