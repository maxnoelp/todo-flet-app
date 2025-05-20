import flet as ft
from helpers.utils import gray, dark_mint, dark_green, dark_gray, gray_light
from time import sleep


def HomePageView(page):
    def FullScreen(event=None):
        page.window.full_screen = not page.window.full_screen
        page.update()

    def SleepMode(timer):
        page.window.visible = False
        page.update()
        sleep(timer)
        page.window.visible = True
        page.update()

    heading = ft.Container(
        content=(
            ft.Text(
                "Willkommen",
                size=30,
                weight="bold",
                color="white",
            )
        ),
        margin=ft.margin.only(top=20),
    )

    def CountIssue(filter_option=None):
        data = page.client_storage.get("issues_list")
        if data is not None:
            count = 0
            for d in data:
                if (
                    filter_option is None
                    or (filter_option == "unchecked" and d["checked"] is False)
                    or (filter_option == "checked" and d["checked"] is True)
                ):
                    count += 1
            return count
        return 0

    count_all = f"Alle({CountIssue(filter_option=None)})"
    count_open = f"To Do({CountIssue(filter_option='unchecked')})"
    count_done = f"Done({CountIssue(filter_option='checked')})"

    def UpdateCount():
        count_all = f"Alle({CountIssue(filter_option=None)})"
        count_open = f"To Do({CountIssue(filter_option='unchecked')})"
        count_done = f"Done({CountIssue(filter_option='checked')})"

        all_btn_count.content = ft.Text(count_all, size=16, color="white")
        open_btn_count.content = ft.Text(count_open, size=16, color="white")
        done_btn_count.content = ft.Text(count_done, size=16, color="white")

    all_btn_count = ft.Container(
        content=ft.Text(count_all, size=16, color="white"),
    )
    # filter btn
    all_btn = ft.Container(
        content=ft.TextButton(
            content=all_btn_count,
            on_click=lambda _: LoadList(filter_option="all"),
        ),
        bgcolor=dark_mint,
        height=80,
        width=140,
        border_radius=10,
        alignment=ft.alignment.center,
    )

    open_btn_count = ft.Container(
        content=ft.Text(count_open, size=16, color="white"),
    )
    open_btn = ft.Container(
        content=ft.TextButton(
            content=open_btn_count,
            on_click=lambda _: LoadList(filter_option="unchecked"),
        ),
        bgcolor=dark_mint,
        height=80,
        width=140,
        border_radius=10,
        alignment=ft.alignment.center,
    )

    done_btn_count = ft.Container(
        content=ft.Text(count_done, size=16, color="white"),
    )
    done_btn = ft.Container(
        content=ft.TextButton(
            content=done_btn_count,
            on_click=lambda _: LoadList(filter_option="checked"),
        ),
        bgcolor=dark_mint,
        height=80,
        width=140,
        border_radius=10,
        alignment=ft.alignment.center,  # → mitten drin (x & y)
    )

    boxen = ft.Row(
        controls=[all_btn, open_btn, done_btn],
        alignment=ft.MainAxisAlignment.CENTER,  # Buttons stehen jetzt zentriert
        spacing=20,  # optionaler Abstand zwischen den Buttons
    )

    issues = ft.Container(
        height=120,
    )

    all_issues = ft.Column(
        scroll="auto",
        expand=True,
    )

    # issue edit
    edit_issue = ft.TextField(
        autofocus=True,
        visible=False,
        text_size=20,
        border_color=dark_mint,
        border_radius=10,
        color="black",
    )

    accept_btn = ft.IconButton(
        icon=ft.Icons.DONE,
        visible=False,
        icon_color=ft.Colors.GREEN_800,
    )

    delete_issue = ft.IconButton(
        icon=ft.Icons.DELETE,
        visible=False,
        icon_color="red",
    )

    def TextFieldVisible(d):
        edit_issue.visible = not edit_issue.visible
        delete_issue.visible = not delete_issue.visible
        accept_btn.visible = not accept_btn.visible
        edit_issue.value = d["text"]
        page.update()
        accept_btn.on_click = lambda _, d=d: SaveEditIssue(d, edit_issue.value)
        delete_issue.on_click = lambda _, d=d: OpenModal(d)
        edit_issue.on_submit = lambda _, d=d: SaveEditIssue(d, edit_issue.value)

    def LoadList(filter_option=None):
        if filter_option is None:
            filter_option = page.client_storage.get("filter_option")
        elif filter_option == "all":
            filter_option = None
            page.client_storage.remove("filter_option")
        is_issues = False
        data = page.client_storage.get("issues_list")
        if data is not None:
            all_issues.controls.clear()
            data.sort(key=lambda d: d["priority"], reverse=True)
            for d in data:
                if (
                    filter_option is None
                    or (filter_option == "unchecked" and d["checked"] is False)
                    or (filter_option == "checked" and d["checked"] is True)
                ):
                    checkbox = ft.Checkbox(
                        value=d["checked"],
                        fill_color=dark_gray,
                        check_color=ft.Colors.TEAL_ACCENT_700,
                        on_change=lambda _, d=d: CheckboxChecked(d),
                    )
                    if d["checked"] is False:
                        text = ft.Text(
                            value=d["text"],
                            size=20,
                            color=ft.Colors.TEAL_ACCENT_700,
                            width=350,
                        )
                    else:
                        text = ft.Text(
                            size=20,
                            color="black",
                            width=350,
                            spans=[
                                ft.TextSpan(
                                    d["text"],
                                    ft.TextStyle(
                                        decoration=ft.TextDecoration.LINE_THROUGH,
                                        color=ft.Colors.GREEN_400,
                                    ),
                                ),
                            ],
                        )
                    edit_btn = ft.IconButton(
                        icon=ft.Icons.EDIT_NOTE,
                        on_click=lambda _, d=d: TextFieldVisible(d),
                        icon_color=dark_mint,
                    )
                    issue_row = ft.Row(
                        controls=[
                            checkbox,
                            text,
                            edit_btn,
                        ]
                    )
                    all_issues.controls.append(issue_row)
                    is_issues = True
                    page.update()

        if filter_option is not None:
            page.client_storage.set("filter_option", filter_option)

        if not is_issues:
            no_issues = ft.Text("Keine Aufgaben", size=20, color="black")
            all_issues.controls.append(no_issues)
            page.update()

    def CheckboxChecked(d):
        data = page.client_storage.get("issues_list")
        if data is not None:
            for i in data:
                if i["text"] == d["text"]:
                    i["checked"] = not i["checked"]
                    break
            page.client_storage.set("issues_list", data)
            UpdateCount()
            LoadList()
            page.update()

    def SaveEditIssue(d, text):
        data = page.client_storage.get("issues_list")
        if data is not None:
            for i in data:
                if i["text"] == d["text"]:
                    i["text"] = text
                    break
            page.client_storage.set("issues_list", data)
            edit_issue.visible = False
            edit_issue.value = ""
            delete_issue.visible = False
            accept_btn.visible = False
            LoadList()
            page.update()

    def DeleteIssue(d, modal):
        data = page.client_storage.get("issues_list")
        if data is not None:
            for i in data:
                if i["text"] == d["text"]:
                    data.remove(i)
                    break
            page.client_storage.set("issues_list", data)
            edit_issue.visible = False
            edit_issue.value = ""
            delete_issue.visible = False
            accept_btn.visible = False
            page.close(modal)
            UpdateCount()
            LoadList()
            page.update()

    def OpenModal(d):
        print("open modal")
        modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Todo löschen"),
            content=ft.Text(f"Möchtest du wirklich das Todo '{d['text']}' löschen?"),
            actions=[
                ft.TextButton("Ja", on_click=lambda _, d=d: DeleteIssue(d, modal)),
                ft.TextButton("Nein", on_click=lambda _: CloseModal(modal)),
            ],
            actions_alignment=ft.MainAxisAlignment.CENTER,
        )
        page.open(modal)

    def CloseModal(modal):
        page.close(modal)
        page.update()

    issue_list = ft.Stack(
        controls=[
            issues,
            ft.FloatingActionButton(
                icon=ft.Icons.ADD,
                bgcolor="black",
                right=0,
                bottom=50,
                on_click=lambda _: page.go("/issues"),
            ),
        ]
    )

    edit_column = ft.Row(
        controls=[
            edit_issue,
            accept_btn,
            delete_issue,
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )

    home_page = ft.SafeArea(
        ft.Row(
            controls=[
                ft.Container(
                    content=ft.Column(
                        controls=[
                            heading,
                            boxen,
                            edit_column,
                            all_issues,
                            issue_list,
                        ]
                    ),
                )
            ]
        )
    )

    LoadList()

    return home_page
