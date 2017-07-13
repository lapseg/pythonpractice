#!/usr/bin/python3

"""Лото
 
Правила игры в лото.
 
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
 
Количество бочонков — 90 штук (с цифрами от 1 до 90).
 
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
 
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
 
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
 
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.
     
Побеждает тот, кто первый закроет все числа на своей карточке.
 
Пример одного хода:
 
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
 
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
 
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
 
"""

import random

number_pool = list(range(1, 91))
computer_card = random.sample(number_pool, 15)
computer_card_sorted = sorted(computer_card)
player_card = random.sample(number_pool, 15)
player_card_sorted = sorted(player_card)


def display_cards():
    print("Computer card:\n")
    print(computer_card_sorted)
    print("====================================")
    print("Player card:\n")
    print(player_card_sorted)


def lotto_choice():
    choice = random.choice(number_pool)
    number_pool.remove(choice)
    return choice


def the_game():
    while number_pool:
        choice = lotto_choice()
        print("The random lotto is: " + str(choice))
        display_cards()
        cross_number = input("Do you want to cross out a number")
        cross_number.lower()
        if cross_number == "y":
            if choice in player_card_sorted:
                player_card_sorted.remove(choice)
            elif choice in computer_card_sorted:
                computer_card_sorted.remove(choice)
        if cross_number == "n":
            if choice in computer_card_sorted:
                computer_card_sorted.remove(choice)
            else:
                continue
    else:
        if len(player_card_sorted) == 0:
            print("Congratulations Player ! You won")
        elif len(computer_card_sorted) == 0:
            print("The computer have won, too bad !")
        else:
            print("It is a tie you both ran out of numbers, very straange !")


the_game()
