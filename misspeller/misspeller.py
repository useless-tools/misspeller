#!/usr/bin/env python3
import random

from .data import symbols_map


def change_symbol(symbol):
    if symbol.lower() not in symbols_map:
        return symbol

    if symbol.islower():
        return random.choice(symbols_map[symbol])
    else:
        return random.choice(symbols_map[symbol.lower()]).upper()


def change_word(word):
    word = list(word)

    if len(word) <= 2:
        mistakes = 0
    elif len(word) <= 3:
        mistakes = 1
    elif len(word) <= 5:
        mistakes = 2
    elif len(word) <= 9:
        mistakes = 3
    else:
        mistakes = len(word) // 3

    for idx in range(mistakes):
        place = random.randint(0, len(word)-1)
        word[place] = change_symbol(word[place])

    return ''.join(word)


def change_text(text):
    new_text = ' '.join(map(change_word, text.split()))
    return new_text


__all__ = ['change_symbol', 'change_text', 'change_word']
