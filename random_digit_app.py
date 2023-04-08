import random


def is_valid(n):
    if n.isdigit():
        if int(n) in range(1, 101):
            return True
        else:
            return False
    else:
        return False


again = 'да'

print('Добро пожаловать в числовую угадайку')

while again == 'да':
    a = random.randint(1, 100)
    print('Введите целое число от 1 до 100:')

    n = input()
    while is_valid(n) is False:
        print('Неверно. Введите целое число от 1 до 100')
        n = input()

    n = int(n)
    x = random.randint(1, 100)
    count = 1
    while n != x:
        if n < x:
            print('Ваше число меньше загаданного, попробуйте еще раз:')
            count += 1
            n = int(input())
        elif n > x:
            print('Ваше число больше загаданного, попробуйте еще раз:')
            count += 1
            n = int(input())
    else:
        print('Вы угадали, поздравляем!')
        print('Количество попыток: ', count)
        print('Начать заново?')
        p = input('Введите да/нет:')
        again = p.lower()
else:
    print('Спасибо, что играли с нами! До свидания!')
