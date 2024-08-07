import flet as ft
from views.auth.login.components import (
    logo_container,
    CustomElevatedButton,
    success_banner,
)
from controllers.auth_controller import authenticate_user
from . import styles


def login_view(page: ft.Page):
    logo = logo_container()

    login_title = ft.Text("Login", style=styles.register_title_style)

    identifier_input = ft.TextField(
        label="E-mail, Nome de Usuário ou Telefone", width=600
    )
    password_input = ft.TextField(
        label="Senha", password=True, can_reveal_password=True, width=600
    )
    error_text = ft.Text(value="", color="red")

    def on_login_click(e):
        identifier = identifier_input.value
        password = password_input.value

        response = authenticate_user(page, identifier, password)

        if response["success"]:

            def go_to_home():
                page.go("/home")

            go_to_home()
            page.update()
        else:
            error_text.value = response["message"]
            page.update()

    login_btn = CustomElevatedButton(
        "Login", styles.email_button_bgcolor, on_click=on_login_click
    )

    divider = ft.Divider()

    register_text = ft.Text(
        "Não tem uma conta?", weight=ft.FontWeight.BOLD, color="#FFFFFF", size=12
    )

    register_text_highlight = ft.Text(
        "Registre-se", weight=ft.FontWeight.BOLD, color="#6EE7B7", size=12
    )

    def go_to_register(e):
        page.go("/select_register")

    register_button = ft.TextButton(
        content=ft.Container(
            content=ft.Row(
                [register_text, register_text_highlight],
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=True,
            )
        ),
        on_click=go_to_register,
    )

    register_text_container = ft.Container(
        content=ft.Column(
            [register_button],
            width=1080,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        width=1080,
    )

    login_form = ft.Column(
        [
            identifier_input,
            password_input,
            error_text,
            login_btn,
            divider,
            register_text_container,
        ],
        spacing=16,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
    )

    login_form_container = ft.Container(
        content=login_form,
        padding=styles.container_padding,
        width=styles.container_width,
        bgcolor=styles.container_bgcolor,
        border_radius=styles.container_border_radius,
    )

    return ft.View("/login", [logo, login_form_container])
