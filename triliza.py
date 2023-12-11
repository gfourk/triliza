
import random


class Board:
	
	def __init__(self):
		self.board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
	
	def print_board(self):
		print ('\n|'+' '+self.board[0][0]+' '+'|'+' '+self.board[0][1]+' '+'|'+' '+self.board[0][2]+' '+'|')
		print ('|---|---|---|')
		print ('|'+' '+self.board[1][0]+' '+'|'+' '+self.board[1][1]+' '+'|'+' '+self.board[1][2]+' '+'|')
		print ('|---|---|---|')
		print ('|'+' '+self.board[2][0]+' '+'|'+' '+self.board[2][1]+' '+'|'+' '+self.board[2][2]+' '+'|')
		print ('|---|---|---|\n')

	
class Player:
	
	def __init__(self,board,symbol):
		self.board = board
		self.symbol = symbol
	
	def play(self):
		c,d = tuple(map(int,input('select position : ').split(',')))
		while c%1!=0 or d%1!=0 or c>2 or c<0 or d>2 or d<0 or self.board[c][d]!=' ':
			print('wrong input')
			c,d = tuple(map(int,input('select position : ').split(',')))
		self.board[c][d] = self.symbol

	
class Computer:
	
	def __init__(self,board,symbol):
		self.board = board
		self.symbol = symbol
		
	def move(self):
		c = random.randint(0,2)
		d = random.randint(0,2)
		while self.board[c][d] != ' ' :
			c = random.randint(0,2)
			d = random.randint(0,2)
		self.board[c][d] = self.symbol

	
class Game:
	
	def __init__(self):
		self.b = Board()
		psymbol = input('select symbol(X/O) : ')
		while psymbol!='X' and psymbol!='O':
		    print('wrong input')
		    psymbol = input('select symbol(X/O) : ')
		if psymbol=='X':
		    csymbol = 'O'
		elif psymbol=='O':
		    csymbol = 'X'
		self.turn()
		if psymbol==self.turn:
		    self.turn = 'player'
		elif csymbol==self.turn:
		    self.turn = 'computer'
		self.computer = Computer(self.b.board,csymbol)
		self.player = Player(self.b.board,psymbol)

		
	def check_win(self,symbol):
		if (self.b.board[0][0]==self.b.board[0][1]==self.b.board[0][2]==symbol) or \
		   (self.b.board[1][0]==self.b.board[1][1]==self.b.board[1][2]==symbol) or \
		   (self.b.board[2][0]==self.b.board[2][1]==self.b.board[2][2]==symbol) or \
		   (self.b.board[0][0]==self.b.board[1][0]==self.b.board[2][0]==symbol) or \
		   (self.b.board[0][1]==self.b.board[1][1]==self.b.board[2][1]==symbol) or \
		   (self.b.board[0][2]==self.b.board[1][2]==self.b.board[2][2]==symbol) or \
		   (self.b.board[0][0]==self.b.board[1][1]==self.b.board[2][2]==symbol) or \
		   (self.b.board[0][2]==self.b.board[1][1]==self.b.board[2][0]==symbol):
			self.b.print_board()
			print('\nthe winner is : ',self.turn,'\n')
			return 'end'
		
	def game_over(self):
		full = 0
		for i in range(len(self.b.board)):
			for j in range(len(self.b.board[i])):
				if self.b.board[i][j]!=' ':
					full=full+1
		if full==9:
			self.b.print_board()
			print('issopalia')
			return 'end'
		
	def change_turn(self):
		if self.turn=='player':
			self.turn = 'computer'
		elif self.turn=='computer':
			self.turn = 'player'
	
	def turn(self):
		a = random.randint(0,1)
		if a==0 :
			self.turn = "O"
		else:
			self.turn = "X"

				
	def start(self):
		while True:
			if self.turn=='computer':
				self.b.print_board()
				self.computer.move()
				if self.check_win(self.computer.symbol)=='end':
					return
				if self.game_over()=='end':
					return
				self.change_turn()
			elif self.turn=='player':
				self.b.print_board()
				self.player.play()
				if self.check_win(self.player.symbol)=='end':
					return
				if self.game_over()=='end':
					return
				self.change_turn()
		
		
def main():
	game = Game()
	game.start()

main()

