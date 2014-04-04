import random
import inputLibrary

side = inputLibrary.int_input("How many sides the die should have?")
diceNumber = inputLibrary.int_input("How many dice do you want to roll?")

for times in range(1,diceNumber+1):
	dice = rand.random(1,side+1)
	print "The result of the dice is", dice