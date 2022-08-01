class game:
	
	def _init_(self):
		self.patt=[]
		
	
	def create_patt(self):
		for i in range (3):
			r=[]
			for j in range(3):
				r.append("_")
			self.patt.append(r)
			
	
	def start_game(self):
		self.create_patt()
		p = 'X'
		while(1):
			print("Player {} can play".format(p))	
			self.show()
			r,c =list(input("enter the position row and colunm"))
			#print()
			self.patt[r-1][c-1]=p
			
			if self.win():
				printf("Player {} has won!!!".format(p))
				break
				
			for r in self.patt:
				for i in r:
					if i!='_':
						print("Match draw!!!")
			
			if(p=='X'):
				p='O'
			else:
				p='X'
				
			self.show()

			
			
			
