import flet as ft
from home_page import HomePageView
from issues import IssueView
from github.news import NewsPage


class Router:
    def __init__(self, page: ft.Page):
        self.page = page  # echtes Page-Objekt speichern
        self.routes = {
            "/": HomePageView,
            "/issues": IssueView,
            "/news": NewsPage,
        }
        self.body = ft.Container(content=self.routes["/"](self.page))

    # >>> ACHTUNG: hier kommt ein RouteChangeEvent!
    def RouteChange(self, e: ft.RouteChangeEvent):
        print(f"RouteChangeEvent.route = '{e.route}'")
        self.page.route = e.route  # (optional) Page-route aktuell halten
        view_fn = self.routes.get(e.route)
        if view_fn is None:
            self.body.content = ft.Text("404 – Seite nicht gefunden")
        else:
            # **jetzt** das echte Page-Objekt in die View geben
            self.body.content = view_fn(self.page)
        print(f"RouteChangeEvent.route = '{e.route}'")

        self.body.update()
