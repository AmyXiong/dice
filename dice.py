import random
import inputLibrary

diceNumber = inputLibrary.int_input("How many dice do you want to roll?")

for times in range(1,diceNumber+1):
	side = inputLibrary.int_input("How many sides the die should have?")
	dice = rand.random(1,side+1)
	print "The result of the dice is", dice