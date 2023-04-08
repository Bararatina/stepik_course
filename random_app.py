import random

a = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')


def is_valid(n):
    if n.isdigit():
        if int(n) in range(1, 101):
            return True
        else:
            return False
    else:
        return False


n = input('Put the number: ')

print(is_valid(n))
