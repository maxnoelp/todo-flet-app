import flet as ft
from helpers.utils import gray


menu = ft.Row(
    controls=[
        ft.Icon(ft.Icons.MENU, color="black", size=40),
        ft.Icon(ft.Icons.POWER_SETTINGS_NEW_OUTLINED, color="black", size=40),
    ],
    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
)
