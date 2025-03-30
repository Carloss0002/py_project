import re

class LoginUser:

    def validate_email(self,email):
        padrao = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        print(re.match(padrao, email))
        return re.match(padrao, email) is not None

    def validate_user(self, email, password):
        logged = False

        if email == '' and password == '':
            message = 'Error: Campos importantes vazios'
            print(email)
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

    def login_user(self,email, password):
        result = self.validate_user(email, password)

        return result

    def register_user(self, email, password):
       result = self.validate_user(email, password)

       return result