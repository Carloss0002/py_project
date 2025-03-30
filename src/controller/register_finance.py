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

    def register_savings(self, value):
        return_test = self.test_balance_savings(value)

        return return_test

    def register_balance(self, value):

        return_test = self.test_balance_savings(value)

        return return_test