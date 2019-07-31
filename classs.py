class Game():
	def __init__(self, name):
		self.name = name



class Player():
	def __init__(self, name, piece):
		self.name = name
		self.piece = piece
		self.history = []

	def addhistory(self, action):
		self.history.append(action)

class Board():
	def __init__(self, name):
		self.name = name
		if name == 'Go':
			self.n = 18
			self.board = [['+'] * (self.n) for _ in range(self.n-1)]
		elif name == 'Chess':
			self.n = 8
			self.board = [[' '] * (self.n + 1) for _ in range(self.n)]
			self.board = self.initboard()
	
	def initboard(self):
		board = self.board
		n = self.n
		for j in range(1, n+1):
			board[1][j] = 'p'
			board[6][j] = 'p'
			if j == 1 or j == n:
				board[0][j] = 'r'
				board[7][j] = 'r'
			if j == 2 or j == n-1:
				board[0][j] = 'k'
				board[7][j] = 'k'
			if j == 3 or j == n-2:
				board[0][j] = 'b'
				board[7][j] = 'b'
			if j == 4:
				board[0][j] = 'Q'
				board[7][j] = 'Q'
			if j == 5:
				board[0][j] = 'K'
				board[7][j] = 'K'
		i = 1
		for row in board:
			row[0] = str(i)
			i += 1
			if i > n:
				break
		board.append([' ', '1', '2', '3', '4', '5', '6', '7', '8'])
		return board

class Piece():
	def __init__(self, name):
		# self.name = name
		if name == 'Go':
			self.pieces_role = ['white', 'black']
			self.pieces_type = {'w':0, 'b':0}
		elif name == 'Chess':
			self.pieces_role = ['white', 'black']
			# self.pieces_type = {'King':1, 'Queen':1, 'rock':2, 'bishop':2, 'knight':2, 'pawn':8}
			self.pieces_type = {'K':1, 'Q':1, 'r':2, 'b':2, 'k':2, 'p':8}

class Position():
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y

class Action():
	def __init__(self, board, player, name):
		self.board = board
		self.player = player
		self.name = name

	def new(self): # 'Go':
		name = self.name
		board = self.board.board
		x = raw_input("Please input x: ")
		y = raw_input("Please input y: ")

		# if name == 'Go':
		board[int(x) - 1][int(y) - 1] = str(self.player.piece.pieces_role)
		self.board.board = board

		self.player.piece.pieces_type[str(self.player.piece.pieces_role)] += 1
		history = 'ADD a new piece at ' + str(x) + ', ' + str(y)
		self.player.addhistory(history)
	
	def move(self): # 'Chess'
		board = self.board.board
		x1 = raw_input("Please input x1: ")
		y1 = raw_input("Please input y1: ")
		while board[int(x1)-1 ][int(y1) ] == ' ':
			x1 = raw_input("Please input right x1: ")
			y1 = raw_input("Please input right y1: ")
		piece = board[int(x1)-1 ][int(y1) ]
		board[int(x1)-1 ][int(y1) ] = ' '
		x2 = raw_input("Please input x2: ")
		y2 = raw_input("Please input y2: ")
		while board[int(x2) -1][int(y2) ] != ' ':
			x2 = raw_input("Please input right x2: ")
			y2 = raw_input("Please input right y2: ")
		board[int(x2) -1][int(y2) ] = piece
		self.board.board = board
		history = 'MOVE a new piece from '+str(x1)+', '+str(y1)+'to '+str(x2)+', '+str(y2)
		self.player.addhistory(history)

	def eat(self):
		name = self.name
		board = self.board.board
		if name in ['Chess', 'chess', 'CHESS', 'C', 'c']:
			x1 = raw_input("Please input x1: ")
			y1 = raw_input("Please input y1: ")
			while board[int(x1) -1][int(y1) ] == ' ':
				x1 = raw_input("Please input right x1: ")
				y1 = raw_input("Please input right y1: ")
			piece = board[int(x1) -1][int(y1) ]
			board[int(x1) -1][int(y1) ] = ' '
			x2 = raw_input("Please input x2: ")
			y2 = raw_input("Please input y2: ")
			while board[int(x2) -1][int(y2) ] == ' ':
				x2 = raw_input("Please input right x2: ")
				y2 = raw_input("Please input right y2: ")
			self.player.piece.pieces_type[board[int(x2) -1][int(y2) ]] -= 1

			board[int(x2) -1][int(y2) ] = piece
			self.board.board = board
			history = 'EAT a piece from '+str(x1)+', '+str(y1)+'to '+str(x2)+', '+str(y2)
			self.player.addhistory(history)
		else:
			x = raw_input("Please input x: ")
			y = raw_input("Please input y: ")
			if board[int(x) - 1][int(y) - 1] == '+':
				print 'No piece in here ! You can not eat !'
			else:
				self.player.piece.pieces_type[board[int(x) - 1][int(y) - 1]] -= 1
				board[int(x) - 1][int(y) - 1] = '+'
			self.board.board = board
			history = 'EAT a piece at ' + str(x) + ', ' + str(y)
			self.player.addhistory(history)

	def query(self):
		name = self.name
		board = self.board.board
		x = raw_input("Please input x: ")
		y = raw_input("Please input y: ")
		free_flag = 0
		if name in ['Chess', 'chess', 'CHESS', 'C', 'c']:
			if board[int(x) -1][int(y) ] == ' ':
				free_flag = 1
			else:
				this = board[int(x) -1][int(y) ]
		else:
			if board[int(x) - 1][int(y) - 1] == '+':
				free_flag = 1
			else:
				this = str(board[int(x) - 1][int(y) - 1])

		if free_flag == 1:
			print('FREE')
			history = 'QUERY a piece at ' + str(x) + ', ' + str(y)+', the result is FREE'
		else:
			print('The piece at '+ str(x) + ', ' + str(y)+' is '+ this)
			history = 'QUERY a piece at ' + str(x) + ', ' + str(y)+', the result is '+this
		self.player.addhistory(history)

	def count(self):
		name = self.name
		board = self.board.board

		if name in ['Chess', 'chess', 'CHESS', 'C', 'c']:
			this = str(self.player.piece.pieces_type)
		else:
			this = str(self.player.piece.pieces_type)

		history = "COUNT your pieces in the board, the result is " + this
		print history
		self.player.addhistory(history)
