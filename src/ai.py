"""
Python algorithm for a mancal robot with an
Alpha Beta Pruning strategy
"""

import math

def miniMax(board, depth, player):
	"""
	This function computes the future moves on the board for a player and returns
	the move with the best score after a certain depth
	"""

	#Maximize the score for this player. Other player is minimized
	maximizePlayer = player
	#Number of move
	move = -1
	#Score representing utility of move
	score = -math.inf

	if (player1Marbles+player2Marbles) == 0:
		return (-1, -1)

	if depth == 0:
		return bestMove(board, -1)

	"""
	Traverse through possible moves return the score based
	on bestMove() and minimize or maximize based on the player
	"""
	#possibleMove(board)
	
	"""
	return the best move for the maximizing or minimizing player
	"""
	#if maximizePlayer:

	 

	return score, move

def possibleMove(board):
	#Holds all the non-empty buckets or possible moves
	moves = []

	#Represents the current bucket being checked
	bucket = 1

	#Loops through all of player 1 buckets
	for marbles in board[1]:
		#If the bucket is not empty then add bucket to list of possible moves
		if marbles != 0:
			moves.append(bucket)
		#Check next bucket
		bucket += 1


	
def bestMove(board):
	"""
	This function calculates the utility of the current
	chosen move and returns the score for the move. The
	higher the number the better the move.
	"""

	#TODO - Represent a player ID so that the AI can play as either player 

	#Represent the players current ampount marble 
	p1_marbles = 0
	p2_marbles = 0

	#Count marbles in both players bucket's
	for marbles in board[1]:
		p1_marbles += marbles

	for marbles in board[3]:
		p2_marbles += marbles

	"""
	Add the marbles within each players mancalas with a double value
	to represent the fact that these marbles cannot be moved
	"""
	p1_marbles += board[0]*2
	p2_marbles += board[0]*2

	"""
	Return the utility of a move by checking how many 
	marbles a  player versus the opponent
	"""
	return p1_marbles - p2_marbles
	

def printNextMove(player, player1Mancala, player1Marbles, player2Mancala, 
				 	player2Marbles):
	
	#Represent all the values on the board
	board = [player1Mancala, player1Marbles, player2Mancala, player2Marbles]

	#Amount of moves we would like to search
	depth = 3

	#Call a function to look a certain amount of moves ahead
	miniMax(board, depth, player)