from PyQt5.QtWidgets import QStackedWidget
from src.view.login_view import LoginView
from src.view.register_view import RegisterView
from src.view.home_view import FinanceApp

class Router(QStackedWidget):
    def __init__(self, width):
        super().__init__()

        self.login_view = LoginView(on_login_success=self.go_to_home, on_register=self.go_to_register, width=width)
        self.register_view = RegisterView(on_login_success=self.go_to_login, width=width)
        self.home_app = FinanceApp()

        self.routes = {
            "login": self.login_view,
            "register": self.register_view,
            "home": self.home_app
        }

        for view in self.routes.values():
            self.addWidget(view)

        self.setCurrentWidget(self.routes["login"])

    def navigate(self, route_name):

        if route_name in self.routes:
            print(self.routes[route_name])
            self.currentWidget(self.routes[route_name])
        else:
            print(f"rota {route_name} não encontrada")

    def go_to_home(self):
        self.setCurrentWidget(self.routes["home"])

    def go_to_register(self):
        self.setCurrentWidget(self.routes["register"])

    def go_to_login(self):
        self.setCurrentWidget(self.routes["login"])

    def is_on_login_screen(self):
        return self.currentWidget() == self.login_view
