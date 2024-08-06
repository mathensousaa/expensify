import flet as ft
from . import styles

def logo_container():
    horizontal_logo = ft.Image(src="/images/logo_horizontal.png", height=60)
    welcome_text = ft.Text(
        "Bem vindo de volta!",
        style=styles.welcome_text_style,
    )

    return ft.Container(
        content=ft.Column(
            [horizontal_logo, welcome_text],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=24,
        ),
        expand=True,
    )

def login_button(text, bgcolor):
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

def login_input(hint_text, password=False):
    return ft.TextField(
        password=password,
        can_reveal_password=password,
        hint_text=hint_text,
        hint_style=styles.input_hint_style,
        filled=True,
        fill_color=styles.button_bgcolor,
        border_radius=ft.border_radius.all(16),
        border_color=styles.button_bgcolor,
        text_size=12,
    )

def forget_password_button():
    return ft.TextButton(
        content=ft.Container(
            content=ft.Text(
                "Esqueci a senha", color="#737373", weight=ft.FontWeight.NORMAL, size=12
            ),
        ),
    )

def register_button(go_to_register):
    register_text = ft.Text(
        "Não tem uma conta?", style=styles.register_text_style
    )

    register_text_highlight = ft.Text(
        "Registre-se", style=styles.register_text_highlight_style
    )

    return ft.TextButton(
        content=ft.Container(
            content=ft.Row(
                [register_text, register_text_highlight],
                alignment=ft.MainAxisAlignment.CENTER,
                wrap=True,
            )
        ),
        on_click=go_to_register,
    )
