# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)
#
# Extras:
#
# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


randomNumber = random.randint(1,9)
tryCount = 0
userChoice = 0

while randomNumber != userChoice and userChoice != "exit":
	userChoice = input("Please enter a number between 1 and 9: ")
	
	if userChoice == "exit":
		break

	userChoice = int(userChoice)
	if randomNumber < userChoice:
		tryCount += 1
		print("Less")
		print(tryCount)
	elif randomNumber > userChoice:
		tryCount += 1
		print("More")
		print(tryCount)
	
else:
	print("Guessed and it just took you {0} tries".format(tryCount))
 	


























# 	print("Yehaaa ! You guessed it right :)")
# 	print(tryCount)
# elif randomNumber < userChoice:
# 	print("Try a bit higher")
# 	tryCount += 1
# elif randomNumber > userChoice:
# 	print("Try a bit lower")
# 	tryCount += 1
# else:
# 	print("Something is wrong")