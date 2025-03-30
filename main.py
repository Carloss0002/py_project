import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget


from router import Router
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        screen = QApplication.primaryScreen()
        screen_rect = screen.availableGeometry()
        width = int(screen_rect.width() * 0.5)
        height = int(screen_rect.height() * 0.5)
        self.setGeometry(0, 0, width, height)
        self.router = Router(width)

        nav_layout = QVBoxLayout()
        nav_layout.addWidget(self.router)
        container = QWidget()
        container.setLayout(nav_layout)
        container.setContentsMargins(0, 0, 0, 0)

        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())