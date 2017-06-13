
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

paperRoll = "бумага"
stoneRoll = "камень"
scissorsRoll = "ножницы"
playerOneChoice = ""
playerTwoChoice = ""
playerOneChoice = input("Игрок 1 выберите свой предмет: ")
playerTwoChoice = input("Игрок 2 выберите свой предмет: ")

while playerOneChoice and playerTwoChoice != 0:
    if playerOneChoice == playerTwoChoice:
        print("ничья")
    elif playerOneChoice == paperRoll and playerTwoChoice == stoneRoll:
        print("бумага бьет камень")
        print("Поздравляю с победой Игрок 1")
        break
    elif playerOneChoice == stoneRoll and playerTwoChoice == scissorsRoll:
        print("камень бьёт ножницы")
        print("Поздравляю с победой Игрок 1")
        break
    elif playerOneChoice == scissorsRoll and playerTwoChoice == paperRoll:
        print("ножницы бьют камень")
        print("Поздравляю с победой Игрок 1")
        break
    elif playerTwoChoice == paperRoll and playerOneChoice == stoneRoll:
        print("бумага бьет камень")
        print("Поздравляю с победой Игрок 2")
        break
    elif playerTwoChoice == stoneRoll and playerOneChoice == scissorsRoll:
        print("камень бьёт ножницы")
        print("Поздравляю с победой Игрок 2")
        break
    elif playerTwoChoice == scissorsRoll and playerOneChoice == paperRoll:
        print("ножницы бьют камень")
        print("Поздравляю с победой Игрок 2")
        break
else:
    print("Вы ничего не ввели, игра завершена !")
