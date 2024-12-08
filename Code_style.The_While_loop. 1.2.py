# Циклы – это команды, которые повторяют другие команды.

# number = int(input('Введите число: '))
# if number % 2 == 0:
#     print('Чётное число')
# else:
#     print('Нечётное число')

# Существует два вида циклов: while and for
# Сейчас мы рассматриваем цикл while.
# Если мы запустим код, то увидим, что нам снова и снова выходит просьба -
# - ввести число. Код, написанный с отступом, так и будет повторяться -
# - бесконечное количество раз.
# Цикл while работает как условие if, но в отличие от него,
# while будет повторяться пока условие остается правдивым.
# while 1 > 0:
#     number = int(input('Введите число: '))
#     if number % 2 == 0:
#         print('Чётное число')
#     else:
#         print('Нечётное число')
# print('Я за циклом')

# Операторы break и continue
# break прерывает цикл.
# continue не даёт перейти к следующему условию, а начинает заново.
while 1 > 0:
    number = int(input('Введите число: '))
    if number % 2 == 0:
        print('Чётное число')
        continue
    else:
        print('Нечётное число')
    print('Меня не забыли')
    break
print('Я за циклом')