import random


def check_input(p):
    x = p.lower()
    while x != 'да' and x != 'нет':
        print('Ошибка.')
        p = input('Введите да/нет: ')
        x = p.lower()


def generate_password(password_len):
    password = ''
    while len(password) != password_len:
        password += random.choice(chars)
    print(password)


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppcase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambiguous_symbols = 'il1Lo0O'
chars = ''

n = input('Введите количество паролей для генерации: ')
while not n.isdigit():
    print('Ошибка. Введите целое число, больше нуля:')
    n = input()
n = int(n)

print('Введите длину пароля:')
password_len = input()
while not password_len.isdigit():
    print('Введите целое число, больше нуля:')
    password_len = input()
password_len = int(password_len)

print('Включать цифры в пароль?')
p = input('Введите да/нет: ')
x = p.lower()
check_input(p)

if x == 'да':
    chars += digits

print('Включать прописные буквы?')
p = input('Введите да/нет: ')
x = p.lower()
check_input(p)

if x == 'да':
    chars += uppcase_letters

print('Включать строчные буквы?')
p = input('Введите да/нет: ')
x = p.lower()
check_input(p)

if x == 'да':
    chars += lowercase_letters

print('Включать символы? (Например, "!@#$" и т.д.)')
p = input('Введите да/нет: ')
x = p.lower()
check_input(p)

if x == 'да':
    chars += punctuation

print('Иключать неоднозначные символы, такие, как: "il1Lo0O"?')
p = input('Введите да/нет: ')
x = p.lower()
check_input(p)

if x == 'да':
    chars = chars.translate(str.maketrans('', '', ambiguous_symbols))
for i in range(n):
    print('Пароль №', i + 1, ':')
    generate_password(password_len)

if n == 0:
    print('Укажите количество паролей больше чем 0')
