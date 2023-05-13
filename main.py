import random
import string

def generate_password(length):
    # Создаем строку, содержащую все символы, которые могут использоваться в пароле
    characters = string.ascii_letters + string.digits + string.punctuation

    # Генерируем пароль из случайных символов
    password = ''.join(random.choice(characters) for i in range(length))

    return password

# Пример использования
password = generate_password(12)
print(password)
