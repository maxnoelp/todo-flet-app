"""Module to handle the main view in the Flet app."""

# pylint: disable=import-error, no-name-in-module

import flet as ft
from navbar.navbar import navbar
from router import Router


def main(page: ft.Page):
    """
    Main entry point for the Flet app.

    This function initializes the Flet page properties such as the window
    size, title, and theme mode. It also sets up the navigation bar using the
    Navbar class and defines the route change handler using the Router class.
    """

    page.navigation_bar = navbar(page)
    navbar_router = Router(page)
    page.on_route_change = navbar_router.RouteChange
    page.window.height = 850
    page.window.width = 500
    page.title = "Todo App"
    page.bgcolor = "black"

    page.theme_mode = ft.ThemeMode.DARK
    page.update()
    page.add(navbar_router.body)
    # page.go("/issues")


ft.app(target=main)
