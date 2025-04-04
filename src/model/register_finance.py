from src.model.connector import BancoDeDados

class RegisterFinanceModel():
    def __init__(self):
        self.db = BancoDeDados()
        self.data = 'users'

    def register_values(self, info='balance', value=None):
        try:
            connection = self.db.connect_database(self.data)
            cursor = connection.cursor()


            query = 'INSERT INTO finance (ID_USER,INFO, VALOR) values (%s, %s, %s);'
            values = (1,info, value)

            cursor.execute(query, values)
            connection.commit()

            cursor.close()
            connection.close()
            return {"message": 'Valor Balance Cadastrado com Sucesso', "response":True}
        except Exception as e:
            print(f"error {e}")
            return {"message": str(e), "response":False}

    def update_values(self, value=None):
        try:
            connection = self.db.connect_database(self.data)
            cursor = connection.cursor()

            query = "UPDATE finance SET valor = %s WHERE info = 'balance'"
            values = (value, )

            cursor.execute(query, values)
            connection.commit()

            cursor.close()
            connection.close()
            return {"message": 'Valor Balance alterado com Sucesso', "response": True}
        except Exception as e:
            print(f"error {e}")
            return {"message": str(e), "response": False}

    def balance_exists(self):
        try:
           connection = self.db.connect_database(self.data)
           cursor = connection.cursor()

           query = 'SELECT * FROM finance WHERE id_user = %s AND info = balance'
           value = (1, )

           cursor.execute(query, value)

           balance_value = cursor.fetchone()

           cursor.close()
           connection.close()

           return balance_value is not None

        except Exception as e:
            return {"message":str(e), "response":False}

    def get_all_receives(self, id_user=1, info_operation='balance'):
        try:
            connection = self.db.connect_database(self.data)
            cursor = connection.cursor()

            query = 'SELECT * FROM finance WHERE id_user = %s AND info = %s'
            value = (id_user, info_operation)

            cursor.execute(query, value)

            user_finance = cursor.fetchall()

            cursor.close()
            connection.close()
            if not user_finance:
                return {"message": '0', "response":False}
            else:
                return  {"message":  user_finance, "response":True}

        except Exception as e:
            print(f"error: {e}")
            return {"message": str(e), "response":False}