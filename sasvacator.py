#!/usr/bin/env python3
import random

symbols_map = {
    # Первый ряд
    'й': 'цуфыв',
    'ц': 'йуфыв',
    'у': 'цкыва',
    'к': 'уевап',
    'е': 'кнапр',
    'н': 'егпро',
    'г': 'ншрол',
    'ш': 'гщолд',
    'щ': 'шзлдж',
    'з': 'щхджэ',
    'х': 'зъджэ',
    'ъ': 'зхджэ',
    # Второй ряд
    'ф': 'йцуывячс',
    'ы': 'йцуфвячс',
    'в': 'цукыачсм',
    'а': 'укевпсми',
    'п': 'кенармит',
    'р': 'енгпоить',
    'о': 'нгшрлтьб',
    'л': 'гшщодьбю',
    'д': 'шщзлжбю',
    'ж': 'щзхдэбю',
    'э': 'зхъжю',
    # Третий ряд
    'я': 'фывчс',
    'ч': 'фывяс',
    'с': 'ывачм',
    'м': 'вапси',
    'и': 'апрмт',
    'т': 'проиь',
    'ь': 'ролтб',
    'б': 'олдью',
    'ю': 'лджэб',
}


def change_symbol(symbol):
    if symbol not in symbols_map:
        return symbol
    return random.choice(symbols_map[symbol])


def change_word(word):
    word = list(word)

    for idx in range(len(word) // 3):
        place = random.randint(0, len(word)-1)
        word[place] = change_symbol(word[place])

    return ''.join(word)


def translate(text):
    # Убираем символы, которыми сасвак не пользуется
    text = text.replace('ё', 'е').replace(',', '')

    new_text = ' '.join(map(change_word, text.split()))
    return new_text


if __name__ == '__main__':
    print('Введите quit чтобы выйти.')

    while True:

        input_data = input('Текст для осасвачивания:')

        # Все маленькими. Негоже расставлять заглавные буквы.
        input_data = input_data.strip().lower()

        if input_data == 'quit':
            break

        print(translate(input_data))
