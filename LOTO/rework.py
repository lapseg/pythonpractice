import random
import os

number_pool = list(range(1, 11))  # 1 , 101
player_card = sorted(random.sample(number_pool, 3))  # 15
computer_card = sorted(random.sample(number_pool, 3))  # 15


def random_choice(num_pool):
    choice = random.choice(num_pool)
    num_pool.remove(choice)
    # print("Current lotto: " + str(choice))
    return choice


def game_status_check():
    if len(player_card) == 0 or len(computer_card) == 0:
        print("Game over !")
        return True
    else:
        return False


def printout_cards():
    print("######################################\n")
    print("Player card: " + str(player_card))
    print("\n######################################\n")
    print("Computer card: " + str(computer_card))


def end_game():
    answer = input("Do you want to restart the game [y or n] ?: ")
    if answer == "y":
        main()
    elif answer == "n":
        print("Thank you for playing ! ")
        exit()
    else:
        print("Enter y or n !")


def main():
    while not game_status_check():
        printout_cards()
        random_number = random_choice(number_pool)
        print("Random lotto is: {}".format(random_number))
        answer = input("Do you want to cross out number [y or n]: ")
        if answer == "y":
            player_card.remove(random_number)
            if random_number in computer_card:
                computer_card.remove(random_number)
        elif answer == "n":
            if random_number in player_card:
                print("The number was in your card, you missed it and lost !")
                end_game()
            elif random_number in computer_card:
                computer_card.remove(random_number)
        os.system("cls")
        game_status_check()


if __name__ == '__main__':
    main()
