def printboard(board):
	n = len(board)
	print(' ' + '-' * (n * 2 + 1) )
	for row in board:
		print('| ' + ' '.join(row) + ' |') 
	print(' ' + '-' * (n * 2 + 1) )

def print_history(history):
	print('\n'.join(history))

# def new():
# def move()
# def eat()
# def query()
# def count()