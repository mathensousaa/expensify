import flet as ft
from .components import logo_container, register_button, success_banner
from . import styles
from controllers.user_controller import create_user
from utils.validation import Validation
from datetime import datetime


def register_with_email_view(page: ft.Page):
    logo = logo_container()

    register_title = ft.Text("Cadastro com E-mail", style=styles.register_title_style)

    first_name_input = ft.TextField(
        label="Primeiro Nome",
        width=600,
    )
    last_name_input = ft.TextField(label="Último Nome", width=600)
    birth_date_text = ft.Text(value="Data de Nascimento: (AAAA-MM-DD)", size=12)
    birth_date_picker = ft.ElevatedButton(
        "Escolher Data", icon=ft.icons.CALENDAR_MONTH, width=600
    )
    username_input = ft.TextField(label="Nome de Usuário", width=600)
    email_input = ft.TextField(label="E-mail", width=600)
    phone_number_input = ft.TextField(label="Número de Telefone", width=600)
    password_input = ft.TextField(
        label="Senha", password=True, can_reveal_password=True, width=600
    )
    error_text = ft.Text(value="", color="red")
    birth_date_error_text = ft.Text(value="", color="red")

    def handle_date_change(e):
        birth_date_text.value = (
            f"Data de Nascimento: {e.control.value.strftime('%Y-%m-%d')}"
        )
        birth_date_text.update()
        birth_date_error_text.value = ""  # Clear error when date is selected
        birth_date_error_text.update()

    def handle_date_dismiss(e):
        page.add(ft.Text("DatePicker dismissed"))

    birth_date_picker.on_click = lambda e: page.open(
        ft.DatePicker(
            first_date=datetime(year=1900, month=1, day=1),
            last_date=datetime(year=2024, month=12, day=31),
            on_change=handle_date_change,
            on_dismiss=handle_date_dismiss,
        )
    )

    def on_register_click(e):
        inputs = {
            "first_name": first_name_input,
            "last_name": last_name_input,
            "birth_date": birth_date_text,
            "username": username_input,
            "email": email_input,
            "phone_number": phone_number_input,
            "password": password_input,
        }

        errors = False
        birth_date_error_text.value = ""  # Limpa o erro anterior

        for field_name, input_field in inputs.items():
            if field_name != "birth_date":
                input_field.error_text = None  # Limpa erros anteriores

        for field_name, input_field in inputs.items():
            value = input_field.value

            if Validation.is_empty(value):
                input_field.error_text = f"O campo {input_field.label} é obrigatório"
                errors = True

            if field_name == "email" and not Validation.is_valid_email(value):
                input_field.error_text = "E-mail inválido"
                errors = True

            if field_name == "password" and not Validation.is_valid_password(value):
                input_field.error_text = "Inclua ao menos 8 caracteres, 1 número, 1 letra e um caractere especial"
                errors = True

        if birth_date_text.value == "Data de Nascimento: (AAAA-MM-DD)":
            birth_date_error_text.value = "O campo Data de Nascimento é obrigatório"
            errors = True

        page.update()

        if errors:
            birth_date_error_text.update()
            return

        first_name = first_name_input.value
        last_name = last_name_input.value
        birth_date = birth_date_text.value.replace("Data de Nascimento: ", "")
        username = username_input.value
        email = email_input.value
        phone_number = phone_number_input.value
        password = password_input.value

        response = create_user(
            first_name, last_name, birth_date, username, email, phone_number, password
        )

        if response["success"]:

            def go_to_login(e):
                page.close(banner)
                page.go("/login")

            success_msg = "Usuário registrado com sucesso!"
            banner = success_banner(page, success_msg, "Ir para Login", go_to_login)
            page.open(banner)
            page.update()
        else:
            if response["field"]:
                inputs[response["field"]].error_text = response["error"]
            else:
                error_text.value = response["error"]
            page.update()

    def on_back_click(e):
        page.go("/select_register")

    register_btn = register_button(
        "Registrar", styles.email_button_bgcolor, on_click=on_register_click
    )

    birth_date_column = ft.Column(
        [birth_date_text, birth_date_picker, birth_date_error_text]
    )

    register_form = ft.Column(
        [
            first_name_input,
            last_name_input,
            birth_date_column,
            username_input,
            phone_number_input,
            email_input,
            password_input,
            error_text,
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

    app_bar = ft.AppBar(
        title=ft.Text("Cadastro com E-mail"),
        leading=ft.IconButton(
            icon=ft.icons.ARROW_BACK,
            on_click=on_back_click,
        ),
        bgcolor=styles.BACKGROUND_COLOR,
    )

    return ft.View("/register_with_email", [app_bar, logo, register_form_container])
