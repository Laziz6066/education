number = 0
x = 9
attempt = 0
while number != x:
    number = int(input('Введите число: '))
    if number > x:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    attempt += 1
print('Вы угадали! Число попыток: ', attempt)

