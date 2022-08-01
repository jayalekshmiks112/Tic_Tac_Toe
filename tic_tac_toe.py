#This is done with to reference to similar programs and coded with the help of algorithms 

class game:
	
	#initialise 
	def __init__(self):
		self.patt=[]
		
	#creating the pattern and filling each of the slots with _
	def create_patt(self):
		for i in range (3):
			r=[]
			for j in range(3):
				r.append('_')
			self.patt.append(r)
	
	#To display the pattern
	def show(self):
		for r in self.patt:
			for it in r:
				print(it,end=" ")
			print()
	
	# To calculate win 			
	def win(self, p):
		w=None
		
		#ICheck if rows matches
		for i in range(len(self.patt)):
			w=True
			for j in range(len(self.patt)):
				if self.patt[i][j]!=p:
					w=False
					break
		if w:
			return w
		
		#check if columns matches
		for i in range(len(self.patt)):
			w=True
			for j in range(len(self.patt)):
				if self.patt[j][i]!=p:
					w=False
					break
		if w:
			return w
			
		w=True
		
		#Check if diagonals matcjhes
		for i in range(len(self.patt)):
			if self.patt[i][len(self.patt)-1-i]!=p:
				w=False
				break
		if w:
			return w
		return False
		
		for r in self.patt:
			for it in r:
				if it =='_':
					return False
		return True
	
	#To check if all slots afre filled or not so that we can conclude if the match draws or not	
	def filled(self):
       		for r in self.patt:
            		for i in r:
                		if i == '_':
                    			return False
        	return True
		
	#The core of the program where 
	def start_game(self):
		self.create_patt()
		p = 'X'
		count =0
		while True:
			print("Player {} can play".format(p))	
			self.show()
			r,c =list(map(int, input("Enter row and column number ").split()))
			print()
			self.patt[r-1][c-1]=p
			
			if self.win(p):
				print("Player {} has won!!!".format(p))
				break
				
			if self.filled():
                		print("Match Draw!")
                		break
			'''	
			for r in self.patt:
				for it in r:
					if it != '_':
						count=count +1
						if count == 9:
							print("It's draw!!!")
					break
			'''
			if(p=='X'):
				p='O'
			else:
				p='X'
			
			print()
			self.show()

			
t=game()
t.start_game()
				
		
			
		
			
			
