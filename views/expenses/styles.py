import flet as ft

# Define estilos
BACKGROUND_COLOR = "#022c22"
BUTTON_COLOR = "#10b981"
BUTTON_TEXT_COLOR = "#fafafa"
CARD_BG_COLOR = "#022c22"
CARD_BORDER_RADIUS = 8


# Estilos de botão
def elevated_button_style():
    return ft.ButtonStyle(
        bgcolor=BUTTON_COLOR,
        color=BUTTON_TEXT_COLOR,
    )


# Estilos de card
def card_style():
    return ft.CardStyle(
        bgcolor=CARD_BG_COLOR,
        border_radius=CARD_BORDER_RADIUS,
    )
