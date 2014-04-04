#! /usr/bin/env python

import random
import inputLibrary

side = inputLibrary.int_input("How many sides the die should have?")
while side < 1:
	print "No one-sided dice are allowed.Try again"
	side = inputLibrary.int_input("How many sides the die should have?")
	
diceNumber = inputLibrary.int_input("How many dice do you want to roll?")
while diceNumber <= 0:
	print "No negative number dice are allowed. Try again."
	diceNumber = inputLibrary.int_input("How many dice do you want to roll?")

for times in range(1,diceNumber+1):
	side = inputLibrary.int_input("How many sides the die should have?")
	dice = rand.random(1,side+1)
	print "The result of the dice is", dice