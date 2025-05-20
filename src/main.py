import flet as ft
from navbar.navbar import Navbar
from router import Router


def main(page: ft.Page):
    page.navigation_bar = Navbar(page)
    navbar_router = Router(page)
    page.on_route_change = navbar_router.RouteChange
    page.window.height = 850
    page.window.width = 500
    page.title = "Todo App"
    page.bgcolor = "black"

    def route_change(event: ft.RouteChangeEvent):
        page.views.clear()
        page.update()

    page.theme_mode = ft.ThemeMode.DARK
    page.update()
    page.add(navbar_router.body)
    # page.go("/issues")


ft.app(target=main)
