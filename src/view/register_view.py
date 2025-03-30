from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QSizePolicy, QGraphicsOpacityEffect, \
    QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from src.controller.login_controle import LoginUser


class RegisterView(QWidget):
    def __init__(self, on_login_success, width):
        super().__init__()
        self.on_login = on_login_success

        self.setStyleSheet("""
            QLineEdit {
                font-size: 16px;
                color: #333;
                border: 2px solid black;  /* Cor da borda */
                padding: 8px;
                border-radius: 5px;  /* Borda arredondada */
                margin-bottom: 22px;
            }
            QLineEdit:focus {
                border-color: gray
                ;  /* Cor da borda ao focar */
            }
            QWidget {
                background-color: black;
            }
        """)
        layout_principal = QVBoxLayout(self)
        layout_principal.setAlignment(Qt.AlignCenter)
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)

        width_range = int(width * 0.7)

        range = QWidget()
        range.setFixedWidth(width_range)
        range.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        range.setStyleSheet("background-color: white; border-radius: 10px; opacity: 0.5;")

        range_layout = QVBoxLayout()
        range_layout.setAlignment(Qt.AlignCenter)

        title = QLabel("FinWise")
        title.setStyleSheet("font-size: 42px; color: #333; font-family: inter;")
        title.setAlignment(Qt.AlignCenter)
        range_layout.addWidget(title)

        self.label_email = QLabel("Email: ")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")
        range_layout.addWidget(self.label_email)
        range_layout.addWidget(self.email_input)

        self.label_password = QLabel("Senha")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Senha")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.toggle_button = QPushButton("👁")
        self.toggle_button.setCheckable(True)
        self.toggle_button.setFixedWidth(30)
        self.toggle_button.clicked.connect(self.toggle_password_visibility)

        pass_layout = QHBoxLayout()
        pass_layout.setAlignment(Qt.AlignCenter)
        pass_layout.addWidget(self.password_input)
        pass_layout.addWidget(self.toggle_button)

        range_layout.addWidget(self.label_password)
        range_layout.addLayout(pass_layout)

        login_btn = QPushButton("Cadastrar-se")
        
        register_btn = QPushButton("Já tem conta? Faça login")
        register_btn.clicked.connect(self.on_login)
        login_btn.setStyleSheet("""
            QPushButton {
                background-color: black;  /* Cor de fundo */
                color: white;  /* Cor do texto */
                font-size: 16px;  /* Tamanho da fonte */
                border-radius: 10px;  /* Bordas arredondadas */
                padding: 10px 20px;  /* Espaçamento interno */
                border: 2px solid #000000;  /* Cor da borda */
                margin-top: 22px;
                margin-bottom: 26px;
            }
            QPushButton:hover {
                background-color: #CCCCCC;  /* Cor de fundo quando o mouse passar por cima */
                color: black;
            }
            QPushButton:pressed {
                background-color: #388e3c;  /* Cor de fundo quando o botão for pressionado */
            }
        """)
        range_layout.addWidget(login_btn)
        range_layout.addWidget(register_btn)
        range.setLayout(range_layout)
        layout_principal.addWidget(range)

    def toggle_password_visibility(self):
        if self.toggle_button.isChecked():
            self.password_input.setEchoMode(QLineEdit.Normal)
            self.toggle_button.setText("🙈")
        else:
            self.password_input.setEchoMode(QLineEdit.Password)
            self.toggle_button.setText("👁")

    def register_user(self):
        register_user_class = LoginUser()
        email = self.email_input.text()
        password = self.email_input.text()
        result = register_user_class.register_user(email, password)

        if result["logged"]:
            QMessageBox.information(self, 'Bem-vindo', 'Usuário conectado com sucesso')
            self.on_login_success()
        else:
            QMessageBox.warning(self, 'error', result["message"])