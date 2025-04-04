from src.model.connector import BancoDeDados

class LoginDataBase():

    def __init__(self):
        self.db = BancoDeDados()
        self.data = 'users'

    def Search_User(self, email=None):
        try:
            connection = self.db.connect_database(self.data)
            myCursor = connection.cursor()

            query = 'SELECT * FROM user WHERE Email = %s'
            values = (email)

            myCursor.execute(query, (values, ))

            user = myCursor.fetchone()

            return user is None

        except Exception as e:
            print(f'não foi dessa vez {e}')

    def Search_User_Login(self, email, senha):
        try:
            connection = self.db.connect_database(self.data)
            myCursor = connection.cursor()
            query = 'SELECT * FROM user WHERE Email = %s AND Senha = %s'
            values = (email, senha)

            myCursor.execute(query, (values))

            userInfo = myCursor.fetchone()


            if not userInfo is None:
                password = userInfo[2]

                if password != senha:
                    return {"message": "Senha/email invalidos", "logged":False}

                return {"logged": True}
            else:
                return {"logged": False, "message": "Usuário não detectado"}
        except Exception as e:
            print(f'não foi dessa vez {e}')

    def write_to_table(self, email, password):
        try:
            if self.Search_User(email):
                data = 'users'
                connection = self.db.connect_database(data)
                myCursor = connection.cursor()
                query = 'INSERT INTO user (EMAIL, SENHA) values (%s, %s);'
                values = (email, password)

                myCursor.execute(query, values)
                connection.commit()

                myCursor.close()
                connection.close()
                return True
            else:
                return {"message": 'Este Usuário já existe', "logged": False}

        except BaseException as e:
            print(e)
            return {"message": e, "logged": False}