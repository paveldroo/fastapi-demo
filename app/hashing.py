from passlib.context import CryptContext


class Hash:
    @staticmethod
    def bcrypt(password: str):
        pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')
        return pwd_cxt.hash(password)
