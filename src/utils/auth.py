from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return password_context.hash(password)
