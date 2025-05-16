import flet as ft
from helpers.utils import gray, dark_mint, dark_green
from menu import menu

heading = ft.Container(
    content=(
        ft.Text(
            "Willkommen",
            size=30,
            weight="bold",
            color="black",
        )
    ),
    margin=ft.margin.only(top=20),
)

box = ft.Container(
    bgcolor=dark_mint,
    height=80,
    width=140,
    border_radius=10,
    margin=ft.margin.only(top=20, bottom=20),
)

boxen = ft.Row(
    controls=[
        box,
        box,
        box,
    ]
)

issues = ft.Container(
    height=450,
)

issue_list = ft.Stack(
    controls=[
        issues,
        ft.FloatingActionButton(
            icon=ft.Icons.ADD, bgcolor="black", right=20, bottom=20
        ),
    ]
)

home_page = ft.Row(
    controls=[
        ft.Container(
            bgcolor=gray,
            height=780,
            width=500,
            content=ft.Column(controls=[menu, heading, boxen, issue_list]),
            padding=ft.padding.only(top=20, left=20, right=40),
        )
    ]
)
