import flet as ft
from . import styles


def logo_container():
    horizontal_logo = ft.Image(src="/images/logo_horizontal.png", height=60)
    welcome_text = ft.Text(
        "Bem-vindo ao Expensify! Cadastre-se e simplifique sua vida financeira.",
        style=styles.welcome_text_style,
    )

    return ft.Container(
        content=ft.Column(
            [horizontal_logo, welcome_text],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=24,
        ),
        padding=styles.logo_padding,
        expand=True,
    )


def register_button(text, bgcolor):
    return ft.ElevatedButton(
        content=ft.Container(
            content=ft.Text(
                text,
                style=styles.button_text_style,
            ),
            padding=styles.button_padding,
        ),
        bgcolor=bgcolor,
        width=1080,
    )


def login_button():
    login_text = ft.Text("Já tem uma conta?", style=styles.login_text_style)
    login_text_highlight = ft.Text("Logue-se", style=styles.login_text_highlight_style)

    return ft.TextButton(
        content=ft.Container(
            content=ft.Row(
                [login_text, login_text_highlight],
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=True,
            )
        ),
    )
