"""Module to handle the navbar view in the Flet app."""

# pylint: disable=import-error, no-name-in-module, no-member
import flet as ft
from navbar.navbar_theme import theme


def navbar(page):
    """
    Creates the navbar for the Flet app.

    This function creates a NavigationBar with three destinations: Home, Aufgaben, and Explore.
    The on_change event calls the call_page function which navigates to the selected page based
    on the index.
    The navbar is themed according to the theme module.

    Parameters
    ----------
    page : flet.Page
        The page object from Flet.

    Returns
    -------
    flet.NavigationBar
        The navbar object created by Flet.
    """

    def call_page(index):
        """Function to call the page based on the index."""
        if index == 0:
            page.go("/")
        elif index == 1:
            page.go("/issues")
        elif index == 2:
            page.go("/news")

    page.theme = theme
    navbar_view = ft.NavigationBar(
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
        on_change=lambda _: call_page(navbar.selected_index),
        bgcolor=ft.Colors.TEAL_ACCENT_700,
    )

    return navbar_view
