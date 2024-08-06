import flet as ft
from .components import logo_container, register_button, login_button
from . import styles


def register_view(page: ft.Page):
    logo = logo_container()

    register_title = ft.Text(
        "Faça seu cadastro para começar", style=styles.register_title_style
    )

    register_options = ft.Column(
        [
            register_button("Continuar com o Google", styles.button_bgcolor),
            register_button("Continuar com o Facebook", styles.button_bgcolor),
            register_button("Continuar com a Apple", styles.button_bgcolor),
            register_button("Continuar com E-mail", styles.email_button_bgcolor),
        ]
    )

    login_btn = login_button()

    register_text_container = ft.Container(
        content=ft.Column(
            [login_btn],
            width=1080,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        alignment=ft.alignment.center,
        width=1080,
    )

    login_form = ft.Column(
        [
            register_options,
            register_text_container,
        ],
        spacing=32,
    )

    login_form_column = ft.Column([register_title, login_form], spacing=32)
    login_form_container = ft.Container(
        content=login_form_column,
        padding=styles.container_padding,
        width=styles.container_width,
        bgcolor=styles.container_bgcolor,
        border_radius=styles.container_border_radius,
    )

    return ft.View("/", [logo, login_form_container])
