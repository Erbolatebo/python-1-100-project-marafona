num1=float(input())
num2=float(input())
func=input()
if func=='+':
    print(num1, '+', num2, '=', num1+num2)
elif func=='-':
    print(num1, '-', num2, '=', num1-num2)
elif func=='*':
    print(num1, '*', num2, '=', num1*num2)      
elif func=='/':
    print(num1, '/', num2, '=', num1/num2)
elif func=='^':
    print(num1, '^', num2, '=', num1**num2)      
elif func=='//':
    print(num1, '//', num2, '=', num1//num2)    
elif func=='%':
    print(num1, '%', num2, '=', num1%num2)    
else:
    print('Ошибка!')   

