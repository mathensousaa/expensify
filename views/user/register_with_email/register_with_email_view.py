import flet as ft
from .components import logo_container, register_button
from . import styles


def register_with_email_view(page: ft.Page):
    logo = logo_container()

    register_title = ft.Text("Cadastro com E-mail", style=styles.register_title_style)

    first_name_input = ft.TextField(label="Primeiro Nome", width=300)
    last_name_input = ft.TextField(label="Último Nome", width=300)
    birth_date_input = ft.TextField(label="Data de Nascimento (AAAA-MM-DD)", width=300)
    username_input = ft.TextField(label="Nome de Usuário", width=300)
    email_input = ft.TextField(label="E-mail", width=300)
    phone_number_input = ft.TextField(label="Número de Telefone", width=300)
    password_input = ft.TextField(
        label="Senha", password=True, can_reveal_password=True, width=300
    )

    def on_register_click(e):
        # Adicione a lógica para registrar o usuário
        first_name = first_name_input.value
        last_name = last_name_input.value
        birth_date = birth_date_input.value
        username = username_input.value
        email = email_input.value
        phone_number = phone_number_input.value
        password = password_input.value
        # Implemente a lógica de registro de usuário aqui
        print(
            "Usuário registrado:",
            first_name,
            last_name,
            birth_date,
            username,
            email,
            phone_number,
            password,
        )

    register_btn = register_button(
        "Registrar", styles.email_button_bgcolor, on_click=on_register_click
    )

    register_form = ft.Column(
        [
            first_name_input,
            last_name_input,
            birth_date_input,
            username_input,
            email_input,
            phone_number_input,
            password_input,
            register_btn,
        ],
        spacing=16,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
    )

    register_form_container = ft.Container(
        content=register_form,
        padding=styles.container_padding,
        width=styles.container_width,
        bgcolor=styles.container_bgcolor,
        border_radius=styles.container_border_radius,
    )

    return ft.View("/register_with_email", [logo, register_form_container])
