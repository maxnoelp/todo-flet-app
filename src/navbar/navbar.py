import flet as ft
from navbar.navbar_theme import theme


def Navbar(page):
    def CallPage(index):
        if index == 0:
            page.go("/")
        elif index == 1:
            page.go("/issues")
        elif index == 2:
            page.go("/news")

    page.theme = theme
    navbar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icon(ft.Icons.HOME_OUTLINED, color=ft.Colors.WHITE),
                selected_icon=ft.Icon(ft.Icons.HOME, color=ft.Colors.BLACK),
                label="Home",
            ),
            ft.NavigationBarDestination(
                icon=ft.Icon(ft.Icons.DESIGN_SERVICES_SHARP, color=ft.Colors.WHITE),
                selected_icon=ft.Icon(
                    ft.Icons.DESIGN_SERVICES_SHARP, color=ft.Colors.BLACK
                ),
                label="Aufgaben",
                bgcolor=ft.Colors.WHITE,
            ),
            ft.NavigationBarDestination(
                icon=ft.Icon(ft.Icons.NEWSPAPER_OUTLINED, color=ft.Colors.WHITE),
                selected_icon=ft.Icon(
                    ft.Icons.NEWSPAPER_OUTLINED, color=ft.Colors.BLACK
                ),
                label="Explore",
                bgcolor=ft.Colors.LIME_50,
            ),
        ],
        on_change=lambda _: CallPage(navbar.selected_index),
        bgcolor=ft.Colors.TEAL_ACCENT_700,
    )

    return navbar
