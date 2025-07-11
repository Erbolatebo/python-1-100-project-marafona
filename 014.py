tasks = []

while True:
    print('1. Показать задачи')
    print('2. Добавить задачу')
    print('3. Удалить задачу')
    print('4. Выход')

    try:
        input_text = int(input('Выберите действие: '))

        if input_text == 1:
            if not tasks:
                print("Список задач пуст!")
            else:
                print("\nСписок задач:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            print()

        elif input_text == 2:
            task = input('Введите задачу: ')
            tasks.append(task)
            print("Задача добавлена!\n")

        elif input_text == 3:
            if not tasks:
                print("Список задач пуст! Нечего удалять.\n")
            else:
                print("\nСписок задач:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                try:
                    task_num = int(input("Введите номер задачи для удаления: "))
                    if 1 <= task_num <= len(tasks):
                        tasks.pop(task_num - 1)
                        print("Задача удалена!\n")
                    else:
                        print("Некорректный номер задачи!\n")
                except ValueError:
                    print("Пожалуйста, введите число!\n")

        elif input_text == 4:
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор! Выберите число от 1 до 4.\n")

    except ValueError:
        print("Пожалуйста, введите число!\n")