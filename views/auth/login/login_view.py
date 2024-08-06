import flet as ft
from .components import (
    logo_container,
    login_button,
    login_input,
    forget_password_button,
    register_button,
)
from . import styles


def login_screen(page: ft.Page):
    def go_to_register(e):
        register_screen(page)

    page.title = "Login"
    page.clean()

    logo = logo_container()

    login_title = ft.Text("Faça seu login para começar", style=styles.login_title_style)

    email_input = login_input("E-mail ou número de telefone")
    password_input = login_input("Senha", password=True)

    password_container = ft.Container(
        content=ft.Column(
            [password_input, forget_password_button()],
            horizontal_alignment=ft.CrossAxisAlignment.END,
            spacing=4,
        )
    )

    submit_button = login_button("Login", styles.submit_button_bgcolor)
    google_login = login_button("Continuar com o Google", styles.button_bgcolor)
    facebook_login = login_button("Continuar com o Facebook", styles.button_bgcolor)
    apple_login = login_button("Continuar com a Apple", styles.button_bgcolor)

    divider = ft.Divider()

    default_login_inputs = ft.Column([email_input, password_container])

    others_login_inputs = ft.Column([google_login, facebook_login, apple_login])

    register_btn = register_button(go_to_register)

    register_text_container = ft.Container(
        content=ft.Column(
            [register_btn],
            width=1080,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        width=1080,
    )

    login_form = ft.Column(
        [
            default_login_inputs,
            submit_button,
            divider,
            others_login_inputs,
            register_text_container,
        ],
        spacing=32,
    )

    login_form_column = ft.Column([login_title, login_form], spacing=32)
    login_form_container = ft.Container(
        content=login_form_column,
        padding=styles.container_padding,
        width=styles.container_width,
        bgcolor=styles.container_bgcolor,
        border_radius=styles.container_border_radius,
    )

    page.add(logo, login_form_container)
