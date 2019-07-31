# import wxPython
# import PyGTK
# import pyui4win
from classs import *
from util import printboard, print_history
print('************************ WELCOME ************************')
while True:
	str00 = raw_input("Which game do you want to play? Go or Chess? You can ignore the case, or type only the first letter.")
	# str00 = 'Go'
	if str00 in ['Go', 'go', 'GO', 'G', 'g']:
		game = Game('Go')
		piece1 = Piece('Go')
		piece2 = Piece('Go')
		print('Here is your chessboard')
		board = Board('Go')
		printboard(board.board)
		break
	elif str00 in ['Chess', 'chess', 'CHESS', 'C', 'c']:
		game = Game('Chess')
		piece1 = Piece('Chess')
		piece2 = Piece('Chess')
		print('Here is your chessboard')
		board = Board('Chess')
		printboard(board.board)
		break
	else:
		print("Please input [Go] or [Chess]. You can ignore the case, or type only the first letter.")

name1 = raw_input("Please input the name of player 1:")
name2 = raw_input("Please input the name of player 2:")
# name1 = 'aaa'
# name2 = 'bbb'
if str00 in ['Chess', 'chess', 'CHESS', 'C', 'c']:
	player1 = Player(name1, piece1)
	player2 = Player(name2, piece2)
else:
	piece1.pieces_role = piece1.pieces_role[0][0]
	player1 = Player(name1, piece1)
	piece2.pieces_role = piece2.pieces_role[1][0]
	player2 = Player(name2, piece2)
action1 = Action(board, player1, str00)
action2 = Action(board, player2, str00)
print '************************ GAME START ************************'
player = 1
while True:
	player = player * -1
	if player == -1:
		p = player1
		a = action1
	else:
		p = player2
		a = action2
	print 'Hello ! ' + p.name
	if str00 in ['Chess', 'chess', 'CHESS', 'C', 'c']:
		str0 = raw_input("Please input your action ['move', 'eat', 'query', 'count', 'NEXT', 'next', 'Next', 'end', 'End', 'END'] ")
	else:
		str0 = raw_input("Please input your action ['new', 'eat', 'query', 'count', 'NEXT', 'next', 'Next', 'end', 'End', 'END'] ")
	while str0 not in ['new', 'move', 'eat', 'query', 'count', 'NEXT', 'next', 'Next', 'end', 'End', 'END']:
		str0 = raw_input("Please reinput your action: ")

	if str0 in ['end', 'End', 'END']:
		print 'END THE GAME '
		break
	if str0 in ['NEXT', 'next', 'Next']:
		continue

	if str0 == 'new':
		a.new()
		printboard(board.board)
	elif str0 == 'move':
		a.move()
		printboard(board.board)
	elif str0 == 'eat':
		a.eat()
		printboard(board.board)
	elif str0 == 'query':
		a.query()
		printboard(board.board)
	elif str0 == 'count':
		a.count()
		printboard(board.board)

str0 = raw_input("Want to check your chess history? Yes or No? ")
if str0 in ['Yes', 'Y', 'yes', 'y']:
	str1 = raw_input("Which player's chess history do you want to check? Please input player's name: ")
	findname = 0
	if player1.name == str1:
		print_history(player1.history)
	elif player2.name == str1:
		print_history(player2.history)
	else:
		print("Can't find this name! ")
		print '************************ GAME OVER ************************'
else:
	print '************************ GAME OVER ************************'