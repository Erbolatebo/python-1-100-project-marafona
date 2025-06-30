import random
import string

# Получаем длину пароля от пользователя
length = int(input("Введите длину пароля: "))

# Проверяем, что длина пароля разумная (например, больше 0)
if length <= 0:
    print("Длина пароля должна быть больше 0!")
else:
    # Собираем все возможные символы
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Генерируем пароль
    password = ''.join(random.choices(all_chars, k=length))
    
    # Выводим готовый пароль
    print("Ваш пароль:", password)