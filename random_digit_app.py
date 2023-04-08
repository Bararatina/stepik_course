import random


def is_valid(n, z):
    if n.isdigit():
        if int(n) in range(1, z + 1):
            return True
        else:
            return False
    else:
        return False


again = 'да'

print('Добро пожаловать в числовую угадайку!')
print('Мы загадаем число, а вы должны угадать его!')
print('Для начала, укажите правую границу диапазона загадываемого числа')

while again == 'да':
    z = input('Угадывать число от 1 до : ')
    z = int(z)
    a = random.randint(1, z)
    print('Введите целое число от 1 до', z, ':')

    n = input()
    while is_valid(n, z) is False:
        print('Неверно. Введите целое число от 1 до', z, ':')
        n = input()

    n = int(n)
    x = random.randint(1, z)
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
