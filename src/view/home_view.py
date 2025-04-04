from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QPushButton, QListWidget, QListWidgetItem, QDialog, QDialogButtonBox, QLineEdit, QMessageBox, QScrollArea
)
from PyQt5.QtGui import QFont, QColor, QIcon
from PyQt5.QtCore import Qt, pyqtSignal, QSize
from functools import partial

from src.controller.register_finance import RegisterFinance

class FinanceApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Finance App")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #f0f0f0;")
        self.initUI()

    def get_info(self, value=0):
        controlle_receive = RegisterFinance()
        response = controlle_receive.get_balance()

        return  f"{response}"

    def get_info_savings(self):
        controlle_receive = RegisterFinance()
        response = controlle_receive.get_savings()
        print(response)
        return response

    def get_info_expense(self):
        controlle_receive = RegisterFinance()
        response = controlle_receive.get_expense()

        return response


    def initUI(self):
        main_layout = QVBoxLayout()

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_saving = QScrollArea()
        self.scroll_area_saving.setWidgetResizable(True)
        self.scroll_area_saving.setStyleSheet('border: none;')
        self.card_layout = QHBoxLayout()

        self.expense_list_widget = QListWidget()
        self.savings_list_widget = QListWidget()

        self.balance_value = self.get_info()
        self.expense_value = self.get_info_expense()
        self.savings_value = self.get_info_savings()


        widget = QWidget()
        layout = QVBoxLayout()

        self.label_title = QLabel('Balance')
        self.label_title.setStyleSheet("border: none;")
        self.label_title.setFont(QFont("Arial", 10))
        self.label_value_balance = QLabel(f'R$ {self.balance_value}')
        self.label_value_balance.setStyleSheet("border: none;")
        self.label_value_balance.setFont(QFont("Arial", 16, QFont.Bold))

        layout.addWidget(self.label_title)
        layout.addWidget(self.label_value_balance)
        widget.setLayout(layout)
        widget.setStyleSheet("background-color: white; border-left: 3px solid green; border-radius: 5px; padding: 10px;")

        widget_expense = QWidget()
        layout = QVBoxLayout()
        self.label_title_expense = QLabel('Expense')
        self.label_title_expense.setStyleSheet("border: none;")
        self.label_title_expense.setFont(QFont("Arial", 10))
        self.label_value_expense = QLabel(f'R$ {self.expense_value["value"]}')
        self.label_value_expense.setStyleSheet("border: none;")
        self.label_value_expense.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(self.label_title_expense)
        layout.addWidget(self.label_value_expense)
        widget_expense.setLayout(layout)
        widget_expense.setStyleSheet(
            "background-color: white; border-left: 3px solid red; border-radius: 5px; padding: 10px;")

        widget_savings = QWidget()
        layout = QVBoxLayout()
        self.label_title_savings = QLabel('Savings')
        self.label_title_savings.setStyleSheet("border: none;")
        self.label_title_savings.setFont(QFont("Arial", 10))
        self.label_value_savings = QLabel(f'R$ {self.savings_value["value"]}')
        self.label_value_savings.setStyleSheet("border: none;")
        self.label_value_savings.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(self.label_title_savings)
        layout.addWidget(self.label_value_savings)
        widget_savings.setLayout(layout)
        widget_savings.setStyleSheet(
            "background-color: white; border-left: 3px solid blueviolet; border-radius: 5px; padding: 10px;")

        self.card_layout.addWidget(widget)
        self.card_layout.addWidget(widget_expense)
        self.card_layout.addWidget(widget_savings)

        main_layout.addLayout(self.card_layout)

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
        self.expense_list = self.create_history_list("Expense History")
        self.saving_list = self.create_history_list("Savings History")

        self.setLayout(main_layout)

        self.populate_initial_data()

        self.scroll_area.setWidget(self.expense_list)
        self.scroll_area_saving.setWidget(self.saving_list)
        self.scroll_area.setStyleSheet('border: none;')
        self.layout().addWidget(self.scroll_area)
        history_layout.addWidget(self.scroll_area)
        history_layout.addWidget(self.scroll_area_saving)
        main_layout.addLayout(history_layout)
    """def create_card(self, title, value, color):
        widget = QWidget()
        layout = QVBoxLayout()
        label_title = QLabel(title)
        label_title.setStyleSheet("border: none;")
        label_title.setFont(QFont("Arial", 10))
        label_value = QLabel('R$ '+value)
        label_value.setStyleSheet("border: none;")
        label_value.setFont(QFont("Arial", 16, QFont.Bold))
        layout.addWidget(label_title)
        layout.addWidget(label_value)
        widget.setLayout(layout)
        widget.setStyleSheet(f"background-color: white; border-left: 3px solid {color}; border-radius: 5px; padding: 10px;")
        return widget"""

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

    """def open_modal(self, action):

        modal = MyModalDialog(self, action)


        modal.exec_()"""

    def open_modal(self, action):
        modal = QDialog(self)
        name = 'Adicionar Receita' if action == 'balance' else 'Adicionar Despesa' if action == 'expense' else "Adicionar Poupança"
        modal.setWindowTitle(name)
        modal.setGeometry(150, 150, 500, 250)
        modal.setStyleSheet("""
                     QLineEdit {
                         font-size: 16px;
                         color: #333;
                         border: 2px solid black;
                         padding: 10px;
                         border-radius: 5px;
                         margin-bottom: 22px;
                     }
                     QLineEdit:focus {
                         border-color: gray;
                     }
                 """
           )

        modal_layout = QVBoxLayout(modal)
        modal_input_div = QVBoxLayout()
        modal_input_div.setAlignment(Qt.AlignCenter)

        if action == 'balance':
               self.label_value = QLabel('Valor: ')
               self.label_value.setContentsMargins(10, 0, 0, 5)
               self.input_value = QLineEdit()
               self.input_value.setContentsMargins(10, 0, 10, 0)
               modal_input_div.addWidget(self.label_value)
               modal_input_div.addWidget(self.input_value)

        elif action == 'savings':
               label_description_savings = QLabel('Descrição: ')
               label_description_savings.setContentsMargins(10, 0, 0, 5)
               self.input_description_savings = QLineEdit()
               self.input_description_savings.setContentsMargins(10, 0, 10, 0)

               label_value_savings = QLabel('Valor: ')
               label_value_savings.setContentsMargins(10, 0, 0, 5)
               self.input_value_savings = QLineEdit()
               self.input_value_savings.setContentsMargins(10, 0, 10, 0)

               modal_input_div.addWidget(label_description_savings)
               modal_input_div.addWidget(self.input_description_savings)
               modal_input_div.addWidget(label_value_savings)
               modal_input_div.addWidget(self.input_value_savings)

        elif action == 'expense':
               self.label_description_expense = QLabel('Descrição: ')
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

        self.modal_close = modal.accept
        modal_layout.addLayout(modal_input_div)
        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        button_box.accepted.connect(lambda: self.register_expense(action))
        button_box.rejected.connect(modal.reject)
        modal_layout.addWidget(button_box)
        modal.setLayout(modal_layout)
        modal.exec_()

    def message_box(self, message, type_box):
        if not type_box:
            QMessageBox.warning(self, 'error', message)
        else:
            QMessageBox.information(self, 'Sucesso', message)

    def register_expense(self, type_element):
        register_expense_controller = RegisterFinance()

        if type_element == 'balance':
            balance_value = self.get_info()
            input_balance = self.input_value.text()
            result = register_expense_controller.register_balance(input_balance, balance_value, 'add')
            self.message_box(result["message"], result["check"])
            if result["check"]:
                balance_value = self.get_info()
                self.label_value_balance.setText(f"R$ {balance_value}")

        elif type_element == 'savings':
            input_savings = self.input_value_savings.text()
            description_savings = self.input_description_savings.text()
            result = register_expense_controller.register_savings(input_savings, description_savings)
            self.message_box(result["message"], result["check"])
            if result["check"]:
                savings_value = self.get_info_savings()
                self.label_value_savings.setText(f"R$ {savings_value["value"]}")
                value = savings_value["json_values"][-1]["value"]
                description = savings_value["json_values"][-1]["description"]
                self.add_item_list(value, description)

        elif type_element == 'expense':
            balance_value = self.get_info()
            input_description_expense = self.input_description_expense.text()
            input_expense = self.input_value_expense.text()
            result = register_expense_controller.register_expense(input_expense, input_description_expense)
            result_balance = register_expense_controller.register_balance(input_expense, balance_value, 'min')
            self.message_box(result["message"], result["check"])
            if result["check"]:
                if result_balance["check"]:
                    balance_value = self.get_info()
                    self.label_value_balance.setText(f"R$ {balance_value}")
                expense_value = self.get_info_expense()
                self.label_value_expense.setText(f"R$ {expense_value["value"]}")
                value = expense_value["json_values"][-1]["value"]
                description = expense_value["json_values"][-1]["description"]
                print(expense_value)
                self.add_item_expense_list(value, description, 1)

        return self.modal_close()

    def populate_initial_data(self):
        if "json_values" in self.expense_value and self.expense_value["json_values"]:
            for card in self.expense_value["json_values"]:
                item = QListWidgetItem()

                widget = QWidget()
                layout = QHBoxLayout()
                layout.setContentsMargins(0, 0, 0, 0)  # Margens internas

                btn_icon = QPushButton()
                btn_icon.setIcon(QIcon("src/assets/arrow_down.png"))  # Ícone do botão
                btn_icon.setFixedSize(QSize(32, 32))  # Tamanho fixo
                btn_icon.setStyleSheet("border: none; background: transparent;")

                label = QLabel(f" {card['description']} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  R$ {card['value']}  ")
                label.setTextFormat(Qt.RichText)
                widget.setStyleSheet("background-color: #D9D9D9; padding: 10px; font-size: 14px;")

                btn_delete = QPushButton()
                btn_delete.setIcon(QIcon("src/assets/trash.png"))  # Substitua pelo caminho do seu ícone
                btn_delete.setFixedSize(QSize(32, 32))
                btn_delete.setStyleSheet("border: none;")
                btn_delete.clicked.connect(partial(self.delete_item_card, card["id"]))

                layout.addWidget(btn_icon)
                layout.addWidget(label)
                layout.addWidget(btn_delete)

                widget.setLayout(layout)
                widget.setFixedHeight(91)

                item.setSizeHint(widget.sizeHint())


                self.expense_list.layout().itemAt(1).widget().addItem(item)
                self.expense_list.layout().addWidget(widget)

        if "json_values" in self.savings_value and self.savings_value["json_values"]:
            for card in self.savings_value["json_values"]:
                item = QListWidgetItem()

                widget = QWidget()
                layout = QHBoxLayout()
                layout.setContentsMargins(0, 0, 0, 0)  # Margens internas

                btn_icon = QPushButton()
                btn_icon.setIcon(QIcon("src/assets/arrow_down.png"))  # Ícone do botão
                btn_icon.setFixedSize(QSize(32, 32))  # Tamanho fixo
                btn_icon.setStyleSheet("border: none; background: transparent;")

                label = QLabel(
                    f" {card['description']} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  R$ {card['value']}  ")
                label.setTextFormat(Qt.RichText)
                widget.setStyleSheet("background-color: #D9D9D9; padding: 10px; font-size: 14px;")

                btn_delete = QPushButton()
                btn_delete.setIcon(QIcon("src/assets/trash.png"))  # Substitua pelo caminho do seu ícone
                btn_delete.setFixedSize(QSize(32, 32))
                btn_delete.setStyleSheet("border: none;")
                btn_delete.clicked.connect(partial(self.delete_item_card, card["id"]))

                layout.addWidget(btn_icon)
                layout.addWidget(label)
                layout.addWidget(btn_delete)

                widget.setLayout(layout)
                widget.setFixedHeight(91)

                item.setSizeHint(widget.sizeHint())

                self.saving_list.layout().itemAt(1).widget().addItem(item)
                self.saving_list.layout().addWidget(widget)

    def add_item_list(self, value, description):
        item = QListWidgetItem(f"⬆️  {value}  |  {description}")
        item.setForeground(QColor("blue"))
        self.saving_list.layout().itemAt(1).widget().addItem(item)

    def add_item_expense_list(self, value, description, id):
        item = QListWidgetItem()

        widget = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)  # Margens internas

        btn_icon = QPushButton()
        btn_icon.setIcon(QIcon("src/assets/arrow_down.png"))  # Ícone do botão
        btn_icon.setFixedSize(QSize(32, 32))  # Tamanho fixo
        btn_icon.setStyleSheet("border: none; background: transparent;")

        label = QLabel(f" {description} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  R$ {value}  ")
        label.setTextFormat(Qt.RichText)
        widget.setStyleSheet("background-color: #D9D9D9; padding: 10px; font-size: 14px;")

        btn_delete = QPushButton()
        btn_delete.setIcon(QIcon("src/assets/trash.png"))  # Substitua pelo caminho do seu ícone
        btn_delete.setFixedSize(QSize(32, 32))
        btn_delete.setStyleSheet("border: none;")
        btn_delete.clicked.connect(partial(self.delete_item_card, id))

        layout.addWidget(btn_icon)
        layout.addWidget(label)
        layout.addWidget(btn_delete)

        widget.setLayout(layout)
        widget.setFixedHeight(91)

        item.setSizeHint(widget.sizeHint())

        self.expense_list.layout().itemAt(1).widget().addItem(item)
        self.expense_list.layout().addWidget(widget)

    def delete_item_card(self, id):
        print(id)

    def update_status(self):
        """Atualiza a renderização condicional com base nos itens da lista"""
        if self.expense_list_widget.count() == 0 and self.savings_list_widget.count() == 0:
            self.status_label.setText("Nenhum dado cadastrado")
        else:
            self.status_label.setText("Dados cadastrados!")

    def atualizar_cards(self, type_element, value):
        print(value)
        self.label_value.setText('R$ 2'+value)



class MyModalDialog(QDialog):
        def __init__(self, parent=None, action=None):
            super().__init__(parent)
            self.parent = parent
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
                self.label_description_savings = QLabel('Descrição: ', self)
                self.label_description_savings.setContentsMargins(10, 0, 0, 5)
                self.input_description_savings = QLineEdit()
                self.input_description_savings.setContentsMargins(10, 0, 10, 0)

                self.label_value_savings = QLabel('Valor: ')
                self.label_value_savings.setContentsMargins(10, 0, 0, 5)
                self.input_value_savings = QLineEdit()
                self.input_value_savings.setContentsMargins(10, 0, 10, 0)

                modal_input_div.addWidget(self.label_description_savings)
                modal_input_div.addWidget(self.input_description_savings)
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
            balance = FinanceApp()

            if type_element == 'balance':
                input_balance = self.input_value.text()
                result = register_expense_controller.register_balance(input_balance)
                self.message_box(result["message"], result["check"])
                self.termo_aceito.emit()

            elif type_element == 'savings':
                input_savings = self.input_value_savings.text()
                description_savings = self.input_description_savings.text()
                result = register_expense_controller.register_savings(input_savings, description_savings)
                self.message_box(result["message"], result["check"])
            elif type_element == 'expense':
                input_description_expense = self.input_description_expense.text()
                input_expense = self.input_value_expense.text()
                result = register_expense_controller.register_expense(input_expense, input_description_expense)
                self.message_box(result["message"], result["check"])


            return  self.accept()