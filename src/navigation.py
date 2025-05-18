import flet as ft
from home_page import HomePageView
from issues import IssueView


def routing(page):
    return {
        "/": ft.View(
            route="/",
            controls=[HomePageView(page)],  # Use home_page directly
        ),
        "/issues": ft.View(
            route="/issues",
            controls=[IssueView(page)],  # Use issues directly
        ),
    }
