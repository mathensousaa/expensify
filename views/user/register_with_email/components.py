import flet as ft
from . import styles


class CustomElevatedButton(ft.ElevatedButton):
    def __init__(self, text, bgcolor, **kwargs):
        super().__init__(
            content=ft.Container(
                content=ft.Text(
                    text,
                    style=styles.button_text_style,
                ),
                padding=styles.button_padding,
            ),
            bgcolor=bgcolor,
            width=1080,
            **kwargs
        )


def logo_container():
    horizontal_logo = ft.Image(src="/images/logo_horizontal.png", height=60)
    welcome_text = ft.Text(
        "Bem-vindo ao Expensify! Cadastre-se e simplifique sua vida financeira.",
        style=styles.welcome_text_style,
        text_align=ft.TextAlign.CENTER,
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


def register_button(text, bgcolor, **kwargs):
    return CustomElevatedButton(text, bgcolor, **kwargs)


def success_banner(page, message, action_text, action):
    action_button_style = ft.ButtonStyle(color=ft.colors.BLUE)

    banner = ft.Banner(
        bgcolor=ft.colors.GREEN_100,
        leading=ft.Icon(ft.icons.CHECK_CIRCLE, color=ft.colors.GREEN, size=40),
        content=ft.Text(
            value=message,
            color=ft.colors.BLACK,
        ),
        actions=[
            ft.TextButton(text=action_text, style=action_button_style, on_click=action),
        ],
    )

    return banner
