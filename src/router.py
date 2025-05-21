"""Module to handle the routing in the Flet app."""

# pylint: disable=import-error, invalid-name, too-few-public-methods
import flet as ft
from home_page import home_page_view
from issues import issue_view
from github.news import news_page


class Router:
    """Class to handle the routing in the Flet app."""

    def __init__(self, page: ft.Page):
        """
        Initializes the Router class with a page object and sets up the routes.

        This constructor stores the provided Flet page object and defines the routing
        paths for the application. It also initializes the body of the page with the
        home page view.

        :param page: The Flet page object to be used for routing.
        :type page: flet.Page
        """

        self.page = page  # echtes Page-Objekt speichern
        self.routes = {
            "/": home_page_view,
            "/issues": issue_view,
            "/news": news_page,
        }
        self.body = ft.Container(content=self.routes["/"](self.page))

    # >>> ACHTUNG: hier kommt ein RouteChangeEvent!
    def RouteChange(self, e: ft.RouteChangeEvent):
        """
        Handles the route change event in the Flet app.

        This function is called whenever the route of the page changes. It gets the
        route from the event and sets the content of the body container of the page
        to the view associated with the route. If the route does not exist, it shows
        a "404 - Page not found" message.

        :param e: The event of the route change.
        :type e: flet.RouteChangeEvent
        """
        print(f"RouteChangeEvent.route = '{e.route}'")
        self.page.route = e.route  # (optional) Page-route aktuell halten
        view_fn = self.routes.get(e.route)
        if view_fn is None:
            self.body.content = ft.Text("404 – Seite nicht gefunden")
        else:
            self.body.content = view_fn(self.page)
        print(f"RouteChangeEvent.route = '{e.route}'")

        self.body.update()
