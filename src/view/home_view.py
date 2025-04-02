from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QListWidgetItem, QDialog, QDialogButtonBox, QLineEdit, QMessageBox
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

from src.controller.register_finance import RegisterFinance




class FinanceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance App")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.initUI()

    def initUI(self):
        main_layout = QVBoxLayout()

        # Top Cards
        card_layout = QHBoxLayout()
        card_layout.addWidget(self.create_card("Balance", "R$ 4.500", "green"))
        card_layout.addWidget(self.create_card("Expense", "R$ 2.000", "red"))
        card_layout.addWidget(self.create_card("Savings", "R$ 16.000", "blueviolet"))
        main_layout.addLayout(card_layout)

        # Botões
        btn_layout = QHBoxLayout()
        btn_add_balance = self.create_button("Add Balance", "green")
        btn_add_savings = self.create_button("Add Savings", "blue")
        btn_add_expense = self.create_button("Add Expense", "red")

        btn_layout.addWidget(btn_add_balance)
        btn_add_balance.clicked.connect(lambda: self.open_modal('balance'))
        btn_layout.addWidget(btn_add_savings)
        btn_add_savings.clicked.connect(lambda: self.open_modal('savings'))
        btn_layout.addWidget(btn_add_expense)
        btn_add_expense.clicked.connect(lambda: self.open_modal('expense'))

        main_layout.addLayout(btn_layout)


        history_layout = QHBoxLayout()
        self.expense_list = self.create_history_list("Expense history")
        self.saving_list = self.create_history_list("Savings Historyc")
        history_layout.addWidget(self.expense_list)
        history_layout.addWidget(self.saving_list)

        main_layout.addLayout(history_layout)
        self.setLayout(main_layout)


        self.add_expense("Spotify", "R$ 24,00", "10/08/1998")
        self.add_saving("R$ 300", "10/08/1998")

    def create_card(self, title, value, color):
        widget = QWidget()
        layout = QVBoxLayout()
        label_title = QLabel(title)
        label_title.setStyleSheet("border: none;")
        label_title.setFont(QFont("Arial", 10))
        label_value = QLabel(value)
        label_value.setStyleSheet("border: none;")
        label_value.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(label_title)
        layout.addWidget(label_value)
        widget.setLayout(layout)
        widget.setStyleSheet(f"background-color: white; border-left: 3px solid {color}; border-radius: 5px; padding: 10px;")
        return widget

    def create_button(self, text, color):
        btn = QPushButton(text)
        btn.setStyleSheet(f"background-color: {color}; color: white; padding: 8px; font-weight: bold; border-radius: 5px;")
        return btn

    def create_history_list(self, title):
        widget = QWidget()
        layout = QVBoxLayout()
        label = QLabel(title)
        label.setFont(QFont("Arial", 12, QFont.Bold))
        list_widget = QListWidget()
        layout.addWidget(label)
        layout.addWidget(list_widget)
        widget.setLayout(layout)
        widget.setStyleSheet("background: #FFF; border-radius: 10px;")
        widget.list_widget = list_widget
        return widget

    def add_expense(self, name, value, date):
        item = QListWidgetItem(f"⬇️  {name} - {value}  |  {date}")
        item.setForeground(QColor("red"))
        self.expense_list.layout().itemAt(1).widget().addItem(item)

    def add_saving(self, value, date):
        item = QListWidgetItem(f"⬆️  {value}  |  {date}")
        item.setForeground(QColor("blue"))
        self.saving_list.layout().itemAt(1).widget().addItem(item)

    def open_modal(self, action):

        modal = MyModalDialog(self, action)


        modal.exec_()

class MyModalDialog(QDialog):
        def __init__(self, parent=None, action=None):
            super().__init__(parent)
            name = 'Adicionar Receita' if action == 'balance' else 'Adicionar Despesa' if action == 'expense' else "Adicionar Poupança"

            self.setWindowTitle(f'{name}')
            self.setGeometry(150, 150, 500, 250)

            self.setStyleSheet("""
                      QLineEdit {
                          font-size: 16px;
                          color: #333;
                          border: 2px solid black;  
                          padding: 10px;
                          border-radius: 5px;  
                          margin-bottom: 22px;
                      }
                      QLineEdit:focus {
                          border-color: gray
                          ;
                      }
                  """)

            # Layout da janela modal
            modal_layout = QVBoxLayout(self)
            modal_input_div = self.modal_layout(action)
            # Adiciona um botão de confirmação (OK) e de cancelamento na janela modal
            self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
            self.button_box.accepted.connect(lambda: self.register_expense(action))  # Fecha a janela quando o botão Ok for pressionado
            self.button_box.rejected.connect(self.reject)  # Fecha a janela quando o botão Cancelar for pressionado

            # Adiciona os botões ao layout
            modal_layout.addLayout(modal_input_div)
            modal_layout.addWidget(self.button_box)

            # Define o layout da janela modal
            self.setLayout(modal_layout)

        def modal_layout(self, typeElement):
            modal_input_div = QVBoxLayout()
            modal_input_div.setAlignment(Qt.AlignCenter)

            if typeElement == 'balance':
                self.label_value = QLabel('Valor: ')
                self.label_value.setContentsMargins(10, 0, 0, 5)
                self.input_value = QLineEdit()
                self.input_value.setContentsMargins(10, 0, 10, 0)

                modal_input_div.addWidget(self.label_value)
                modal_input_div.addWidget(self.input_value)

            elif typeElement == 'savings':
                self.label_value_savings = QLabel('Valor: ')
                self.label_value_savings.setContentsMargins(10, 0, 0, 5)
                self.input_value_savings = QLineEdit()
                self.input_value_savings.setContentsMargins(10, 0, 10, 0)

                modal_input_div.addWidget(self.label_value_savings)
                modal_input_div.addWidget(self.input_value_savings)

            elif typeElement == 'expense':
                self.label_description_expense = QLabel('Descrição: ', self)
                self.label_description_expense.setContentsMargins(10, 0, 0, 5)
                self.input_description_expense = QLineEdit()
                self.input_description_expense.setContentsMargins(10, 0, 10, 0)
                self.label_value_expense = QLabel('Valor: ')
                self.label_value_expense.setContentsMargins(10, 0, 0, 5)
                self.input_value_expense = QLineEdit()
                self.input_value_expense.setContentsMargins(10, 0, 10, 0)
                modal_input_div.addWidget(self.label_description_expense)
                modal_input_div.addWidget(self.input_description_expense)

                modal_input_div.addWidget(self.label_value_expense)
                modal_input_div.addWidget(self.input_value_expense)

            return modal_input_div

        def message_box(self, message, type_box):
            if not type_box:
                QMessageBox.warning(self, 'error', message)
            else:
                QMessageBox.information(self, 'Sucesso', message)

        def register_expense(self, type_element):
            register_expense_controller = RegisterFinance()
            if type_element == 'balance':
                input_balance = self.input_value.text()
                result = register_expense_controller.register_balance(input_balance)
                self.message_box(result["message"], result["check"])
            elif type_element == 'savings':
                input_savings = self.input_value_savings.text()
                result = register_expense_controller.register_savings(input_savings)
                self.message_box(result["message"], result["check"])
            elif type_element == 'expense':
                input_description_expense = self.input_description_expense.text()
                input_expense = self.input_value_expense.text()
                result = register_expense_controller.register_expense(input_expense, input_description_expense)
                print(result.values())
                self.message_box(result["message"], result["check"])


            return  self.accept()