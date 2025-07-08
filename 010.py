import time

def countdown_timer(hours, minutes, seconds):
    # Проверка на корректность ввода
    if hours < 0 or minutes < 0 or seconds < 0:
        print("Ошибка: Время не может быть отрицательным!")
        return
    if minutes >= 60 or seconds >= 60:
        print("Ошибка: Минуты и секунды должны быть меньше 60!")
        return

    # Переводим всё время в секунды для упрощения обработки
    total_seconds = hours * 3600 + minutes * 60 + seconds

    if total_seconds == 0:
        print("Таймер завершён!")
        return

    # Обратный отсчёт
    while total_seconds > 0:
        # Вычисляем часы, минуты и секунды из total_seconds
        h = total_seconds // 3600
        m = (total_seconds % 3600) // 60
        s = total_seconds % 60
        # Форматируем вывод в формате HH:MM:SS
        print(f"{h:02d}:{m:02d}:{s:02d}", end="\r")  # \r для перезаписи строки
        time.sleep(1)
        total_seconds -= 1

    print("Таймер завершён!")

# Получение ввода от пользователя
try:
    hours = int(input("Введите часы: "))
    minutes = int(input("Введите минуты: "))
    seconds = int(input("Введите секунды: "))
    countdown_timer(hours, minutes, seconds)
except ValueError:
    print("Ошибка: Введите целые числа!")