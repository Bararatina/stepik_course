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
    guessed_letters = []
    guessed_words = []
    list_word_comp = ['_'] * len(word)
    word_if_lost = word
    tries = 6
    print('Давайте играть в виселицу!')
    print('Вы должны угадать слово, пока человечек не повесится.')
    print('Всего у вас будет', tries, 'попыток.')
    display_hangman(tries)
    while tries != 0:
        list_index_letters = []
        print(*list_word_comp)
        print('Введите букву или слово целиком')
        letter = input().upper()
        if len(letter) == 1:
            while not (1040 <= ord(letter) <= 1071 or ord(letter) == 1105) or \
                    letter in guessed_letters:
                print('Некорректный ввод или вы вводили эту букву.'
                      'Буква Ё = Е. Попробуйте еще раз.')
                break
            else:
                guessed_letters.append(letter)
                if letter in word:
                    index = word.find(letter)
                    list_index_letters = []
                    while index != -1:
                        word = word.replace(letter, '_', 1)
                        list_index_letters.append(index)
                        index = word.find(letter)
                    for index in list_index_letters:
                        list_word_comp[index] = letter
                elif letter not in word:
                    tries -= 1
                    print(display_hangman(tries))
                    print('Такой буквы нет')
        elif len(letter) == len(word):
            if letter == word:
                print('Поздравляем! Вы угадали слово!')
                break
            elif letter in guessed_words:
                print('Вы уже пробовали это слово. Будьте внимательнее!')
            else:
                guessed_words.append(letter)
                tries -= 1
                print(display_hangman(tries))
                print('Неверное слово!')
        else:
            print('Некорректный ввод.')
        if '_' not in list_word_comp:
            print('Поздравляем! Вы угадали слово!')
            print(*list_word_comp)
            break
    else:
        print('Вы проиграли!')
        print('Загаданное слово:')
        print(word_if_lost)


play(word)
