import json

from src.model.register_finance import RegisterFinanceModel

class RegisterFinance():
    def message_return(self, message, check):
        return {"message": message, "check":check}

    def number_test(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def convert_number(self, value:str):
        remove_comma = value.replace(',', '.')
        convert_for_number = float(remove_comma)

        return convert_for_number

    def register_expense(self, value, description):
        check = False
        if value == '' and description == '':
            message = 'Error: Ambos os valores estão vazios'
            return self.message_return(message, check)
        elif value == '':
            message = 'Error: Valor não enviado'
            return self.message_return(message, check)
        elif description == '':
            message = 'Error: Descrição não encontrada'
            return self.message_return(message, check)
        else:
            if self.number_test(value):
                converted_number = self.convert_number(value)
                description_card = description
                test = {"number": converted_number, "description": description_card}

                message = 'Despesa cadastrada com sucesso'
                check = True
                return self.message_return(message, check)

            else:
                message = 'Error: Valor não válido'
                return self.message_return(message, check)

    def test_balance_savings(self, value):
        if value == '':
            return self.message_return('Error: Não encontramos valor no card cadastrado', False)
        elif self.number_test(value):
            return self.message_return('Error: Tipo não aceito', False)
        else:
            return self.message_return("Error: Nenhuma ação a partir daqui tente novamente", False)

    def register_savings(self, value, description):
        if self.number_test(value):
            controller_send_savings = RegisterFinanceModel()
            expense_data = {
                "value": value,
                "description": description
            }

            expense_json = json.dumps(expense_data)

            result = controller_send_savings.register_values('savings', expense_json)

            return self.message_return(result["message"], result["response"])
        else:
            return self.test_balance_savings(value)

    def register_balance(self, value, old_value,calc):
        controller_requisition = RegisterFinanceModel()

        if self.number_test(value) and not controller_requisition.balance_exists():
            controller_send_balance = RegisterFinanceModel()

            result = controller_send_balance.register_values('balance', value)

            return  self.message_return(result["message"], result["response"])
        elif self.number_test(value) and  controller_requisition.balance_exists():
            if calc == 'add':
                sum = float(old_value) + float(value)
                result_calc = str(sum)
            else:
                min = float(old_value) - float(value)
                result_calc = str(min)

            result = controller_requisition.update_values(result_calc)
            return  self.message_return(result["message"], result["response"])
        else:
            return self.test_balance_savings(value)

    def register_expense(self, value, description):

        if self.number_test(value):
            controller_send_balance = RegisterFinanceModel()
            expense_data = {
                "value": value,
                "description": description
            }
            expense_json = json.dumps(expense_data)

            result = controller_send_balance.register_values('expense', expense_json)

            return self.message_return(result["message"], result["response"])
        else:
            return self.test_balance_savings(value)

    def update_balance(self, value):
        pass

    def get_balance(self):
        controlle_receive = RegisterFinanceModel()
        response = controlle_receive.get_all_receives(1, 'balance')

        if response["response"]:
          all_values = response["message"]

          return all_values[-1][-1]
        else:
            return response["message"]

    def get_savings(self):
        controlle_receive = RegisterFinanceModel()
        response = controlle_receive.get_all_receives(1, 'savings')

        if response["response"]:
            all_values = response["message"]
            convert_data = [{**json.loads(value[3]), "id": value[0]} for value in all_values]
            total = sum(int(json.loads(values[3])["value"]) for values in all_values)

            return {"value":total, "json_values": convert_data}
        else:
            return {"value":response["message"]}

    def get_expense(self):
        controlle_receive = RegisterFinanceModel()
        response = controlle_receive.get_all_receives(1, 'expense')

        if response["response"]:
            all_values = response["message"]
            print(all_values)
            convert_data = [{**json.loads(value[3]), "id": value[0]} for value in all_values]
            total = sum(int(json.loads(values[3])["value"]) for values in all_values)
            print(total)
            return {"value": total, "json_values": convert_data}
        else:
            return {"value":response["message"]}