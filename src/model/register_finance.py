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