import random

print('Я загадал число от 1 до 100. Попробуй угадать!')
secret = random.randint(1, 100)  # Исправлено: randint вместо randit
attempts = 0

while True:
    try:
        n = int(input('Введи число: '))  # Ввод внутри цикла
        attempts += 1
        
        if n < secret:
            print('Слишком мало!')
        elif n > secret:
            print('Слишком много!')
        else:
            print(f'Ты угадал! Число было {secret}. Попыток: {attempts}')
            break
            
    except ValueError:
        print('Ошибка: Введи целое число!')
        attempts += 1  # Можно не считать попытку при ошибке, если хочешь

# Предложение сыграть снова
play_again = input('Хочешь сыграть ещё раз? (да/нет): ').lower()
if play_again in ['да', 'yes', 'д']:
    # Здесь можно перезапустить игру, вызвав функцию или рекурсию
    print('Новую игру пока не запрограммировали, но ты крут!')