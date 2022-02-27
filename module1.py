print('Задача 2. Максимум из трёх чисел 2')
number1=int(input('Введите первое число: '))
number2=int(input('Введите второе число: '))
number3=int(input('Введите третье число: '))
if number1 > number2 and number1 > number3:
    print('Первое число самое большое!')
elif  number2 > number3:
    print('Второе число самое большое!')
else:
    print('Третье число самое большое!')
print('//////////////////////////////////////')
