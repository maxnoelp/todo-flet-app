import flet as ft
from helpers.utils import gray, gray_light, dark_mint, dark_green
from home_page import home_page


def main(page: ft.Page):
    page.window_height = 800
    page.window_width = 500
    page.title = "Todo App"
    page.bgcolor = "black"
    home_container = ft.Container(
        bgcolor=dark_mint,
        height=780,
        width=500,
        border_radius=30,
        content=ft.Stack(controls=[home_page]),
    )

    page.add(home_container)

    page.update()


ft.app(target=main)
