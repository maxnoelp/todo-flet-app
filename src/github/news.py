"""Module to handle the github news view in the Flet app."""

# pylint: disable=import-error
import flet as ft
import requests


def fetch_github_releases():
    """Fetches the latest releases from GitHub."""
    url = "https://api.github.com/repos/maxnoelp/todo-flet-app/releases"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print("Fehler beim Abrufen:", e)
        return []


def news_page(page):  # pylint: disable=unused-argument
    """Displays the latest releases from GitHub."""
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
