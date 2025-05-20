import flet as ft

theme = ft.Theme(
    navigation_bar_theme=ft.NavigationBarTheme(
        label_text_style={
            ft.ControlState.DEFAULT: ft.TextStyle(color=ft.Colors.WHITE),
            ft.ControlState.SELECTED: ft.TextStyle(color=ft.Colors.BLACK),
        },
        indicator_color=ft.Colors.WHITE,
    )
)
