from src.model.login_model import LoginDataBase
import re


class LoginUser:

    def validate_email(self,email):
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(padrao, email) is not None

    def validate_user(self, email, password):
        logged = False

        if email == '' and password == '':
            message = 'Error: Campos importantes vazios'
            return {"message": message, "logged": logged}
        elif email == '':
            message = 'Error: Campo de email vazio'
            return {"message": message, "logged": logged}
        elif password == '':
            message = 'Error: Não foi possível validar o cliente. Campo de senha vazio'
            return {"message": message, "logged": logged}
        else:
            logged = True

            return {"logged": logged}

    def register_user(self, email, password):
       result = self.validate_user(email, password)

       if result["logged"]:

           send_userData = LoginDataBase()

           result = send_userData.write_to_table(email, password)

           if result:

                return {"message": 'Usuário criado com sucesso', "logged": True}
           else:
               return result
       else:
           return result

    def login_user(self, email, password):

        result = self.validate_user(email, password)

        if result["logged"]:
            search_user_login = LoginDataBase()

            result = search_user_login.Search_User_Login(email, password)

            if result["logged"]:
               return  {"message": 'Bem Vindo', "logged": True}
            else:
                return result

        return result