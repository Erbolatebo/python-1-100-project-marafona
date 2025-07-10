temp = float(input("Введите температуру: "))
unit = input("В какой единице указано? (C/F): ").upper()

result = 0

if unit == 'C':
    F = (temp * (9 / 5)) + 32
    result = round(F,1)
    print(f"{temp}°{unit} = {result}°F")
elif unit == 'F':
    C = (temp - 32) * (5 / 9)
    result = round(C,1)
    print(f"{temp}°{unit} = {result}°C")
else:
    print("Ошибка: нужно ввести только 'C' или 'F'")   


