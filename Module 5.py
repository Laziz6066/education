# 5.2 Вложенные условия

# print('курс стоит 75000')
# bank=int(input('Введите состояние счёта: '))
# if bank >= 75000:
#     bank-=75000
#     print('Курс успешно приобретён.')
#     if bank < 5000:
#         bank +=1000
#         print('Сделана скидка!')
# else:
#     print('Не хватает денег на счёту.')
# print('Остаток на счету: ', bank)
# print('Хорошего дня!')

# product = int(input('Введите сумму чека: '))
# delivery = int(input('Введите сумму доставки: '))
# discount = 0
# if product > 10000:
#     print('Хороший чек! Доставка снижена вдвое')
#     delivery /=2
#     if product % 2 == 0:
#         print('Покупателю положен подарок!')
#         discount = 500
# price = product + delivery - discount
# print('Полная стоимость товаров: ', price)
# Задача 2. Скидки!
# # Напишите программу для примера, разобранного в уроке.
# Пользователь покупает курс стоимостью 75 000 рублей. Если денег на счету достаточно, то нужно:
# # Списать со счёта деньги.
# Проверить баланс счёта. Если там меньше 5000 рублей, то зачислить на счёт 1000 рублей
# и вывести сообщение: «Сделана скидка».
# Вывести сообщение: «Курс успешно приобретён».
# А иначе вывести: «Не хватает денег на счету». Также в конце
# вывести остаток счёта и сообщение: «Хорошего дня!»
# # # # Пример:
# # Сколько денег на счету? 78500
# # Курс успешно приобретён
# # Сделана скидка
# # Остаток на счету: 4500
# # Хорошего дня!


# x=int(input('Введите икс: '))
# y=int(input('Введите игрек: '))
#
# if x>y:
#     plus=x
#     print('X', 'больше', 'Y')
# elif x<y:
#     plus=y
#     print('X' , 'меньше', 'Y')
# else x==y:
#     print('X', 'равен', 'Y')

# # # # Задача 3
# # Мама дала Маше денег и отправила её в магазин за сыром.
# А ещё сказала: «Если останутся деньги, то можешь купить себе мороженое.
# Если денег на сыр не хватит, то денег маловато — а значит, и мороженого не будет».
# # Сделайте программу, которая получает на вход количество денег.
# Сыр стоит 60 рублей, мороженое — 20 рублей. Если денег на сыр хватает (больше либо равно), то:
# # Выводите сообщение: «На сыр денег хватило», — и вычитайте стоимость сыра из кошелька.
# Если оставшихся денег хватает на мороженое, то выводите:
# «И на мороженое тоже!». Иначе выводите: «Денег маловато».

# money=int(input('Сколько денег у вас есть: '))
# caseus=60
# ice_cream=20
#
# if money >= caseus:
#     money -= caseus
#     print(money)
#     print('На сыр денег хватило')
#
#
# else:
#     print('Денег не хватило')
#
#
# if  money >= ice_cream:
#      print( 'И на мороженное тоже!')
#
# if  money < ice_cream:
#     print('А на мороженное нет')
#
# profit=int(input('вдите размер прибыли: '))
# if profit < 10000:
#     tax=profit * 13 /100
#     print("Размер налога (13%) равен", tax)
# elif profit < 50000:
#     tax = profit * 20 / 100
#     print("Размер налога (20%) равен", tax)
# else:
#     tax = profit * 30 / 100
#     print("Размер налога (30%) равен", tax)

#Цель задания

# Потренироваться в написании цепочек условий if-elif-else.
# Что нужно сделать
# # # # Задача 1. Координаты
# # Вернёмся к задаче про подводную лодку и её координаты.
# Теперь мы знаем, что вместо трёх отдельных проверок можно
# использовать оператор elif — «»иначе-если». То есть если одна
# координата больше другой, то будет одно сообщение, иначе если одна меньше другой, то…
# # # # Напишите программу, которая сравнивает координаты X (икс)
# и Y (игрек) и выводит соответствующий результат. Для этого используйте оператор elif.
# x=int(input('Введите икс: '))
# y=int(input('Введите игрек: '))
# if x>y:
#     plus=x
#     print('X', 'больше', 'Y')
# elif x<y:
#     plus=y
#     print('X' , 'меньше', 'Y')
# else :
#     print('X', 'равен', 'Y')
# #  # # Задача 2. Прогрессивный налог
# # В некоторых странах действует так называемая прогрессивная шкала
# налогообложения: чем больше ты зарабатываешь, тем больший налог платишь.
# Нужно написать программу, которая будет рассчитывать сумму налога исходя
# из прибыли. Если прибыль до 10 000 — ставка налога равна 13%, начиная
# с 10 000 и до 50 000 — 20%. А начиная с 50 000 — 30%. А также нужно
# добавить «проверку на дурака»: если ввели число меньше нуля,
# то вывести сообщение: «Ошибка: доход не может быть отрицательным».

# income=int(input('Введите годовой доход: '))
# if income >0 and income< 10000:
#     tax = income * 13 / 100
#     print('Налог (13%) составляет: ', tax)
# elif income >0 and income < 50000:
#     tax = income * 20 / 100
#     print('Налог (20%) составляет: ', tax)
# if income >0 and income>= 50000:
#     tax = income * 30 / 100
#     print('Налог (30%) составляет: ', tax)
# elif income <0:
#     print('Ошибка: доход не может быть отрицательным')

# # # # Задача 3. Фальшивомонетчики
# # Пете дали три монетки и сказали, что если он сможет на весах без гирь определить,
# какая из них фальшивая (более лёгкая), то сможет забрать их все.
# А Петя в одной из книжек прочитал, что для этого достаточно одного
# взвешивания: если две монеты весят одинаково, то фальшивая третья,
# а иначе фальшивая та, которая легче на весах. Напишите программу,
# которая принимает на вход вес трёх монет (две одинаковые, третья меньше) и определяет, какая из них легче.
# # # # Задания для практической работы не нужно отправлять на проверку.

# a=int(input('Введите вес первой монеты: '))
# b=int(input('Введите вес второй монеты: '))
# c=int(input('Введите вес третьей монеты: '))
# if a==b:
#     print('Третья монета фальшивая!')
# elif a==c:
#     print('Вторая монета фальшивая!')
# else:
#     print('Первая монета фальшивая!')



# Практика
# # # # Цель задания
# # Потренироваться в написании цепочек условий if-elif-else.
# # # # Что нужно сделать
# # # # Задача 1. Покупка велосипеда
# # Напишите программу, которую мы разбирали в рамках теории.
# Нашему ребёнку нужен новый хороший велосипед. Правда,
# никто из нас в них не разбирается, всё что нам нужно —
# чтобы велосипед не был устаревшим и чтоб скоростей на нём было побольше,
# а сколько он стоит — пока неважно. Чтобы не искать велосипед на сайте
# вручную, мы хотим написать программу, которая будет проверять каждый
# велосипед на нужный нам год выпуска и на количество скоростей.
# # Используя один из логических операторов (and, or),
# напишите программу из урока, которая запрашивает год
# выпуска велосипеда и количество скоростей на нём и выводит
# на экран сообщение о том, подходит этот велик или нет.
# Год выпуска — не старше 2018-го, количество скоростей — не менее 24.
# year = int(input('Введите год выпуска: '))
# speeds = int(input('Введите скорости: '))
# if year >= 2018 and speeds >= 24:
#     print('Подходит!')
# else:
#     print('Не подходит!')


# # # # Задача 2. Как поступить?
# # Илья хочет в лучший вуз страны, а для этого нужно
# не только хорошо сдать экзамены (балл должен быть больше 280),
# но и иметь золотую медаль.
# # Напишите программу, которая запрашивает у пользователя два числа:
# результат экзаменов и наличие золотой медали
# (0 — нет медали, 1 — медаль есть), а затем проверяет,
# поступил ли Илья в вуз. Выведите соответствующее сообщение.
# # # # Пример:
# # Сколько баллов набрал? 290
# # Есть медаль? 1
# # Поздравляем! Ты поступил!
# # # # Пример 2:
# # Сколько баллов набрал? 269
# # Есть медаль? 1
# # К сожалению, ты не прошёл в наш университет.
# scores=int(input('Сколько баллов набрал: '))
# medal=int(input('Есть медаль: '))
# if scores >=290 and medal >0:
#     print('Поздравляем! Ты поступил!')
# else:
#     print('К сожалению, ты не прошёл в наш университет.')


# # # # Задача 3. Бактерии живут комфортно
# # Биолог Арсений изучает микробы и их поведение при разных
# температурных нагрузках. Он помещает их в специальную среду
# , где температура скачет в промежутке от 0 до 100 градусов.
# Если же температура в среде выходит за рамки промежутка, то выводится предупреждение.
# # Напишите программу, которая запрашивает у пользователя температуру,
# и, если она меньше нуля или больше 100, то выводится сообщение об опасности.

# temperature=int(input('Введите температуру: '))
# if temperature < 0 or temperature > 100:
#     print('Опасность!!!')

# Задача 1. Калькулятор опыта
# Что нужно сделать
# Андрей любит играть в компьютерные игры. В один прекрасный день у него появилась классная
# идея для сюжета своей игры. Чтобы воплотить её в жизнь, он начал изучать программирование
# и геймдизайн. Начал он с главного героя и его системы прокачки.
# Напишите программу, которая определяет уровень персонажа в компьютерной игре. Пользователь
# вводит число «очков опыта», а программа вычисляет уровень. Новый уровень даётся при
# достижении 1000, 2500 и 5000 «очков опыта». Начальный уровень равен единице.
# Пример:
# Введите количество опыта: 6000
# Ваш уровень: 4
# Пример 2:
# Введите количество опыта: 2000
# Ваш уровень: 2

print('*****************************************************')

print('Задача 1. Калькулятор опыта')
experience=int(input('Введите количество опыта: '))
level = 1
print('Ваш уровень: ', level)
if 1000 <=  experience < 2500:
    level = 2
    print('Ваш уровень: ', level)
elif 2500 <= experience < 5000:
    level = 3
    print('Ваш уровень: ', level)
else:
    level = 4
    print('Ваш уровень: ', level)
print('*****************************************************')

# Задача 2. Максимум из трёх чисел 2
# Что нужно сделать
# # У нас уже было задание на нахождение максимума из трёх чисел с помощью
# дополнительной переменной. Теперь, когда вы знаете намного больше,
# вы можете оптимизировать программу, не тратя память компьютера на лишние переменные.
# # Напишите программу, которая находит максимум из трёх чисел, не используя дополнительные переменные.

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
print('*****************************************************')
#
# Задача 3. Функция
# Что нужно сделать
# # Учитель математики придумывает каждому своему ученику отдельные функции,
# которые нужно отобразить на графике и посчитать. А ещё этот учитель
# разбирается в программировании. Поэтому, чтобы не считать вручную все
# эти функции, он написал программу, которая делает всю работу за него.
# # Напишите программу, которая получает от пользователя число X и
# вычисляет значение функции Y по следующей схеме:
# # # # y= {x −12, x>0, 5,  x=0 x²,  x<0
# # # # Напомним, как это работает:
# # для X > 0, Y = X − 12
# # для X = 0,  Y = 5
# # для X < 0, Y = X²
# # # # Пример:
# # Введите икс: 0
# # Игрек равен 5
# # # Пример 2:
# # Введите икс: −6
# # Игрек равен 36


print('Задача 3. Функция')
x=int(input('Введите икс: '))
if x > 0:
    y = x - 12
elif x == 0:
    y = 5
else:
    y = x ** 2
print(y)
print('*****************************************************')

# Задача 4. Поступление
# Что нужно сделать
# # В университете на факультет кибернетики очень серьёзный конкурс — поступают
# только сильнейшие, первые десять человек из списка. Потом среди поступивших
# определяется, кто будет получать стипендию. Для стипендии общий балл
# при поступлении должен быть не менее 290.
# # Напишите программу, которая получает на вход место студента в списке и его балл,
# а затем выводит соответствующие сообщения о поступлении и получении стипендии.
# # # # Пример 1:
# # Введите место в списке поступающих: 3
# # Введите количество баллов за экзамены: 295
# # Поздравляем, вы поступили!
# # Бонусом вам будет начисляться стипендия.
# # # # Пример 2:
# # Введите место в списке поступающих: 3
# # Введите количество баллов за экзамены: 270
# # Поздравляем, вы поступили!
# # Но вам не хватило баллов для стипендии.
# Пример 3:
# # Введите место в списке поступающих: 11
# # К сожалению, вы не поступили.


print('Задача 4. Поступление')
list=int(input('Введите место в списке поступающих: '))
if list <= 10 :
    score = int(input('Введите количество баллов за экзамены: '))
    print('Поздравляем, вы поступили!')
    if score >= 290:
        print('Бонусом вам будет начисляться стипендия.')
    else:
        print('Но вам не хватило баллов для стипендии.')
else:
    print('К сожалению, вы не поступили.')
print('*****************************************************')

# Задача 5. Опять двойка
# Что нужно сделать
# # Папа-программист уже настолько обленился, что вместо того, чтобы самому спросить
# у сына, какую оценку тот получил в школе, он написал для этого вот такую программу:
# rating = int(input('Что получил по математике? '))
# if rating == 2:
#  print('Плохо. Марш учиться!')
# if rating == 3:
#  print('Плохо. Марш учиться!')
# if rating == 4:
#  print('Молодец! Можешь отдохнуть.')
# if rating == 5:
#  print('Молодец! Можешь отдохнуть.')
# Сын после того, как «сообщил» свою оценку, посмотрел на код программы и понял,
# что её можно улучшить, и даже рассказал папе, как это сделать, за что получил безграничное уважение отца.
# # # # Скопируйте программу в редактор и оптимизируйте:
# # При плохой оценке (2 или 3) выводится сообщение: «Плохо. Марш учиться!»
# При хорошей оценке (4 или 5) выводится сообщение: «Молодец! Можешь отдохнуть».
# В программе не должно быть повторяющихся строк.

print('Задача 5. Опять двойка')
rating = int(input('Что получил по математике? '))
if   1 < rating  < 4 :
    print('Плохо. Марш учиться!')
else:
    print('Молодец! Можешь отдохнуть.')
print('*****************************************************')

# Задача 6. Защита от дурака
# Что нужно сделать
# # Вы участвуете в разработке приложения для математиков, где можно будет делать всё,
# начиная от простейших вычислений и заканчивая построением сложных графиков.
# В этом приложении реализована установка диапазона чисел, и вам необходимо
# написать этакую «защиту от дурака».
# # Напишите программу, которая получает на вход число и проверяет, двузначное
# оно или нет. Выведите соответствующее сообщение. Числа −42 и −99 тоже считаются
# двузначными. Сделайте это, используя не более одного оператора if-elsе. Не используйте elif.


print('Задача 6. Защита от дурака')
number=int(input('Введите число: '))
if  9 < number < 100 or -100 < number < -9:
    print(number)
else:
    print("Вы ввели некорректное число")
print('*****************************************************')


# Задача 7. Костя хочет выигрывать
# Что нужно сделать
# # После игры в кубики Костя захотел немного изучить работу игровых
# автоматов, а заодно математику и теорию вероятностей. Но ему нужно
# с чего-то начать: написать программу, которая поможет выявить
# закономерности в комбинациях чисел на автомате.
# # Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают),
# 2 (если два совпадают) или 0 (если все числа различны).


print('Задача 7. Костя хочет выигрывать')
number1=int(input('Введите первое число: '))
number2=int(input('Введите второе число: '))
number3=int(input('Введите третье число: '))
if number1 == number2 == number3:
    print('3')
elif number1 == number2 or number1 == number3 or number2 == number3:
    print("2")
else:
    print('0')
print('*****************************************************')


# Задача 8. Новоселье
# Что нужно сделать
## Семья из трёх человек устала тесниться в однушке и наконец решила переехать
# . При обсуждении, какую купить квартиру исходя из своих предпочтений и семейного
# бюджета, они остановились на двух вариантах:
## Взять квартиру попросторнее (не менее 100 м2), но стоимостью не более 10 млн.
# Немного расширить круг поиска, то есть взять квартиру поменьше (от 80 м2),
# но и стоимостью не более 7 млн.
# Напишите программу, которая получает на вход стоимость квартиры и её площадь
# и выводит сообщение о том, подходит она или нет.

print('Задача 8. Новоселье')
house=int(input('Сколько м2? '))
price=int(input('Сколько стоит дом? '))
if house >= 100 and price <= 10000000:
    print('Дом  подходит!')
elif house >= 80 and price <= 7000000:
    print('Дом  подходит!')
else:
    print('Дом не подходит!')
print('*****************************************************')




# Вы уже писали программу, вычисляющую сумму налога по прогрессивной шкале в зависимости
# от полученного заработка: 13% на доход до 10 000, 20% на доход от 10 000 до 50 000,
# 30% на доход выше 50 000.
# # Однако во многих странах, использующих такую шкалу, эта сумма вычисляется более сложным
# способом: налоговая ставка 30% на доход выше 50 000 означает, что 30% уплачивается
# не со всей суммы, а лишь с той её части, которая превосходит 50 000. Аналогично
# ставка 20% на доход от 10 000 до 50 000 обязывает уплатить 20% лишь с той части
# суммы, которая превосходит 10 000, но не превосходит 50 000.
# # Так, например, с дохода 100 000 придётся заплатить такой налог:
# # 30% × (100 000 − 50 000) + 20% × (50 000 − 10 000) + 13% × 10 000 = 15 000 + 8 000 + 1 300 = 24 300
# # А с дохода 30 000 — такой:  20% × (30 000 − 10 000) + 13% × 10 000 = 4 000 + 1 300 = 5 300
# # Напишите программу, которая спрашивает у пользователя его доход и высчитывает
# сумму налога для него по вышеописанным правилам.


print('Задача 9. Прогрессивный налог 2')
sum=int(input('Введите сумму прибыли: '))
if sum > 50000:
    tax = (30 * (sum - 50000)  / 100) + 40000 * 20 / 100 + 10000 * 13 / 100
elif sum >= 10000 and sum <= 50000:
    tax = (20 * (sum-10000) / 100) + 10000 * 13 / 100
elif sum > 0 < 10000:
    tax = sum * 13 / 100
if sum <= 0:
    print("Вы ввели некорретные данные!!!")
print(tax)
print('*****************************************************')

# Задача 10. Почта
# Что нужно сделать
## Почтовое отделение открывается в 08:00 и закрывается в 22:00.
# С 14:00 до 15:00 все сотрудники уходят на обед, а в 10:00 и 18:00
# приезжают машины с посылками, и тогда все сотрудники на два часа
# заняты их разгрузкой. Во время обеда, разумеется, посылки никто не
# выдаёт, как и в моменты, когда разгружаются машины.
## Напишите программу, которая получает на вход время в часах — число
# от 0 до 23 — и пишет, можно ли в этот час получить посылку.
# Используйте только один условный оператор if-else, без elif и прочего.
# Решите задание двумя способами:
## При выполнении условия выводится сообщение: «Можно получить посылку».
# При выполнении условия выводится сообщение: «Посылку получить нельзя».

print('Задача 10. Почта')
n1=int(input('Введите число: '))
if (n1 < 8 or n1 > 21) or (n1 < 15 and n1 > 13)  or\
        (n1 > 9 and n1 < 12) or (n1 < 20 and n1 > 17) :
    print('Посылку получить нельзя!')
else:
    print('Можно получить посылку!!!')