import random
word_list = ['Кант', 'Хроника', 'Зал', 'Галера', 'Балл', 'Вес', 'Кафель',
             'Знак', 'Фильтр', 'Башня', 'Кондитер', 'Омар', 'Чан', 'Пламя',
             'Банк', 'Тетерев', 'Муж', 'Камбала', 'Груз', 'Кино', 'Лаваш',
             'Калач', 'Геолог', 'Бальзам', 'Бревно', 'Жердь', 'Борец',
             'Самовар', 'Карабин', 'Подлокотник', 'Барак', 'Мотор', 'Шарж',
             'Сустав', 'Амфитеатр', 'Скворечник', 'Подлодка', 'Затычка',
             'Ресница', 'Спичка', 'Кабан', 'Муфта', 'Синоптик', 'Характер',
             'Мафиози', 'Фундамент', 'Бумажник', 'Библиофил', 'Дрожжи',
             'Казино', 'Конечность', 'Пробор', 'Дуст', 'Комбинация',
             'Мешковина', 'Процессор', 'Крышка', 'Сфинкс', 'Пассатижи', 'Фунт',
             'Кружево', 'Агитатор', 'Формуляр', 'Прокол', 'Абзац', 'Караван',
             'Леденец', 'Кашпо', 'Баркас', 'Кардан', 'Вращение', 'Заливное',
             'Метрдотель', 'Клавиатура', 'Сегмент', 'Обещание', 'Магнитофон',
             'Кордебалет', 'Заварушка']


# def get_word():
#     word = random.choice(word_list).upper()
#     return word
word = random.choice(word_list).upper()


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     /
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                '''
    ]
    return stages[tries]


def play(word):
    list_word_comp = []
    list_num_letters = []
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    list_word_comp.extend(word_completion)
    print('Давайте играть в угадайку слов!')
    print(display_hangman(6))
    while tries != 0:
        print(*list_word_comp)
        print('Введите букву или слово целиком')
        letter = input().upper()
        if len(letter) == 1:
            while not (1040 <= ord(letter) <= 1071 or ord(letter) == 1105) or letter in guessed_letters:
                print('Некорректный ввод или вы вводили эту букву. Буква Ё = Е Попробуйте еще раз.')
                letter = input().upper()
            else:
                guessed_letters.append(letter)
                if letter in word:
                    a = word.find(letter)
                    while a != -1:
                        word = word.replace(letter, '_', 1)
                        list_num_letters.append(a)
                        a = word.find(letter)
                    for i in range(len(list_num_letters)):
                        del list_word_comp[list_num_letters[i]]
                        list_word_comp.insert(list_num_letters[i], letter)
                        # word_completion = word_completion[:list_num_letters[i]] + letter + word_completion[(list_num_letters[i] + 1):]
                elif letter not in word:
                    print('Такой буквы нет')
                    tries -= 1
                    print(display_hangman(tries))
        if '_' not in list_word_comp:
            print('Поздравляем! Вы угадали слово!')
            print(*list_word_comp)
            break
    else:
        print('Вы проиграли!')


print(word)
play(word)
