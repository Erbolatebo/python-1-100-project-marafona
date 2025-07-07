num = int(input("Введите число:"))
total=1

for i in range(1,num+1):
    total *= i
    
print("Из введенного цифра", num, "получили факториал", total)    