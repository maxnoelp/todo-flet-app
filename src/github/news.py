import flet as ft
import requests


def fetch_github_releases():
    url = "https://api.github.com/repos/maxnoelp/todo-flet-app/releases"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print("Fehler beim Abrufen:", e)
        return []


def NewsPage(page):
    releases = fetch_github_releases()

    if not releases:
        return ft.Text("Keine Releases gefunden oder Fehler bei der Abfrage.")

    return ft.Column(
        controls=[
            ft.Container(
                content=ft.Column(
                    [
                        ft.Text(
                            f"📦 {release['name'] or release['tag_name']}",
                            size=20,
                            weight="bold",
                        ),
                        ft.Text(release["body"] or "Keine Beschreibung", size=14),
                        ft.Text(
                            f"Date: {release['published_at'][:10]}",
                            italic=True,
                            size=12,
                        ),
                        ft.Divider(),
                    ]
                )
            )
            for release in releases
        ]
    )
    return releases
