import math

weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))

bmi = weight / math.pow(height,2)

if 18.5<=bmi<=24.9:
    print("Ваш ИМТ:", bmi, "- Нормальный")
elif bmi<18.5:
    print("Ваш ИМТ:", bmi, "- Недостаточный вес")
elif 25<=bmi<=29.9:
    print("Ваш ИМТ:", bmi, "- Избыточный вес")
elif bmi>=30:
    print("Ваш ИМТ:", bmi, "- Ожирение")            