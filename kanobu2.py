# -*- coding: utf-8 -*-
from __future__ import unicode_literals

playerName1 = input("Enter your name Player 1: ")
playerName2 = input("Enter your name Player 2: ")

playerOneChoice = input("So what would like dear {0}, rock, paper or scissors: ".format(playerName1))
playerTwoChoice = input("And you ? Glorious warrior {0}, choose your weapon - rock, paper or scissors: ".format(playerName2))

def getTheGameStarted(p1, p2):
	if p1 == p2:
		print("Tie !")
	elif p1 == "rock":
		if p2 == "paper":
			print("Paper beats rock")
		else:
			print("Scissors cut paper")
	elif p1 == "paper":
		if p2 == "rock":
			print("Paper covers rock")
		else:
			print("Scissors cut paper")
	elif p1 == "scissors":
		if p2 == "paper":
			print("Scissors cut paper")
		else:
			print("Paper covers rock")
	elif p1 and p2 != "rock" or "paper" or "scissors":
		print("Please enter the correct values of rock, paper or scissors")

getTheGameStarted(playerOneChoice, playerTwoChoice)