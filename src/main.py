import flet as ft
from helpers.utils import gray, gray_light, dark_mint, dark_green
from home_page import HomePageView
from navigation import routing


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
        content=ft.Stack(controls=[HomePageView(page)]),
    )

    def route_change(event: ft.RouteChangeEvent):
        page.views.clear()
        page.views.append(routing(page)[page.route])
        page.update()

    page.theme_mode = ft.ThemeMode.DARK
    page.add(home_container)
    page.update()

    page.on_route_change = route_change
    # page.go("/issues")


ft.app(target=main)
