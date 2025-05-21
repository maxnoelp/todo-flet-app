"""Module to handle the issues view in the Flet app."""

import flet as ft
from helpers.utils import DARK_MINT, DARK_GREEN, DARK_GRAY


def issue_view(page):  # pylint: disable=too-many-locals, too-many-statements
    """
    Handles the issues view in the Flet app.

    This view displays an input field and a button to add a new issue to the list.
    It also displays a toggle switch to show/hide the options for the issue, which
    include a dropdown for the category and a slider for the priority.

    The page is updated whenever the user interacts with the input field or
    the toggle switch.

    :param page: The Flet page object.
    :type page: flet.Page
    """
    heading = ft.Container(
        content=(
            ft.Text(
                "Erstelle ein Todo",
                size=30,
                weight="bold",
                color="white",
            )
        ),
        margin=ft.margin.only(top=20),
    )

    # all issues
    def new_issue():
        # local storage
        # load issues from storage
        """
        Add a new issue to the list and save it to local storage.

        Triggered by the "Add" button.

        :param event: The event of the button click.
        :type event: flet.Event
        """
        issues_list = page.client_storage.get("issues_list")
        if issues_list is None:
            issues_list = []

        # new issue add list
        new_issue = {
            "checked": False,
            "text": input_field.value,
            "category": category.value,
            "priority": prio_slider.value,
        }
        # print(new_issue)
        issues_list.append(new_issue)
        page.client_storage.set("issues_list", issues_list)

        # clear input and update
        input_field.value = ""
        issues.update()

        page.go("/")

        # test
        # data = page.client_storage.get("issues_list")
        # page.client_storage.remove("issues_list")
        # print(data)

    # input field + button in one row
    input_field = ft.TextField(
        hint_text="Todo hinzufügen",
        expand=True,
        color="black",
        autofocus=True,
        border_color=DARK_GREEN,
    )
    input_field.on_submit = new_issue
    ok_button = ft.IconButton(
        icon=ft.Icons.ADD,
        icon_color=ft.Colors.WHITE,
        on_click=new_issue,
    )
    view_issue = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    input_field,
                    ok_button,
                ]
            )
        ]
    )

    def visibile_option():
        """Toggle the visibility of the option and update the page."""

        option.visible = not option.visible
        page.update()

    option_switch = ft.Switch(
        track_color=DARK_MINT,
        active_color=DARK_GREEN,
        inactive_thumb_color=DARK_GRAY,
        label="Optionen",
        on_change=visibile_option,
    )

    category = ft.Dropdown(
        border_color=DARK_GREEN,
        label="Kategorie",
        color="black",
        options=[
            ft.dropdown.Option("Arbeit"),
            ft.dropdown.Option("Freizeit"),
            ft.dropdown.Option("Sport"),
            ft.dropdown.Option("Einkaufen"),
        ],
    )

    def slider_text(event):
        """Function to handle the slider in the Flet app."""
        slider_header.content.value = f"Priorität {round(event.control.value)}%"
        page.update()

    prio_slider = ft.Slider(
        width=400,
        active_color=DARK_GREEN,
        inactive_color=DARK_MINT,
        expand=True,
        value=0,
        min=0,
        max=100,
        divisions=5,
        label="{value}%",
        on_change=slider_text,
    )

    slider_header = ft.Container(
        content=(
            ft.Text(
                "Priorität",
                size=16,
                color="black",
            )
        ),
        margin=ft.margin.only(top=20),
    )

    option = ft.Column(
        controls=[
            category,
            slider_header,
            prio_slider,
        ],
        visible=False,
    )

    option_box = ft.Container(
        content=option,
        margin=ft.margin.only(top=20),
    )

    menu = ft.Row(
        controls=[
            ft.IconButton(
                icon=ft.Icons.CANCEL,
                icon_color="black",
                on_click=lambda _: page.go("/"),
            ),
        ],
        alignment=ft.MainAxisAlignment.END,
    )
    issues = ft.Row(
        controls=[
            ft.Container(
                content=ft.Column(
                    controls=[menu, heading, view_issue, option_switch, option_box]
                ),
                padding=ft.padding.only(top=20, left=20, right=40),
            )
        ]
    )

    return issues
